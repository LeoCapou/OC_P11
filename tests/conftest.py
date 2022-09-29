import pytest
from unittest.mock import patch
import server
from server import app

"""
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

"""        

def mocks():
    clubs_obj = [
                {
                    "name":"TEST Simply Lift",
                    "email":"test_john@simplylift.co",
                    "points":"13"
                },
                {
                    "name":"TEST Iron Temple",
                    "email":"test_admin@irontemple.com",
                    "points":"4"
                }
            ]

    competitions_obj = [
                {
                    "name": "TEST Spring Festival",
                    "date": "2020-03-27 10:00:00",
                    "numberOfPlaces": "25"
                },
                {
                    "name": "TEST Fall Classic",
                    "date": "2020-10-22 13:30:00",
                    "numberOfPlaces": "13"
                }
            ]
    return clubs_obj, competitions_obj            


@pytest.fixture(scope="class")
def client(request):
    clubs_obj, competitions_obj = mocks()
    print(clubs_obj)
    with patch("server.clubs", clubs_obj):
        with patch("server.competitions", competitions_obj):
            with server.app.test_client() as client:
                request.cls.clubs = clubs_obj
                request.cls.competitions = competitions_obj
                request.cls.client = client
                yield    