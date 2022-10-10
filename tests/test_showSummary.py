from unittest import TestCase
from pytest import mark


@mark.usefixtures("client")
class TestServer(TestCase):
    def test_showSummary_valid_email(self):
        for comp in self.competitions:
            for club in self.clubs:
                mock = {
                    "email": club.get("email"),
                }
                response = self.client.post(
                    "/showSummary",
                    data=mock,
                )
                assert response.status_code == 200
                assert f"Welcome, {mock['email']}" in response.data.decode()

    def test_showSummary_wrong_email(self):
        mock = {"email": "test@test.fr"}
        response = self.client.post("/showSummary", data=mock)
        assert response.status_code == 200
        assert f"Cet email ne correspond à aucun utilisateur." in response.data.decode()

    def test_showSummary_no_email(self):
        mock = {"email": ""}
        response = self.client.post("/showSummary", data=mock)
        assert response.status_code == 200
