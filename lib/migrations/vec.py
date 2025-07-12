"""
Vector database migration script.
"""
import asyncio

from openai import AsyncOpenAI

from lib.db.vec import Vec
from settings import MIGRATION_OPENAI_API_KEY

from settings import logger


def init_vec() -> None:
    """
    Initialize and seed the vector database with documents.
    :return: None
    """
    client = AsyncOpenAI(api_key=MIGRATION_OPENAI_API_KEY)
    vec = Vec(client)

    logger.debug("Initializing vector database...")
    try:
        asyncio.run(vec.init())
    except Exception as e:
        logger.error(f"Failed to initialize vector database: {e}")
        return

    logger.debug("Seeding vector database with documents...")
    try:
        asyncio.run(vec.seed("lib/migrations/rag_docs.json"))
    except Exception as e:
        logger.error(f"Failed to seed vector database: {e}")
        return

    logger.debug("Vector database initialized and seeded successfully.")

if __name__ == "__main__":
    init_vec()
    logger.debug("Vector database migration completed.")
