import json

def get_club_by_email(email):
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
    return [club for club in listOfClubs if club["email"] == email][0]

def get_club_by_name(name):
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
    return [club for club in listOfClubs if club["name"] == name][0]    

def get_competition_by_name(name):
    with open('competitions.json') as c:
         listOfCompetitions  = json.load(c)['competitions']
    return [comp for comp in listOfCompetitions if comp["name"] == name][0]      