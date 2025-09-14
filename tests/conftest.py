# Imports
import pytest
from app import app as flask_app


@pytest.fixture
def client():
    """
    Pytest fixture to create a test client for the Flask app.
    - Enables TESTING mode (better error handling, no server needed).
    - Provides a temporary client to simulate HTTP requests.
    """
    # Enable Flask test mode
    flask_app.config.update(TESTING=True)

    # Create and yield a test client for use in tests
    with flask_app.test_client() as client:
        yield client
