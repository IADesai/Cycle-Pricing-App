from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys


# def test_cycle001_h1_text_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the home page is available
#     THEN the H1 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
#     """
#     dash_duo.wait_for_element("h1", timeout=4)
#     h1_text = dash_duo.find_element("h1").text
#     assert h1_text.casefold() == "TFL Cycle Hire Pricing".casefold()

# def test_cycle002_id_d2_text_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the home page is available
#     THEN the element with id = '#id-d2' should include the text 'Month of Year:' (not case sensitive)
#     """
#     dash_duo.wait_for_element("#id-d2", timeout=4)
#     id_d2_text = dash_duo.find_element("#id-d2").text
#     assert id_d2_text.casefold() == "Month of Year:".casefold()

# def test_cycle003_id_title1_text_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the home page is available
#     THEN the element with id = '#id-title1'should include the text 'Daily Data' (not case sensitive)
#     """
#     dash_duo.wait_for_element("#id-title1", timeout=4)
#     id_title_1_text = dash_duo.find_element("#id-title1").text
#     assert id_title_1_text.casefold() == "Daily Data".casefold()

# def test_cycle004_id_title2_text_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the home page is available
#     THEN the element with id = '#id-title2'should include the text 'Monthly Data' (not case sensitive)
#     """
#     dash_duo.wait_for_element("#id-title2", timeout=4)
#     id_title_2_text = dash_duo.find_element("#id-title2").text
#     assert id_title_2_text.casefold() == "Monthly Data".casefold()

# def test_cycle005_id_title3_text_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the home page is available
#     THEN the element with id = '#id-title3'should include the text 'Pollution Data' (not case sensitive)
#     """
#     dash_duo.wait_for_element("#id-title3", timeout=4)
#     id_title_3_text = dash_duo.find_element("#id-title3").text
#     assert id_title_3_text.casefold() == "Pollution Data".casefold()


# def test_cycle006_monthdropdowncontainsjanuary(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
#     THEN 'January' should appear in the month dropdown
#     """
#     dash_duo.wait_for_element("#month-dropdown", timeout=4)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "January" in dash_duo.find_element("#month-dropdown").text
#     ), "'January' should appear in the month dropdown"

# def test_cycle007_monthdropdownchangesdropdown(dash_duo, app):
#     """
#     GIVEN the recycle Dash app is running
#     WHEN the month dropdown for the Pricing Data Choropleth Map is changed to 'February'
#     THEN 'February' should appear in the month dropdown"
#     """
#     dash_duo.wait_for_element("#month-dropdown", timeout=4)
#     select_input = dash_duo.find_element("#month-dropdown input")
#     select_input.send_keys("February")
#     select_input.send_keys(Keys.RETURN)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "February" in dash_duo.find_element("#month-dropdown").text
#     ), "'February' should appear in the month dropdown"

# def test_cycle008_hourdropdowncontains00_06(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
#     THEN '00:00-06:00' should appear in the hour dropdown
#     """
#     dash_duo.wait_for_element("#hour-dropdown", timeout=4)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "00:00-06:00" in dash_duo.find_element("#hour-dropdown").text
#     ), "'00:00-06:00' should appear in the hour dropdown"

# def test_cycle009_hourdropdownchangesdropdown(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the hour dropdown for the Pricing Data Choropleth Map is changed to '06:00-09:00'
#     THEN '06:00-09:00' should appear in the hour dropdown
#     """
#     dash_duo.wait_for_element("#hour-dropdown", timeout=4)
#     select_input = dash_duo.find_element("#hour-dropdown input")
#     select_input.send_keys("06:00-09:00")
#     select_input.send_keys(Keys.RETURN)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "06:00-09:00" in dash_duo.find_element("#hour-dropdown").text
#     ), "'06:00-09:00' should appear in the hour dropdown"

# def test_cycle010_daydropdowncontainsjul1(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the Daily data usage figure has loaded
#     THEN 'Sunday, Jul 1 2018.xlsx' should appear in the day dropdown
#     """
#     dash_duo.wait_for_element("#day-dropdown", timeout=4)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "Sunday, Jul 1 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
#     ), "'Sunday, Jul 1 2018.xlsx' should appear in the day dropdown"


# def test_cycle011_daydropdownchangesdropdown(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the day dropdown for the Daily data usage figure has changed to 'Monday, Jul 2 2018.xlsx'
#     THEN 'Monday, Jul 2 2018.xlsx' should appear in the day dropdown
#     """
#     dash_duo.wait_for_element("#day-dropdown", timeout=4)
#     select_input = dash_duo.find_element("#day-dropdown input")
#     select_input.send_keys("Monday, Jul 2 2018.xlsx")
#     select_input.send_keys(Keys.RETURN)
#     dash_duo.driver.implicitly_wait(5)
#     assert (
#         "Monday, Jul 2 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
#     ), "'Monday, Jul 2 2018.xlsx' should appear in the day dropdown"

def test_cycle012_daily_usage_graph_title_equals(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Daily data usage figure has loaded
    THEN the title should include the text "Cycle Usage for Sunday, Jul 1 2018.xlsx"
    """
    dash_duo.driver.implicitly_wait(10)
    title = dash_duo.find_element("#daily-usage-graph .gtitle").text
    assert title.casefold() == "Cycle Usage for Sunday, Jul 1 2018.xlsx".casefold()


# def test_cycle013_monthly_avgusage_graph_title_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the Monthly average usage figure has loaded
#     THEN the title should include the text "Average Cycle Hire Usage per Month"
#     """
#     dash_duo.driver.implicitly_wait(10)
#     title = dash_duo.find_element("#monthly-avgusage-graph .gtitle")
#     assert title.text == "Average Cycle Hire Usage per Month"

# def test_cycle014_monthly_totusage_graph_title_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the Monthly total usage figure has loaded
#     THEN the title should include the text "Cycle Hire Usage per Month across 11 Years""
#     """
#     dash_duo.driver.implicitly_wait(10)
#     title = dash_duo.find_element("#monthly-totusage-graph .gtitle")
#     assert title.text == "Cycle Hire Usage per Month across 11 Years"

# def test_cycle015_pollution_bar_graph_title_equals(dash_duo, app):
#     """
#     GIVEN the Dash app is running
#     WHEN the Pollution bar chart has loaded
#     THEN the title should include the text "Pollution Levels in the Boroughs of London"
#     """
#     dash_duo.driver.implicitly_wait(10)
#     title = dash_duo.find_element("#pollution-bar-graph .gtitle")
#     assert title.text == "Pollution Levels in the Boroughs of London"


def test_cycle016_daily_usage_graph_x_axis_equals(dash_duo, app):
    """
    .
    """
    dash_duo.wait_for_element("#daily-usage-graph", timeout=20)
    # select_input = dash_duo.find_element("#day-dropdown input")
    # select_input.send_keys("Sunday, Jul 1 2018.xlsx")
    # select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(21)
    x_axis = dash_duo.find_element("#daily-usage-graph .x-axis-title").text
    assert x_axis.casefold() == "Hour".casefold()