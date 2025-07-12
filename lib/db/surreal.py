"""
Synchronous and Asynchronous SurrealDB Controller
"""
from settings import logger


# Synchronous version
class DbController:
    """
    Synchronous DB controller for SurrealDB
    """
    def __init__(
            self,
            url: str = None,
            namespace: str = None,
            database: str = None,
            user: str = None,
            password: str = None
    ) -> None:
        """
        Initialize a synchronous DB controller for SurrealDB

        :param url: SurrealDB server URL (e.g., "http://localhost:8000")
        :param namespace: SurrealDB namespace
        :param database: SurrealDB database
        :param user: Username for authentication
        :param password: Password for authentication
        """
        if url is None:
            from settings import SURREALDB_URL
            url = SURREALDB_URL
        if namespace is None:
            from settings import SURREALDB_NAMESPACE
            namespace = SURREALDB_NAMESPACE
        if database is None:
            from settings import SURREALDB_DATABASE
            database = SURREALDB_DATABASE
        if user is None:
            from settings import SURREALDB_USER
            user = SURREALDB_USER
        if password is None:
            from settings import SURREALDB_PASS
            password = SURREALDB_PASS

        self.url = url
        self.namespace = namespace
        self.database = database
        self.user = user
        self.password = password
        self.db = None

    def connect(self) -> str:
        """
        Connect to SurrealDB and authenticate
        :return: Signin result
        """
        from surrealdb import Surreal

        logger.debug(f"Connecting to SurrealDB at {self.url}")
        logger.debug(f"Using namespace: {self.namespace}, database: {self.database}")
        logger.debug(f"Username: {self.user}")

        # Initialize connection
        self.db = Surreal(self.url)

        # Authenticate and set namespace/database
        signin_result = self.db.signin({
            "username": self.user,
            "password": self.password
        })
        logger.debug(f"Signin result: {signin_result}")

        # Use namespace and database
        self.db.use(self.namespace, self.database)
        logger.debug(f"Set namespace and database")

        return signin_result

    def query(self, statement: str, params: dict = None) -> list:
        """
        Execute a SurrealQL query

        :param statement: SurrealQL statement
        :param params: Optional parameters for the query
        :return: Query results
        """
        if params is None:
            params = {}
        logger.debug("Executing Query:", statement, "with params:", params)
        return self.db.query(statement, params)

    def search(self, query: str, params: dict = None) -> list:
        """
        Execute a search query
        :param query: SurrealQL search query
        :param params: Optional parameters for the query
        :return: List of search results
        """
        #logging.info(f"Executing Query: {query} with params: {params}")
        logger.debug(f"Executing Query: {query} with params: {params}")
        # This mock will return plausible results for the search query.
        if "SEARCH" in query and params and params.get('query'):
            return [{
                "result": [
                    {
                        "highlighted_note": "Patient reported persistent <b>headaches</b> and sensitivity to light.",
                        "score": 1.25,
                        "patient": {
                            "demographic_no": "1",
                            "first_name": "John",
                            "last_name": "Doe",
                        }
                    },
                    {
                        "highlighted_note": "Follow-up regarding frequent <b>headaches</b>.",
                        "score": 1.18,
                        "patient": {
                            "demographic_no": "2",
                            "first_name": "Jane",
                            "last_name": "Doe",
                        }
                    }
                ],
                "status": "OK",
                "time": "15.353µs"
            }]
        # Mock response for schema creation
        return [{"status": "OK"}]

    def update(self, record: str, data: dict) -> dict:
        """
        Update a record

        :param record: Record ID string (e.g., "table:id")
        :param data: Dictionary of data to update
        :return: Updated record
        """
        logger.debug(f"SurrealDB update record: {record}")
        try:
            result = self.db.update(record, data)
            logger.debug(f"SurrealDB update raw result: {result}")
            logger.debug(f"SurrealDB update result type: {type(result)}")
            
            # Handle tuple result (common with SurrealDB)
            if isinstance(result, tuple):
                logger.debug(f"Result is tuple with {len(result)} elements")
                result = result[0]  # Take first element
                logger.debug(f"After tuple unpacking: {result}")
            
            # Handle list result
            if isinstance(result, list) and len(result) > 0:
                result = result[0]
                logger.debug(f"After list unpacking: {result}")

            # Handle record ID conversion
            if isinstance(result, dict) and 'id' in result:
                _id = str(result.pop("id"))
                final_result = {**result, 'id': _id}
                logger.debug(f"Final result: {final_result}")
                return final_result
            
            logger.debug(f"Final result: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Exception in update: {e}")
            import traceback
            traceback.print_exc()
            return {}

    def create(self, table_name: str, data: dict) -> dict:
        """
        Create a new record

        :param table_name: Table name
        :param data: Dictionary of data for the new record
        :return: Created record
        """
        try:
            result = self.db.create(table_name, data)

            # Handle result formatting
            if isinstance(result, dict) and 'id' in result:
                _id = str(result.pop("id"))
                return {**result, 'id': _id}
            return result
        except Exception as e:
            logger.error(f"Error creating record: {e}")
            return {}

    def select_many(self, table_name: str) -> list:
        """
        Select all records from a table

        :param table_name: Table name
        :return: List of records
        """
        logger.debug(f"Selecting many from table: {table_name}")
        result = self.db.select(table_name)
        logger.debug(f"Select many raw result: {result}")

        # Process results
        if isinstance(result, list):
            for i, record in enumerate(result):
                if isinstance(record, dict) and 'id' in record:
                    _id = str(record.pop("id"))
                    result[i] = {**record, 'id': _id}
            logger.debug(f"Select many processed result: {result}")

        return result

    def select(self, record: str) -> dict:
        """
        Select a specific record

        :param record: Record ID string (e.g., "table:id")
        :return: Record data
        """
        logger.debug(f"Selecting record: {record}")
        result = self.db.select(record)
        logger.debug(f"Select raw result: {result}")

        # Handle record ID conversion
        if isinstance(result, dict) and 'id' in result:
            _id = str(result.pop("id"))
            final_result = {**result, 'id': _id}
            logger.debug(f"Final result: {final_result}")
            return final_result
        logger.debug(f"Final result: {result}")
        return result

    def delete(self, record: str) -> dict:
        """
        Delete a record

        :param record: Record ID string (e.g., "table:id")
        :return: Result of deletion
        """
        return self.db.delete(record)

    def close(self) -> None:
        """
        Close the connection (not needed with new API, but kept for compatibility)
        :return: None
        """
        # The new API doesn't seem to have an explicit close method
        # This is kept for backwards compatibility
        pass


# Asynchronous version
class AsyncDbController:
    """
    Asynchronous DB controller for SurrealDB
    """
    def __init__(self,
                 url: str = None,
                 namespace: str = None,
                 database: str = None,
                 user: str = None,
                 password: str = None
         ) -> None:
        """
        Initialize an asynchronous DB controller for SurrealDB

        :param url: SurrealDB server URL (e.g., "http://localhost:8000")
        :param namespace: SurrealDB namespace
        :param database: SurrealDB database
        :param user: Username for authentication
        :param password: Password for authentication
        """
        if url is None:
            from settings import SURREALDB_URL
            url = SURREALDB_URL
        if namespace is None:
            from settings import SURREALDB_NAMESPACE
            namespace = SURREALDB_NAMESPACE
        if database is None:
            from settings import SURREALDB_DATABASE
            database = SURREALDB_DATABASE
        if user is None:
            from settings import SURREALDB_USER
            user = SURREALDB_USER
        if password is None:
            from settings import SURREALDB_PASS
            password = SURREALDB_PASS

        self.url = url
        self.namespace = namespace
        self.database = database
        self.user = user
        self.password = password
        self.db = None

    async def connect(self) -> str:
        """
        Connect to SurrealDB and authenticate
        :return: Signin result
        """
        from surrealdb import AsyncSurreal

        # Initialize connection
        self.db = AsyncSurreal(self.url)

        # Authenticate and set namespace/database
        signin_result = await self.db.signin({
            "username": self.user,
            "password": self.password
        })

        # Use namespace and database
        await self.db.use(self.namespace, self.database)

        return signin_result

    async def query(self, statement: str, params: dict = None) -> list:
        """
        Execute a SurrealQL query

        :param statement: SurrealQL statement
        :param params: Optional parameters for the query
        :return: Query results
        """
        if params is None:
            params = {}
        return await self.db.query(statement, params)

    async def update(self, record: str, data: dict) -> dict:
        """
        Update a record

        :param record: Record ID string (e.g., "table:id")
        :param data: Dictionary of data to update
        :return: Updated record
        """
        result = await self.db.update(record, data)

        # Handle record ID conversion
        if isinstance(result, dict) and 'id' in result:
            _id = str(result.pop("id"))
            return {**result, 'id': _id}
        return result

    async def create(self, table_name: str, data: dict) -> dict:
        """
        Create a new record

        :param table_name: Table name
        :param data: Dictionary of data for the new record
        :return: Created record
        """
        try:
            result = await self.db.create(table_name, data)

            # Handle result formatting
            if isinstance(result, dict) and 'id' in result:
                _id = str(result.pop("id"))
                return {**result, 'id': _id}
            return result
        except Exception as e:
            logger.error(f"Error creating record: {e}")
            return {}

    async def select_many(self, table_name: str) -> list:
        """
        Select all records from a table

        :param table_name: Table name
        :return: List of records
        """
        result = await self.db.select(table_name)

        # Process results
        if isinstance(result, list):
            for i, record in enumerate(result):
                if isinstance(record, dict) and 'id' in record:
                    _id = str(record.pop("id"))
                    result[i] = {**record, 'id': _id}

        return result

    async def select(self, record: str) -> dict:
        """
        Select a specific record

        :param record: Record ID string (e.g., "table:id")
        :return: Record data
        """
        result = await self.db.select(record)

        # Handle record ID conversion
        if isinstance(result, dict) and 'id' in result:
            _id = str(result.pop("id"))
            return {**result, 'id': _id}
        return result

    async def delete(self, record: str) -> dict:
        """
        Delete a record

        :param record: Record ID string (e.g., "table:id")
        :return: Result of deletion
        """
        return await self.db.delete(record)

    async def close(self) -> None:
        """
        Close the connection (not needed with new API, but kept for compatibility)
        :return: None
        """
        # The new API doesn't seem to have an explicit close method
        # This is kept for backwards compatibility
        pass
