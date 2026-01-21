from utils.api_client import APIClient


def test_get_users():
    response = APIClient.get_users()

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert "id" in response.json()[0]


def test_create_post():
    response = APIClient.create_post(
        title="API Automation",
        body="Learning API testing with pytest",
        user_id=1
    )

    assert response.status_code == 201
    assert response.json()["title"] == "API Automation"
