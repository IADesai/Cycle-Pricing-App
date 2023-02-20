# Models
1. Prediction
2. Account

## Account Class
Attributes
- first_name (str)
- last_name (str)
- email (str)
- password (str)

Methods
- signup(first_name :str, last_name :str, email :str, password :str)
- login(email :str, password :str) :bool
- verify_password(password :str) :bool

## Prediction Class
Attributes
- date_input (str)
- location_input (str)
- pollution_prediction (float)

Methods
- make_prediction(date_input :str, location_input :str) :float
- verify_input(date_input :str, location_input :str) :bool
- display_result(pollution_prediction :float)



# Controllers
| Route                   | View Description  | Controller Function |
| -----------             | -----------       | -----------         |
| '/'                     | x                 | index() Returns the home page template |
| '/login'                | x                 | login() Takes entered info, checks against details in database, returns error if details incorrect, redirects to prediction page |
| '/sign-up'              | x                 | signup() Takes entered info, adds to database and redirects user <br> verify_password() returns error if password not strong enough|
| '/prediction-request'   | x                 | verify_input() Takes entered paramters and checks if they are valid, returns error message if not <br> make_prediction() takes verified parameters and passes into ML model to make prediction|
| '/prediction-response'  | x                 | display_result() Displays prediction based on entered parameters|
