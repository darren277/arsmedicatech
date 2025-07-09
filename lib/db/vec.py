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

    async def seed(self, data_source: str, data_type: str = 'json'):
        db = AsyncSurreal(DB_URL)
        await db.connect()
        await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})
        await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)

        res = await db.query("INFO FOR DB;")
        print("[DEBUG] Database info:", res)

        res = await db.query("INFO FOR TABLE knowledge;")
        print("[DEBUG] Table info:", res)

        if data_type == 'jsonl':
            docs = [json.loads(l) for l in open(data_source, "r", encoding="utf-8") if l.strip()]
        elif data_type == 'json':
            with open(data_source, "r", encoding="utf-8") as f:
                docs = json.load(f)
        else:
            raise ValueError(f"Unsupported data type: {data_type}. Supported types are 'jsonl' and 'json'.")

        chunk, batch = 96, []

        for doc in docs:
            batch.append(doc)
            if len(batch) == chunk:
                print(f"[SEED] Inserting {len(batch)} records...")
                await self.insert(batch, db)
                print("[SEED] Insert complete.")
                batch = []
        if batch:
            print(f"[SEED] Inserting {len(batch)} records...")
            await self.insert(batch, db)
            print("[SEED] Insert complete.")

        res = await db.query("SELECT id, text FROM knowledge LIMIT 5;")
        print("[DEBUG] Sample records:", res)

    async def insert(self, batch, db):
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")

        texts  = [d["text"] for d in batch]
        resp = await self.client.embeddings.create(model=self.embed_model, input=texts)
        embeds = [e.embedding for e in resp.data]

        inserted = 0
        for i, (b, e) in enumerate(zip(batch, embeds)):
            record_id = f"knowledge:{b['id']}"
            print(f"\n[DEBUG] RECORD {i} → {record_id}")
            print(f"  → type(embedding): {type(e)}")
            print(f"  → type(e[0]): {type(e[0]) if isinstance(e, list) and e else 'N/A'}")
            print(f"  → len(embedding): {len(e) if isinstance(e, list) else 'N/A'}")
            print(f"  → sample values: {e[:5] if isinstance(e, list) else 'N/A'}")

            # Surreal expects: array<float>
            if not isinstance(e, list):
                print(f"[ERROR] Embedding is not a list.")
                continue
            if not all(isinstance(x, float) for x in e):
                bad_types = {type(x) for x in e}
                print(f"[ERROR] Non-float types in embedding: {bad_types}")
                continue
            if len(e) != 1536:
                print(f"[ERROR] Bad vector length: {len(e)}")
                continue

            record = {
                "id": record_id,
                "text": b["text"],
                "embedding": e,
            }

            try:
                # Build the full query
                value_tuples = ",\n".join(
                    f"{{ id: 'knowledge:{b['id']}', text: {json.dumps(b['text'])}, embedding: {json.dumps(e)} }}"
                    for b, e in zip(batch, embeds)
                )

                query = f"INSERT INTO knowledge [{value_tuples}];"
                result = await db.query(query)
                print(f"[OK] Inserted {record_id}")
                print(f"SurrealDB result: {result}")
                inserted += 1
            except Exception as ex:
                print(f"[FAIL] {record_id}: {ex}")

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

