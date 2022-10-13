from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_reservation_max_12_places(self):
        for comp in self.competitions:
            for club in self.clubs:
                mock = {
                    "club": club.get("name"),
                    "competition": comp.get("name"),
                    "places": 13,
                }
                response = self.client.post(
                    "/purchasePlaces",
                    data=mock,
                )
                assert response.status_code == 403
