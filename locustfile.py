from locust import HttpUser, task, between
import random

from server import clubs, competitions


class User(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def view_clubs_points(self):
        club_email = clubs[0]["email"]
        self.client.get(f"/clubs_points/{club_email}")

    @task(1)
    def view_index(self):
        self.client.get("/")

    @task(2)
    def login(self):
        club_email = clubs[0]["email"]
        self.client.post("/showSummary", {"email": club_email})

    @task(2)
    def booking(self):
        competition = competitions[0]["name"]
        club = clubs[0]["name"]
        self.client.get(f"/book/{competition}/{club}")

    @task(3)
    def purchase_places(self):
        places = 1
        competition = competitions[0]["name"]
        club = clubs[0]["name"]

        self.client.post(
            "/purchasePlaces",
            {"competition": competition, "club": club, "places": places},
        )
