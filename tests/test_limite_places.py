def test_reservation_max_12_places(client):
    response = client.post('/purchasePlaces', data={
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": 13
    })
    assert response.status_code == 403