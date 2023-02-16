from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys


# test case id format is an abbreviation in the pattern of mmffddd where m stands for module,
# f for file, and d for three digits which convey the number of your test case.
def test_rec001_h1_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'Waste and recycling' (not case sensitive)
    """
    app = import_app(app_file="recycle_app.recycle_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h2", timeout=4)
    h1_text = dash_duo.find_element("h2").text
    assert h1_text.casefold() == "Sidebar".casefold()
