import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

# Convert the 'Month' column to a datetime type
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m-%D %H-%M-%S')

# Group the data by month and calculate the average of the 3rd and 4th columns
df_grouped = df.groupby(pd.Grouper(key='Month', freq='M'))[df.columns[1]].mean()

# Create the bar chart
fig = px.bar(x=df_grouped.index, y=df_grouped)

# Create the Dash app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
