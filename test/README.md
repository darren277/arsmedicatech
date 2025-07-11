# Testing Guide

This directory contains the test suite for the arsmedicatech project. The tests are organized using pytest and follow best practices for unit testing, integration testing, and test-driven development.

## Quick Start

### Running Tests

1. **Install test dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run all tests:**
   ```bash
   python run_tests.py all
   ```

3. **Run unit tests only:**
   ```bash
   python run_tests.py unit
   ```

4. **Run tests with coverage:**
   ```bash
   python run_tests.py coverage
   ```

5. **Run quick tests (excluding slow tests):**
   ```bash
   python run_tests.py quick
   ```

### Using pytest directly

You can also run pytest directly with various options:

```bash
# Run all tests
pytest

# Run tests in verbose mode
pytest -v

# Run tests with specific markers
pytest -m "unit and not slow"

# Run tests from a specific file
pytest test/unit/db/test_surreal_graph.py

# Run tests matching a function name pattern
pytest -k "test_relate"

# Run tests with coverage
pytest --cov=lib --cov-report=html
```

## Test Structure

```
test/
├── conftest.py                 # Shared fixtures and configuration
├── unit/                       # Unit tests
│   └── db/                     # Database-related unit tests
│       └── test_surreal_graph.py
├── integration/                # Integration tests (future)
└── README.md                   # This file
```

## Test Categories

### Unit Tests (`@pytest.mark.unit`)
- Test individual functions and classes in isolation
- Use mocks to isolate dependencies
- Fast execution
- Located in `test/unit/`

### Integration Tests (`@pytest.mark.integration`)
- Test interactions between components
- May require external services (database, APIs)
- Slower execution
- Located in `test/integration/`

### Database Tests (`@pytest.mark.db`)
- Tests that interact with the database
- May require database setup/teardown
- Can be slow

### Async Tests (`@pytest.mark.asyncio`)
- Tests for asynchronous functions
- Use `pytest-asyncio` for async test support

### Slow Tests (`@pytest.mark.slow`)
- Tests that take a long time to run
- Can be excluded with `-m "not slow"`

## Writing Tests

### Test File Naming
- Test files should be named `test_*.py`
- Test classes should be named `Test*`
- Test functions should be named `test_*`

### Example Test Structure

```python
import pytest
from unittest.mock import Mock
from lib.db.surreal_graph import GraphController

class TestGraphController:
    """Test cases for the GraphController class."""
    
    @pytest.fixture
    def mock_db_controller(self):
        """Create a mock database controller for testing."""
        mock_db = Mock()
        mock_db.query = Mock()
        return mock_db
    
    @pytest.fixture
    def graph_controller(self, mock_db_controller):
        """Create a GraphController instance with mocked dependencies."""
        return GraphController(mock_db_controller)
    
    def test_relate_basic(self, graph_controller, mock_db_controller):
        """Test basic relationship creation without edge data."""
        from_record = "person:123"
        edge_table = "order"
        to_record = "product:456"
        
        graph_controller.relate(from_record, edge_table, to_record)
        
        expected_query = "RELATE person:123 -> order:ulid() -> product:456"
        mock_db_controller.query.assert_called_once_with(expected_query)
```

### Using Fixtures

Fixtures are defined in `conftest.py` and can be used across all test files:

```python
def test_with_shared_fixture(sample_patient_data, mock_db_controller):
    """Test using shared fixtures."""
    assert sample_patient_data["first_name"] == "John"
    assert mock_db_controller.query is not None
```

### Testing Async Functions

For testing async functions, use the `@pytest.mark.asyncio` decorator:

```python
@pytest.mark.asyncio
async def test_async_function(async_graph_controller, mock_async_db_controller):
    """Test async function."""
    await async_graph_controller.relate("person:123", "order", "product:456")
    mock_async_db_controller.query.assert_called_once()
```

## Test Configuration

### pytest.ini
The main pytest configuration is in `pytest.ini` at the project root:

```ini
[tool:pytest]
testpaths = test
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --color=yes
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow running tests
    db: Database tests
    async: Async tests
```

### conftest.py
Shared fixtures and configuration are in `test/conftest.py`:

- Common mock objects
- Sample test data
- Environment setup
- Database mocking

## Best Practices

### 1. Test Isolation
- Each test should be independent
- Use fixtures for setup and teardown
- Mock external dependencies

### 2. Descriptive Names
- Test names should clearly describe what is being tested
- Use descriptive variable names
- Add docstrings to test functions

### 3. Arrange-Act-Assert Pattern
```python
def test_example():
    # Arrange - Set up test data and mocks
    mock_db = Mock()
    controller = GraphController(mock_db)
    
    # Act - Execute the function being tested
    result = controller.relate("a", "b", "c")
    
    # Assert - Verify the results
    assert result is not None
    mock_db.query.assert_called_once()
```

### 4. Test Edge Cases
- Test with empty data
- Test with invalid input
- Test error conditions
- Test boundary conditions

### 5. Use Appropriate Assertions
- Use specific assertions (`assert_called_once_with` vs `assert_called`)
- Test both positive and negative cases
- Verify error messages when testing exceptions

## Coverage

To generate coverage reports:

```bash
# Generate HTML coverage report
pytest --cov=lib --cov-report=html

# Generate terminal coverage report
pytest --cov=lib --cov-report=term

# Generate both
pytest --cov=lib --cov-report=html --cov-report=term
```

Coverage reports will be generated in the `htmlcov/` directory.

## Continuous Integration

Tests should be run automatically in CI/CD pipelines. The test runner script (`run_tests.py`) provides a consistent interface for running tests in different environments.

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure the project root is in the Python path
2. **Missing Dependencies**: Install test dependencies with `pip install -r requirements.txt`
3. **Async Test Issues**: Ensure `pytest-asyncio` is installed and configured
4. **Database Connection Issues**: Use mocks for unit tests, real connections for integration tests

### Debugging Tests

```bash
# Run tests with more verbose output
pytest -v -s

# Run a specific test with debugging
pytest test/unit/db/test_surreal_graph.py::TestGraphController::test_relate_basic -v -s

# Run tests with print statements visible
pytest -s
```

## Contributing

When adding new tests:

1. Follow the existing naming conventions
2. Add appropriate markers to tests
3. Use shared fixtures when possible
4. Add docstrings to test functions
5. Ensure tests are isolated and repeatable
6. Update this README if adding new test categories or patterns 