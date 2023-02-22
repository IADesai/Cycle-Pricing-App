![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)
# COMP0034 Coursework 1 repository

# Set-up instructions

In order to set up and run the dash app, please first install all the requirements outlined in the requirements.txt file within the main branch of the repository. With these, you can run our dash and testing applications, ensuring to click on the dash server created once the dash app has run.

URL to our GitHub repo here: https://github.com/ucl-comp0035/comp0034-cw1-g-team_7

# Visualisation design

visualisation-design.pdf can be found in COMP0034 CW1 folder of the repository

# Dash app

The Coding Cyclists have tackled TFL's cycle hire pricing, masterminding an algorithm to adjust the price of the cycle hire dependent on hourly and monthly cycle hire data, alongside PM 2.5 pollution levels across the boroughs of London. Our dash app displays this pricing with an interactive pricing choropleth map as the main homepage feature, allowing users to identify the price of santander cycles in different boroughs of london, at different times of day, and different months of the year. This map can be broken down into the varioius graphs, identifying and visualizing the hourly, monthly, and pollution data used to form the main map. These graphs are stored in tabs on a sidebar, accessible to the users to view and analyse. 

# Testing
As the Dash app originally created is a multi-page app and the sidebar feature used wasn't testable, a single-page app was created for the purpose of testing. It was named as `app_for_testing.py` and can be found in the test folder.

The created dash app was tested using the pytest library and Selenium. The following x number of tests were created, each of which are explained in detail using the GIVEN-WHEN-THEN Approach in the `test_app.py` code. The mmffddd format was used when naming the test functions, where m represents module (test), f file (cycle), and d three digits for the number of test case.

 ### Test function 1 
 - The function called `test_cycle001_h1_text_equals(dash_duo, app)` aims to test if element header 1 (H1) equals the text TFL Cycle Hire Pricing.

 ### Test functions 2-5
The following functions test if the elements referenced by their given ID equals the text they expected to equal:
 - `test_cycle002_id_d2_text_equals(dash_duo, app)` tests if element "#id-d2" equals the text 'Month of Year:'
 - `test_cycle003_id_title1_text_equals(dash_duo, app)` tests if element "#id-title1" equals the text 'Daily Data'
 - `test_cycle004_id_title2_text_equals(dash_duo, app)` tests if element "#id-title2" equals the text 'Monthly Data"'
 - `test_cycle005_id_title3_text_equals(dash_duo, app)` tests if element "#id-title3" equals the text 'Pollution Data"'

 ### Test functions 6-11
For each dropdown element (month-dropdown, hour-dropdown, day-dropdown) two tests were created, one to test if the intital month, hour and day apper in the dropdowns and the second to see if the dropdown is updated when the monrh, hour or day is changed.
  - `test_cycle006_monthdropdowncontainsjanuary(dash_duo, app)` tests if the month 'January' appers in the month-dropdown, when the corresponding figure (Pricing Data Choropleth Map, id='london-map') is loaded
  - `test_cycle007_monthdropdownchangesdropdown(dash_duo, app)` tests if the month-dropdown is updated when the month 'February' is selected in the dropdown
  - `test_cycle008_hourdropdowncontains00_06(dash_duo, app)` tests if the time period of '00:00-06:00' appers in the hour-dropdown, when the corresponding figure (Pricing Data Choropleth Map, id='london-map') is loaded
  - `test_cycle009_hourdropdownchangesdropdown(dash_duo, app)` tests if the hour-dropdown is updated when the time period of '06:00-09:00' is selected in the dropdown
  - `test_cycle010_daydropdowncontainsjul1(dash_duo, app)` tests if the day 'Sunday, Jul 1 2018.xlsx' appers in the day-dropdown, when the corresponding figure (Daily data usage figure, id="daily-usage-graph") is loaded
  - `test_cycle011_daydropdownchangesdropdown(dash_duo, app):` tests if the day-dropdown is updated when the day 'Monday, Jul 2 2018.xlsx' is selected in the dropdown

 ### Test functions 12-15
For each figure that had a title provided in the dash app, tests have been created to test if the titles equal the expected texts.
- `test_cycle012_daily_usage_graph_title_equals(dash_duo, app)` tests if the title of the Daily data usage figure (id="daily-usage-graph") equals 'Cycle Usage for Sunday, Jul 1 2018.xlsx' 
- `test_cycle013_monthly_avgusage_graph_title_equals(dash_duo, app)` tests if the title of the Monthly average usage figure (id="monthly-avgusage-graph") equals 'Average Cycle Hire Usage per Month' 
- `test_cycle014_monthly_totusage_graph_title_equals(dash_duo, app)` tests if the title of the Monthly total usage figure (id="monthly-totusage-graph") equals 'Cycle Hire Usage per Month across 11 Years' 
- `test_cycle015_pollution_bar_graph_title_equals(dash_duo, app)` tests if the title of the Pollution bar chart (id="pollution-bar-graph") equals 'Pollution Levels in the Boroughs of London' 

These functions allowed us to test all the created figures and dropdown features in the single-page app.

## Fixtures
As all testing functions require the same input for the dash apo, to simplify the code, fixtures can be added to the `conftest.py` code to create a common function which returns the test app.The fixture added to `conftest.py` can be found below.

```py
@pytest.fixture(scope="function")
def app(dash_duo):
    test_app = import_app(app_file="app_for_testing")
    yield dash_duo.start_server(test_app)
```
## Test Results

Running the tests in Visual Studio code, using `Pytest` and selenium, the produced output was the following:

![WhatsApp Image 2023-02-22 at 13 56 33](https://user-images.githubusercontent.com/88077512/220644984-935d9d3c-24c6-47b6-b118-14c40c4de595.jpeg)
![WhatsApp Image 2023-02-22 at 13 57 44](https://user-images.githubusercontent.com/88077512/220645035-6d13f4c2-01f0-4920-9756-2a0d0ad12357.jpeg)
![WhatsApp Image 2023-02-22 at 13 58 13](https://user-images.githubusercontent.com/88077512/220645075-d7cd3b68-e2e2-4022-af78-aaba549fe7a0.jpeg)
![WhatsApp Image 2023-02-22 at 13 58 37](https://user-images.githubusercontent.com/88077512/220645125-b86f58b8-a7f6-49d9-a460-8a534b03c718.jpeg)
![WhatsApp Image 2023-02-22 at 14 00 01](https://user-images.githubusercontent.com/88077512/220645188-a055046b-927f-44fc-abde-dfb820f3a468.jpeg)
![WhatsApp Image 2023-02-22 at 14 00 37](https://user-images.githubusercontent.com/88077512/220645204-00d2d593-ae97-4ce0-bc62-2e90d03366ef.jpeg)
![WhatsApp Image 2023-02-22 at 13 56 13](https://user-images.githubusercontent.com/88077512/220644220-c9314e4a-9c97-479a-8861-20687be24d28.jpeg)

The above screenshots show that even with the warnings, all the 15 tests passed.

# Coverage Reports
`pytest` was also used with coverage to generate coverage reports. These show what percentage of the code that requires testing is tested. Therefore, we should aim for code coverage of 80% or above across all testing files (`app_for_testing.py`, `conftest.py`, and `test_app.py`) to ensure the majority of the relavent code is tested. The generated coverage report can be seen below:

![WhatsApp Image 2023-02-22 at 15 07 22](https://user-images.githubusercontent.com/88077512/220663463-01b80d17-f3cb-486a-9983-15ae45630654.jpeg)


After all 15 tests were successfully run, the coverage report indicates FILL THIS IN% coverage across both files since they are both relatively large in size.

# Continuous Integration
A continuous integration workflow was employed to run every time a commit is made to the master branch. The YAML code used to do this can be seen below:
```YML
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.11
      uses: actions/setup-python@v3
      with:
        python-version: "3.11"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest and coverage
      run: |
        coverage run -m pytest -v && coverage report
```
From the YAML script above we can see the build is divided into 5 main sections:
1. Python 3.11 is set up
2. Dependencies are installed including pip to install the other modules, `flake8` for linting, `pytest` for testing, `pytest-cov` for coverage, as well as any other modules listed in `requirements.txt`
3. The `test` folder which contains the `app_for_testing.py` code must be identified as a package
4. The code is linted using `flake8` to find any presentation errors
5. `pytest` is run on the code as well as coverage to generate a coverage report

With this workflow, all of these tests can now be carried out on the code each time a commit is made to the master branch. These can be seen below in the GitHub Actions tab:

![WhatsApp Image 2023-02-22 at 14 47 24](https://user-images.githubusercontent.com/88077512/220657850-12b0683a-c329-4885-991b-ecfa0ecfaaab.jpeg)

After investigating each build individually after a new commit has been made, we can see how pytest is run and a coverage report is generated for the tested files:

![WhatsApp Image 2023-02-22 at 15 01 35](https://user-images.githubusercontent.com/88077512/220662124-0d2c6d44-942d-425f-b2b1-7ac784886aa2.jpeg)
![WhatsApp Image 2023-02-22 at 15 02 06](https://user-images.githubusercontent.com/88077512/220662167-30792f4e-2085-424e-b64f-714f8c5658c5.jpeg)

The GitHub actions workflow also highlights failed tests. The example below is the same failed test as shown previously:

![image](PICTURE OF FAILED TEST FROM WORKFLOW TAB)
