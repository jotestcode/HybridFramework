import pytest

from api.data.user_payload import create_user_payload
from utilities.custom_logger import LogMaker

logger = LogMaker.log_gen("API")


@pytest.mark.api
@pytest.mark.regression
def test_update_user(api_client):

    logger.info("******* Update User test started ******")

    create = api_client.post("/users", create_user_payload())

    assert create.status_code == 201, create.text

    user_id = create.json()["id"]

    payload = {
        "status": "inactive"
    }

    response = api_client.put(f"/users/{user_id}", payload)


    assert response.status_code == 200

    assert response.json()["status"] == "inactive"

    logger.info("******* Update User test passed ******")