import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

# Read the second sheet of the excel file
df = pd.read_excel("data_set_prepared.xlsx", sheet_name=1)

# Convert the 'Month' column to a datetime type
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m-%d %H:%M:%S')

# Extract the month from the datetime object
df['month'] = df['Month'].dt.month

# Group the data by month and average the usage
grouped = df.groupby('month').mean()

# Create the bar chart
fig = px.bar(x=grouped.index, y=grouped.iloc[:, 1])

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Average Usage"
)

# Create the Dash app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)