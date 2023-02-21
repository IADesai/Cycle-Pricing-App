import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, dcc, html
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

cwd = Path(__file__).resolve().parent.parent

excel_file_path = cwd / "data_set_prepared.xlsx"

df = pd.read_excel(excel_file_path, sheet_name=1)
dp = pd.read_excel(excel_file_path, sheet_name=0)

# Get the sheet names from the excel file
sheet_names = list(pd.read_excel(excel_file_path, sheet_name=None).keys())
# Remove the first two sheets from the list
sheet_names = sheet_names[2:]
# Remove the .xlsx to allow the sheet names to be sorted 
sheet_names = [name.rstrip('.xlsx') for name in sheet_names]
# Order the sheet names by date
sheet_names = sorted(sheet_names, key=lambda x: pd.to_datetime(x, format="%A, %b %d %Y"))
# Add the '.xlsx' back into the file
sheet_names = [name + '.xlsx' for name in sheet_names]

# src for the gif created by using the free version of the Stripo aplication, ref: https://stripo.email
# The gif logo was created by Canva
top_card = dbc.Card(
    [
        dbc.CardImg(src="https://lzqqcs.stripocdn.email/content/guids/CABINET_797e23668dad8bd7e5aee86260d52cc9/images/the_coding_cyclists.gif", top=True),
        
    ],
    style={"width": "18rem"},
)

def create_daily_chart(day_selected):
    # Read the sheet from the excel file
    df = pd.read_excel(excel_file_path, sheet_name=sheet_names[day_selected])
    # Convert the 'TimeString' column to a datetime type
    df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')

    # Extract the hour from the datetime object
    df['hour'] = df['TimeString'].dt.hour

    # Group the data by hour and sum the usage
    grouped_sum = df.groupby('hour').sum(numeric_only=True)
    grouped_mean = df.groupby('hour').mean(numeric_only=True)
    grouped = grouped_sum/grouped_mean

    # Create the bar chart
    fig = px.bar(x=grouped.index, y=grouped.iloc[:,0])

    fig.update_layout(
        xaxis_title="Hour",
        yaxis_title="Cycle hires",
        title=f"Cycle Usage for {sheet_names[day_selected]}"
    )
    return fig

def create_daily_stats(day_selected):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_names[day_selected])
    # Convert the 'TimeString' column to a datetime type
    df['TimeString'] = pd.to_datetime(df['TimeString'], format='%H:%M:%S:%f')
    # Extract the hour from the datetime object
    df['hour'] = df['TimeString'].dt.hour

    # Group the data by hour and sum the usage
    grouped_sum = df.groupby('hour').sum(numeric_only=True)
    grouped_mean = df.groupby('hour').mean(numeric_only=True)
    grouped = grouped_sum/grouped_mean
    # calculate the average usage per hour
    avg_usage_per_hour = round(grouped.iloc[:, 0].mean(), 2)

    # calculate the total usage for the day
    total_usage = round(grouped.iloc[:, 0].sum(), 2)

    # create the stats panel
    stats_panel = dbc.Card(
        [
            dbc.CardHeader("Daily Usage Stats"),
            dbc.CardBody(
                [
                    html.P(f"Average Usage per Hour: {avg_usage_per_hour}"),
                    html.P(f"Total Usage: {total_usage}"),
                ]
            ),
        ],
        color="dark",
        inverse=True,
    )

    return stats_panel


app.layout = dbc.Container(
    # HTML layout elements here
    children=[
        
        html.Div([
        # [  html.H1("The Coding Cyclists", className="display-4"),
           
        #    html.P(
        #     "TFL Cycle Hire Pricing Data Made Easy", className="lead"
        #     ),
        
    dbc.Row(
    [
        dbc.Col(top_card,  width={"size": 6, "offset": 4}),
    ]
),
        ],
),


   
       
    html.Div(style={'display': 'flex'}, children=[
    html.Div(style={'flex': 1}, children=[
    html.Br(),
    html.P(f'Daily Data'),
    html.Hr(),
    html.P("The daily data consists of recorded cycle hire data for every day in an entire month. We used this data to identify and visualize how many cycles were hired per hour of the day for each day in the month and then created a chart with the average of the entire month, to identify the average daily cycle hire pattern. This can be viewed in the tab above, where a selector can be used to view the data for each day. If you choose Monday and compare it to a Sunday for example, we see that the trends are slightly different. This can be seen throughout the month, where weekends have unusual patterns as opposed to working week days. This is only one of many trends visible."),
    html.Br(),
    dcc.Graph(id='daily-usage-graph', figure=create_daily_chart(day_selected=0))
    ]),
    html.Div(style={'flex': 0.5, 'padding': 20}, children=[
    dcc.Dropdown(id='day-dropdown', options=[{'label': sheet_name, 'value': i} for i, sheet_name in enumerate(sheet_names)], value=0),
    html.Br(),
    html.Div(id="stats-card"),
    ])
    ],
    
        className="p-3 bg-light rounded-3",
    
    ),


    html.Br(),
    ]
)



@app.callback(
    dash.dependencies.Output('daily-usage-graph', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')]
)
def update_graph(day_selected):
    return create_daily_chart(day_selected)

@app.callback(
    Output("stats-card", "children"),
    Input("day-dropdown", "value"),
)
def update_daily_stats(day_selected):
    return create_daily_stats(day_selected=day_selected)

if __name__ == '__main__':
    app.run_server(debug=True)