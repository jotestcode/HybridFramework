import pytest

from api.data.user_payload import create_user_payload


@pytest.mark.api
@pytest.mark.regression
def test_delete_user(api_client):

    create = api_client.post("/users", create_user_payload())

    assert create.status_code == 201

    user_id = create.json()["id"]
    print(f"User_id: {user_id}")

    response = api_client.delete(f"/users/{user_id}")

    assert response.status_code == 204

    print(f"Response status code: {response.status_code}")