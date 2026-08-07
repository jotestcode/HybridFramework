import pytest

from utilities.custom_logger import LogMaker

logger = LogMaker.log_gen("API")


@pytest.mark.api
@pytest.mark.sanity
def test_get_invalid_user(api_client):

    logger.info("******* GET INVALID USER test started ******")

    response = api_client.get("/users/9999999999")

    assert response.status_code == 404

    print(f"Invalid user id response status code: {response.status_code}")

    logger.info("******* GET INVALID USER test passed ******")
