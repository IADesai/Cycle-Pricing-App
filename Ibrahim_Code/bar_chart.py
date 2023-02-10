import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
import pandas as pd

# Load the London Borough Boundary dataset
dc = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/london_borough_boundaries.csv")

# Load the population data
population = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/london_population.csv")

# Merge the population data with the boundary data
dc = pd.merge(dc, population, on="NAME")

# Create the choropleth map
fig = px.choropleth(dc,
                    locations="NAME",
                    color="population",
                    geojson=dc.geometry.iloc[0],
                    color_continuous_scale="Viridis",
                    range_color=(0, 100000),
                    title="London Borough Population",
                    hover_name="NAME",
                    hover_data=["population"],
                    labels=dict(population="Population"))

# Show the map
fig.show()
# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=0)

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash App"),
    dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,4], 'type': 'bar'}],
                      'layout': {'title': 'Borough PM 2.5 Pollution Bar Chart from Excel Data'}})
])

if __name__ == "__main__":
    app.run_server()
