import json
from flask import Flask, render_template, request, redirect, flash, url_for

from datetime import datetime


def loadClubs():
    with open("clubs.json") as c:
        jsonfile = json.load(c)
        if "clubs" in jsonfile.keys():
            listOfClubs = jsonfile["clubs"]
        else:
            listOfClubs = {}
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        jsonfile = json.load(comps)
        if "competitions" in jsonfile.keys():
            listOfCompetitions = jsonfile["competitions"]
        else:
            listOfCompetitions = {}
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()
valeur_place = 3


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            email=request.form["email"],
        )
    except:
        flash("Cet email ne correspond à aucun utilisateur.")
        return render_template("index.html")


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
    elif placesRequired > 12:
        flash("Il n' est pas autorisé de réserver plus de 12 places.")
        return render_template("booking.html", club=club, competition=competition), 403
    elif datetime.fromisoformat(competition.get("date")) < datetime.now():
        flash("La date de cette compétition est passée.")
        return render_template("booking.html", club=club, competition=competition), 403
    elif placesRequired * valeur_place > int(club.get("points")):
        flash("Vous ne disposez pas d'assez de points")
        return (
            render_template("welcome.html", club=club, competitions=competitions),
            403,
        )
    else:
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - placesRequired
        )
        club["points"] = str(int(club["points"]) - placesRequired * valeur_place)
        flash("Great-booking complete!")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/clubs_points/<email>")
def display_clubs_points(email):
    other_clubs = [club for club in clubs if club["email"] != email]
    return render_template("clubs_points.html", clubs=other_clubs)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
