"""
This module defines a Clinic class and provides functions to interact with a SurrealDB database.
"""
import json

from surrealdb import Surreal

from lib.db.surreal import AsyncDbController

from settings import logger


class Clinic:
    """
    Represents a medical clinic with its address and geospatial location.
    """
    def __init__(
            self,
            name: str,
            street: str,
            city: str,
            state: str,
            zip_code: str,
            longitude: float,
            latitude: float
    ) -> None:
        """
        Initializes a Clinic object.

        Args:
            name (str): The name of the clinic.
            street (str): The street address.
            city (str): The city.
            state (str): The state or province.
            zip_code (str): The postal or ZIP code.
            longitude (float): The longitude of the clinic's location.
            latitude (float): The latitude of the clinic's location.
        """
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.longitude = longitude
        self.latitude = latitude

    def to_geojson_point(self) -> dict:
        """
        Converts the clinic's location to a GeoJSON Point dictionary.
        Note: GeoJSON specifies longitude, then latitude.

        :return: A dictionary representing the clinic's location in GeoJSON format.
        """
        return {
            "type": "Point",
            "coordinates": [self.longitude, self.latitude]
        }

    def __repr__(self) -> str:
        """
        Provides a string representation of the Clinic object.
        """
        return (f"Clinic(name='{self.name}', address='{self.street}, {self.city}, {self.state} {self.zip_code}', location=({self.longitude}, {self.latitude}))")

def generate_surrealql_create_query(clinic: Clinic, table_name: str = "clinic") -> str:
    """
    Generates a SurrealQL CREATE statement for a given Clinic object.

    Args:
        clinic (Clinic): The clinic object to create a query for.
        table_name (str): The name of the table to insert the clinic into.

    Returns:
        str: A SurrealQL CREATE statement string.
    """
    # Using a dictionary to build the SET clause for clarity and easier JSON conversion
    data_to_set = {
        "name": clinic.name,
        "address": {
            "street": clinic.street,
            "city": clinic.city,
            "state": clinic.state,
            "zip": clinic.zip_code
        },
        "location": clinic.to_geojson_point()
    }

    # SurrealDB's query language can often take JSON directly for the SET clause.
    # We will format this into a string.
    # We use json.dumps to handle proper string quoting and formatting.
    set_clause = json.dumps(data_to_set, indent=4)

    # The record ID can be generated or based on some unique property.
    # For this example, we'll create a simplified version of the name for the ID.
    record_id = clinic.name.lower().replace(" ", "_").replace("'", "")

    query = f"CREATE {table_name}:{record_id} CONTENT {set_clause};"

    return query

if __name__ == '__main__':
    # Define a schema for the clinic table for strong data typing.
    logger.debug("-- Schema Definition (run this once)")
    logger.debug("DEFINE TABLE clinic SCHEMAFULL;")
    logger.debug("DEFINE FIELD name ON clinic TYPE string;")
    logger.debug("DEFINE FIELD address ON clinic TYPE object;")
    logger.debug("DEFINE FIELD address.street ON clinic TYPE string;")
    logger.debug("DEFINE FIELD address.city ON clinic TYPE string;")
    logger.debug("DEFINE FIELD address.state ON clinic TYPE string;")
    logger.debug("DEFINE FIELD address.zip ON clinic TYPE string;")
    logger.debug("DEFINE FIELD location ON clinic TYPE geometry (point);")
    logger.debug("-" * 30)

    # Create instances of the Clinic class for some sample clinics.
    # Coordinates are in (longitude, latitude) order.
    clinic1 = Clinic(
        name="Downtown Health Clinic",
        street="123 Main St",
        city="Metropolis",
        state="CA",
        zip_code="90210",
        longitude=-118.40,
        latitude=34.07
    )

    clinic2 = Clinic(
        name="Uptown Wellness Center",
        street="456 Oak Ave",
        city="Metropolis",
        state="CA",
        zip_code="90212",
        longitude=-118.42,
        latitude=34.09
    )

    clinic3 = Clinic(
        name="Seaside Medical Group",
        street="789 Ocean Blvd",
        city="Bayview",
        state="CA",
        zip_code="90215",
        longitude=-118.49,
        latitude=34.01
    )

    # Generate and print the SurrealQL queries
    logger.debug("-- Generated SurrealQL CREATE Statements")
    query1 = generate_surrealql_create_query(clinic1)
    logger.debug(query1)

    query2 = generate_surrealql_create_query(clinic2)
    logger.debug(query2)

    query3 = generate_surrealql_create_query(clinic3)
    logger.debug(query3)

    # Example of how you might query this data
    logger.debug("-" * 30)
    logger.debug("-- Example Query: Find clinics within 5km of a point")
    # A point somewhere in Metropolis
    search_point_lon = -118.41
    search_point_lat = 34.08
    logger.debug(f"SELECT name, address, location, geo::distance(location, ({search_point_lon}, {search_point_lat})) AS distance")
    logger.debug(f"FROM clinic")
    logger.debug(f"WHERE geo::distance(location, ({search_point_lon}, {search_point_lat})) < 5000;")


client = AsyncDbController()


async def create_clinic(clinic: Clinic):
    """
    Asynchronously creates a clinic record in the SurrealDB database.

    Args:
        clinic (Clinic): The clinic object to be created in the database.

    Returns:
        str: The ID of the created clinic record.
    """
    query = generate_surrealql_create_query(clinic)
    result = await client.query(query)
    logger.debug('result', type(result), result)
    return result[0]['id'] if result else None


async def get_clinic_by_id(clinic_id: str):
    """
    Asynchronously retrieves a clinic record by its ID.

    Args:
        clinic_id (str): The ID of the clinic to retrieve.

    Returns:
        dict: The clinic record if found, otherwise None.
    """
    query = f"SELECT * FROM clinic WHERE id = '{clinic_id}';"
    result = await client.query(query)
    return result[0] if result else None


async def get_all_clinics() -> list:
    """
    Asynchronously retrieves all clinic records from the database.

    Returns:
        list: A list of all clinic records.
    """
    query = "SELECT * FROM clinic;"
    result = await client.query(query)
    return result if result else []


async def search_clinics_by_location(longitude: float, latitude: float, radius: float = 5000):
    """
    Asynchronously searches for clinics within a specified radius of a given location.

    Args:
        longitude (float): The longitude of the search point.
        latitude (float): The latitude of the search point.
        radius (float): The search radius in meters (default is 5000).

    Returns:
        list: A list of clinics within the specified radius.
    """
    query = f"""
    SELECT name, address, location, geo::distance(location, ({longitude}, {latitude})) AS distance
    FROM clinic
    WHERE geo::distance(location, ({longitude}, {latitude})) < {radius};
    """
    result = await client.query(query)
    return result if result else []


async def update_clinic(clinic_id: str, clinic: Clinic):
    """
    Asynchronously updates a clinic record in the database.

    Args:
        clinic_id (str): The ID of the clinic to update.
        clinic (Clinic): The updated clinic object.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    query = f"""
    UPDATE clinic:{clinic_id} SET
        name = '{clinic.name}',
        address = {{
            street: '{clinic.street}',
            city: '{clinic.city}',
            state: '{clinic.state}',
            zip: '{clinic.zip_code}'
        }},
        location = {json.dumps(clinic.to_geojson_point())}
    ;
    """
    result = await client.query(query)
    return len(result) > 0


async def delete_clinic(clinic_id: str):
    """
    Asynchronously deletes a clinic record from the database.

    Args:
        clinic_id (str): The ID of the clinic to delete.

    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
    query = f"DELETE FROM clinic WHERE id = '{clinic_id}';"
    result = await client.query(query)
    return len(result) > 0


def km_m(meters: float) -> float:
    """
    Converts kilometers to meters.

    Args:
        meters (float): The distance in kilometers.

    Returns:
        float: The distance in meters.
    """
    return meters * 1000


def test() -> None:
    """
    Test function to demonstrate the functionality of the Clinic class and database operations.
    :return: None
    """
    import asyncio
    import random

    async def run_tests() -> None:
        """
        Runs a series of tests to demonstrate the functionality of the Clinic class and database operations.
        :return: None
        """
        await client.connect()

        random_name = f"Clinic {random.randint(1, 1000)}"

        lon = random.uniform(-115.0, -120.0)
        lat = random.uniform(30.0, 35.0)

        # Create a clinic
        clinic = Clinic(
            name=random_name,
            street="123 Test St",
            city="Test City",
            state="TS",
            zip_code="12345",
            longitude=lon,
            latitude=lat
        )
        clinic_id = await create_clinic(clinic)
        logger.debug(f"Created clinic with ID: {clinic_id}")

        # Retrieve the clinic by ID
        retrieved_clinic = await get_clinic_by_id(clinic_id)
        logger.debug(f"Retrieved clinic: {retrieved_clinic}")

        # Update the clinic
        #clinic.name = "Updated Test Clinic"
        #updated = await update_clinic(clinic_id, clinic)
        #logger.debug(f"Clinic updated: {updated}")

        # Search clinics by location
        nearby_clinics = await search_clinics_by_location(-118.0, 34.0, radius=km_m(100))
        logger.debug(f"Nearby clinics: {nearby_clinics}")

        # Delete the clinic
        #deleted = await delete_clinic(clinic_id)
        #logger.debug(f"Clinic deleted: {deleted}")

    asyncio.run(run_tests())


if __name__ == "__main__":
    test()
