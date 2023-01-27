
# Elecititation techniques

### Interview - Adnan

Interviews allow for the elicitation of information via a conversation with a person or group of people. The interviewee, usually a stakeholder would be asked a series of questions and their responses would be documented. These responses would help formulate the requirements needed for the application. There are two types of interviews that can be used: structured or non-structured. The former having a pre-defined set of questions while the later favouring an open discussion. A mix of these two types can also be implemented depending on the situation. This elicitation technique is useful as it allows us to find out what a stakeholder would exactly need helping in the formation of the requirements. 

The process of using interviews consists of three elements:

Preparation of the interview: - in this element the interview focus would be defined, and the interview structure would be chosen. This consists of forming the questions, whether open or closed, organizing the order of questions, selecting the location and time of the interview.

Conducting the interview: - in this element the interview would be undertaken, and the goals and questions previously decided should be met and discussed. The results would either be recorded or scribed. 

Follow-up interview: - in this element all information would be gathered and processed. The requirements would then be formed. The interviewee would also be sent a review and a thank you. 

Advantages: - 
-	 Allows interviewer to establish a relationship with the interviewee (stakeholder) 
-	The interview is conducted in private allowing the interviewee to answer questions more openly
-	The interviewer can observe body language and tone to understand more from the answers than just the words. Helping to give more insight than other techniques which do not use face to face contact.

Disadvantages: - 
-	All three elements of the interview process can be time consuming
-	The interviewer would need to be trained which can be expensive and time consuming
-	Multiple interviews would need to be conducted for the different stakeholders which is again expensive and time consuming
-	The answers given in an open discussion type interview are more subject to interpretation


### Observation - Ibrahim
Observation employs the use of a business analyst. The analyst assesses how a user does their job by shadowing their work environment and daily activities. This technique helps to provide context to requirements. Observation can involve watching over someone doingh typical activities, documenting, and asking questions for explanation on completion of tasks. ([1](https://businessanalystmentor.com/elicitation-technique/))

Advantages:
- Effective form of observation, allowing to assimilate more information quickly and confirm understanding as you go
- As you ask follow-up questions and shadow varying activites, you might understand the full process without doing any work
- Mainly important in providing context to requirements

Disadvantages:
- The work proceedings may not encompass the whole of the project requirements
- It restricts what you learn to what is already implemented, lacking creativity
- It requires processes already in place and does not support start ups

### Brainstorming - Greg
This is where the group comes together to faciliate creative thinking in order to come up with new ideas based upon the problem description.There is no limit to the number of requirements and usually, teams try to come up with as many as possible which can then be later sorted in the prioritization stage. Also focuses on what the group know they can do in order to solve the problem. ([2](https://babokpage.wordpress.com/techniques/brainstorming/))

Can be split into 3 main sections: Perparation, Session, Wrap-up.
1. **Preparation**: The area of focus needs to be defined here so that the ideas are relevant to the problem. The criteria for judging each idea is also established so that each member knows what constitues a useful idea.
2. **Session**: This is where the group shares the ideas togther in the brainstorming session. The ideas should be recorded visually for all memebers as certain ideas can faciliate new ideas from other members. There should be no limit on the number of ideas to try and get as many uselful ones as possible.
3. **Wrap-up**: The ideas are discussed individually. Duplicate ideas are removed and similar ideas can be combined with otehrs. The ideas can then be orderd in terms of relevane and priority.

Advantages:
- Many ideas can be elicited in s short period of time
- Creative thinking allows for novel approcahes to situations
- Since no external sources are required, the process can be quick, easy and cost effective.

Disadvantages:
- Depends heavily on the teams creativity.
- Since only members of the team participate, they may miss certain ideas which would be important to a user
- Can be limited by the personalities and opinions of the group members

### Survey/Questionnaire - Reka

A set of questions is given to stakeholders, based on existing systems or proposed requirements. Then collect and tabulate/ analyze the responses to identify the interests of the stakeholders. ([3](https://www.softwaretestinghelp.com/requirements-elicitation-techniques/)) ([4](https://www.businessanalystlearnings.com/ba-techniques/2015/3/16/tips-for-developing-questionnaires-surveys))

Questions can be of the following types:
- Close Ended: containing a predefined set of answers from which the respondent has to choose. Variations for the questions:
  - Multiple Choice
  - Binary
  - Ranking (from not important to very important)
  - Checklist response
  - Production
  - Number scaled ([5](https://www.businessanalystlearnings.com/ba-techniques/2015/3/16/tips-for-developing-questionnaires-surveys))
- Open-Ended: freedom is given to the respondent to provide answers in their own words, which might be numeric or text. This is useful but interpreting the responses is time-consuming
- Semi Closed-Ended Questions: provide both the structure of the closed-ended questions and the flexibility of the open-ended questions, by adding free text boxes, for example when giving the "Other" option for multiple choice questions and a free text box may be displayed to provide additional details ([3](https://www.thebazone.com/bablog/2017/7/11/survey-says-elicitation-tool-1))

Advantages:
- More accurate than interview
- Easy to get data from a large audience
- Less time to respond for the responders' ([3](https://www.softwaretestinghelp.com/requirements-elicitation-techniques/))
- They can be versatile and relatively inexpensive ([6](https://www.thebazone.com/bablog/2017/7/11/survey-says-elicitation-tool-1))

Disadvantages:
- Questions might not be clear to all participants
- Open-ended questions are time-consuming to interpret (hence more analysis required)
- Might not all stakeholders participate
- Follow-up questionnaires might be required (based on the answers of the first) ([3](https://www.softwaretestinghelp.com/requirements-elicitation-techniques/))
- Easy to introduce bias by poor survey design, poor survey administration, small response rates ([6](https://www.thebazone.com/bablog/2017/7/11/survey-says-elicitation-tool-1))

# Requirements
 (Functional)  (Non-Functional)
Must Have:
- The dash app will take an input from the user asking for a postcode. And return the cycle hire data in and around that location. (Functional)
- The dash app will take an input from the user asking for a postcode. And return the pollution data in and around that location. (Functional)
- The dash app will take an input from the user for a specific time period (past) and location and provide past cycle higher data. (Functional)
- The dash app will be able to provide pricing information based on location and time (hour, day, season). (Functional)
- The dash app shall support computer devices running windows, linux and macOS. (Non-Functional)
- The dash app shall meet [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21/) ([7](https://www.w3.org/TR/WCAG21/)) ([8](https://www.perforce.com/blog/alm/what-are-non-functional-requirements-examples)). (Non-Functional)
- The dash app shall provide simple and interactive graphs to visually show pricing data at any given time (to promote cycle usage). (Functional)
- The dash app shall protect all customer data shared (Data Protection Act 2018) ([9](https://www.gov.uk/data-protection)) (Non-Functional)
- The dash app shall provide historical cycle hire data in the form of a scatter plot. (Functional)
- The dash app shall provide an explanation of each plot with its relevance in regard to the problem statement. (Functional)

Should Have:
- The dash app shall respond to users action under 3 seonds or less, including the rendering of text and images ([10](https://www.altexsoft.com/blog/non-functional-requirements/)). (Non-Functional)
- The dash app shall allow tfl to view how pricing is determined via the data used (clear and transparent). (Functional)
- The dash app shall display a map of London Boroughs with corresponding pollution levels. (Functional)

Could Have:
- The dash app shall support both mobile phone and tablets. (Non-Functional)
- The dash app shall support Iphone devices running OS verions 3.4, 3.5 and 3.6. (Non-Functional)

Won't have for now:
- The dash app will take an input from the user of two locations and plan a route between them while avoiding areas with high pollution. (Functional)
- The dash app might ask for users location and display it on the map if permission is given from the user. (Functional)
- The dash app might indicate pollution levels (with written explanations) of their current location if permission is given from the user. (Functional)
- The dash app might send notifications, if permission is given from the user, about calculated pricing based on time and pollution data. (Functional)
- The dash app must be scalable enough to support a large number visits at the same time ([10](https://www.altexsoft.com/blog/non-functional-requirements/)). (Non-Functional)
- The dash app might ask for user location data to recommend cheaper routes based on current calculated pricing (dependant on time and area). (Functional)
- The dash app might ask for permission to access user usage data to find the most popular routes and present further pricing development opportunities. (Functional)


## ML Requirements
- The ML app will employ a simple machine learning algorithm to make a prediction of the pollution level given the location and date inputted by the user
- The ML app will allow users to create an account before they can access the app
- The ML app will check if the password entered by the user is strong enough by ensuring there is at least one capital letter and symbol and the length is over 8 characters
- The ML app will allow users to login to their account in order to access the app
- The ML app will verify that the inpitted parameters are acceptable and will provide a suitable error message if they are not
- The ML app should provide users with easy-to-read data
- The ML app should perform without failure in 95 percent of use cases ([10](https://www.altexsoft.com/blog/non-functional-requirements/))
- The ML app should restore in case of failure in no more than 15 minutes
- The ML app should send a confirmation email if a new account is created
- The ML app should be available in all hours of the day
- The ML app should allow users to log in with their Google accounts ([11](https://www.nuclino.com/articles/functional-requirements))
- The ML app should allow users to provide feedback through the app ([11](https://www.nuclino.com/articles/functional-requirements))
- The ML app should notify the user about any conflict with the requested location and date
- The ML app should allow the user to update the inputted location and date to resolve the conflict
- The ML app should operate in a fair and unbiased manner ([12](https://greg4cr.github.io/pdf/22nfrexplore.pdf))
- The ML app should be easy to modify to improve performance or adapt to changes ([12](https://greg4cr.github.io/pdf/22nfrexplore.pdf))
- The ML app should repeatedly run the same algorithm and obtain the same or similar results

# Detailed use cases

## Use case 01	Login

Brief Description	User logs in

Primary Actors	TFL staff, App developers, TFL data services, LAEI data services

Pre-conditions	User has an account

Main flow	1.	User enters email and password for log in
2.	System checks if email and password matches to a registered account
3.	If there is a match, user is logged in and sent to the Price Map page

Alternative flow	a.	If only the email matches to a registered account, the user is informed that there is an error in the password
b.	If the email does not match, the user is sent to the sign up page.

##Use case 02	Logout

Brief Description	User logs out

Primary Actors	TFL staff, App developers, TFL data services, LAEI data services

Pre-conditions	User is logged in

Main flow	1.	User clicks log out
2.	They are logged out and sent to the home page

Alternative flow	N/A

## Use case 03	Sign up

Brief Description	User creates an account

Primary Actors	TFL staff, TFL data services, LAEI data services

Pre-conditions	N/A

Main flow	1.	User is prompted to fill in the Sign Up form
2.	System checks if email given is a valid  email.
3.	If email is valid, account is created and user is redirected to the Price Map page

Alternative flow	a.	If email is invalid, user is prompted with an invalid email message and requested to enter a different email.

## Use case 04	View graphs

Brief Description	User accesses graph pages

Primary Actors	TFL staff, App Developers

Pre-conditions	User is logged in, user has access to page

Main flow	1.	User clicks on either the pollution graph or usage graph page
2.	System checks if user has the appropriate permissions to access the clicked page
3.	if user has permission, the user is sent to the chosen page

Alternative flow	a.	If user does not have permission, the user is prompted with an invalid permission message

## Use case 05	Change data

Brief Description	data is added or updated in the App

Primary Actors	TFL data services, LAEI data services, App developers

Pre-conditions	User is logged in, user can change data 

Main flow	1.	User changes either pollution or usage data to the app
2.	System checks if user has appropriate permissions and if data is in the correct form
3.	If data is appropriate, system updates website pages with new data

Alternative flow	a.	If user does not have permission, the user is prompted with an invalid permissions message
b.	If Data is not appropriate, user is prompted with an invalid data prompt

## Use case 06	Predict pollution level

Brief Description	System predicts the pollution level for a specific date and location

Primary Actors	TFL staff, App developers

Pre-conditions	User is logged in, user can access the machine learning app

Main flow	1.	User adds date and location parameters and clicks to make a prediction
2.	System checks if user has appropriate permissions and if parameters are valid
3.	If both are true, a prediction is made for pollution level for the corresponding parameters and displayed for the use.

Alternative flow	a.	If user does not have permission, the user is prompted with a invalid permissions message
b.	If user inputs invalid parameters, user is prompted with a re-enter parameters message
