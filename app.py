# Import the required packages
from pathlib import Path
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

DATA_FILEPATH = Path(__file__).parent.joinpath("data_set_prepared.xlsx")

# Creates the Dash app
#app = Dash(__name__)
app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

# Creates the HTML page layout and adds it to the app. This uses dash.html package to add HTML components.
""" app.layout = dbc.Container(
    # HTML layout elements here
     children=[
        # The 'children' of the H1 element in this case is the content to be displayed. You can also ommit the keyword as shown in the P example.
        html.H1(children='Hello, World!'),
        html.P('My first app'),
        ]
)
 """

app.layout = dbc.Container(
    children=[
        html.H1(children='Hello, World!', className="display-1"),
    ]
)
""" app.layout = html.Div(
    # The first element is the html.Div. The 'child' elements of the Div are those elements that are inside the Div. In this case a H1 heading.
    children=[
        # The 'children' of the H1 element in this case is the content to be displayed. You can also ommit the keyword as shown in the P example.
        html.H1(children='Hello, World!'),
        html.P('My first app'),
        ]
) """

if __name__ == '__main__':
    app.run_server(debug=True)
