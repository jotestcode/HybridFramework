import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

from api.client.api_client import APIClient
from configurations.config import apipageUrl, api_token


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="specify the browser: Chrome or Firefox or Safari")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Unsupported browser")

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.quit()


# hook to add environment info in a html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Hybrid Automation Framework - UI + API'
    config.stash[metadata_key]['Test Modules'] = ('UI: Login page tests', 'Home page tests', 'Shop page tests',
                                                  'Miscellaneous UI tests',
                                                  'API: User CRUD tests')
    config.stash[metadata_key]['Automation Type'] = ('UI Automation (Selenium) + ',
                                                     'API Automation (Requests)')
    config.stash[metadata_key]['Tester Name'] = 'Josephine Job'

# hook to delete environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA HOME', None)
    metadata.pop('Plugins', None)


# API
@pytest.fixture(scope="session")
def api_client():
    return APIClient(
        apipageUrl,
        api_token
    )
