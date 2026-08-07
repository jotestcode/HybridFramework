import pytest

from api.data.user_payload import create_user_payload
from utilities.custom_logger import LogMaker

logger = LogMaker.log_gen("API")


@pytest.mark.api
@pytest.mark.sanity
def test_delete_user(api_client):

    logger.info("******* Delete User test started *******")

    create = api_client.post("/users", create_user_payload())

    assert create.status_code == 201

    user_id = create.json()["id"]

    response = api_client.delete(f"/users/{user_id}")

    assert response.status_code == 204


    logger.info("******* Delete User test passed *******")