""""""

class GraphController:
    """
    A controller class for graph operations in SurrealDB.
    This class leverages an existing DbController to perform graph-specific operations.
    """

    def __init__(self, db_controller):
        """
        Initialize the GraphController with an existing DbController

        :param db_controller: An instance of DbController or AsyncDbController
        """
        self.db = db_controller
        self._is_async = hasattr(db_controller.query, "__await__")

    def _execute(self, func, *args, **kwargs):
        """Helper method to handle sync/async execution"""
        if self._is_async:
            import asyncio
            return asyncio.ensure_future(func(*args, **kwargs))
        return func(*args, **kwargs)

    def relate(self, from_record, edge_table, to_record, edge_data=None):
        """
        Create a relationship between two records

        :param from_record: Source record ID (e.g., "person:123")
        :param edge_table: Edge table name (e.g., "order")
        :param to_record: Target record ID (e.g., "product:456")
        :param edge_data: Optional dictionary of data to set on the edge
        :return: The created edge record
        """
        # Base RELATE query
        query = f"RELATE {from_record} -> {edge_table}:ulid() -> {to_record}"

        # Add content if provided
        if edge_data:
            # Convert dict to SurrealQL content format
            content_parts = []
            for key, value in edge_data.items():
                # Handle special arrow syntax for references
                if isinstance(value, str) and value.startswith("->"):
                    content_parts.append(f"{key}: {value}")
                elif isinstance(value, str) and value.startswith("<-"):
                    content_parts.append(f"{key}: {value}")
                elif isinstance(value, str):
                    content_parts.append(f"{key}: \"{value}\"")
                else:
                    content_parts.append(f"{key}: {value}")

            content_str = ", ".join(content_parts)
            query += f" CONTENT {{ {content_str} }}"

        return self._execute(self.db.query, query)

    def get_relations(self, start_node: str, edge_table: str, end_table: str, direction: str = "->"):
        """
        Get records connected via outgoing relationships

        :param start_node: Starting node ID
        :param edge_table: Edge table to filter by
        :param end_table: Ending node ID
        :param direction: Direction of the relationship (default is "->")
        :return: Connected records
        """
        # Example: "SELECT ->HAS_SYMPTOM->symptom FROM diagnosis:depression"
        query = f"SELECT {direction}{edge_table}{direction}{end_table} FROM {start_node}"
        return self._execute(self.db.query, query)

    def count_connections(self):
        """
        TODO
        """
        query = ""
        return self._execute(self.db.query, query)

    def find_path(self):
        """
        TODO
        """
        query = ""
        return self._execute(self.db.query, query)


class AsyncGraphController:
    """
    An asynchronous controller class for graph operations in SurrealDB.
    """

    def __init__(self, async_db_controller):
        """
        Initialize the AsyncGraphController with an existing AsyncDbController

        :param async_db_controller: An instance of AsyncDbController
        """
        self.db = async_db_controller

    async def relate(self, from_record, edge_table, to_record, edge_data=None):
        """
        Create a relationship between two records

        :param from_record: Source record ID (e.g., "person:123")
        :param edge_table: Edge table name (e.g., "order")
        :param to_record: Target record ID (e.g., "product:456")
        :param edge_data: Optional dictionary of data to set on the edge
        :return: The created edge record
        """
        # Base RELATE query
        query = f"RELATE {from_record} -> {edge_table}:ulid() -> {to_record}"

        # Add content if provided
        if edge_data:
            # Convert dict to SurrealQL content format
            content_parts = []
            for key, value in edge_data.items():
                # Handle special arrow syntax for references
                if isinstance(value, str) and value.startswith("->"):
                    content_parts.append(f"{key}: {value}")
                elif isinstance(value, str) and value.startswith("<-"):
                    content_parts.append(f"{key}: {value}")
                elif isinstance(value, str):
                    content_parts.append(f"{key}: \"{value}\"")
                else:
                    content_parts.append(f"{key}: {value}")

            content_str = ", ".join(content_parts)
            query += f" CONTENT {{ {content_str} }}"

        return await self.db.query(query)

    async def get_relations(self, start_node: str, edge_table: str, end_table: str, direction: str = "->"):
        """
        Get records connected via outgoing relationships

        :param start_node: Starting node ID
        :param edge_table: Edge table to filter by
        :param end_table: Ending node ID
        :param direction: Direction of the relationship (default is "->")
        :return: Connected records
        """
        # Example: "SELECT ->HAS_SYMPTOM->symptom FROM diagnosis:depression"
        query = f"SELECT {direction}{edge_table}{direction}{end_table} FROM {start_node}"
        return await self.db.query(query)

    async def count_connections(self):
        """
        TODO
        """
        query = ""
        return await self.db.query(query)

    async def find_path(self):
        """
        TODO
        """
        query = ""
        return await self.db.query(query)
