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
import plotly.graph_objects as go

df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)
dp = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)


def create_daily_chart(day_selected):
    # Read the sheet from the excel file
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=sheet_names[day_selected])
    # Convert the 'TimeString' column to a datetime type
    df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')

    # Extract the hour from the datetime object
    df['hour'] = df['TimeString'].dt.hour

    # Group the data by hour and sum the usage
    grouped_sum = df.groupby('hour').sum(numeric_only=True)
    grouped_mean = df.groupby('hour').mean(numeric_only=True)
    grouped = grouped_sum/grouped_mean
    # Create the bar chart
    fig = px.bar(x=grouped.index, y=grouped.iloc[:,0])

    fig.update_layout(
        xaxis_title="Hour",
        yaxis_title="Cycle hires",
        title=f"Cycle Usage for {sheet_names[day_selected]}"
    )
    return fig

# Get the sheet names from the excel file
sheet_names = list(pd.read_excel("data_set_prepared.xlsx", sheet_name=None).keys())
# Remove the first two sheets from the list
sheet_names = sheet_names[2:]
# Remove the .xlsx to allow the sheet names to be sorted 
sheet_names = [name.rstrip('.xlsx') for name in sheet_names]
# Order the sheet names by date
sheet_names = sorted(sheet_names, key=lambda x: pd.to_datetime(x, format="%A, %b %d %Y"))

sheet_title=sheet_names
# Add the '.xlsx' backl into the file
sheet_names = [name + '.xlsx' for name in sheet_names]

#function for average monthly usage chart
def create_monthly_barchart():
    # Read the second sheet of the excel file
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

    # Convert the 'Month' column to a datetime type
    df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m-%d %H:%M:%S')

    # Extract the month from the datetime object
    df['month'] = df['Month'].dt.month

    # Slice the data frame to exclude the first 18 rows in order to prevent the skewing of the graph
    df = df.iloc[18:, :]

    # Group the data by month and average the usage
    grouped = df.groupby('month').mean()

    # Create the bar chart
    fig2 = px.bar(x=grouped.index, y=grouped.iloc[:, 1])

    fig2.update_layout(
        xaxis_title="Month",
        yaxis_title="Average Usage",
        xaxis = dict(
        tickmode = 'array',
        tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ))
    return fig2

#function for a monehtly line chart
def create_monthly_linechart():

    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

    fig3 = px.line(df, x="Month", y="Number of Bicycle Hires.1")
    fig3.update_layout(
        xaxis_title="Time(year)",
        yaxis_title="Average Usage"
    )

    return fig3



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

tab1_content = html.Div(style={'display': 'flex'}, children=[
    html.Div(style={'flex': 1}, children=[
        dcc.Graph(id='daily-usage-graph', figure=create_daily_chart(day_selected=0))
    ]),
    html.Div(style={'flex': 0.5, 'padding': 20}, children=[
        dcc.Dropdown(id='day-dropdown', options=[{'label': sheet_name, 'value': i} for i, sheet_name in enumerate(sheet_names)], value=0)
    ])
    ],
        className="p-3 bg-light rounded-3",
    )
tab2_content = html.Div(
        [ 
        dcc.Graph(figure=create_monthly_barchart())
        ],
        className="p-3 bg-light rounded-3",
    )
tab3_content = html.Div(
        [ 
        dcc.Graph(figure=create_monthly_linechart())
        ],
        className="p-3 bg-light rounded-3",
    )

tab4_content = html.Div(
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


# Create the app layout using Bootstrap fluid container
# app.layout = dbc.Container(
#     fluid=True,
#     children=[
#         # Second row here
#         dbc.Row(
#             [
#                 # This is for the London area selector and the statistics panel.
#                 dbc.Col(
#                     width=3,
#                     children=[
#                         html.H4("Select day"),
#                         # dcc.Dropdown(
#                         #     id="day-select",
#                         #     options=[
#                         #         {"label": x, "value": x}
#                         #         for x in data.area_list
#                         #     ],
#                         #     value="London",
#                         # ),
#                         html.Br(),
#                         html.Div(id="stats-card"),
#                     ],
#                 ),
#                 # Add the second column here. This is for the figure.
#                 dbc.Col(
#                     width=9,
#                     children=[
#                         html.H2("Usage"),
#                         dcc.Graph(id="recycle-chart", figure=create_daily_chart(day_selected)),
#                     ],
#                 ),
#             ]
#         ),
#     ],
# )

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return dbc.Tabs(
            [
                dbc.Tab(tab1_content, label="Daily Usage Bar Chart"),
                dbc.Tab(tab2_content, label="Average Monthly Usage Bar Chart"),
                dbc.Tab(tab3_content, label="Usage Vs Time Line Chart")
            ],
            id="tabs",
            active_tab="scatter",
        ),
    elif pathname == "/page-2":
        return dbc.Tabs(
            [
                dbc.Tab(tab4_content, label="Chart 1"),
                dbc.Tab(tab1_content, label="Chart 2"),
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

@app.callback(
    dash.dependencies.Output('daily-usage-graph', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')]
)
def update_graph(day_selected):
    return create_daily_chart(day_selected)


# import dash
# import dash_bootstrap_components as dbc
# from dash import Input, Output, dcc, html
# from dash import dcc
# import pandas as pd

# df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)
# dp = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)




# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# # the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }

# # the styles for the main content position it to the right of the sidebar and
# # add some padding.
# CONTENT_STYLE = {
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# }

# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Chart 1", href="/page-1", active="exact"),
#                 dbc.NavLink("Chart 2", href="/page-2", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )

# content = html.Div(id="page-content", style=CONTENT_STYLE)

# app.layout = html.Div([dcc.Location(id="url"), sidebar, content])



# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return html.P("This is the content of the home page!")
#     elif pathname == "/page-1":
#         return html.Div(
#         [ 
#             html.Hr(),
#             html.P(f"Bar chart"),
#             html.Hr(),
#             dcc.Graph(id='bar-chart',
#               figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,2], 'type': 'bar'}],
#                       'layout': {'title': 'Montly Cycle Usage Bar Chart from Excel Data'}})
#         ],
#         className="p-3 bg-light rounded-3",
#     )
#     elif pathname == "/page-2":
#         return html.Div(
#         [ 
#             html.Hr(),
#             html.P(f"Bar chart"),
#             html.Hr(),
#             dcc.Graph(id='bar-chart2',
#               figure={'data': [{'x': dp.iloc[:,1], 'y': dp.iloc[:,4], 'type': 'bar'}],
#                       'layout': {'title': 'Borough PM 2.5 Pollution Bar Chart from Excel Data'}})
#         ],
#         className="p-3 bg-light rounded-3",    
#     )
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
