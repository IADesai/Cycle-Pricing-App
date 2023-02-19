"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.
dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.
For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash import dcc
import pandas as pd
import plotly.express as px

df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)
dp = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)




app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

tab1_content = html.Div(
        [ 
            html.Hr(),
            html.P(f"Bar chart"),
            html.Hr(),
            dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,2], 'type': 'bar'}],
                      'layout': {'title': 'Montly Cycle Usage Bar Chart from Excel Data'}})
        ],
        className="p-3 bg-light rounded-3",
    )


tab2_content = html.Div(
        [
            html.Hr(),
            html.P(f"Bar chart"),
            html.Hr(),
            dcc.Graph(id='bar-chart2',
              figure={'data': [{'x': dp.iloc[:,1], 'y': dp.iloc[:,4], 'type': 'bar'}],
                      'layout': {'title': 'Borough PM 2.5 Pollution Bar Chart from Excel Data'}})
        ],

)

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Chart 1", href="/page-1", active="exact"),
                dbc.NavLink("Chart 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.Div(
        [ 
            html.Hr(),
            html.P(f"Bar chart"),
            html.Hr(),
            dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,2], 'type': 'bar'}],
                      'layout': {'title': 'Montly Cycle Usage Bar Chart from Excel Data'}})
        ],
        className="p-3 bg-light rounded-3",
    )
    elif pathname == "/page-2":
        return dbc.Tabs(
            [
                dbc.Tab(tab1_content, label="Chart 1"),
                dbc.Tab(tab2_content, label="Chart 2"),
            ],
            id="tabs",
            active_tab="scatter",
        ),
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return html.P("This is the content of the home page!")
#     elif pathname == "/page-1":
#         return html.P("This is the content of page 1. Yay!")
#     elif pathname == "/page-2":
#         return html.P("Oh cool, this is page 2!")
#     # If the user tries to reach a different page, return a 404 message
#     return html.Div(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ],
#         className="p-3 bg-light rounded-3",
#     )


# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return html.P("This is the content of the home page!")
#     elif pathname == "/page-1": 
#         return dcc.Graph(id='bar-chart',
#               figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,2], 'type': 'bar'}],
#                       'layout': {'title': 'Montly Cycle Usage Bar Chart from Excel Data'}})

   

# app.layout = html.Div([
#     html.H1("Dash App"),
#     dcc.Graph(id='bar-chart',
#               figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,2], 'type': 'bar'}],
#                       'layout': {'title': 'Montly Cycle Usage Bar Chart from Excel Data'}})
# , sidebar, content])


if __name__ == "__main__":
    app.run_server(port=8889)
