**E-commerce Web Application – Sauce Demo**

**Title**

Automated Testing of the Web Application https://www.saucedemo.com/

**Test Objective**

The objective of this project is to automate the testing of the demo e-commerce web application, ensuring core functionalities like login, product selection, cart operations, and checkout processes work as expected.
The automation framework will simulate user interactions such as logging in with different user roles, navigating the product catalog, adding items to the cart, and completing the purchase flow. Validation of web behavior, dynamic UI content, and overall system response will be carried out through structured test scenarios.

**Test Scenario**

Test Case 1 -  Login with various predefined users. 

Test Case 2 - Login with invalid credentials.

Test Case 3 - Validate logout functionality.

Test Case 4 - Check cart icon visibility.

Test Case 5- Random selection of products and data extraction.

Test Case 6- Add selected products to cart and validate.

Test Case 7- Validate product details inside the cart. 

Test Case 8- Complete checkout and validate order.

Test Case 9- Validate sorting functionality on the products page.

Test Case 10 -Validate "Reset App State" functionality.

**Project Overview**

This project is a test automation suite for an E-Commerce Web Application, developed using Hybrid Frame work( Keyword-driven, Data-driven approach and POM) with Selenium. 

The main objective is to automate functional testing for various critical flows in an E-Commerce Web Application, 
such as login, sorting functionality, adding products to checkout, cart validation and Logout. 

By using Hybrid Framework with Selenium, the test suite validates that application operates as intended and provides seamless experience for users.

**Table of Contents**
•	Features
•	Tech Stack
•	Setup and Installation
•	Running Tests
•	Project Structure

**Features**

•	Automation POM Framework: Base Page (reusable actions), Page Object automated with page specific actions and reusable actions. Locators are kept in separate file so that it will easy to maintain and easy to update.

•	Data-driven approach: Test data is maintained in separate files(Excel, python). So it can be maintain easily. Used Excel based data driven approach to validate 
login functionality using multiple sets of credentials.

•	Keyword-driven approach: Test cases are written using keywords (like open_browser, click, enter_text) instead of hard-coded scripts. The actual Selenium code is mapped to these keywords, making tests easy to read, maintain, and reuse.

•	Cross Browser Validation: It supports Chrome, Firefox, Edge and Safari

•	Config driven Approach: Used 'config.ini' for browser settings and Credentials.

•	Logging and Reporting Support: We can get test result in HTML format and test logs file is also generated. 

To get allure report, use below commands

pytest --alluredir=test_reports/allure-results

allure serve allure-results

allure generate allure-results -o allure-report --clean

**Tech Stack**

•	Programming Language: Python

•	Test Framework: pytest 

•	Automation Tool: Selenium Web Driver

•	Reporting: pytest-html, pytest—alluredir, test_log, 

•	Browser Compatibility: Chrome, Firefox, Edge and Safari

•	CI/CD Integration: GitHub Actions

**Setup and Installation**

To set up and run this project locally, follow these steps:

**Clone the Repository: **

**1.	Clone the Repository**

  	 git clone https://github.com/username/Project3_Sauce_Demo.git cd Project3_Sauce_Demo
  
**2. Create a Virtual Environment (optional but recommended) **

   python3 -m venv env source env/bin/activate # Linux/Mac env\Scripts\activate # Windows
   
**3. Install Dependencies: **
   
   pip install -r requirements.txt
   
**4. Set Up Environment Variables: **
    
    Create a .env file in the root directory to store sensitive information such as login credentials and URLs. Example:
    BASE_URL=https://example.com
    USER_EMAIL=test@example.com
    USER_PASSWORD=yourpassword


**Running Tests**

To execute tests, use the following commands:

1.	Run All Tests:

pytest

2.	Generate HTML Report:

pytest --html=html-report.html

3.	Run Tests by Marker (e.g., only "login" tests):

pytest -m login

4.	Headless Browser Execution:

You can set up tests to run in headless mode by configuring the config.ini file or directly in your test script.

**Project Structure**  




