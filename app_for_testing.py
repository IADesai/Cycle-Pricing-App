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

hours=('00:00-06:00','06:00-09:00','09:00-16:00','16:00-19:00','19:00-24:00')
months=('January','February','March','April','May','June','July','August','September','October','November','December')


app.layout = dbc.Container(
    # HTML layout elements here
    children=[
        html.H1(children='Hello, World!', className="display-1"),
        html.Div(
        [
            dash.html.H1('TFL Cycle Hire Pricing'),
            html.P("The Coding Cyclists have tackled TFL's cycle hire pricing, masterminding an algorithm to adjust the price of the cycle hire dependent on hourly and monthly cycle hire data, alongside PM 2.5 pollution levels across the boroughs of London. The aim was to create a price map that increases TFL revenue by promoting cycle hire and taking advantage of rush hour prices, as well as, promoting cycle hire in highly polluted boroughs with hopes to reduce pollution across greater London."),
            html.Hr(),
            html.P(f'Choropleth Map Showing Pricing Data for Each Borough of London'),
            html.Hr(),
            dcc.Graph(id='london-map', figure=create_pricing_choropleth_map(hour_selected=0,month_selected=0), style={'width': '1100px', 'height': '550px'}),
            dcc.Dropdown(id='hour-dropdown', options=[{'label': hour, 'value': i} for i, hour in enumerate(hours)], value=0),
            dcc.Dropdown(id='month-dropdown', options=[{'label': month, 'value': i} for i, month in enumerate(months)], value=0)
        ],
)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)