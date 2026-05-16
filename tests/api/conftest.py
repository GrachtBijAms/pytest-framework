import pytest
from api.user_api import UserAPI

@pytest.fixture(scope="session")
def user_api(config):
    # create UserAPI with base api url
    api_client = UserAPI(base_url=config.api_url)
    api_client.logger.info("Initialized UserAPI client")
    return api_client