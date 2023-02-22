from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

# Import the names of callback functions you want to test
from test_app import update_pricegraph, create_pricing_choropleth_map

def test_update_callback():
    output = update_pricegraph(hour_selected,month_selected)
    assert output == create_pricing_choropleth_map(hour_selected,month_selected)