import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    """Setup options for the Chromedriver when using Selenium"""
    options = Options()
    # Uncomment the following if testing on GitHub actions
    # the browser needs to run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    return options

@pytest.fixture(scope="function")
def app(dash_duo):
    #app = import_app("dashapp.dashboard")
    test_app = import_app(app_file="app2")
    yield dash_duo.start_server(test_app)
