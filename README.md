# Front End Automation Challenge
This repository contains a Proof of Concept (POC) of a test automation framework for Swag Labs using Selenium.
The tests can either be run with Chrome or with Internet Explorer

## Prerequisites
1. Python3 and pip must be installed on your system and added to the PATH
2. For chrome tests:
   - Works with chrome version 86
3. For Internet Explorer tests:
   - Works with version 11.1457
   - Protected mode must be disabled on every security setting
   - Zoom setting must be at 100%

## Steps
1. Clone the repository with the following command:
`git clone https://github.com/andreagnavarro/FrontEndAutomationChallenge.git`
2.  Run the following command: `pip install -r requirements.txt` that installs the following python 3 packages:
   - Selenium
   - DDT
   - HtmlTestRunner
3. To run with chrome use the following command:
`python3 Tests/Tests.py --browser chrome`
4. To run with Internet Explorer use the following command:
`python3 Tests/Tests.py --browser internet_explorer`

## Results
1. There will be an html file generated with the results of the tests inside the Reports folder

## Tests to run
1. Login with a valid user: This test will run 3 times with 3 valid users ("standard_user", "problem_user",
"performance_glitch_user")
   - Expected​: Validate the user navigates to the product’s page.
2. Login with an invalid user
   - Expected​: Validate error message is displayed.
3. Logout from product’s page
   - Expected: ​Validate the user navigates to the login page.
4. Navigate to the shopping cart
   - Expected: ​Validate the user navigates to the shopping cart page.
5. Add a single item to the shopping cart
   - Expected: ​Validate the item has been added to the shopping cart.
6. Add multiple items to the shopping cart
   - Expected: ​Validate all the items that have been added to the shopping cart.
7. Continue with missing mail information
   - Expected: ​Validate error message is displayed on the user’s information page.
8. Fill user’s information
   - Expected: ​Validate the user navigates to the overview page once the data has been filled.
9. Final order items
   - Expected: ​Validate items in the overview page match with the added items.
10. Complete a purchase
    - Expected: validate the user navigates to the confirmation page.

