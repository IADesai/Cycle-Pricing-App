import dash
import json
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)

# Load GeoJSON file
with open('london_boroughs_proper.geojson') as f:
    geo = json.load(f)

fig = px.choropleth(df, geojson=geo, color='Total PM 2.5',
                        color_continuous_scale='Viridis',
                        featureidkey='Borough',
                        locations='Borough',
                        center={"lat": 51.5074, "lon": -0.1278})

# Create Dash app
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='London Boroughs Choropleth Map'),
    dcc.Graph(id='london-map', figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
