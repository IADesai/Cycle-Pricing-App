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

df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)
dp = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)

# Get the sheet names from the excel file
sheet_names = list(pd.read_excel("data_set_prepared.xlsx", sheet_name=None).keys())
# Remove the first two sheets from the list
sheet_names = sheet_names[2:]
# Remove the .xlsx to allow the sheet names to be sorted 
sheet_names = [name.rstrip('.xlsx') for name in sheet_names]
# Order the sheet names by date
sheet_names = sorted(sheet_names, key=lambda x: pd.to_datetime(x, format="%A, %b %d %Y"))
# Add the '.xlsx' back into the file
sheet_names = [name + '.xlsx' for name in sheet_names]


top_card = dbc.Card(
    [
        dbc.CardImg(src="https://lzqqcs.stripocdn.email/content/guids/CABINET_797e23668dad8bd7e5aee86260d52cc9/images/the_coding_cyclists.gif", top=True),
        
    ],
    style={"width": "18rem"},
)




def create_pricing_choropleth_map(hour_selected,month_selected):
    # Load data
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)

    # Group the data by month and average the usage
    grouped = df.groupby('Borough').sum('Total PM 2.5')

    # Load GeoJSON file
    with open('london_boroughs.json') as f:
        geo = json.load(f)

    if hour_selected==1:
        multiplier = 2.0
    elif hour_selected==2:
        multiplier = 1.5
    elif hour_selected==3:
        multiplier = 1.0
    elif hour_selected==4:
        multiplier = 1.0
    else:
        multiplier = 1.2

    if month_selected==1:
        multiplier2 = 2.0
    elif month_selected==2:
        multiplier2 = 1.5
    elif month_selected==3:
        multiplier2 = 1.0
    elif month_selected==4:
        multiplier2 = 1.0
    elif month_selected==5:
        multiplier2 = 1.0
    elif month_selected==6:
        multiplier2 = 1.5
    elif month_selected==7:
        multiplier2 = 1.0
    elif month_selected==8:
        multiplier2 = 1.0
    elif month_selected==9:
        multiplier2 = 1.0
    elif month_selected==10:
        multiplier2 = 1.5
    elif month_selected==11:
        multiplier2 = 1.0
    else:
        multiplier2 = 1.2
    
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
    data = pd.DataFrame({'Borough': grouped.index, 'Cycle Hire Price (£/30min)': grouped.iloc[:, 3]})

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

def create_daily_stats(day_selected):
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=sheet_names[day_selected])
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


app.layout = dbc.Container(
    # HTML layout elements here
    children=[
        
        html.Div(
        [  html.H1("The Coding Cyclists", className="display-4"),
           
           html.P(
            "TFL Cycle Hire Pricing Data Made Easy", className="lead"
            ),
        
    dbc.Row(
    [
        dbc.Col(top_card, width="auto"),
    ]
),
            html.Hr(),
            html.H2('TFL Cycle Hire Pricing'),
            html.P("The Coding Cyclists have tackled TFL's cycle hire pricing, masterminding an algorithm to adjust the price of the cycle hire dependent on hourly and monthly cycle hire data, alongside PM 2.5 pollution levels across the boroughs of London. The aim was to create a price map that increases TFL revenue by promoting cycle hire and taking advantage of rush hour prices, as well as, promoting cycle hire in highly polluted boroughs with hopes to reduce pollution across greater London."),
            html.Hr(),
            html.P(f'Choropleth Map Showing Pricing Data for Each Borough of London'),
            dcc.Graph(id='london-map', figure=create_pricing_choropleth_map(hour_selected=0,month_selected=0), style={'width': '1100px', 'height': '550px'}),
            dcc.Dropdown(id='hour-dropdown', options=[{'label': hour, 'value': i} for i, hour in enumerate(hours)], value=0),
            html.Br(),
            dcc.Dropdown(id='month-dropdown', options=[{'label': month, 'value': i} for i, month in enumerate(months)], value=0),
            html.Br(),
            html.Br()
            
            
    
           
        ],
),
    html.Div(style={'display': 'flex'}, children=[
    html.Div(style={'flex': 1}, children=[
    html.Br(),
    html.Hr(),
    html.Hr(),
    html.P(f'Daily Data'),
    html.Hr(),
    html.P("The daily data consists of recorded cycle hire data for every day in an entire month. We used this data to identify and visualize how many cycles were hired per hour of the day for each day in the month and then created a chart with the average of the entire month, to identify the average daily cycle hire pattern. This can be viewed in the tab above, where a selector can be used to view the data for each day. If you choose Monday and compare it to a Sunday for example, we see that the trends are slightly different. This can be seen throughout the month, where weekends have unusual patterns as opposed to working week days. This is only one of many trends visible."),
    html.Br(),
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
    

    ]
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


if __name__ == '__main__':
    app.run_server(debug=True)