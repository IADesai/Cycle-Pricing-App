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

# def test_cycle001_h1_text_equals(dash_duo, app):
#     """
#     GIVEN the app is running
#     WHEN the home page is available
#     THEN the H1 heading element should include the text 'The Coding Cyclists' (not case sensitive)
#     """
#     #app = import_app(app_file="app_for_testing")
#     #dash_duo.start_server(app)
#     dash_duo.wait_for_element("H2", timeout=4)
#     h1_text = dash_duo.find_element("H2").text
#     assert h1_text.casefold() == "Month of Year:".casefold()


def test_cycle001_h2_text_equals(dash_duo, app2):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H2 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
    """
    dash_duo.wait_for_element("h2", timeout=4)
    h2_text = dash_duo.find_element("h2").text
    assert h2_text.casefold() == "Choropleth Map Showing Pricing Data for Each Borough of London".casefold()


<<<<<<< HEAD
def test_cycle002_h3_text_equals(dash_duo, app):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H2 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
    """
    dash_duo.wait_for_element("h3", timeout=4)
    h3_text = dash_duo.find_element("h3").text
    assert h3_text.casefold() == "Month of Year:".casefold()
=======
# def test_cycle002_h2_text_equals_2(dash_duo, app2):
#     """
#     GIVEN the app is running
#     WHEN the home page is available
#     THEN the H2 heading element should include the text 'TFL Cycle Hire Pricing' (not case sensitive)
#     """
#     dash_duo.wait_for_element("h2", timeout=4)
#     h2_text_2 = dash_duo.find_element("h2").text
#     assert h2_text_2.casefold() == "Month of Year:".casefold()
>>>>>>> 58c9e3add01269dcdaea52b5bb920c442ba6ba7f
    
