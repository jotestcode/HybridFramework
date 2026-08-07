import pytest

from api.data.user_payload import create_user_payload
from utilities.custom_logger import LogMaker

logger = LogMaker.log_gen("API")


@pytest.mark.api
@pytest.mark.regression
def test_create_user(api_client):

    logger.info("******* Create User test started *******")

    payload = create_user_payload()

    response = api_client.post("/users", payload)

    assert response.status_code == 201

    user = response.json()

    assert user["name"] == payload["name"]

    logger.info(f"Created User ID: {user['id']}")
    logger.info("******* Create User test passed *******")
