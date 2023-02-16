# import dash
# from dash import html
# from dash import dcc
# import pandas as pd
# import plotly.express as px


# def create_daily_chart(day_selected):
#     # Read the sheet from the excel file
#     df = pd.read_excel("data_set_prepared.xlsx", sheet_name=sheet_names[day_selected])
#     # Convert the 'TimeString' column to a datetime type
#     df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')

#     # Extract the hour from the datetime object
#     df['hour'] = df['TimeString'].dt.hour

#     # Group the data by hour and sum the usage
#     grouped_sum = df.groupby('hour').sum()
#     grouped_mean = df.groupby('hour').mean()
#     grouped = grouped_sum/grouped_mean

#     # Create the bar chart
#     fig = px.bar(x=grouped.index, y=grouped.iloc[:,0])

#     fig.update_layout(
#         xaxis_title="Hour",
#         yaxis_title="Average Usage",
#         title=f"Average Usage for {sheet_names}"
#     )
#     return fig

# # Get the sheet names from the excel file
# sheet_names = pd.read_excel("data_set_prepared.xlsx", sheet_name=None).keys()
# print(sheet_names)

# # Create the Dash app
# app = dash.Dash()
# app.layout = html.Div(style={'display': 'flex'}, children=[
#     html.Div(style={'flex': 1}, children=[
#         dcc.Graph(id='daily-usage-graph', figure=create_daily_chart(day_selected=2))
#     ]),
#     html.Div(style={'flex': 0.5, 'padding': 20}, children=[
#         dcc.Dropdown(id='day-dropdown', options=[{'label': sheet_name, 'value': i} for i, sheet_name in enumerate(sheet_names)], value=2)
#     ])
# ])

# @app.callback(
#     dash.dependencies.Output('daily-usage-graph', 'figure'),
#     [dash.dependencies.Input('day-dropdown', 'value')]
# )
# def update_graph(day_selected):
#     return create_daily_chart(day_selected)

# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px


def create_daily_chart(day_selected):
    # Read the sheet from the excel file
    df = pd.read_excel("data_set_prepared.xlsx", sheet_name=sheet_names[day_selected])
    # Convert the 'TimeString' column to a datetime type
    df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')

    # Extract the hour from the datetime object
    df['hour'] = df['TimeString'].dt.hour

    # Group the data by hour and sum the usage
    grouped_sum = df.groupby('hour').sum()
    grouped_mean = df.groupby('hour').mean()
    grouped = grouped_sum/grouped_mean

    # Create the bar chart
    fig = px.bar(x=grouped.index, y=grouped.iloc[:,0])

    fig.update_layout(
        xaxis_title="Hour",
        yaxis_title="Cycle hires",
        title=f"Cycle Usage for {sheet_names[day_selected]}"
    )
    return fig

# Get the sheet names from the excel file
sheet_names = list(pd.read_excel("data_set_prepared.xlsx", sheet_name=None).keys())
# Remove the first two sheets from the list
sheet_names = sheet_names[2:]
# Remove the .xlsx to allow the sheet names to be sorted 
sheet_names = [name.rstrip('.xlsx') for name in sheet_names]
# Order the sheet names by date
sheet_names = sorted(sheet_names, key=lambda x: pd.to_datetime(x, format="%A, %b %d %Y"))
# Add the '.xlsx' backl into the file
sheet_names = [name + '.xlsx' for name in sheet_names]


# Create the Dash app
app = dash.Dash()
app.layout = html.Div(style={'display': 'flex'}, children=[
    html.Div(style={'flex': 1}, children=[
        dcc.Graph(id='daily-usage-graph', figure=create_daily_chart(day_selected=2))
    ]),
    html.Div(style={'flex': 0.5, 'padding': 20}, children=[
        dcc.Dropdown(id='day-dropdown', options=[{'label': sheet_name(name.rstrip('.xlsx') for name in sheet_name), 'value': i} for i, sheet_name in enumerate(sheet_names)], value=0)
    ])
])

@app.callback(
    dash.dependencies.Output('daily-usage-graph', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')]
)
def update_graph(day_selected):
    return create_daily_chart(day_selected)

if __name__ == '__main__':
    app.run_server(debug=True)
