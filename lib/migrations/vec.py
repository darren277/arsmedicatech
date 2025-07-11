""""""
import asyncio

from openai import AsyncOpenAI

from lib.db.vec import Vec
from settings import MIGRATION_OPENAI_API_KEY

from settings import logger


def init_vec():
    client = AsyncOpenAI(api_key=MIGRATION_OPENAI_API_KEY)
    vec = Vec(client)

    logger.debug("Initializing vector database...")
    asyncio.run(vec.init())

    logger.debug("Seeding vector database with documents...")
    asyncio.run(vec.seed("lib/migrations/rag_docs.json"))

    logger.debug("Vector database initialized and seeded successfully.")

if __name__ == "__main__":
    init_vec()
    logger.debug("Vector database migration completed.")
