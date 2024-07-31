
This is an automated test plan which can be used for saucedemo.com.

The test is configured using Python as the coding language, and behave as the testrunner, 
it is scalable, easy to maintain etc.

Using the playwright library for it's easy to use API's that allow interaction with a webpage, I figured
this would be a good choice for UI based web end-to-end testing of the saucedemo site, I have written a series of tests using BDD framework. This is written with gherkin syntax and I've stored this in the feature file.

I have added 2 scenarios, the user logs into the site, adds an item to their cart and checks out sucessfully, in the other scenario the user fails
to log in. 

To run the tests:

Install an IDE 
clone the repo from Github
install Python 3 from https://www.python.org/downloads/
in a powershell terminal, navigate to the project folder, run 'python -m venv venv'
(for Mac/Linux)-  (Mac) python3 -m venv venv  (Linux) source venv/bin/activate

this will setup a virtual environment, activate it by running '.\venv\Scripts\Activate'
install the required packages by running 'pip install -r requirements.txt'
install playwright browsers by running 'playwright install'
Install the test runner by running 'pip install behave'

You can then run the tests by simply running 'behave' in the project folder

I've also added tags to the Scenarios, you can run them individually by running behave --tags 'scenario name'(e.g. behave --tags valid login)

You can view a report of the test results by opening 'report.json' inside the project folder
feel free to use your preferred json formatter for viewing 


Thank you for taking the time to look at this test project!





















