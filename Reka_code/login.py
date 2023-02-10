import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Keep track of the current page
current_page = "signup"

# Dummy data to represent a database of user accounts
user_db = {}

# Define the layout for the sign up page
signup_layout = html.Div([
    html.H1("Sign Up Page"),
    html.H3("Please enter your information below:"),
    html.Div([
        html.P("Username:"),
        dcc.Input(id="signup-username", type="text", placeholder="Enter your username")
    ]),
    html.Div([
        html.P("Password:"),
        dcc.Input(id="signup-password", type="password", placeholder="Enter your password")
    ]),
    html.Div([
        html.P("Confirm Password:"),
        dcc.Input(id="signup-confirm-password", type="password", placeholder="Confirm your password")
    ]),
    html.Button("Submit", id="signup-submit-button", n_clicks=0),
    html.Br(),
    html.H3("Already have an account?"),
    html.A("Login", href="#", id="signup-login-link")
], style={"width": "500px", "margin": "auto"})

# Define the layout for the login page
login_layout = html.Div([
    html.H1("Login Page"),
    html.H3("Please enter your information below:"),
    html.Div([
        html.P("Username:"),
        dcc.Input(id="login-username", type="text", placeholder="Enter your username")
    ]),
    html.Div([
        html.P("Password:"),
        dcc.Input(id="login-password", type="password", placeholder="Enter your password")
    ]),
    html.Button("Submit", id="login-submit-button", n_clicks=0),
    html.Br(),
    html.H3("Don't have an account yet?"),
    html.A("Sign Up", href="#", id="login-signup-link")
], style={"width": "500px", "margin": "auto"})

# Define the layout for the homepage
home_layout = html.Div([
    html.H1("Welcome to the Home Page"),
    html.P("You are now logged in!")
], style={"width": "500px", "margin": "auto"})

# Set the initial layout of the app
app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page-content")
])

# Update the page content based on the URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    global current_page
    if pathname == "/signup":
        current_page
