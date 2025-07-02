""""""
import os
from os.path import join, dirname

from dotenv import load_dotenv

from logger import Logger

logger = Logger()

logger.info = print


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


SURREALDB_NAMESPACE = os.environ.get("SURREALDB_NAMESPACE")
SURREALDB_DATABASE = os.environ.get("SURREALDB_DATABASE")
SURREALDB_URL = os.environ.get("SURREALDB_URL")
SURREALDB_USER = os.environ.get("SURREALDB_USER")
SURREALDB_PASS = os.environ.get("SURREALDB_PASS")

SURREALDB_PROTOCOL = os.environ.get("SURREALDB_PROTOCOL", 'ws')
SURREALDB_HOST = os.environ.get("SURREALDB_HOST", 'localhost')
SURREALDB_PORT = os.environ.get("SURREALDB_PORT", 8700)

SURREALDB_ICD_DB = os.environ.get("SURREALDB_ICD_DB", 'diagnosis')

print("SUREALDB_NAMESPACE:", SURREALDB_NAMESPACE)
print("SURREALDB_DATABASE:", SURREALDB_DATABASE)
print("SURREALDB_URL:", SURREALDB_URL)
print("SURREALDB_USER:", SURREALDB_USER)
print("SURREALDB_PASS:", SURREALDB_PASS)

PORT = os.environ.get('PORT', 5000)
DEBUG = os.environ.get('DEBUG', True)
HOST = os.environ.get('HOST', '0.0.0.0')

print("PORT:", PORT)
print("DEBUG:", DEBUG)
print("HOST:", HOST)


OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
