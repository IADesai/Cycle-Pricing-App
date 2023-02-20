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


# Create a DatetimeIndex with the month numbers
month_index = pd.date_range(start='2010-07-01', end='2022-9-01', freq='M')
month_names = month_index.strftime('%B')

# Convert the index of the grouped DataFrame to match the format of the month_names variable
grouped.index = [month_names[index - 1] for index in grouped.index]

# Select the data for the months from January to December
grouped_months = grouped.loc[month_names, :]

# Create the bar chart
fig = px.bar(x=month_names, y=grouped_months.iloc[:, 1])

# Update the x axis label to use the month names
fig.update_layout(xaxis_tickangle=-45, xaxis_tickfont=dict(size=14, color='black'))

# Create the bar chart
#fig = px.bar(x=grouped.index, y=grouped.iloc[:,1])

# Create the Dash app
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)

# # Group the data by month and calculate the average of the 3rd and 4th columns
# df_grouped = df.groupby(pd.Grouper(key='Month', freq='M'))[df.columns[1]].mean()

# # Create the bar chart
# fig = px.bar(x=df_grouped.index, y=df_grouped)

