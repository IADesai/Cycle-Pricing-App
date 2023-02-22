from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys

# py -m pytest -v
def test_cycle001_h1_text_equals(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
    """
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == "TFL Cycle Hire Pricing".casefold()

def test_cycle002_id_d2_text_equals(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the home page is available
    THEN the element with id = '#id-d2' should include the text 'Month of Year:' (not case sensitive)
    """
    dash_duo.wait_for_element("#id-d2", timeout=4)
    id_d2_text = dash_duo.find_element("#id-d2").text
    assert id_d2_text.casefold() == "Month of Year:".casefold()

def test_cycle003_id_title1_text_equals(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the home page is available
    THEN the element with id = '#id-title1'should include the text 'Daily Data' (not case sensitive)
    """
    dash_duo.wait_for_element("#id-title1", timeout=4)
    id_title_1_text = dash_duo.find_element("#id-title1").text
    assert id_title_1_text.casefold() == "Daily Data".casefold()

def test_cycle004_id_title2_text_equals(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the home page is available
    THEN the element with id = '#id-title2'should include the text 'Monthly Data' (not case sensitive)
    """
    dash_duo.wait_for_element("#id-title2", timeout=4)
    id_title_2_text = dash_duo.find_element("#id-title2").text
    assert id_title_2_text.casefold() == "Monthly Data".casefold()

def test_cycle005_id_title3_text_equals(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the home page is available
    THEN the element with id = '#id-title3'should include the text 'Pollution Data' (not case sensitive)
    """
    dash_duo.wait_for_element("#id-title3", timeout=4)
    id_title_3_text = dash_duo.find_element("#id-title3").text
    assert id_title_3_text.casefold() == "Pollution Data".casefold()


def test_cycle006_monthdropdowncontainsjanuary(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
    THEN 'January' should appear in the month dropdown
    """
    dash_duo.wait_for_element("#month-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "January" in dash_duo.find_element("#month-dropdown").text
    ), "'January' should appear in the month dropdown"

def test_cycle007_monthdropdownchangesdropdown(dash_duo, app):
    """
    GIVEN the recycle Dash app is running
    WHEN the month dropdown for the Pricing Data Choropleth Map is changed to 'February'
    THEN 'February' should appear in the month dropdown"
    """
    dash_duo.wait_for_element("#month-dropdown", timeout=4)
    select_input = dash_duo.find_element("#month-dropdown input")
    select_input.send_keys("February")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "February" in dash_duo.find_element("#month-dropdown").text
    ), "'February' should appear in the month dropdown"

def test_cycle008_hourdropdowncontains00_06(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
    THEN '00:00-06:00' should appear in the hour dropdown
    """
    dash_duo.wait_for_element("#hour-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "00:00-06:00" in dash_duo.find_element("#hour-dropdown").text
    ), "'00:00-06:00' should appear in the hour dropdown"

def test_cycle009_hourdropdownchangesdropdown(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the hour dropdown for the Pricing Data Choropleth Map is changed to '06:00-09:00'
    THEN '06:00-09:00' should appear in the hour dropdown
    """
    dash_duo.wait_for_element("#hour-dropdown", timeout=4)
    select_input = dash_duo.find_element("#hour-dropdown input")
    select_input.send_keys("06:00-09:00")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "06:00-09:00" in dash_duo.find_element("#hour-dropdown").text
    ), "'06:00-09:00' should appear in the hour dropdown"

def test_cycle010_daydropdowncontainsjul1(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the Daily data usage figure has loaded
    THEN 'Sunday, Jul 1 2018.xlsx' should appear in the day dropdown
    """
    dash_duo.wait_for_element("#day-dropdown", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "Sunday, Jul 1 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
    ), "'Sunday, Jul 1 2018.xlsx' should appear in the day dropdown"


def test_cycle011_daydropdownchangesdropdown(dash_duo, app):
    """
    GIVEN the Dash app is running
    WHEN the day dropdown for the Daily data usage figure has changed to 'Monday, Jul 2 2018.xlsx'
    THEN 'Monday, Jul 2 2018.xlsx' should appear in the day dropdown
    """
    dash_duo.wait_for_element("#day-dropdown", timeout=4)
    select_input = dash_duo.find_element("#day-dropdown input")
    select_input.send_keys("Monday, Jul 2 2018.xlsx")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "Monday, Jul 2 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
    ), "'Monday, Jul 2 2018.xlsx' should appear in the day dropdown"

def test_cycle012_daydropdownchangesdropdown(dash_duo, app):
    """
    .
    """
    dash_duo.wait_for_element("#day-dropdown", timeout=9)
    select_input = dash_duo.find_element("#day-dropdown input")
    select_input.send_keys("Sunday, Jul 1 2018.xlsx")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(10)
    title = dash_duo.find_element("#daily-usage-graph .gtitle")
    assert title.text == "Cycle Usage for Sunday, Jul 1 2018.xlsx"


def test_cycle012_daydropdownchangesdropdown(dash_duo, app):
    """
    .
    """
    dash_duo.wait_for_element("#day-dropdown", timeout=9)
    # select_input = dash_duo.find_element("#day-dropdown input")
    # select_input.send_keys("Sunday, Jul 1 2018.xlsx")
    # select_input.send_keys(Keys.RETURN)
    # dash_duo.driver.implicitly_wait(10)
    title = dash_duo.find_element("#daily-usage-graph.gtitle")
    assert title.text == "Cycle Usage for Sunday, Jul 1 2018.xlsx"


def test_cycle013_daydropdownchangesdropdown(dash_duo, app):
    """
    .
    """
    #dash_duo.wait_for_element("#day-dropdown", timeout=9)
    # select_input = dash_duo.find_element("#day-dropdown input")
    # select_input.send_keys("Sunday, Jul 1 2018.xlsx")
    # select_input.send_keys(Keys.RETURN)
    # dash_duo.driver.implicitly_wait(10)
    title = dash_duo.find_element("#monthly-avgusage-graph.gtitle")
    assert title.text == "Average Cycle Hire Usage per Month"

def test_cycle014_daydropdownchangesdropdown(dash_duo, app):
    """
    .
    """
    #dash_duo.wait_for_element("#day-dropdown", timeout=9)
    # select_input = dash_duo.find_element("#day-dropdown input")
    # select_input.send_keys("Sunday, Jul 1 2018.xlsx")
    # select_input.send_keys(Keys.RETURN)
    # dash_duo.driver.implicitly_wait(10)
    title = dash_duo.find_element("#monthly-totusage-graph.gtitle")
    assert title.text == "Cycle Hire Usage per Month across 11 Years"

def test_cycle015_daydropdownchangesdropdown(dash_duo, app):
    """
    .
    """
    #dash_duo.wait_for_element("#day-dropdown", timeout=9)
    # select_input = dash_duo.find_element("#day-dropdown input")
    # select_input.send_keys("Sunday, Jul 1 2018.xlsx")
    # select_input.send_keys(Keys.RETURN)
    # dash_duo.driver.implicitly_wait(10)
    title = dash_duo.find_element("#pollution-bar-graph.gtitle")
    assert title.text == "Pollution Levels in the Boroughs of London"







#####


# def test_cycle007_monthdropdownchangesdropdown(dash_duo):
#     """
#     GIVEN the Dash app is running
#     WHEN the area dropdown is changed to Hackney
#     THEN the card title for the stats panel is also changed to Hackney.
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

# def test_cycle008_monthdropdownchangesdropdown(dash_duo):
#     """
#     GIVEN the recycle Dash app is running
#     WHEN the area dropdown is changed to Hackney
#     THEN the card title for the stats panel is also changed to Hackney.
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


# # # def test_cycle001_h1_text_equals(dash_duo, app):
# # #     """
# # #     GIVEN the app is running
# # #     WHEN the home page is available
# # #     THEN the H1 heading element should include the text 'The Coding Cyclists' (not case sensitive)
# # #     """
# # #     #app = import_app(app_file="app_for_testing")
# # #     #dash_duo.start_server(app)
# # #     dash_duo.wait_for_element("h1", timeout=4)
# # #     h1_text = dash_duo.find_element("h1").text
# # #     assert h1_text.casefold() == "The Coding Cyclists".casefold()

# # # def test_cycle001_h1_text_equals(dash_duo, app):
# # #     """
# # #     GIVEN the app is running
# # #     WHEN the home page is available
# # #     THEN the H1 heading element should include the text 'The Coding Cyclists' (not case sensitive)
# # #     """
# # #     #app = import_app(app_file="app_for_testing")
# # #     #dash_duo.start_server(app)
# # #     dash_duo.wait_for_element("H2", timeout=4)
# # #     h1_text = dash_duo.find_element("H2").text
# # #     assert h1_text.casefold() == "Month of Year:".casefold()



    

# # def test_cycle002_monthdropdowncontainsjanuary(dash_duo, app):
# #     """
# #     GIVEN the Dash app is running
# #     WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
# #     THEN 'January' should appear in the area dropdown created for months
# #     """
# #     dash_duo.wait_for_element("#month-dropdown", timeout=4)
# #     dash_duo.driver.implicitly_wait(5)
# #     assert (
# #         "January" in dash_duo.find_element("#month-dropdown").text
# #     ), "'January' should appear in the month dropdown"

# # # def test_cycle004_monthdropdownchangesdropdown(dash_duo):
# # #     """
# # #     GIVEN the recycle Dash app is running
# # #     WHEN the area dropdown is changed to Hackney
# # #     THEN the card title for the stats panel is also changed to Hackney.

# # #     Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
# # #     """
# # #     app = import_app(app_file="app_for_testing")
# # #     dash_duo.start_server(app)
# # #     dash_duo.wait_for_element("#month-select", timeout=4)
# # #     select_input = dash_duo.find_element("#month-select input")
# # #     select_input.send_keys("February")
# # #     select_input.send_keys(Keys.RETURN)
# # #     dash_duo.driver.implicitly_wait(5)
# # #     assert (
# # #         "February" in dash_duo.find_element("#month-select").text
# # #     ), "'February' should appear in the month dropdown"

# # # def test_cycle004_monthdropdownchangesdropdown(dash_duo):
# # #     """
# # #     GIVEN the recycle Dash app is running
# # #     WHEN the area dropdown is changed to Hackney
# # #     THEN the card title for the stats panel is also changed to Hackney.

# # #     Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
# # #     """
# # #     app = import_app(app_file="app_for_testing")
# # #     dash_duo.start_server(app)
# # #     dash_duo.wait_for_element("#month-dropdown", timeout=4)
# # #     select_input = dash_duo.find_element("#month-dropdown")
# # #     select_input.send_keys("February")
# # #     select_input.send_keys(Keys.RETURN)
# # #     dash_duo.driver.implicitly_wait(5)
# # #     assert (
# # #         "February" in dash_duo.find_element("#month-dropdown").text
# # #     ), "'February' should appear in the month dropdown"

# # def test_cycle003_monthdropdownchangesdropdown(dash_duo, app):
# #     """
# #     GIVEN the recycle Dash app is running
# #     WHEN the area dropdown is changed to Hackney
# #     THEN the card title for the stats panel is also changed to Hackney.
# #     """
# #     dash_duo.wait_for_element("#month-dropdown", timeout=4)
# #     select_input = dash_duo.find_element("#month-dropdown input")
# #     select_input.send_keys("February")
# #     select_input.send_keys(Keys.RETURN)
# #     dash_duo.driver.implicitly_wait(5)
# #     assert (
# #         "February" in dash_duo.find_element("#month-dropdown").text
# #     ), "'February' should appear in the month dropdown"

# # def test_cycle004_hourdropdowncontains00_06(dash_duo, app):
# #     """
# #     GIVEN the Dash app is running
# #     WHEN the Choropleth Map Showing Pricing Data for Each Borough of London has loaded
# #     THEN 'January' should appear in the area dropdown created for months
# #     """
# #     dash_duo.wait_for_element("#hour-dropdown", timeout=4)
# #     dash_duo.driver.implicitly_wait(5)
# #     assert (
# #         "00:00-06:00" in dash_duo.find_element("#hour-dropdown").text
# #     ), "'00:00-06:00' should appear in the hour dropdown"

# # def test_cycle005_hourdropdownchangesdropdown(dash_duo, app):
# #     """
# #     GIVEN the recycle Dash app is running
# #     WHEN the area dropdown is changed to Hackney
# #     THEN the card title for the stats panel is also changed to Hackney.
# #     """
# #     dash_duo.wait_for_element("#hour-dropdown", timeout=4)
# #     select_input = dash_duo.find_element("#hour-dropdown input")
# #     select_input.send_keys("06:00-09:00")
# #     select_input.send_keys(Keys.RETURN)
# #     dash_duo.driver.implicitly_wait(5)
# #     assert (
# #         "06:00-09:00" in dash_duo.find_element("#hour-dropdown").text
# #     ), "'06:00-09:00' should appear in the hour dropdown"

# # def test_cycle006_daydropdowncontainsjul1(dash_duo, app):
# #     """
# #     GIVEN the Dash app is running
# #     WHEN the Daily data page has loaded
# #     THEN 'Sunday, Jul 1 2018.xlsx' should appear in the area dropdown
# #     """
# #     dash_duo.wait_for_element("#day-dropdown", timeout=4)
# #     dash_duo.driver.implicitly_wait(5)
# #     assert (
# #         "Sunday, Jul 1 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
# #     ), "'Sunday, Jul 1 2018.xlsx' should appear in the daydropdown"


# # def test_cycle007_daydropdownchangesdropdown(dash_duo, app):
# #     """
# #     GIVEN the recycle Dash app is running
# #     WHEN the area dropdown is changed to Hackney
# #     THEN the card title for the stats panel is also changed to Hackney.
# #     """
# #     dash_duo.wait_for_element("#day-dropdown", timeout=4)
# #     select_input = dash_duo.find_element("#day-dropdown input")
# #     select_input.send_keys("Monday, Jul 2 2018.xlsx")
# #     select_input.send_keys(Keys.RETURN)
# #     dash_duo.driver.implicitly_wait(5)
# #     assert (
# #         "Monday, Jul 2 2018.xlsx" in dash_duo.find_element("#day-dropdown").text
# #     ), "'Monday, Jul 2 2018.xlsx' should appear in the day dropdown"


# def test_cycle008_daydropdownchangesdropdown(dash_duo, app):
#     """

#     """
#     dash_duo.wait_for_element("#day-dropdown", timeout=40)
#     select_input = dash_duo.find_element("#day-dropdown input")
#     updated_input = select_input[1]

# #    updated_input = dash_duo.find_element("#day-dropdown input")[1]
#     updated_input.click()
#     dash_duo.driver.implicitly_wait(50)
#     title = dash_duo.find_element("#daily-usage-graph.title")
#     updated_title = title[1].text
#     assert updated_title == "%Change (New)"


# def test_cycle009_daydropdownchangesdropdown(dash_duo, app):
#     """
#     .
#     """
#     dash_duo.wait_for_element("#day-dropdown", timeout=9)
#     select_input = dash_duo.find_element("#day-dropdown input")
#     select_input.send_keys("Monday, Jul 2 2018.xlsx")
#     select_input.send_keys(Keys.RETURN)
#     dash_duo.driver.implicitly_wait(10)
#     title = dash_duo.find_element("#daily-usage-graph .gtitle")
#     assert title[1].text == "Cycle Usage for Monday, Jul 2 2018.xlsx"

# def test_day_dropdown_changes_data_displayed(dash_duo, app):
#     """
#     GIVEN the recycle Dash app is running
#     WHEN a day is selected from the day dropdown
#     THEN the data displayed on the graph should change accordingly.
#     """
#     # GIVEN the recycle Dash app is running
#     dash_duo.start_server(app)

#     # Wait for the day dropdown to appear and select a day
#     day_dropdown = dash_duo.wait_for_element("#day-dropdown", timeout=60)
#     day_dropdown.click()
#     day_option = dash_duo.find_element(".Select-menu-outer .Select-option", index=1)
#     day_option.click()

#     # Wait for the page to finish loading
#     dash_duo.driver.implicitly_wait(60)

#     # THEN the data displayed on the graph should change accordingly.
#     title = dash_duo.find_element("#daily-usage-graph .titletext")
#     assert title.text == "Cycle Usage for the selected day"

# # def test_cycle008_daydropdownchangesdropdown(dash_duo, app):
# #     """
# #     Test that the daily usage chart updates when a different day is selected from the dropdown.
# #     """
# #     dash_duo.wait_for_element("#day-dropdown", timeout=40)
# #     select_input = dash_duo.find_element("#day-dropdown input")
# #     updated_input = select_input[1]
# #     dash_duo.driver.execute_script("arguments[0].scrollIntoView();", updated_input)
# #     updated_input.click()
# #     dash_duo.driver.implicitly_wait(50)
# #     title = dash_duo.find_element("#daily-usage-graph.title")
# #     updated_title = title[1].text
# #     assert updated_title == "%Change (New)"



# def test_cycle001_h3_text_equals(dash_duo, app):
#     """
#     GIVEN the app is running
#     WHEN the home page is available
#     THEN the H2 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
#     """
#     dash_duo.wait_for_element("h3", timeout=4)
#     h2_text = dash_duo.find_element("h3").text
#     assert h2_text.casefold() == "Choropleth Map Showing Pricing Data for Each Borough of London".casefold()


