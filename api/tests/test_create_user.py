import pytest

from api.data.user_payload import create_user_payload


@pytest.mark.api
@pytest.mark.regression
def test_create_user(api_client):

    payload = create_user_payload()

    response = api_client.post("/users", payload)
    print(response.status_code)

    assert response.status_code == 201

    user = response.json()
    print(user)

    assert user["name"] == payload["name"]
    assert user["gender"] == payload["gender"]

