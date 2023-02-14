import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px




def create_daily_chart(day_selected):
    # Read the second sheet of the excel file
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=day_selected)
    # Convert the 'TimeString' column to a datetime type
    df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')

    # Extract the hour from the datetime object
    df['hour'] = df['TimeString'].dt.hour

    # Group the data by hour and sum the usage
    grouped_sum = df.groupby('hour').sum()
    grouped_mean = df.groupby('hour').mean()#
    grouped = grouped_sum/grouped_mean

    # Create the bar chart
    fig = px.bar(x=grouped.index, y=grouped.iloc[:,0])

    fig.update_layout(
        xaxis_title="Hour",
        yaxis_title="Average Usage"
    )
    return fig
# Create the Dash app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=create_daily_chart(day_selected=2))
])

if __name__ == '__main__':
    app.run_server(debug=True) 
