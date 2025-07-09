""""""
import json, asyncio
from openai import AsyncOpenAI
from surrealdb import AsyncSurreal

from settings import SURREALDB_NAMESPACE, SURREALDB_DATABASE, SURREALDB_HOST, SURREALDB_PORT, SURREALDB_PROTOCOL, SURREALDB_USER, SURREALDB_PASS

DB_URL  = f"{SURREALDB_PROTOCOL}://{SURREALDB_HOST}:{SURREALDB_PORT}/rpc"

knowledge_hsnw = """
-- Switch to your namespace / database
USE ns {ns} DB {db};

-- Table for each passage / triple
DEFINE TABLE knowledge
  PERMISSIONS NONE
  SCHEMAFULL;            -- optional but nice: enforces field types

-- Add fields
DEFINE FIELD text       ON knowledge TYPE string;
DEFINE FIELD embedding  ON knowledge TYPE array;   -- OpenAI returns 1536‑floats arrays

-- Create a 1536‑dim HNSW vector index for cosine similarity
DEFINE INDEX idx_knn ON knowledge
  FIELDS embedding
  HNSW DIMENSION 1536 DIST COSINE;
""".format(
    ns=SURREALDB_NAMESPACE,
    db=SURREALDB_DATABASE
)

knowledge_hsnw_v2 = """
-- Switch to your namespace / database
USE ns {ns} DB {db};

-- Table for each passage / triple
DEFINE TABLE knowledge
  PERMISSIONS NONE
  SCHEMAFULL;            -- optional but nice: enforces field types

-- ONE‑TIME migration -------------------------------------------
REMOVE FIELD embedding ON knowledge;           -- if the field exists
REMOVE INDEX idx_knn ON knowledge;             -- if the index exists

-- Re‑define field as an array of 64‑bit floats, dimension 1536
DEFINE FIELD embedding ON knowledge
  TYPE array<float>
  ASSERT array::len($value) = 1536;

-- Re‑create the same HNSW index
DEFINE INDEX idx_knn ON knowledge
  FIELDS embedding
  HNSW DIMENSION 1536 DIST COSINE TYPE F64;
""".format(
    ns=SURREALDB_NAMESPACE,
    db=SURREALDB_DATABASE
)

DEFAULT_SYSTEM_PROMPT = """
You are a medical knowledge retrieval assistant who has access to a large database of medical knowledge.
Your task is to answer questions based on the provided context.
If the context does not contain enough information, you should indicate that you cannot answer the question.
"""


class Vec:
    """Vector database for RAG (retrieval‑augmented generation) with SurrealDB."""

    def __init__(self,
                 openai_client: AsyncOpenAI or None = None,
                 db_url=DB_URL,
                 system_prompt: str = DEFAULT_SYSTEM_PROMPT,
                 embed_model: str = "text-embedding-3-small",
                 inference_model: str = "gpt-4.1-nano"
                 ):
        self.client = openai_client
        self.system_prompt = system_prompt
        self.db_url = db_url
        self.embed_model = embed_model
        self.model = inference_model

    async def init(self):
        """Initialize the vector database."""
        db = AsyncSurreal(self.db_url)
        await db.connect()
        await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})
        await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)
        await db.query(knowledge_hsnw_v2)
        await db.close()

    async def seed(self, data_source: str):
        db = AsyncSurreal(DB_URL)
        await db.connect()
        await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})
        await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)

        docs = [json.loads(l) for l in open("docs.jsonl")]
        chunk, batch = 96, []

        for doc in docs:
            batch.append(doc)
            if len(batch) == chunk:
                await self.insert(batch, db)
                batch = []
        if batch:
            await self.insert(batch, db)

    async def insert(self, batch, db):
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")

        texts  = [d["text"] for d in batch]
        embeds = (await client.embeddings.create(model=self.embed_model, input=texts)).data
        records = [
            {
                "id": f"knowledge:{b['id']}",
                "text": b["text"],
                "embedding": e.embedding,
            }
            for b, e in zip(batch, embeds)
        ]
        await db.create("knowledge", records)

    async def get_context(self, question, k=4):
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")
        qvec = (await self.client.embeddings.create(model=self.embed_model, input=[question])).data[0].embedding
        db   = AsyncSurreal(DB_URL)
        await db.connect()
        await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})
        await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)

        # SurrealQL k‑NN syntax:  <|k, COSINE|> $vector
        res = await db.query(
            "LET $q := $vec RETURN SELECT text FROM knowledge WHERE embedding <|$k,COSINE|> $q;",
            {
                "vec": qvec,
                "k":   k
            }
        )
        await db.close()
        return [row["text"] for row in res[0]["result"]]

    async def rag_chat(self, question, max_tokens: int = 400):
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")
        context = await self.get_context(question, k=4)
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": "Context:\n" + "\n".join(f"- {c}" for c in context)},
            {"role": "user",   "content": question},
        ]
        answer = (await self.client.chat.completions.create(
            model=self.model, messages=messages, max_tokens=max_tokens
        )).choices[0].message.content
        return answer



def example_usage():
    client = AsyncOpenAI(api_key="your-openai-api-key")
    vec = Vec(client)
    msg = asyncio.run(vec.rag_chat("Some query..."))
    print(msg)

