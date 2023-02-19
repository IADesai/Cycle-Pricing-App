import dash
from dash import html
from dash import dcc
import pandas as pd

# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)
#look for read csv parse_dates

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash App"),
    dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df.iloc[:,1], 'y': df.iloc[:,2], 'type': 'bar'}],
                      'layout': {'title': 'Montly Cycle Usage Bar Chart from Excel Data'}})
])

if __name__ == "__main__":
    app.run_server()



