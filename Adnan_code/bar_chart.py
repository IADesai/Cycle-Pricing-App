import dash
from dash import html
from dash import dcc
import pandas as pd

# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash App"),
    dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df['B'], 'y': df['C'], 'type': 'bar'}],
                      'layout': {'title': 'Bar Chart from Excel Data'}})
])

if __name__ == "__main__":
    app.run_server()
