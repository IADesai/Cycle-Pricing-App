from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys
# py -m pytest -v


# def test_cycle001_h1_text_equals(dash_duo, app):
#     """
#     GIVEN the app is running
#     WHEN the home page is available
#     THEN the H1 heading element should include the text 'The Coding Cyclists' (not case sensitive)
#     """
#     #app = import_app(app_file="app_for_testing")
#     #dash_duo.start_server(app)
#     dash_duo.wait_for_element("h1", timeout=4)
#     h1_text = dash_duo.find_element("h1").text
#     assert h1_text.casefold() == "The Coding Cyclists".casefold()

def test_cycle001_h1_text_equals(dash_duo, app):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'The Coding Cyclists' (not case sensitive)
    """
    #app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("P", timeout=4)
    h1_text = dash_duo.find_element("P").text
    assert h1_text.casefold() == "Month of Year:".casefold()


def test_cycle002_h2_text_equals(dash_duo, app):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H2 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
    """
    #app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("h2", timeout=4)
    h1_text = dash_duo.find_element("h2").text
    assert h1_text.casefold() == "TFL Cycle Hire Pricing".casefold()
    

def test_cycle003_monthdropdowncontainsjanuary(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
    THEN 'January' should appear in the area dropdown created for months
    """
   # app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("#month-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "January" in dash_duo.find_element("#month-dropdown").text
    ), "'January' should appear in the month dropdown"

# def test_cycle004_monthdropdownchangesdropdown(dash_duo):
#     """
#     GIVEN the recycle Dash app is running
#     WHEN the area dropdown is changed to Hackney
#     THEN the card title for the stats panel is also changed to Hackney.

#     Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
#     """
#     app = import_app(app_file="app_for_testing")
#     dash_duo.start_server(app)
#     dash_duo.wait_for_element("#month-select", timeout=4)
#     select_input = dash_duo.find_element("#month-select input")
#     select_input.send_keys("February")
#     select_input.send_keys(Keys.RETURN)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "February" in dash_duo.find_element("#month-select").text
#     ), "'February' should appear in the month dropdown"

# def test_cycle004_monthdropdownchangesdropdown(dash_duo):
#     """
#     GIVEN the recycle Dash app is running
#     WHEN the area dropdown is changed to Hackney
#     THEN the card title for the stats panel is also changed to Hackney.

#     Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
#     """
#     app = import_app(app_file="app_for_testing")
#     dash_duo.start_server(app)
#     dash_duo.wait_for_element("#month-dropdown", timeout=4)
#     select_input = dash_duo.find_element("#month-dropdown")
#     select_input.send_keys("February")
#     select_input.send_keys(Keys.RETURN)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "February" in dash_duo.find_element("#month-dropdown").text
#     ), "'February' should appear in the month dropdown"

def test_cycle004_monthdropdownchangesdropdown(dash_duo, app):
    """
    GIVEN the recycle Dash app is running
    WHEN the area dropdown is changed to Hackney
    THEN the card title for the stats panel is also changed to Hackney.

    Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
    """
    #app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("#month-dropdown", timeout=4)
    select_input = dash_duo.find_element("#month-dropdown input")
    select_input.send_keys("February")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "February" in dash_duo.find_element("#month-dropdown").text
    ), "'February' should appear in the month dropdown"

def test_cycle005_hourdropdowncontains00_06(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
    THEN 'January' should appear in the area dropdown created for months
    """
    #app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("#hour-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "00:00-06:00" in dash_duo.find_element("#hour-dropdown").text
    ), "'00:00-06:00' should appear in the hour dropdown"

def test_cycle006_hourdropdownchangesdropdown(dash_duo, app):
    """
    GIVEN the recycle Dash app is running
    WHEN the area dropdown is changed to Hackney
    THEN the card title for the stats panel is also changed to Hackney.

    Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
    """
    #app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("#hour-dropdown", timeout=4)
    select_input = dash_duo.find_element("#hour-dropdown input")
    select_input.send_keys("06:00-09:00")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "06:00-09:00" in dash_duo.find_element("#hour-dropdown").text
    ), "'06:00-09:00' should appear in the hour dropdown"

def test_cycle007_daydropdowncontainsjul1(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Daily data page has loaded
    THEN 'Sunday, Jul 1 2018.xlsx' should appear in the area dropdown
    """
   # app = import_app(app_file="app_for_testing")
   # dash_duo.start_server(app)
    dash_duo.wait_for_element("#day-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "Sunday, Jul 1 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
    ), "'Sunday, Jul 1 2018.xlsx' should appear in the daydropdown"


def test_cycle008_daydropdownchangesdropdown(dash_duo, app):
    """
    GIVEN the recycle Dash app is running
    WHEN the area dropdown is changed to Hackney
    THEN the card title for the stats panel is also changed to Hackney.

    Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
    """
    #app = import_app(app_file="app_for_testing")
    #dash_duo.start_server(app)
    dash_duo.wait_for_element("#day-dropdown", timeout=4)
    select_input = dash_duo.find_element("#day-dropdown input")
    select_input.send_keys("Monday, Jul 2 2018.xlsx")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "Monday, Jul 2 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
    ), "'Monday, Jul 2 2018.xlsx' should appear in the hour dropdown"