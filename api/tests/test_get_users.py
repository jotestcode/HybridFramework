import pytest


@pytest.mark.api
@pytest.mark.sanity
def test_get_users(api_client):

    response = api_client.get("/users")
    print(response.status_code)

    assert response.status_code == 200

    users = response.json()
    print(users)

    assert isinstance(users, list)
    assert len(users) > 0