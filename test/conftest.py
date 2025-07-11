"""
Common test configuration and fixtures for the test suite.

This file provides shared fixtures and configuration that can be used
across all test files in the project.
"""

import pytest
import os
import sys
from unittest.mock import Mock, AsyncMock

# Add the project root to the Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture(scope="session")
def test_settings():
    """Provide test-specific settings."""
    return {
        "SURREALDB_URL": "http://localhost:8000",
        "SURREALDB_NAMESPACE": "test",
        "SURREALDB_DATABASE": "test",
        "SURREALDB_USER": "test_user",
        "SURREALDB_PASS": "test_password"
    }


@pytest.fixture
def mock_db_controller():
    """Create a mock database controller for testing."""
    mock_db = Mock()
    mock_db.query = Mock()
    mock_db.connect = Mock()
    mock_db.close = Mock()
    mock_db.create = Mock()
    mock_db.select = Mock()
    mock_db.select_many = Mock()
    mock_db.update = Mock()
    mock_db.delete = Mock()
    mock_db.search = Mock()
    return mock_db


@pytest.fixture
def mock_async_db_controller():
    """Create a mock async database controller for testing."""
    mock_db = Mock()
    mock_db.query = AsyncMock()
    mock_db.connect = AsyncMock()
    mock_db.close = AsyncMock()
    mock_db.create = AsyncMock()
    mock_db.select = AsyncMock()
    mock_db.select_many = AsyncMock()
    mock_db.update = AsyncMock()
    mock_db.delete = AsyncMock()
    mock_db.search = AsyncMock()
    return mock_db


@pytest.fixture
def sample_patient_data():
    """Provide sample patient data for testing."""
    return {
        "id": "patient:123",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "email": "john.doe@example.com",
        "phone": "555-123-4567"
    }


@pytest.fixture
def sample_diagnosis_data():
    """Provide sample diagnosis data for testing."""
    return {
        "id": "diagnosis:depression",
        "name": "Major Depressive Disorder",
        "icd_code": "F32.1",
        "description": "Moderate depression with symptoms"
    }


@pytest.fixture
def sample_symptom_data():
    """Provide sample symptom data for testing."""
    return {
        "id": "symptom:headache",
        "name": "Headache",
        "severity": "moderate",
        "description": "Persistent headache"
    }


@pytest.fixture
def sample_edge_data():
    """Provide sample edge data for testing relationships."""
    return {
        "severity": "moderate",
        "onset_date": "2024-01-15",
        "notes": "Patient reported persistent symptoms",
        "reference_field": "->symptom:headache->severity"
    }


@pytest.fixture(autouse=True)
def setup_test_environment(monkeypatch):
    """Set up test environment variables and configurations."""
    # Mock environment variables for testing
    monkeypatch.setenv("SURREALDB_URL", "http://localhost:8000")
    monkeypatch.setenv("SURREALDB_NAMESPACE", "test")
    monkeypatch.setenv("SURREALDB_DATABASE", "test")
    monkeypatch.setenv("SURREALDB_USER", "test_user")
    monkeypatch.setenv("SURREALDB_PASS", "test_password")
    
    # Mock settings module if it doesn't exist
    try:
        import settings
    except ImportError:
        # Create a mock settings module
        mock_settings = Mock()
        mock_settings.SURREALDB_URL = "http://localhost:8000"
        mock_settings.SURREALDB_NAMESPACE = "test"
        mock_settings.SURREALDB_DATABASE = "test"
        mock_settings.SURREALDB_USER = "test_user"
        mock_settings.SURREALDB_PASS = "test_password"
        
        sys.modules['settings'] = mock_settings


@pytest.fixture
def mock_surrealdb(monkeypatch):
    """Mock the surrealdb module for testing."""
    mock_surreal = Mock()
    mock_surreal.Surreal = Mock()
    
    # Mock the Surreal class
    mock_surreal_instance = Mock()
    mock_surreal_instance.signin = Mock(return_value={"status": "OK"})
    mock_surreal_instance.use = Mock()
    mock_surreal_instance.query = Mock()
    mock_surreal_instance.create = Mock()
    mock_surreal_instance.select = Mock()
    mock_surreal_instance.update = Mock()
    mock_surreal_instance.delete = Mock()
    
    mock_surreal.Surreal.return_value = mock_surreal_instance
    
    monkeypatch.setattr("surrealdb", mock_surreal)
    return mock_surreal


@pytest.fixture
def mock_asyncio(monkeypatch):
    """Mock asyncio for testing async functionality."""
    mock_asyncio = Mock()
    mock_asyncio.ensure_future = Mock()
    
    monkeypatch.setattr("asyncio", mock_asyncio)
    return mock_asyncio 