""""""
import csv
import asyncio
from surrealdb import AsyncSurreal

from settings import SURREALDB_NAMESPACE, SURREALDB_ICD_DB
from settings import SURREALDB_USER, SURREALDB_PASS
from settings import SURREALDB_URL


async def import_icd_codes(csv_file_path):
    db = AsyncSurreal(SURREALDB_URL)
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    await db.signin({'username': SURREALDB_USER, 'password': SURREALDB_PASS})

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        i = 0
        for row in reader:
            i += 1
            print(row)
            icd_code = row['CODE']
            short_description = row['SHORT DESCRIPTION (VALID ICD-10 FY2025)']

            await db.create(f"icd:{icd_code}", {"code": icd_code, "description": short_description})

            if i % 100 == 0:
                print(f"{i} records inserted...")

    print(f"{i} ICD codes imported successfully!")
    await db.close()


async def define_index():
    q = "DEFINE INDEX code_idx ON TABLE icd COLUMNS code;"

    db = AsyncSurreal(SURREALDB_URL)
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    await db.signin({'username': SURREALDB_USER, 'password': SURREALDB_PASS})

    # Define the index
    await db.query(q)

    await db.close()



async def search_icd_by_description(search_term):
    db = AsyncSurreal(SURREALDB_URL)
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


async def lookup_icd_code(icd_code):
    db = AsyncSurreal(SURREALDB_URL)
    await db.use(SURREALDB_NAMESPACE, SURREALDB_ICD_DB)
    await db.signin({'username': SURREALDB_USER, 'password': SURREALDB_PASS})

    # Query the specific ICD code
    # TODO: Does not work?
    #result = await db.select(f"icd:{icd_code}")
    #print("RESULT", result)

    query = f"SELECT * FROM icd WHERE code = '{icd_code}';"
    result = await db.query(query)
    print(f"Alternative query result: {result}")

    await db.close()

    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("To migrate ICD data from CSV to SurrealDB: python lib/models/icd.py migrate <path_to_csv>")
        print("To search for an ICD code: python lib/models/icd.py search <search_term> (ex: A000)")
        sys.exit(1)

    if sys.argv[1] == "migrate":
        if len(sys.argv) < 3:
            print("Please provide the path to the CSV file.")
            sys.exit(1)

        path_to_csv = sys.argv[2]

        # Migrate
        asyncio.run(import_icd_codes(path_to_csv))

        # Define index
        asyncio.run(define_index())

    elif sys.argv[1] == "search":
        icd_code = sys.argv[2]

        result = asyncio.run(lookup_icd_code(icd_code))
        print(result)
