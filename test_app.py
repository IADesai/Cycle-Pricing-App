from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys


# test case id format is an abbreviation in the pattern of mmffddd where m stands for module,
# f for file, and d for three digits which convey the number of your test case.
def test_cycle001_h1_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'Waste and recycling' (not case sensitive)
    """
    app = import_app(app_file="app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h2", timeout=4)
    h1_text = dash_duo.find_element("h2").text
    assert h1_text.casefold() == "Sidebar".casefold()
    
    
def test_cycle002_datedropdowncontainsjul1(dash_duo):
    """
    GIVEN the Dash app is running
    WHEN the home page has loaded
    THEN 'London' should appear in the area dropdown
    """
    app = import_app(app_file="app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "Sunday, Jul 1 2018.xlsx" in dash_duo.find_element("#date-select").text
    ), "'Sunday, Jul 1 2018.xlsx' should appear in the area dropdown"

