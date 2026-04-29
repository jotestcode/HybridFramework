import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="specify the browser: Chrome or Firefox or Edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
    elif browser == "Edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
    else:
        raise ValueError("unsupported browser")


# hook to add environment info in a html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce project, rahulshettyacademy'
    config.stash[metadata_key]['Test Module Name'] = 'Login page tests', 'Home page tests', 'Shop page tests', 'Miscellaneous UI tests'
    config.stash[metadata_key]['Tester Name'] = 'Emma Watson'


# hook to delete environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA HOME', None)
    metadata.pop('Plugins', None)