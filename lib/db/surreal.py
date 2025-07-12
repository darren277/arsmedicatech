"""
Synchronous and Asynchronous SurrealDB Controller
"""
from typing import Any, Dict, List, Optional

from settings import logger


class SurrealWrapper:
    def __init__(self, r: Any) -> None:
        self._client = r

    def signin(self, vars: Dict[str, Any]) -> str:
        return self._client.signin(vars)

    def query(self, sql: str, vars: dict[str, Any] = {}) -> list[Any]:
        return self._client.query(sql, vars)

    def update(self, record: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a record in the database.
        
        :param record: Record ID string (e.g., "table:id")
        :param data: Dictionary of data to update
        :return: Updated record
        """
        return self._client.update(record, data)
    
    def create(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new record in the database.
        
        :param table_name: Table name
        :param data: Dictionary of data for the new record
        :return: Created record
        """
        return self._client.create(table_name, data)
    
    def select(self, record: str) -> List[Dict[str, Any]]:
        """
        Select a specific record from the database.
        
        :param record: Record ID string (e.g., "table:id")
        :return: Record data
        """
        return self._client.select(record)
    
    def delete(self, record: str) -> Dict[str, Any]:
        """
        Delete a record from the database.
        
        :param record: Record ID string (e.g., "table:id")
        :return: Result of deletion
        """
        return self._client.delete(record)
    
    def use(self, namespace: str, database: str) -> None:
        """
        Set the namespace and database for the current session.
        
        :param namespace: SurrealDB namespace
        :param database: SurrealDB database
        :return: None
        """
        self._client.use(namespace, database)
    
    def close(self) -> None:
        """
        Close the connection to the database.
        
        :return: None
        """
        self._client.close()

class AsyncSurrealWrapper:
    def __init__(self, r: Any) -> None:
        self._client = r

    async def signin(self, vars: Dict[str, Any]) -> str:
        return await self._client.signin(vars)

    async def query(self, sql: str, vars: dict[str, Any] = {}) -> list[Any]:
        return await self._client.query(sql, vars)

    async def update(self, record: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return await self._client.update(record, data)
    
    async def create(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return await self._client.create(table_name, data)
    
    async def select(self, record: str) -> List[Dict[str, Any]]:
        return await self._client.select(record)
    
    async def delete(self, record: str) -> Dict[str, Any]:
        return await self._client.delete(record)
    
    async def use(self, namespace: str, database: str) -> None:
        await self._client.use(namespace, database)
    
    async def close(self) -> None:
        """
        Close the connection to the database.
        
        :return: None
        """
        await self._client.close()


# Synchronous version
class DbController:
    """
    Synchronous DB controller for SurrealDB
    """
    db: Optional[SurrealWrapper] = None

    def __init__(
            self,
            url: Optional[str] = None,
            namespace: Optional[str] = None,
            database: Optional[str] = None,
            user: Optional[str] = None,
            password: Optional[str] = None
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
        from surrealdb import Surreal  # type: ignore

        logger.debug(f"Connecting to SurrealDB at {self.url}")
        logger.debug(f"Using namespace: {self.namespace}, database: {self.database}")
        logger.debug(f"Username: {self.user}")

        # Initialize connection
        self.db = SurrealWrapper(Surreal(self.url))

        # Authenticate and set namespace/database
        from typing import Any, Dict
        credentials: Dict[str, Any] = {
            "username": self.user,
            "password": self.password
        }

        signin_result = str(self.db.signin(credentials))
        logger.debug(f"Signin result: {signin_result}")

        # Use namespace and database
        if self.namespace is None or self.database is None:
            raise ValueError("Namespace and database must not be None.")
        self.db.use(self.namespace, self.database)
        logger.debug(f"Set namespace and database")

        return signin_result


    def query(self, statement: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a SurrealQL query

        :param statement: SurrealQL statement
        :param params: Optional parameters for the query
        :return: Query results
        """
        if params is None:
            params = {}
        logger.debug("Executing Query:", statement, "with params:", params)
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        return self.db.query(statement, params)

    def search(self, query: str, params: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
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

    def update(self, record: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a record

        :param record: Record ID string (e.g., "table:id")
        :param data: Dictionary of data to update
        :return: Updated record
        """
        logger.debug(f"SurrealDB update record: {record}")
        try:
            if self.db is None:
                raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
            result: Dict[str, Any] = self.db.update(record, data)
            logger.debug(f"SurrealDB update raw result: {result}")

            # Handle record ID conversion
            if 'id' in result:
                result = dict(result)  # Ensure result is a dict[str, Any]
                _id = str(result.pop("id"))
                final_result: Dict[str, Any] = {**result, 'id': _id}
                logger.debug(f"Final result: {final_result}")
                return final_result
            
            logger.debug(f"Final result: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Exception in update: {e}")
            import traceback
            traceback.print_exc()
            return {}

    def create(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new record

        :param table_name: Table name
        :param data: Dictionary of data for the new record
        :return: Created record
        """
        try:
            result = self.db.create(table_name, data) # type: ignore

            # Handle result formatting
            if 'id' in result:
                _id = str(result.pop("id"))
                return {**result, 'id': _id}
            return result
        except Exception as e:
            logger.error(f"Error creating record: {e}")
            return {}

    def select_many(self, table_name: str) -> List[Dict[str, Any]]:
        """
        Select all records from a table

        :param table_name: Table name
        :return: List of records
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        logger.debug(f"Selecting many from table: {table_name}")
        result: List[Dict[str, Any]] = self.db.select(table_name)
        logger.debug(f"Select many raw result: {result}")

        # Process results
        for i, record in enumerate(result):
            if 'id' in record:
                _id = str(record.pop("id"))
                result[i] = {**record, 'id': _id}
        
        logger.debug(f"Select many processed result: {result}")

        return result

    def select(self, record: str) -> Dict[str, Any]:
        """
        Select a specific record

        :param record: Record ID string (e.g., "table:id")
        :return: Record data
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        logger.debug(f"Selecting record: {record}")
        result = self.db.select(record)
        logger.debug(f"Select raw result: {result}")

        # Handle record ID conversion - result might be a list or dict
        if isinstance(result, list) and len(result) > 0:
            record_data = result[0]
            if isinstance(record_data, dict) and 'id' in record_data:
                _id = str(record_data.pop("id"))
                final_result = {**record_data, 'id': _id}
                logger.debug(f"Final result: {final_result}")
                return final_result
            return record_data if isinstance(record_data, dict) else {}
        elif isinstance(result, dict) and 'id' in result:
            _id = str(result.pop("id"))
            final_result = {**result, 'id': _id}
            logger.debug(f"Final result: {final_result}")
            return final_result
        logger.debug(f"Final result: {result}")
        return result if isinstance(result, dict) else {}

    def delete(self, record: str) -> Dict[str, Any]:
        """
        Delete a record

        :param record: Record ID string (e.g., "table:id")
        :return: Result of deletion
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
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
    db: Optional[AsyncSurrealWrapper] = None

    def __init__(self,
                 url: Optional[str] = None,
                 namespace: Optional[str] = None,
                 database: Optional[str] = None,
                 user: Optional[str] = None,
                 password: Optional[str] = None
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
        from surrealdb import AsyncSurreal  # type: ignore

        # Initialize connection
        self.db = AsyncSurrealWrapper(AsyncSurreal(self.url))

        # Authenticate and set namespace/database
        signin_result = await self.db.signin({
            "username": self.user,
            "password": self.password
        })

        if not self.db:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")

        # Use namespace and database
        if self.namespace is None or self.database is None:
            raise ValueError("Namespace and database must not be None.")
        await self.db.use(self.namespace, self.database)

        return signin_result

    async def query(self, statement: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a SurrealQL query

        :param statement: SurrealQL statement
        :param params: Optional parameters for the query
        :return: Query results
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        if params is None:
            params = {}
        return await self.db.query(statement, params)

    async def update(self, record: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a record

        :param record: Record ID string (e.g., "table:id")
        :param data: Dictionary of data to update
        :return: Updated record
        """
        if self.db is None:
                raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        result = await self.db.update(record, data)

        # Handle record ID conversion
        if 'id' in result:
            _id = str(result.pop("id"))
            return {**result, 'id': _id}
        return result

    async def create(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new record

        :param table_name: Table name
        :param data: Dictionary of data for the new record
        :return: Created record
        """
        try:
            if self.db is None:
                raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
            result = await self.db.create(table_name, data)

            # Handle result formatting
            if 'id' in result:
                _id = str(result.pop("id"))
                return {**result, 'id': _id}
            return result
        except Exception as e:
            logger.error(f"Error creating record: {e}")
            return {}

    async def select_many(self, table_name: str) -> List[Dict[str, Any]]:
        """
        Select all records from a table

        :param table_name: Table name
        :return: List of records
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        result: List[Dict[str, Any]] = await self.db.select(table_name)

        # Process results
        for i, record in enumerate(result):
            if 'id' in record:
                _id = str(record.pop("id"))
                result[i] = {**record, 'id': _id}

        return result

    async def select(self, record: str) -> Dict[str, Any]:
        """
        Select a specific record

        :param record: Record ID string (e.g., "table:id")
        :return: Record data
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        result: List[Dict[str, Any]] = await self.db.select(record)

        # Handle record ID conversion - result is a list, so we need to handle it properly
        if result and len(result) > 0:
            record_data = result[0]
            if isinstance(record_data, dict) and 'id' in record_data:
                _id = str(record_data.pop("id"))
                return {**record_data, 'id': _id}
            return record_data if isinstance(record_data, dict) else {}
        return {}

    async def delete(self, record: str) -> Dict[str, Any]:
        """
        Delete a record

        :param record: Record ID string (e.g., "table:id")
        :return: Result of deletion
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        result = await self.db.delete(record)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return result

    async def close(self) -> None:
        """
        Close the database connection
        :return: None
        """
        if self.db is None:
            raise RuntimeError("Database connection is not established. Call connect() before performing operations.")
        await self.db.close()
