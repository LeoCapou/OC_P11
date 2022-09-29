from unittest import TestCase
from pytest import mark

@mark.usefixtures('client')
class TestServer(TestCase):
    def test_inscription_nombre_points(self):
        for comp in self.competitions:
            for club in self.clubs:
                mock = {
                    "club": club.get('name'),
                    "competition": comp.get('name'),
                    "places": int(club.get('points')) + 1
                }
                response = self.client.post('/purchasePlaces', data=mock)
                self.assertEqual(response.status_code, 403)