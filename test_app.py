
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_addition():
    client = app.test_client()
    response = client.get(
        "/calculate?a=10&b=5&operation=add"
    )
    assert response.json["result"] == 15

def test_subtraction():
    client = app.test_client()
    response = client.get(
        "/calculate?a=10&b=5&operation=subtract"
    )
    assert response.json["result"] == 5

def test_multiplication():
    client = app.test_client()
    response = client.get(
        "/calculate?a=10&b=5&operation=multiply"
    )
    assert response.json["result"] == 50

def test_division():
    client = app.test_client()
    response = client.get(
        "/calculate?a=10&b=5&operation=divide"
    )
    assert response.json["result"] == 2

def test_division_by_zero():
    client = app.test_client()
    response = client.get(
        "/calculate?a=10&b=0&operation=divide"
    )
    assert response.status_code == 400
