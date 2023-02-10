import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash App"),
    dcc.Graph(id='line-chart',
              figure=px.line(df, x="Month", y="Number of Bicycle Hires.1",))
])


if __name__ == "__main__":
    app.run_server()

