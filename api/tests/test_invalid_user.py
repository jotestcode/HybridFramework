import pytest


@pytest.mark.api
@pytest.mark.sanity
def test_invalid_user(api_client):

    response = api_client.get("/users/999999999")

    assert response.status_code == 404, response.text

    print(f"Invalid user id status code: {response.status_code}")

