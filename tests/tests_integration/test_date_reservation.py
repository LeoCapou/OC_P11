from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_date_competition_expiree(self):
        club = self.clubs[0]
        competition = self.competitions[1]
        mock = {
            "club": club.get("name"),
            "competition": competition.get("name"),
            "places": 1,
        }
        response = self.client.post(
            "/purchasePlaces",
            data=mock,
        )
        assert response.status_code == 403
