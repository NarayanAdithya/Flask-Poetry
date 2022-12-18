from app import app


def test_base():
    response = app.test_client().get('/')
    assert response.text == "Home of Application With Poetry"
    assert response.status_code == 200


def test_nameroute():
    response = app.test_client().get('/adithya')
    assert response.text == "adithya was passed in the URL"
    assert response.status_code == 200
