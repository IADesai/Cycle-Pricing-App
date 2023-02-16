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

print (grouped.iloc[1, 3])

for i in range(0,33):
    if  grouped.iloc[i, 3]> 0 and grouped.iloc[i, 3] < 25:
        grouped.iloc[i, 3]=1.65
    elif grouped.iloc[i, 3] > 25 and grouped.iloc[i, 3] < 50:
        grouped.iloc[i, 3]=1.45
    elif grouped.iloc[i, 3] > 50 and grouped.iloc[i, 3] < 75:
        grouped.iloc[i, 3]=1.25
    elif grouped.iloc[i, 3] > 75:
        grouped.iloc[i, 3]=1.00

# Create a DataFrame with the borough names and usage values
data = pd.DataFrame({'Borough': grouped.index, 'Cycle Hire Price per Half Hour in Pounds': grouped.iloc[:, 3]})

# Create map figure
fig = px.choropleth_mapbox(data, geojson=geo, color='Cycle Hire Price per Half Hour in Pounds',
                           color_continuous_scale='RdYlGn_r',
                           opacity=0.8,
                           mapbox_style='carto-positron',
                           featureidkey='properties.name',
                           locations='Borough',
                           center={"lat": 51.5, "lon": -0.1},
                           zoom=9)

# Create Dash app layout
app = dash.Dash()
app.layout = dash.html.Div([
    dash.html.H1('London Boroughs Choropleth Map'),
    dash.dcc.Graph(id='london-map', figure=fig, style={'width': '1400px', 'height': '900px'})
])

# Run the app
if __name__ == "__main__":
    app.run_server()