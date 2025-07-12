"""
ICD Code Management with SurrealDB
"""
import asyncio
import csv
from typing import Any, Dict, List

from surrealdb import AsyncSurreal  # type: ignore

from lib.services.apis import ICD10Code
from settings import (SURREALDB_ICD_DB, SURREALDB_NAMESPACE, SURREALDB_PASS,
                      SURREALDB_URL, SURREALDB_USER, logger)


async def import_icd_codes(csv_file_path: str) -> None:
    """
    Imports ICD codes from a CSV file into SurrealDB.
    The CSV file should have the following columns:
    - CODE
    - SHORT DESCRIPTION (VALID ICD-10 FY2025)
    The function connects to SurrealDB, reads the CSV file, and inserts each ICD code
    with its description into the `icd` table.
    The `icd` table is expected to have a structure like:
    {
        "code": "ICD_CODE",
        "description": "SHORT_DESCRIPTION"
    }
    The function also logs the progress of the import operation.
    It creates a new record for each ICD code in the format `icd:ICD_CODE`.
    The function does not return any value but logs the number of records inserted.
    :param csv_file_path: str - Path to the CSV file containing ICD codes and descriptions.
    :return: None
    """
    db = AsyncSurreal(SURREALDB_URL)
    if not SURREALDB_NAMESPACE or not SURREALDB_ICD_DB:
        raise ValueError("SURREALDB_NAMESPACE and SURREALDB_ICD_DB must not be empty")
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    if SURREALDB_USER is None or SURREALDB_PASS is None:
        raise ValueError("SURREALDB_USER and SURREALDB_PASS must not be None")
    
    credentials: Dict[str, Any] = {'username': SURREALDB_USER, 'password': SURREALDB_PASS}
    await db.signin(credentials)

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        i = 0
        for row in reader:
            i += 1
            logger.debug(str(row))
            icd_code = row['CODE']
            short_description = row['SHORT DESCRIPTION (VALID ICD-10 FY2025)']

            await db.create(f"icd:{icd_code}", {"code": icd_code, "description": short_description})

            if i % 100 == 0:
                logger.debug(f"{i} records inserted...")

    logger.debug(f"{i} ICD codes imported successfully!")
    await db.close()


async def define_index() -> None:
    """
    Defines an index on the `icd` table for the `code` column.
    :return: None
    """
    q = "DEFINE INDEX code_idx ON TABLE icd COLUMNS code;"

    db = AsyncSurreal(SURREALDB_URL)
    if not SURREALDB_NAMESPACE or not SURREALDB_ICD_DB:
        raise ValueError("SURREALDB_NAMESPACE and SURREALDB_ICD_DB must not be empty")
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    await db.signin({'username': SURREALDB_USER, 'password': SURREALDB_PASS})

    # Define the index
    await db.query(q)

    await db.close()



async def search_icd_by_description(search_term: str) -> List[Dict[str, Any]]:
    """
    Searches for ICD codes by description using a case-sensitive search.
    :param search_term: str - The term to search for in the ICD descriptions.
    :return: list - A list of ICD records that match the search term.
    """
    db = AsyncSurreal(SURREALDB_URL)
    if not SURREALDB_NAMESPACE or not SURREALDB_ICD_DB:
        raise ValueError("SURREALDB_NAMESPACE and SURREALDB_ICD_DB must not be empty")
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    await db.signin({'username': SURREALDB_USER, 'password': SURREALDB_PASS})

    # Use SurrealQL to search for matching descriptions
    # The CONTAINS operator performs a case-sensitive search
    query = "SELECT * FROM icd WHERE description CONTAINS $search"
    results = await db.query(query, {"search": search_term})

    await db.close()

    if results and len(results) > 0 and 'result' in results[0]:
        return results[0]['result']
    else:
        return []


async def lookup_icd_code(icd_code: ICD10Code) -> dict | None:
    """
    Looks up an ICD code in the SurrealDB database.
    :param icd_code: ICD10Code - The ICD code to look up.
    :return: dict | None - The ICD record if found, otherwise None.
    """
    if not icd_code:
        logger.debug("No ICD code provided for lookup.")
        return None

    if not icd_code.validate():
        logger.debug(f"Invalid ICD code: {icd_code}")
        return None

    db = AsyncSurreal(SURREALDB_URL)
    if not SURREALDB_NAMESPACE or not SURREALDB_ICD_DB:
        raise ValueError("SURREALDB_NAMESPACE and SURREALDB_ICD_DB must not be empty")
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    await db.signin({'username': SURREALDB_USER, 'password': SURREALDB_PASS})

    # Query the specific ICD code
    # TODO: Does not work?
    #result = await db.select(f"icd:{icd_code}")
    #logger.debug("RESULT", result)

    query = f"SELECT * FROM icd WHERE code = '{icd_code}';"
    result = await db.query(query)
    logger.debug(f"Alternative query result: {result}")

    await db.close()

    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        logger.debug("Usage:")
        logger.debug("To migrate ICD data from CSV to SurrealDB: python lib/models/icd.py migrate <path_to_csv>")
        logger.debug("To search for an ICD code: python lib/models/icd.py search <search_term> (ex: A000)")
        sys.exit(1)

    if sys.argv[1] == "migrate":
        if len(sys.argv) < 3:
            logger.debug("Please provide the path to the CSV file.")
            sys.exit(1)

        path_to_csv = sys.argv[2]

        # Migrate
        asyncio.run(import_icd_codes(path_to_csv))

        # Define index
        asyncio.run(define_index())

    elif sys.argv[1] == "search":
        icd_code = sys.argv[2]

        result = asyncio.run(lookup_icd_code(icd_code))
        logger.debug(result)
