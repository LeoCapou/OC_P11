import pytest
import server
from server import app

@pytest.fixture
def client():
    # client fixture to provide instances of test client against our server app
    with app.test_client() as client:
        yield client