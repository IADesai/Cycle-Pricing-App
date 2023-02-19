from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys
# py -m pytest -v

# test case id format is an abbreviation in the pattern of mmffddd where m stands for module,
# f for file, and d for three digits which convey the number of your test case.
def test_cycle001_h1_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
    """
    app = import_app(app_file="app_for_testing")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == "The Coding Cyclists".casefold()

def test_cycle002_h2_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
    """
    app = import_app(app_file="app_for_testing")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h2", timeout=4)
    h1_text = dash_duo.find_element("h2").text
    assert h1_text.casefold() == "TFL Cycle Hire Pricing".casefold()
    

def test_cycle003_monthdropdowncontainsjanuary(dash_duo):
    """
    GIVEN the Dash app is running
    WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
    THEN 'January' should appear in the area dropdown created for months
    """
    app = import_app(app_file="app_for_testing")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#month-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "January" in dash_duo.find_element("#month-dropdown").text
    ), "'January' should appear in the month dropdown"

    
# def test_cycle002_datedropdowncontainsjul1(dash_duo):
#     """
#     GIVEN the Dash app is running
#     WHEN the Daily data page has loaded
#     THEN 'Sunday, Jul 1 2018.xlsx' should appear in the area dropdown
#     """
#     app = import_app(app_file="app")
#     dash_duo.start_server(app)
#     dash_duo.wait_for_element("#day-dropdown", timeout=14)
#     dash_duo.driver.implicitly_wait(15)
#     assert (
#         0 in dash_duo.find_element("#day-dropdown")
#     ), "0 should appear in the area dropdown"
