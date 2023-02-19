import dash_bootstrap_components as dbc
import dash
import json
from dash import Input, Output, dcc, html
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

app.layout = dbc.Container(
    # HTML layout elements here
    children=[
        html.H1(children='Hello, World!', className="display-1"),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)