""""""
import asyncio

from openai import AsyncOpenAI

from lib.db.vec import Vec
from settings import MIGRATION_OPENAI_API_KEY


def init_vec():
    client = AsyncOpenAI(api_key=MIGRATION_OPENAI_API_KEY)
    vec = Vec(client)

    print("Initializing vector database...")
    asyncio.run(vec.init())

    print("Seeding vector database with documents...")
    asyncio.run(vec.seed("lib/migrations/rag_docs.json"))

    print("Vector database initialized and seeded successfully.")

if __name__ == "__main__":
    init_vec()
    print("Vector database migration completed.")
