
This is an automated test plan which can be used for saucedemo.com.

The test is configured using Python as the coding language, and pytest as the testrunner, 
it is scalable, easy to maintain etc.

Using the playwright library for it's easy to use API's that allow interaction with a webpage, I figured
this would be a good choice for UI based web end-to-end testing of the saucedemo site, using Behave
as a plugin to expand Pytest, I have written a series of tests using BDD framework. This is written with 
gherkin syntax and I've stored this in the feature file

To run these tests:

Install an IDE 
clone the repo from Github
install Python 3 from https://www.python.org/downloads/
in a powershell terminal, navigate to the project folder, run 'python -m venv venv'
(for Mac/Linux)-  (Mac) python3 -m venv venv  (Linux) source venv/bin/activate

this will setup a virtual environment, activate it by running '.\venv\Scripts\Activate'
install the required packages by running 'pip install -r requirements.txt'
install playwright browsers by running 'playwright install'
You can then run the tests by simply running 'behave' in the project folder
You can view a report of the test results by opening 'report.json' inside the project folder
feel free to use your preferred json formatter for viewing 


Thank you for taking the time to look at this test project!





















