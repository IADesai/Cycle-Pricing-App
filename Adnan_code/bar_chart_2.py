import dash
from dash import html
from dash import dcc
import pandas as pd

# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

# Convert the month column to datetime and set it as the index
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

# Group the data by month and get the mean for each month
df_grouped = df.groupby(pd.Grouper(freq='M')).mean()

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash App"),
    dcc.Graph(id='bar-chart',
              figure={'data': [{'x': df_grouped.index, 'y': df_grouped['Number of Bicycle Hires.1'], 'type': 'bar'}],
                      'layout': {'title': 'Monthly Average Usage'}})
])

if __name__ == "__main__":
    app.run_server()
