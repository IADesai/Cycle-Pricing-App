import dash
import json
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)

# Group the data by month and average the usage
grouped = df.groupby('Borough').sum('Total PM 2.5')

# Load GeoJSON file
with open('london_boroughs.json') as f:
    geo = json.load(f)
    
# Create a DataFrame with the borough names and usage values
data = pd.DataFrame({'locations': grouped.index, 'Total PM 2.5': grouped.iloc[:, 3]})

# Create map figure
fig = px.choropleth_mapbox(data, geojson=geo, color='Total PM 2.5',
                           color_continuous_scale='RdYlGn_r',
                           mapbox_style='carto-positron',
                           featureidkey='properties.name',
                           locations='locations',
                           center={"lat": 51.5074, "lon": -0.1278},
                           zoom=10)

# Create Dash app layout
app = dash.Dash()
app.layout = dash.html.Div([
    dash.html.H1('London Boroughs Choropleth Map'),
    dash.dcc.Graph(id='london-map', figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run_server()