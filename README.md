[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9809938&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 


# Set-up instructions

Add any instructions here for the markers on how to setup and run your Dash app.

Add the URL to your GitHub repo here e.g. https://github.com/ucl-comp0035name_of_your_repo

# Visualisation design

Overall Dashboard Design:
The overall dashboard will look to provide a choropleth pricing map that takes the calculated final pricing (based on a calculation of hour of the day and month of the year, applying a percentage reduction based on the pollution level of the borough) and displays it on a visually appealing price map, with each borough clearly sectioned off, displaying the pricing in each borough. 
This main dashboard map can be broken down into all other visualisation pieces that are explained below, showing how each piece of pricing data was calculated from the hourly, monthly and pollution data provided. These can be selected on a tab on the dashboard that then opens each graph as specifically selected by the user.
Question the visualisation is designed to address:
Visualisation 1:
Is there a positive/negative correlation between hire use in London and X hours in a day? How could the pricing strategy be adapted throughout a day to account for busier times? Would the target audience think the pricing system throughout the day is reasonable? 
The visualisation for this question should be a line chart as it can show the number of cycle hires per each hour clearly. 
As the target audience is a manager from TFL, the chart should be professional, the axes and title should explain the data represented clearly and the colours used should be professional and not distracting.
The line chart should indicate the busier times, when the number of cycle hires per hour is high (higher than the average?), those are the hours for which pricing should be increased. Similarly, the chart should show the hours when the number of cycling hires is low and for those the pricing should be decreased. The target audience should find the changes in the pricing reasonable if the new price for the busier hours is not much higher than the previous price. The charts could also be published to the public to help the target audience understand the reason behind changing the prices (?).
Visualisation 2:
In which areas of London is the air quality better/worse? How should a new pricing strategy then be formulated based upon this disparity in air quality in order to improve areas in which the air pollution is worse? What are the best ways for the target audience to visualise these trends?

Are there any specific areas in which the pollution level is significantly impacting people’s health? How could the pricing strategy be adapted for these highly polluted areas to encourage more cycle hire use?  

The visualisation for these questions should be a bar chart as it can show the London borough versus the pollution levels of each borough, giving an indication of which boroughs produce the most pollution according to our data. A third y axis can be added to visualize the zones with which the lowered pricing systems will take effect (as percentage decreases in price).

As the target audience is a manager from TFL, the chart should be easy to read, professional and be visually appealing, as to express data clearly.

The bar chart should show the levels of pollution for all the boroughs in London against one another, with a shading of the pricing axis to give an indication of which boroughs would fall into which percentage decreased pricing zones. This means that the manager can see which boroughs should be given cheaper prices due to high amounts of pollution as to increase TFL cycle usage and hopefully decrease pollution levels. This data should allow easy implementation of strategic price changes for bettering the environment through decreasing pollution levels. The chart could also be published to the public to help the further audience understand the aims of the pricing changes and the impact TFL are trying to make.

Visualisation 3:
Is there a positive correlation between cycle hire use and X month of year in London? How could the pricing strategy be adapted throughout a year to account for differences in seasonal demand? 
And the target audience for the chart would be the TFL staff. 
The data used for the visualisation is monthly data, and so the chart will be in the design of a bar chart. However, the chart will also have a line chart element which would display the price of cycle hire vs month. 
Since the visualisation is for TFL staff it must be a professional. Therefore, the axis labels should be clear and in easily readable (in both font and size). The colour should also be professional and appealing by including a variety of colours while avoiding colours which are too bright. As the bar chart is a plot of cycle usage against month there will be no units for either axis. However, the y axis of the line chart element which shows price would have a unit (£). A legend would be needed for the line element of the visualisation. Also, to make the information easier to digest the inclusion of white space between each bar could be helpful.

# Dash app

Add any notes here (optional).

# Testing

Add evidence here (groups).
