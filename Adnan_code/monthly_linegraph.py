import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

# Read the second sheet of the excel file
def create_monthly_linechart():
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

    app = dash.Dash()

    app.layout = html.Div([
        html.H1("Dash App"),
        dcc.Graph(id='line-chart',
                figure=px.line(df, x="Month", y="Number of Bicycle Hires.1",))
    ])
    return fig

if __name__ == "__main__":
    app.run_server()

