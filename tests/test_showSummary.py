from server import showSummary

def test_showSummary_valid_email(client, valid_club):
    data = {
        "email": valid_club["email"]
    }
    response = client.post('/showSummary', data=data)
    assert response.status_code == 200
    assert f"Welcome, {valid_club['email']}" in response.data.decode()    

def test_showSummary_wrong_email(client):
    data = {
        "email": "test@test.fr"
    }
    response = client.post('/showSummary', data=data)
    assert response.status_code == 200 
    assert f"Cet email ne correspond à aucun utilisateur." in response.data.decode()    

def test_showSummary_no_email(client):
    data = {
        "email": ""
    }
    response = client.post('/showSummary', data=data)
    assert response.status_code == 200       