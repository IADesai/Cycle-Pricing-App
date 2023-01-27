#dont copy this code
import dash
from dash import html
from dash import dcc
import pandas as pd

# Read the excel file
df = pd.read_excel("data_set_prepared.xlsx")

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash App"),
    dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df.column_name, 'y': df.value, 'type': 'bar'}],
                      'layout': {'title': 'Bar Chart from Excel Data'}})
])

if __name__ == "__main__":
    app.run_server()

