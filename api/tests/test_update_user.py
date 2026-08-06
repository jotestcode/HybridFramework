import pytest

from api.data.user_payload import create_user_payload


@pytest.mark.api
@pytest.mark.sanity
def test_update_user(api_client):

    create = api_client.post("/users", create_user_payload())

    assert create.status_code == 201, create.text

    user_id = create.json()["id"]

    payload = {
        "status": "inactive"
    }

    response = api_client.put(f"/users/{user_id}", payload)

    assert response.status_code == 200
    assert response.json()["status"] == "inactive"

    print(f"Response status code: {response.status_code}")
    print(f"Updated user: {response.json()}")