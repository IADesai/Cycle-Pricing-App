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
import json
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, dcc, html
from dash import dcc
from pathlib import Path

cwd = Path(__file__).resolve().parent.parent

excel_file_path = cwd / "data_set_prepared.xlsx"

json_file_path = cwd / "london_boroughs.json"

df = pd.read_excel(excel_file_path, sheet_name=1)
dp = pd.read_excel(excel_file_path, sheet_name=0)

def create_pricing_choropleth_map(hour_selected,month_selected):
    # Load data
    df = pd.read_excel(excel_file_path, sheet_name=0)

    # Group the data by month and average the usage
    grouped = df.groupby('Borough').sum('Total PM 2.5')

    # Load GeoJSON file
    with open(json_file_path) as f:
        geo = json.load(f)

    if hour_selected==1:
        multiplier = 0.8
    elif hour_selected==2:
        multiplier = 1.4
    elif hour_selected==3:
        multiplier = 0.9
    elif hour_selected==4:
        multiplier = 1.0
    else:
        multiplier = 0.85

    if month_selected==1:
        multiplier2 = 0.9
    elif month_selected==2:
        multiplier2 = 0.9
    elif month_selected==3:
        multiplier2 = 1.0
    elif month_selected==4:
        multiplier2 = 1.0
    elif month_selected==5:
        multiplier2 = 1.1
    elif month_selected==6:
        multiplier2 = 1.2
    elif month_selected==7:
        multiplier2 = 1.3
    elif month_selected==8:
        multiplier2 = 1.2
    elif month_selected==9:
        multiplier2 = 1.1
    elif month_selected==10:
        multiplier2 = 1.0
    elif month_selected==11:
        multiplier2 = 1.0
    else:
        multiplier2 = 0.9
    
    for i in range(0,33):
        if  grouped.iloc[i, 3]> 0 and grouped.iloc[i, 3] < 25:
            grouped.iloc[i, 3]=1.65 * multiplier * multiplier2
        elif grouped.iloc[i, 3] > 25 and grouped.iloc[i, 3] < 50:
            grouped.iloc[i, 3]=1.45 * multiplier * multiplier2
        elif grouped.iloc[i, 3] > 50 and grouped.iloc[i, 3] < 75:
            grouped.iloc[i, 3]=1.25 * multiplier * multiplier2
        elif grouped.iloc[i, 3] > 75:
            grouped.iloc[i, 3]=1.00 * multiplier * multiplier2

    # Create a DataFrame with the borough names and usage values
    data = pd.DataFrame({'Borough': grouped.index, 'Cycle Hire Price (£/30min)': round(grouped.iloc[:, 3], 2)})

    # Create map figure
    figprice = px.choropleth_mapbox(data, geojson=geo, color='Cycle Hire Price (£/30min)',
                            color_continuous_scale='RdYlGn_r',
                            opacity=0.8,
                            mapbox_style='carto-positron',
                            featureidkey='properties.name',
                            locations='Borough',
                            center={"lat": 51.4933, "lon": -0.1},
                            zoom=8.7)
    return figprice

# def create_daily_chart(day_selected):
#     # Read the sheet from the excel file
#     df = pd.read_excel(excel_file_path, sheet_name=sheet_names[day_selected])
#     # Convert the 'TimeString' column to a datetime type
#     df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')

#     # Extract the hour from the datetime object
#     df['hour'] = df['TimeString'].dt.hour

#     # Group the data by hour and sum the usage
#     grouped_sum = df.groupby('hour').sum(numeric_only=True)
#     grouped_mean = df.groupby('hour').mean(numeric_only=True)
#     grouped = grouped_sum/grouped_mean
#     # Create the bar chart
#     fig = px.bar(x=grouped.index, y=grouped.iloc[:,0])

#     fig.update_layout(
#         xaxis_title="Hour",
#         yaxis_title="Cycle hires",
#         title=f"Cycle Usage for {sheet_names[day_selected]}"
#     )
#     return fig

# # Get the sheet names from the excel file
# sheet_names = list(pd.read_excel(excel_file_path, sheet_name=None).keys())
# # Remove the first two sheets from the list
# sheet_names = sheet_names[2:]
# # Remove the .xlsx to allow the sheet names to be sorted 
# sheet_names = [name.rstrip('.xlsx') for name in sheet_names]
# # Order the sheet names by date
# sheet_names = sorted(sheet_names, key=lambda x: pd.to_datetime(x, format="%A, %b %d %Y"))

# sheet_title=sheet_names
# # Add the '.xlsx' backl into the file
# sheet_names = [name + '.xlsx' for name in sheet_names]

def create_daily_chart(day_selected):
    # Read the sheet from the excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_names[day_selected])
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
sheet_names = list(pd.read_excel(excel_file_path, sheet_name=None).keys())
# Remove the first two sheets from the list
sheet_names = sheet_names[2:]
# Remove the .xlsx to allow the sheet names to be sorted 
sheet_names = [name.rstrip('.xlsx') for name in sheet_names]
# Order the sheet names by date
sheet_names = sorted(sheet_names, key=lambda x: pd.to_datetime(x, format="%A, %b %d %Y"))
# Add the '.xlsx' back into the file
sheet_names = [name + '.xlsx' for name in sheet_names]

# src for the gif created by using the free version of the Stripo aplication, ref: https://stripo.email
# The gif logo was created by Canva
top_card = dbc.Card(
    [
        dbc.CardImg(src="https://lzqqcs.stripocdn.email/content/guids/CABINET_797e23668dad8bd7e5aee86260d52cc9/images/the_coding_cyclists.gif", top=True),
        
    ],
    style={"width": "14rem"},
    
)



# Function for the stats panel
def create_daily_stats(day_selected):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_names[day_selected])
    # Convert the 'TimeString' column to a datetime type
    df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')
    # Extract the hour from the datetime object
    df['hour'] = df['TimeString'].dt.hour

    # Group the data by hour and sum the usage
    grouped_sum = df.groupby('hour').sum(numeric_only=True)
    grouped_mean = df.groupby('hour').mean(numeric_only=True)
    grouped = grouped_sum/grouped_mean
    # calculate the average usage per hour
    avg_usage_per_hour = round(grouped.iloc[:, 0].mean(), 2)

    # calculate the total usage for the day
    total_usage = round(grouped.iloc[:, 0].sum(), 2)

    # create the stats panel
    stats_panel = dbc.Card(
        [
            dbc.CardHeader("Daily Usage Stats"),
            dbc.CardBody(
                [
                    html.P(f"Average Usage per Hour: {avg_usage_per_hour}"),
                    html.P(f"Total Usage: {total_usage}"),
                ]
            ),
        ],
        color="dark",
        inverse=True,
    )

    return stats_panel

hours=('00:00-06:00','06:00-09:00','09:00-16:00','16:00-19:00','19:00-24:00')
months=('January','February','March','April','May','June','July','August','September','October','November','December')
# # Function for the stats panel
# def create_daily_stats(day_selected):
#     df = pd.read_excel(excel_file_path, sheet_name=sheet_names[day_selected])
#     # Convert the 'TimeString' column to a datetime type
#     df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')
    
#     # calculate the average usage per hour
#     df['hour'] = df['TimeString'].dt.hour
#     grouped_mean = df.groupby('hour').mean(numeric_only=True)
#     avg_usage_per_hour = round(grouped_mean.iloc[:, 0].mean(), 2)

#     # calculate the total usage for the day
#     total_usage = round(df.iloc[:, 1].sum(), 2)

#     # create the stats panel
#     stats_panel = dbc.Card(
#         [
#             dbc.CardHeader("Daily Usage Stats"),
#             dbc.CardBody(
#                 [
#                     html.P(f"Average Usage per Hour: {avg_usage_per_hour}"),
#                     html.P(f"Total Usage: {total_usage}"),
#                 ]
#             ),
#         ],
#         color="light",
#         inverse=True,
#     )

#     return stats_panel


#function for average monthly usage chart
def create_monthly_barchart():
    # Read the second sheet of the excel file
    df = pd.read_excel(excel_file_path, sheet_name=1)

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

    df = pd.read_excel(excel_file_path, sheet_name=1)

    fig3 = px.line(df, x="Month", y="Number of Bicycle Hires.1")
    fig3.update_layout(
        xaxis_title="Time(year)",
        yaxis_title="Average Usage"
    )

    return fig3

def create_choropleth_pollution_map():
    # Load data
    df = pd.read_excel(excel_file_path, sheet_name=0)

    # Group the data by month and average the usage
    grouped = df.groupby('Borough').sum('Total PM 2.5')

    # Load GeoJSON file
    with open(json_file_path) as f:
        geo = json.load(f)
        
    # Create a DataFrame with the borough names and usage values
    data = pd.DataFrame({'Borough': grouped.index, 'Total PM 2.5': grouped.iloc[:, 3]})

    # Create map figure
    fig5 = px.choropleth_mapbox(data, geojson=geo, color='Total PM 2.5',
                            color_continuous_scale='RdYlGn_r',
                            opacity=0.8,
                            mapbox_style='carto-positron',
                            featureidkey='properties.name',
                            locations='Borough',
                            center={"lat": 51.5, "lon": -0.1},
                            zoom=8.85)
    return fig5



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

home_content = html.Div(
        [
            dash.html.H1('TFL Cycle Hire Pricing'),
           
            html.P("The Coding Cyclists have tackled TFL's cycle hire pricing, masterminding an algorithm to adjust the price of the cycle hire dependent on hourly and monthly cycle hire data, alongside PM 2.5 pollution levels across the boroughs of London. The aim was to create a price map that increases TFL revenue by promoting cycle hire and taking advantage of rush hour prices, as well as, promoting cycle hire in highly polluted boroughs with hopes to reduce pollution across greater London."),
            html.Hr(),
            html.P(f'Choropleth Map Showing Pricing Data for Each Borough of London'),
            html.Hr(),
            html.Div([
            dcc.Graph(id='london-map', figure=create_pricing_choropleth_map(hour_selected=0, month_selected=0), style={'width': '1100px', 'height': '650px'}),
            html.Div([
                html.P("Time of Day (24 Hour Clock):",style={'margin-top': '200px'}),
                dcc.Dropdown(id='hour-dropdown', options=[{'label': hour, 'value': i} for i, hour in enumerate(hours)], value=0),
                html.P("Month of Year:",style={'margin-top': '30px'}),
                dcc.Dropdown(id='month-dropdown', options=[{'label': month, 'value': i} for i, month in enumerate(months)], value=0)
            ], style={'float': 'right', 'width': '30%'})
        ], style={'display': 'flex', 'justify-content': 'space-between'})
    ]
)
daily_content = html.Div(
    [
        html.Hr(),
        html.P(f'Choropleth Map Showing Pricing Data for Each Borough of London'),
        html.Hr(),
        html.P("The Coding Cyclists have tackled TFL's cycle hire pricing, masterminding an algorithm to adjust the price of the cycle hire dependent on hourly and monthly cycle hire data, alongside PM 2.5 pollution levels across the boroughs of London. The aim was to create a price map that increases TFL revenue by promoting cycle hire and taking advantage of rush hour prices, as well as, promoting cycle hire in highly polluted boroughs with hopes to reduce pollution across greater London."),
         
    ],
)
tab1_content = html.Div(style={'display': 'flex'}, children=[
    html.Div(style={'flex': 1}, children=[
        dcc.Graph(id='daily-usage-graph', figure=create_daily_chart(day_selected=0))
    ]),
    html.Div(style={'flex': 0.5, 'padding': 20}, children=[
        dcc.Dropdown(id='day-dropdown', options=[{'label': sheet_name, 'value': i} for i, sheet_name in enumerate(sheet_names)], value=0),
    html.Br(),
    html.Div(id="stats-card"),
    ])
    ],
        className="p-3 bg-light rounded-3",
    )

# tab1_content = html.Div(style={'display': 'flex'}, children=[
#     html.Div(style={'flex': 1}, children=[
#         dcc.Graph(id='daily-usage-graph', figure=create_daily_chart(day_selected=0))
#     ]),
#     html.Div(style={'flex': 0.5, 'padding': 20}, children=[
#         dcc.Dropdown(id='day-select', options=[{'label': sheet_name, 'value': x}
#                                                for x, sheet_name in enumerate(sheet_names)], value=0),
#         html.Br(),
#         html.Div(id="stats-card"),
#     ])
# ], className="p-3 bg-light rounded-3", 
# )
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
            html.P(f"Bar Chart Showing PM 2.5 Pollution in Each Borough of London"),
            html.Hr(),
            dcc.Graph(id='bar-chart2',
              figure={'data': [{'x': dp.iloc[:,1], 'y': dp.iloc[:,4], 'type': 'bar'}]})
        ],
)
tab5_content = html.Div(
        [
            html.Hr(),
            html.P(f'Choropleth Map Showing Total Recorded PM 2.5 Particle Data for Each Borough of London'),
            html.Hr(),
            dcc.Graph(id='london-map', figure=create_choropleth_pollution_map(), style={'width': '1100px', 'height': '600px'})
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
        dbc.Row(
            [dbc.Col(top_card, width="auto"),
            ]),
        html.Br(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Daily/Hourly Data", href="/page-1", active="exact"),
                dbc.NavLink("Monthly Data", href="/page-2", active="exact"),
                dbc.NavLink("Pollution Data", href="/page-3", active="exact"),
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
        return home_content
    elif pathname == "/page-1":
        return html.Div([
                dbc.Tabs(
                [
                    dbc.Tab(tab1_content, label="Daily Usage Bar Chart"),
                ],
                id="tabs",
                active_tab=None,
                ),
                html.Hr(),
                html.P(f'Daily Data'),
                html.Hr(),
                html.P("The daily data consists of recorded cycle hire data for every day in an entire month. We used this data to identify and visualize how many cycles were hired per hour of the day for each day in the month and then created a chart with the average of the entire month, to identify the average daily cycle hire pattern. This can be viewed in the tab above, where a selector can be used to view the data for each day. If you choose Monday and compare it to a Sunday for example, we see that the trends are slightly different. This can be seen throughout the month, where weekends have unusual patterns as opposed to working week days. This is only one of many trends visible.")
            ]),
    elif pathname == "/page-2":
        return html.Div([
            dbc.Tabs(
            [
                dbc.Tab(tab2_content, label="Average Monthly Usage Bar Chart"),
                dbc.Tab(tab3_content, label="Usage Vs Time Line Chart")
            ],
            id="tabs",
            active_tab="scatter",
            ),
            html.Hr(),
            html.P(f'Monthly Data'),
            html.Hr(),
            html.P("The monthly data consists of recorded cycle hire data for every month over multiple years. We used this data to identify and visualize how many cycles were hired in each month over multiple years, averaging the number of cycles for each month over the various years, to identify the average monthly cycle hire usage pattern. This can be viewed in the tab above. We also added a usage versus time line chart, to show the cycle hire trends from the beginning of TFL santander cycle history. This gives indications of monthly/seasonal trends aswell as for example, Covid effects in 2020.")
        ]),
    elif pathname == "/page-3":
        return html.Div([
            dbc.Tabs(
            [
                dbc.Tab(tab5_content, label="London Borough Pollution Choropleth Map"),
                dbc.Tab(tab4_content, label="London Borough Pollution Bar Chart"),
            ],
            id="tabs",
            active_tab="scatter",
            ),
            html.Hr(),
            html.P(f'Pollution Data'),
            html.Hr(),
            html.P("The pollution data consists of numerous recorded PM 2.5 particle data pieces from each borough of London. The recorded data was summed for each borough, providing data for the total PM 2.5 particles released from methods of transport, in each borough. This data was plotted onto a choropleth map, where it is possible to visibily see the levels of PM 2.5 in each specified borough. This can be seen above, accompanied by a bar chart for extra clarity.")
        ]),
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

@app.callback(
    Output("stats-card", "children"),
    Input("day-dropdown", "value"),
)
def update_daily_stats(day_selected):
    return create_daily_stats(day_selected=day_selected)

@app.callback(
    dash.dependencies.Output('london-map', 'figure'),
    [dash.dependencies.Input('hour-dropdown', 'value')],
    [dash.dependencies.Input('month-dropdown', 'value')]
)
def update_pricegraph(hour_selected,month_selected):
    return create_pricing_choropleth_map(hour_selected,month_selected)

# @app.callback(
#     Output("stats-card", "children"),
#     Input("day-select", "value"),
# )
# def update_daily_stats(day_selected):
#     return create_daily_stats(day_selected=day_selected)
# import dash
# import dash_bootstrap_components as dbc
# from dash import Input, Output, dcc, html
# from dash import dcc
# import pandas as pd

# df = pd.read_excel(excel_file_path, sheet_name=1)
# dp = pd.read_excel(excel_file_path, sheet_name=0)




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
# create the stats panel for daily usage


if __name__ == "__main__":
    app.run_server(port=8050)
# if __name__ == '__main__':
#     app.run_server(debug=True)