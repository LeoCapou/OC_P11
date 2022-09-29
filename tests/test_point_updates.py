from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_update_points_club(self):
        places = 1
        club = self.clubs[0]
        points = int(club.get("points"))
        competition = self.competitions[0]
        response = self.client.post(
            "/purchasePlaces",
            data={
                "club": club.get("name"),
                "competition": competition.get("name"),
                "places": places,
            },
        )
        assert int(club.get("points")) == points - places * self.valeur_place
