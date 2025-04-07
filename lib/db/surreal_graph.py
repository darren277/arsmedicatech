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

    def find_connected(self, record_id, edge_table=None, direction="out", limit=100):
        """
        Find records connected to the given record

        :param record_id: Record ID to find connections for
        :param edge_table: Optional edge table to filter by (None for all connections)
        :param direction: Direction of relationship - "out", "in", or "both"
        :param limit: Maximum number of results to return
        :return: List of connected records
        """
        if edge_table:
            if direction == "out":
                query = f"SELECT ->{edge_table}->id AS connected FROM {record_id} LIMIT {limit}"
            elif direction == "in":
                query = f"SELECT <-{edge_table}<-id AS connected FROM {record_id} LIMIT {limit}"
            else:  # both
                query = f"""
                SELECT 
                    ->{edge_table}->id as outgoing, 
                    <-{edge_table}<-id as incoming 
                FROM {record_id} 
                LIMIT {limit}
                """
        else:
            if direction == "out":
                query = f"SELECT ->->id AS connected FROM {record_id} LIMIT {limit}"
            elif direction == "in":
                query = f"SELECT <-<-id AS connected FROM {record_id} LIMIT {limit}"
            else:  # both
                query = f"""
                SELECT 
                    ->->id as outgoing, 
                    <-<-id as incoming 
                FROM {record_id} 
                LIMIT {limit}
                """

        return self._execute(self.db.query, query)

    def find_path(self, from_record, to_record, max_depth=3):
        """
        Find paths between two records

        :param from_record: Starting record ID
        :param to_record: Ending record ID
        :param max_depth: Maximum path depth to search
        :return: List of paths between the records
        """
        query = f"""
        SELECT 
            array::len(path) AS length,
            path
        FROM 
            (SELECT path FROM {from_record} TO {to_record} LIMIT BY {max_depth})
        ORDER BY length
        """
        return self._execute(self.db.query, query)

    def count_connections(self, record_id, edge_table=None):
        """
        Count the number of connections for a record

        :param record_id: Record ID to count connections for
        :param edge_table: Optional edge table to filter by
        :return: Dictionary with counts for incoming and outgoing connections
        """
        if edge_table:
            query = f"""
            SELECT 
                count(->({edge_table})->*) AS outgoing,
                count(<-({edge_table})<-*) AS incoming
            FROM {record_id}
            """
        else:
            query = f"""
            SELECT 
                count(->*->*) AS outgoing,
                count(<-*<-*) AS incoming
            FROM {record_id}
            """
        return self._execute(self.db.query, query)

    def traverse(self, start_record, edge_tables=None, direction="out", depth=1, where_clause=None):
        """
        Traverse the graph starting from a record

        :param start_record: Starting record ID
        :param edge_tables: Optional list of edge tables to traverse (None for all)
        :param direction: Direction of traversal - "out", "in", or "both"
        :param depth: Depth of traversal
        :param where_clause: Optional WHERE clause for filtering
        :return: Results of the traversal
        """
        # Construct the edge table portion of the query
        edge_part = ""
        if edge_tables:
            if isinstance(edge_tables, list):
                edge_list = ", ".join([f"'{table}'" for table in edge_tables])
                edge_part = f"[{edge_list}]"
            else:
                edge_part = f"['{edge_tables}']"

        # Construct the traversal part based on direction
        if direction == "out":
            traversal = f"->|{depth}{edge_part}->*"
        elif direction == "in":
            traversal = f"<-|{depth}{edge_part}<-*"
        else:  # both
            # For "both", we'll do two separate queries
            out_query = f"SELECT ->|{depth}{edge_part}->* AS results FROM {start_record}"
            in_query = f"SELECT <-|{depth}{edge_part}<-* AS results FROM {start_record}"

            if where_clause:
                out_query += f" WHERE {where_clause}"
                in_query += f" WHERE {where_clause}"

            # Return a combined result
            out_result = self._execute(self.db.query, out_query)
            in_result = self._execute(self.db.query, in_query)

            # For async, we need to handle this differently
            if self._is_async:
                import asyncio

                async def combined():
                    out = await out_result
                    inn = await in_result
                    return {"outgoing": out, "incoming": inn}

                return asyncio.ensure_future(combined())

            return {"outgoing": out_result, "incoming": in_result}

        # Construct the complete query for single direction
        query = f"SELECT {traversal} AS results FROM {start_record}"
        if where_clause:
            query += f" WHERE {where_clause}"

        return self._execute(self.db.query, query)

    def get_edge(self, edge_id):
        """
        Get an edge by its ID

        :param edge_id: Edge ID (e.g., "order:123")
        :return: Edge data including connected records
        """
        query = f"""
        SELECT 
            *,
            ->* as outgoing,
            <-* as incoming
        FROM {edge_id}
        """
        return self._execute(self.db.query, query)


# Async Graph Controller with explicit async methods
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

    async def find_connected(self, record_id, edge_table=None, direction="out", limit=100):
        """
        Find records connected to the given record

        :param record_id: Record ID to find connections for
        :param edge_table: Optional edge table to filter by (None for all connections)
        :param direction: Direction of relationship - "out", "in", or "both"
        :param limit: Maximum number of results to return
        :return: List of connected records
        """
        if edge_table:
            if direction == "out":
                query = f"SELECT ->{edge_table}->id AS connected FROM {record_id} LIMIT {limit}"
            elif direction == "in":
                query = f"SELECT <-{edge_table}<-id AS connected FROM {record_id} LIMIT {limit}"
            else:  # both
                query = f"""
                SELECT 
                    ->{edge_table}->id as outgoing, 
                    <-{edge_table}<-id as incoming 
                FROM {record_id} 
                LIMIT {limit}
                """
        else:
            if direction == "out":
                query = f"SELECT ->->id AS connected FROM {record_id} LIMIT {limit}"
            elif direction == "in":
                query = f"SELECT <-<-id AS connected FROM {record_id} LIMIT {limit}"
            else:  # both
                query = f"""
                SELECT 
                    ->->id as outgoing, 
                    <-<-id as incoming 
                FROM {record_id} 
                LIMIT {limit}
                """

        return await self.db.query(query)

    async def find_path(self, from_record, to_record, max_depth=3):
        """
        Find paths between two records

        :param from_record: Starting record ID
        :param to_record: Ending record ID
        :param max_depth: Maximum path depth to search
        :return: List of paths between the records
        """
        query = f"""
        SELECT 
            array::len(path) AS length,
            path
        FROM 
            (SELECT path FROM {from_record} TO {to_record} LIMIT BY {max_depth})
        ORDER BY length
        """
        return await self.db.query(query)

    async def count_connections(self, record_id, edge_table=None):
        """
        Count the number of connections for a record

        :param record_id: Record ID to count connections for
        :param edge_table: Optional edge table to filter by
        :return: Dictionary with counts for incoming and outgoing connections
        """
        if edge_table:
            query = f"""
            SELECT 
                count(->({edge_table})->*) AS outgoing,
                count(<-({edge_table})<-*) AS incoming
            FROM {record_id}
            """
        else:
            query = f"""
            SELECT 
                count(->*->*) AS outgoing,
                count(<-*<-*) AS incoming
            FROM {record_id}
            """
        return await self.db.query(query)

    async def traverse(self, start_record, edge_tables=None, direction="out", depth=1, where_clause=None):
        """
        Traverse the graph starting from a record

        :param start_record: Starting record ID
        :param edge_tables: Optional list of edge tables to traverse (None for all)
        :param direction: Direction of traversal - "out", "in", or "both"
        :param depth: Depth of traversal
        :param where_clause: Optional WHERE clause for filtering
        :return: Results of the traversal
        """
        # Construct the edge table portion of the query
        edge_part = ""
        if edge_tables:
            if isinstance(edge_tables, list):
                edge_list = ", ".join([f"'{table}'" for table in edge_tables])
                edge_part = f"[{edge_list}]"
            else:
                edge_part = f"['{edge_tables}']"

        # Construct the traversal part based on direction
        if direction == "out":
            traversal = f"->|{depth}{edge_part}->*"
        elif direction == "in":
            traversal = f"<-|{depth}{edge_part}<-*"
        else:  # both
            # For "both", we'll do two separate queries
            out_query = f"SELECT ->|{depth}{edge_part}->* AS results FROM {start_record}"
            in_query = f"SELECT <-|{depth}{edge_part}<-* AS results FROM {start_record}"

            if where_clause:
                out_query += f" WHERE {where_clause}"
                in_query += f" WHERE {where_clause}"

            # Execute both queries and combine results
            out_result = await self.db.query(out_query)
            in_result = await self.db.query(in_query)

            return {"outgoing": out_result, "incoming": in_result}

        # Construct the complete query for single direction
        query = f"SELECT {traversal} AS results FROM {start_record}"
        if where_clause:
            query += f" WHERE {where_clause}"

        return await self.db.query(query)

    async def get_edge(self, edge_id):
        """
        Get an edge by its ID

        :param edge_id: Edge ID (e.g., "order:123")
        :return: Edge data including connected records
        """
        query = f"""
        SELECT 
            *,
            ->* as outgoing,
            <-* as incoming
        FROM {edge_id}
        """
        return await self.db.query(query)