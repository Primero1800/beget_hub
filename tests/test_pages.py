import pytest

from apps.pages.models import SubProject


@pytest.mark.django_db
def test_hub_index_returns_200(client):
    response = client.get("/ru/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_hub_index_contains_title(client):
    response = client.get("/ru/")
    assert b"primero1800.ru" in response.content


@pytest.mark.django_db
def test_hub_index_shows_active_projects(client):
    SubProject.objects.create(
        name_ru="Тест",
        name_en="Test",
        url="https://test.primero1800.ru",
        active=True,
    )
    response = client.get("/ru/")
    assert b"test.primero1800.ru" in response.content


@pytest.mark.django_db
def test_hub_index_hides_inactive_projects(client):
    SubProject.objects.create(
        name_ru="Скрытый",
        name_en="Hidden",
        url="https://hidden.primero1800.ru",
        active=False,
    )
    response = client.get("/ru/")
    assert b"hidden.primero1800.ru" not in response.content


@pytest.mark.django_db
def test_hub_index_english(client):
    response = client.get("/en/")
    assert b"Projects list" in response.content
