import json
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = [club for club in clubs if club["email"] == request.form["email"]][0]
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    competition_places = int(competition["numberOfPlaces"])
    club_points = int(club["points"])

    if placesRequired > competition_places:
        flash(
            f"Vous ne pouvez pas réserver {placesRequired} places. Le nombre maximum de places disponibles pour cette compétition est de {competition_places}."
        )
        return render_template("booking.html", club=club, competition=competition), 403
    elif placesRequired > club_points:
        flash(
            f"Vous ne pouvez pas réserver {placesRequired} places. Votre club ne dispose que de {club_points} points."
        )
        return render_template("booking.html", club=club, competition=competition), 403
    else:
        flash("Great-booking complete!")
        club["points"] = club_points - placesRequired
        competition["numberOfPlaces"] = competition_places - placesRequired
        return (
            render_template("welcome.html", club=club, competitions=competitions),
            200,
        )


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
