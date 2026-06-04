import pytest


@pytest.mark.django_db
def test_hub_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_hub_index_contains_title(client):
    response = client.get("/")
    assert b"primero1800.ru" in response.content
