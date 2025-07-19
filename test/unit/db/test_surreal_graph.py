"""
Unit tests for surreal_graph module.

Tests the GraphController and AsyncGraphController classes for graph operations
in SurrealDB, including relationship creation, querying, and edge cases.
"""

import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch
from lib.db.surreal_graph import GraphController, AsyncGraphController


# Module-level fixtures that can be used across all test classes
@pytest.fixture
def graph_controller(mock_db_controller):
    """Create a GraphController instance with mocked dependencies."""
    return GraphController(mock_db_controller)


@pytest.fixture
def async_graph_controller(mock_async_db_controller):
    """Create an AsyncGraphController instance with mocked dependencies."""
    return AsyncGraphController(mock_async_db_controller)


class TestGraphController:
    """Test cases for the synchronous GraphController class."""
    
    pytestmark = pytest.mark.unit

    @pytest.fixture
    def mock_db_controller(self):
        """Create a mock database controller for testing."""
        mock_db = Mock()
        mock_db.query = Mock()
        return mock_db

    def test_init_with_sync_db_controller(self, mock_db_controller):
        """Test GraphController initialization with sync database controller."""
        controller = GraphController(mock_db_controller)
        assert controller.db == mock_db_controller
        assert controller._is_async is False

    def test_init_with_async_db_controller(self):
        """Test GraphController initialization with async database controller."""
        from lib.db.surreal import AsyncDbController
        mock_async_db = Mock(spec=AsyncDbController)
        # Mock the query method to have __await__ attribute
        mock_async_db.query.__await__ = Mock()
        
        controller = GraphController(mock_async_db)
        assert controller.db == mock_async_db
        assert controller._is_async is True

    def test_relate_basic(self, graph_controller, mock_db_controller):
        """Test basic relationship creation without edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        
        graph_controller.relate(from_record, edge_table, to_record)
        
        expected_query = "RELATE person:123 -> order:ulid() -> product:456"
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_relate_with_edge_data(self, graph_controller, mock_db_controller):
        """Test relationship creation with edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        edge_data = {
            "quantity": 2,
            "price": 29.99,
            "note": "Express delivery"
        }
        
        graph_controller.relate(from_record, edge_table, to_record, edge_data)
        
        expected_query = 'RELATE person:123 -> order:ulid() -> product:456 CONTENT { quantity: 2, price: 29.99, note: "Express delivery" }'
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_relate_with_reference_values(self, graph_controller, mock_db_controller):
        """Test relationship creation with reference values (-> and <- syntax)."""
        from_record = "diagnosis:depression"
        edge_table = "HAS_SYMPTOM"
        to_record = "symptom:headache"
        edge_data = {
            "severity": "->symptom:headache->severity",
            "onset": "<-diagnosis:depression<-created_at",
            "note": "Patient reported"
        }
        
        graph_controller.relate(from_record, edge_table, to_record, edge_data)
        
        expected_query = 'RELATE diagnosis:depression -> HAS_SYMPTOM:ulid() -> symptom:headache CONTENT { severity: ->symptom:headache->severity, onset: <-diagnosis:depression<-created_at, note: "Patient reported" }'
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_relate_with_empty_edge_data(self, graph_controller, mock_db_controller):
        """Test relationship creation with empty edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        edge_data = {}
        
        graph_controller.relate(from_record, edge_table, to_record, edge_data)
        
        expected_query = "RELATE person:123 -> order:ulid() -> product:456"
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_get_relations_basic(self, graph_controller, mock_db_controller):
        """Test basic relationship querying."""
        start_node = "diagnosis:depression"
        edge_table = "HAS_SYMPTOM"
        end_table = "symptom"
        
        graph_controller.get_relations(start_node, edge_table, end_table)
        
        expected_query = "SELECT ->HAS_SYMPTOM->symptom FROM diagnosis:depression"
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_get_relations_with_direction(self, graph_controller, mock_db_controller):
        """Test relationship querying with custom direction."""
        start_node = "person:123"
        edge_table = "FRIEND"
        end_table = "person"
        direction = "<-"
        
        graph_controller.get_relations(start_node, edge_table, end_table, direction)
        
        expected_query = "SELECT <-FRIEND<-person FROM person:123"
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_count_connections_not_implemented(self, graph_controller, mock_db_controller):
        """Test that count_connections method is not yet implemented."""
        result = graph_controller.count_connections()
        
        # Should call query with empty string (as per current implementation)
        mock_db_controller.query.assert_called_once_with("")
        assert result is not None  # Should return whatever the mock returns

    def test_find_path_not_implemented(self, graph_controller, mock_db_controller):
        """Test that find_path method is not yet implemented."""
        result = graph_controller.find_path()
        
        # Should call query with empty string (as per current implementation)
        mock_db_controller.query.assert_called_once_with("")
        assert result is not None  # Should return whatever the mock returns

    def test_execute_with_sync_db(self, graph_controller, mock_db_controller):
        """Test _execute method with synchronous database controller."""
        mock_db_controller.query.return_value = "test_result"
        
        result = graph_controller._execute(mock_db_controller.query, "test_query")
        
        assert result == "test_result"
        mock_db_controller.query.assert_called_once_with("test_query")

    @patch('asyncio.ensure_future')
    def test_execute_with_async_db(self, mock_ensure_future):
        """Test _execute method with asynchronous database controller."""
        mock_async_db = Mock()
        mock_async_db.query.__await__ = Mock()
        mock_async_db.query.return_value = "async_result"
        
        controller = GraphController(mock_async_db)
        mock_ensure_future.return_value = "future_result"
        
        result = controller._execute(mock_async_db.query, "test_query")
        
        assert result == "async_result"


class TestAsyncGraphController:
    """Test cases for the asynchronous AsyncGraphController class."""
    
    pytestmark = [pytest.mark.unit, pytest.mark.asyncio]

    @pytest.fixture
    def mock_async_db_controller(self):
        """Create a mock async database controller for testing."""
        mock_db = Mock()
        mock_db.query = AsyncMock()
        return mock_db

    def test_init(self, mock_async_db_controller):
        """Test AsyncGraphController initialization."""
        controller = AsyncGraphController(mock_async_db_controller)
        assert controller.db == mock_async_db_controller

    @pytest.mark.asyncio
    async def test_relate_basic(self, async_graph_controller, mock_async_db_controller):
        """Test basic async relationship creation without edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        
        await async_graph_controller.relate(from_record, edge_table, to_record)
        
        expected_query = "RELATE person:123 -> order:ulid() -> product:456"
        mock_async_db_controller.query.assert_called_once_with(expected_query)

    @pytest.mark.asyncio
    async def test_relate_with_edge_data(self, async_graph_controller, mock_async_db_controller):
        """Test async relationship creation with edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        edge_data = {
            "quantity": 2,
            "price": 29.99,
            "note": "Express delivery"
        }
        
        await async_graph_controller.relate(from_record, edge_table, to_record, edge_data)
        
        expected_query = 'RELATE person:123 -> order:ulid() -> product:456 CONTENT { quantity: 2, price: 29.99, note: "Express delivery" }'
        mock_async_db_controller.query.assert_called_once_with(expected_query)

    @pytest.mark.asyncio
    async def test_relate_with_reference_values(self, async_graph_controller, mock_async_db_controller):
        """Test async relationship creation with reference values."""
        from_record = "diagnosis:depression"
        edge_table = "HAS_SYMPTOM"
        to_record = "symptom:headache"
        edge_data = {
            "severity": "->symptom:headache->severity",
            "onset": "<-diagnosis:depression<-created_at",
            "note": "Patient reported"
        }
        
        await async_graph_controller.relate(from_record, edge_table, to_record, edge_data)
        
        expected_query = 'RELATE diagnosis:depression -> HAS_SYMPTOM:ulid() -> symptom:headache CONTENT { severity: ->symptom:headache->severity, onset: <-diagnosis:depression<-created_at, note: "Patient reported" }'
        mock_async_db_controller.query.assert_called_once_with(expected_query)

    @pytest.mark.asyncio
    async def test_get_relations_basic(self, async_graph_controller, mock_async_db_controller):
        """Test basic async relationship querying."""
        start_node = "diagnosis:depression"
        edge_table = "HAS_SYMPTOM"
        end_table = "symptom"
        
        await async_graph_controller.get_relations(start_node, edge_table, end_table)
        
        expected_query = "SELECT ->HAS_SYMPTOM->symptom FROM diagnosis:depression"
        mock_async_db_controller.query.assert_called_once_with(expected_query)

    @pytest.mark.asyncio
    async def test_get_relations_with_direction(self, async_graph_controller, mock_async_db_controller):
        """Test async relationship querying with custom direction."""
        start_node = "person:123"
        edge_table = "FRIEND"
        end_table = "person"
        direction = "<-"
        
        await async_graph_controller.get_relations(start_node, edge_table, end_table, direction)
        
        expected_query = "SELECT <-FRIEND<-person FROM person:123"
        mock_async_db_controller.query.assert_called_once_with(expected_query)

    @pytest.mark.asyncio
    async def test_count_connections_not_implemented(self, async_graph_controller, mock_async_db_controller):
        """Test that async count_connections method is not yet implemented."""
        await async_graph_controller.count_connections()
        
        # Should call query with empty string (as per current implementation)
        mock_async_db_controller.query.assert_called_once_with("")

    @pytest.mark.asyncio
    async def test_find_path_not_implemented(self, async_graph_controller, mock_async_db_controller):
        """Test that async find_path method is not yet implemented."""
        await async_graph_controller.find_path()
        
        # Should call query with empty string (as per current implementation)
        mock_async_db_controller.query.assert_called_once_with("")


class TestGraphControllerIntegration:
    """Integration tests for GraphController with real database operations."""

    @pytest.mark.integration
    @pytest.mark.db
    def test_relate_integration(self):
        """Integration test for relationship creation (requires database)."""
        # This test would require a real database connection
        # For now, we'll skip it in unit tests
        pytest.skip("Integration test requires database connection")

    @pytest.mark.integration
    @pytest.mark.db
    @pytest.mark.asyncio
    async def test_async_relate_integration(self):
        """Integration test for async relationship creation (requires database)."""
        # This test would require a real database connection
        # For now, we'll skip it in unit tests
        pytest.skip("Integration test requires database connection")


class TestGraphControllerEdgeCases:
    """Test edge cases and error conditions for GraphController."""
    
    pytestmark = pytest.mark.unit

    @pytest.fixture
    def mock_db_controller_with_error(self):
        """Create a mock database controller that raises exceptions."""
        mock_db = Mock()
        mock_db.query = Mock(side_effect=Exception("Database error"))
        return mock_db

    def test_relate_with_database_error(self, mock_db_controller_with_error):
        """Test that database errors are properly propagated."""
        controller = GraphController(mock_db_controller_with_error)
        
        with pytest.raises(Exception, match="Database error"):
            controller.relate("person:123", "order", "product:456")

    def test_relate_with_none_edge_data(self, graph_controller, mock_db_controller):
        """Test relationship creation with None edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        
        graph_controller.relate(from_record, edge_table, to_record, None)
        
        expected_query = "RELATE person:123 -> order:ulid() -> product:456"
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_relate_with_complex_edge_data(self, graph_controller, mock_db_controller):
        """Test relationship creation with complex edge data types."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        edge_data = {
            "string_value": "test",
            "int_value": 42,
            "float_value": 3.14,
            "bool_value": True,
            "list_value": [1, 2, 3],
            "dict_value": {"nested": "value"},
            "arrow_ref": "->table:id->field",
            "back_arrow_ref": "<-table:id<-field"
        }
        
        graph_controller.relate(from_record, edge_table, to_record, edge_data)
        
        expected_query = "RELATE person:123 -> order:ulid() -> product:456 CONTENT { string_value: \"test\", int_value: 42, float_value: 3.14, bool_value: True, list_value: [1, 2, 3], dict_value: {'nested': 'value'}, arrow_ref: ->table:id->field, back_arrow_ref: <-table:id<-field }"
        mock_db_controller.query.assert_called_once_with(expected_query)

    def test_get_relations_with_empty_strings(self, graph_controller, mock_db_controller):
        """Test relationship querying with empty string parameters."""
        start_node = ""
        edge_table = ""
        end_table = ""
        
        graph_controller.get_relations(start_node, edge_table, end_table)
        
        expected_query = "SELECT ->-> FROM "
        mock_db_controller.query.assert_called_once_with(expected_query)
