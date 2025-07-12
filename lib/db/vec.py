"""
Vector database for RAG (retrieval‑augmented generation) with SurrealDB.
"""
import json
from typing import Any, Dict, List, Optional, cast

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam

# Import surrealdb with type ignore since it lacks proper stubs
from surrealdb import AsyncSurreal  # type: ignore[import-untyped]

from settings import (SURREALDB_DATABASE, SURREALDB_HOST, SURREALDB_NAMESPACE,
                      SURREALDB_PASS, SURREALDB_PORT, SURREALDB_PROTOCOL,
                      SURREALDB_USER, logger)

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


class BatchItem:
    """
    A simple class to represent a single item in a batch for insertion.
    Each item should have 'id' and 'text' keys.
    """

    def __init__(self, id: str, text: str) -> None:
        """
        Initialize a BatchItem instance.
        :param id: Unique identifier for the item.
        :param text: The text content of the item.
        :raises ValueError: If id or text is empty.
        :return: None
        """
        if not id or not text:
            raise ValueError("Both 'id' and 'text' must be provided and cannot be empty.")
        self.id = id
        self.text = text


class BatchList:
    """
    A simple class to represent a list of dictionaries for batch processing.
    """

    def __init__(self, data: List[BatchItem]) -> None:
        """
        Initialize a BatchList instance.
        :param data: A list of BatchItem instances.
        :raises ValueError: If data is empty or contains non-BatchItem instances.
        :return: None
        """
        if not data:
            raise ValueError("Data cannot be empty.")
        self.data = data


class Vec:
    """
    Vector database for RAG (retrieval‑augmented generation) with SurrealDB.

    Example usage:
    ```python
    client = AsyncOpenAI(api_key="your-openai-api-key")
    vec = Vec(client)
    msg = asyncio.run(vec.rag_chat("Some query..."))
    logger.debug(msg)
    ```
    """

    def __init__(
            self,
            openai_client: Optional[AsyncOpenAI] = None,
            db_url: str = DB_URL,
            system_prompt: str = DEFAULT_SYSTEM_PROMPT,
            embed_model: str = "text-embedding-3-small",
            inference_model: str = "gpt-4.1-nano"
    ) -> None:
        """
        Initialize the Vec instance.
        :param openai_client: An instance of AsyncOpenAI client for making API calls.
        :param db_url: URL of the SurrealDB instance.
        :param system_prompt: A system prompt to guide the model's responses.
        :param embed_model: The OpenAI model to use for embeddings (default: "text-embedding-3-small").
        :param inference_model: The OpenAI model to use for inference (default: "gpt-4.1-nano").
        """
        self.client = openai_client
        self.system_prompt = system_prompt
        self.db_url = db_url
        self.embed_model = embed_model
        self.model = inference_model

    async def init(self) -> None:
        """
        Initialize the vector database.
        This method connects to the SurrealDB instance, signs in with credentials,
        and sets up the necessary schema for the knowledge table.
        It creates the knowledge table with the required fields and indices.
        :raises Exception: If the connection or query fails.
        :return: None
        """
        db = AsyncSurreal(self.db_url)  # type: ignore[no-untyped-call]
        try:
            await db.connect()  # type: ignore[no-untyped-call]
        except Exception as e:
            logger.error(f"[ERROR] Failed to connect to SurrealDB: {e}")
            raise
        try:
            await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})  # type: ignore[no-untyped-call]
        except Exception as e:
            logger.error(f"[ERROR] Failed to sign in to SurrealDB: {e}")
            raise
        try:
            if SURREALDB_NAMESPACE is None or SURREALDB_DATABASE is None:
                raise ValueError("SURREALDB_NAMESPACE and SURREALDB_DATABASE must not be None.")
            await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)  # type: ignore[no-untyped-call]
        except Exception as e:
            logger.error(f"[ERROR] Failed to use namespace/database: {e}")
            raise
        try:
            await db.query(knowledge_hsnw_v2)  # type: ignore[no-untyped-call]
        except Exception as e:
            logger.error(f"[ERROR] Failed to create knowledge table: {e}")
            raise
        try:
            await db.close()  # type: ignore[no-untyped-call]
        except Exception as e:
            logger.error(f"[ERROR] Failed to close SurrealDB connection: {e}")
            raise

    async def seed(self, data_source: str, data_type: str = 'json') -> None:
        """
        Seed the vector database with knowledge data.
        :param data_source: Path to the data source file (JSON or JSONL).
        :param data_type: Type of the data source file ('json' or 'jsonl').
        :return: None
        """
        db = AsyncSurreal(DB_URL)  # type: ignore[no-untyped-call]
        await db.connect()  # type: ignore[no-untyped-call]
        await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})  # type: ignore[no-untyped-call]
        if SURREALDB_NAMESPACE is None or SURREALDB_DATABASE is None:
                raise ValueError("SURREALDB_NAMESPACE and SURREALDB_DATABASE must not be None.")
        await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)  # type: ignore[no-untyped-call]

        res = await db.query("INFO FOR DB;")  # type: ignore[no-untyped-call]
        logger.debug("Database info:", res)

        res = await db.query("INFO FOR TABLE knowledge;")  # type: ignore[no-untyped-call]
        logger.debug("Table info:", res)

        if data_type == 'jsonl':
            docs: List[Dict[str, Any]] = [json.loads(l) for l in open(data_source, "r", encoding="utf-8") if l.strip()]
        elif data_type == 'json':
            with open(data_source, "r", encoding="utf-8") as f:
                docs = json.load(f)
        else:
            raise ValueError(f"Unsupported data type: {data_type}. Supported types are 'jsonl' and 'json'.")

        chunk = 96
        batch: List[Dict[str, Any]] = []
        batch_data: List[Dict[str, str]] = []

        for doc in docs:
            batch.append(doc)
            if len(batch) == chunk:
                logger.debug(f"[SEED] Inserting {len(batch)} records...")
                batch_data = [{"id": str(d["id"]), "text": str(d["text"])} for d in batch]
                batch_list = BatchList([BatchItem(**d) for d in batch_data])
                await self.insert(batch_list, db)
                logger.debug("[SEED] Insert complete.")
                batch = []
        if batch:
            logger.debug(f"[SEED] Inserting {len(batch)} records...")
            batch_data = [{"id": str(d["id"]), "text": str(d["text"])} for d in batch]
            batch_list = BatchList([BatchItem(**d) for d in batch_data])
            await self.insert(batch_list, db)
            logger.debug("[SEED] Insert complete.")

        res = await db.query("SELECT id, text FROM knowledge LIMIT 5;")  # type: ignore[no-untyped-call]
        logger.debug("Sample records:", res)

    async def insert(self, batch: BatchList, db: Any) -> None:
        """
        Insert a batch of records into the knowledge table.
        :param batch: A list of dictionaries, each containing 'id' and 'text' keys.
        :param db: An instance of AsyncSurreal connected to the database.
        :return: None
        """
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")

        if not batch.data:
            logger.warning("Batch is empty. Nothing to insert.")
            return
        # All items in batch.data are guaranteed to be BatchItem instances by BatchList validation.
        logger.debug(f"[DEBUG] Inserting {len(batch.data)} records into SurrealDB...")

        # Prepare the batch for OpenAI embedding
        batch_dicts = [item.__dict__ for item in batch.data] # Convert BatchItem to dict

        texts  = [d["text"] for d in batch_dicts]
        resp = await self.client.embeddings.create(model=self.embed_model, input=texts)
        embeds = [e.embedding for e in resp.data]

        inserted = 0
        for i, (b, e) in enumerate(zip(batch_dicts, embeds)):
            record_id = f"knowledge:{b['id']}"
            logger.debug(f"\n[DEBUG] RECORD {i} → {record_id}")
            logger.debug(f"  → type(embedding): {type(e)}")
            logger.debug(f"  → type(e[0]): {type(e[0]) if e else 'N/A'}")
            logger.debug(f"  → len(embedding): {len(e) if e else 'N/A'}")
            logger.debug(f"  → sample values: {e[:5] if e else 'N/A'}")

            # Surreal expects: array<float>
            if not all(isinstance(x, float) for x in e):
                bad_types = {type(x) for x in e}
                logger.error(f"Non-float types in embedding: {bad_types}")
                continue
            if len(e) != 1536:
                logger.error(f"Bad vector length: {len(e)}")
                continue

            try:
                # Build the full query
                value_tuples = ",\n".join(
                    f"{{ id: 'knowledge:{b['id']}', text: {json.dumps(b['text'])}, embedding: {json.dumps(e)} }}"
                    for b, e in zip(batch_dicts, embeds)
                )

                query = f"INSERT INTO knowledge [{value_tuples}];"
                result = await db.query(query)  # type: ignore[no-untyped-call]
                logger.debug(f"[OK] Inserted {record_id}")
                logger.debug(f"SurrealDB result: {result}")
                inserted += 1
            except Exception as ex:
                logger.debug(f"[FAIL] {record_id}: {ex}")

    async def get_context(self, question: str, k: int = 4) -> Optional[List[str]]:
        """
        Retrieve context from the knowledge base for a given question.
        :param question: The question for which context is to be retrieved.
        :param k: The number of nearest neighbors to retrieve (default: 4).
        :return: List of context strings or None if an error occurs.
        """
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")
        qvec = (await self.client.embeddings.create(model=self.embed_model, input=[question])).data[0].embedding
        db   = AsyncSurreal(DB_URL)  # type: ignore[no-untyped-call]
        await db.connect()  # type: ignore[no-untyped-call]
        await db.signin({"username": SURREALDB_USER, "password": SURREALDB_PASS})  # type: ignore[no-untyped-call]
        if SURREALDB_NAMESPACE is None or SURREALDB_DATABASE is None:
            raise ValueError("SURREALDB_NAMESPACE and SURREALDB_DATABASE must not be None.")
        await db.use(SURREALDB_NAMESPACE, SURREALDB_DATABASE)  # type: ignore[no-untyped-call]

        # SurrealQL k‑NN syntax: <k, COSINE|> $vector
        q = f"SELECT text FROM knowledge WHERE embedding <|{k}, COSINE|> $vec;"

        try:
            res = await db.query(q, {"vec": qvec})  # type: ignore[no-untyped-call]
            logger.debug('[DEBUG] Raw SurrealDB result:', json.dumps(res, indent=2))
        except Exception as e:
            logger.error('[ERROR] Exception while querying SurrealDB:', e)
            return None
        finally:
            await db.close()  # type: ignore[no-untyped-call]

        # Ensure 'res' is a list of dicts containing 'text'
        if isinstance(res, list):
            return [row["text"] for row in res if isinstance(row, dict) and "text" in row]  # type: ignore
        elif "result" in res and isinstance(res["result"], list):
            return [row["text"] for row in res["result"] if isinstance(row, dict) and "text" in row]  # type: ignore
        else:
            logger.error(f"[ERROR] Unexpected result format from SurrealDB: {res}")
            return None

    async def rag_chat(self, question: str, max_tokens: int = 400) -> str:
        """
        Perform a retrieval-augmented generation (RAG) chat with the OpenAI model.
        :param question: The question to ask the model.
        :param max_tokens: The maximum number of tokens to generate in the response (default: 400).
        :return: str: The model's response to the question.
        """
        if not self.client:
            raise ValueError("This function requires an OpenAI client to be initialized.")
        context = await self.get_context(question, k=4)

        if not context:
            return "I don't have enough information to answer that question."

        # Convert messages to proper ChatCompletionMessageParam format
        def to_message_param(role: str, content: str) -> ChatCompletionMessageParam:
            if role == "system":
                return cast(ChatCompletionMessageParam, {"role": "system", "content": content})
            elif role == "user":
                return cast(ChatCompletionMessageParam, {"role": "user", "content": content})
            else:
                raise ValueError(f"Unknown role: {role}")

        messages = [
            to_message_param("system", self.system_prompt),
            to_message_param("system", "Context:\n" + "\n".join(f"- {c}" for c in context)),
            to_message_param("user", question),
        ]
        
        answer = (await self.client.chat.completions.create(
            model=self.model, messages=messages, max_tokens=max_tokens
        )).choices[0].message.content
        return answer if answer is not None else ""
