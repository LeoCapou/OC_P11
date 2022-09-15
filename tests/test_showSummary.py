from server import showSummary

def test_showSummary(client):
    """
    TEST
    """
    data = {
        "email": "patate@gmail.com"
    }
    response = client.post('/showSummary', data=data)
    assert response.status_code == 200