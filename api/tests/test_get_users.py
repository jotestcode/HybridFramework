import pytest

from utilities.custom_logger import LogMaker

logger = LogMaker.log_gen("API")


@pytest.mark.api
@pytest.mark.sanity
def test_get_users(api_client):

    logger.info("******* GET USERS test started *******")

    response = api_client.get("/users")

    assert response.status_code == 200

    users = response.json()

    assert isinstance(users, list)
    assert len(users) > 0

    logger.info("******* GET USERS test passed ******")