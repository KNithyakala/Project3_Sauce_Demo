from Project3_Sauce_Demo.utils.excel_reader import ExcelReader
from Project3_Sauce_Demo.utils.keyword_reader import KeywordReader
from Project3_Sauce_Demo.keywords.keywords import KeywordEngine
import os
import pytest
import logging

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_data_path = os.path.join(root_path, "testdata", "login_users.xlsx")
keyword_sheet_path = os.path.join(root_path,"testdata","keywords_saucedemo.xlsx")

@pytest.mark.usefixtures("setup")
class Test_saucedemo:
    # Test Case Runner
    def run_steps(self, test_case_id, users = None):
        excel = KeywordReader(keyword_sheet_path)
        steps = excel.get_steps(test_case_id)
        kw = KeywordEngine(self.driver)
        # If data-driven users are provided
        if users:
            for username, password, expected in users:
                for step in steps:

                    keyword = step["keyword"]
                    page = step["page"]
                    element = step["element"]
                    data = step["data"]
                    expected_result = step["expected"]

                    # Replace placeholders
                    if data == "{{username}}":
                        data = username
                    if data == "{{password}}":
                        data = password
                    if data == "{{expected}}":
                        data = expected
                    kw.execute_step(step["keyword"], step["page"], step["element"], data, step["expected"])
        else:
            # Normal keyword -only execution
            for step in steps:
                kw.execute_step(step["keyword"], step["page"], step["element"], step["data"], step["expected"])

    # Testcase1 - Login with various predefined users
    @pytest.mark.smoke
    @pytest.mark.login
    def test_case01(self):
        logging.info(f"--Running testcase01 -- Login Functionality for predefined users--")
        users = ExcelReader(test_data_path, "predefined_users").get_data()
        self.run_steps("TC01",users)
        logging.info(f"Testing completed for Login functionality of predefined users.")

    # Testcase2 - Login with invalid credentials
    @pytest.mark.login
    def test_case02(self):
        logging.info(f"-- Running testcase02 -- Login Functionality for non standard users ---")
        non_standard_users = ExcelReader(test_data_path,"nonstandard_users").get_data()
        self.run_steps("TC02",non_standard_users)
        logging.info("Testing completed for Login functionality of non standard users.")

    # Testcase3 - Validate logout functionality
    # Testcase4 - Check cart icon visibility
    # Testcase10- Validate "Reset App State" functionality
    @pytest.mark.regression
    def test_case03_04_10(self):
        logging.info(f"-Running testcase03-Logout Functionality, testcase04-Cart Icon Visibility and testcase10-Reset App State Functionality")
        self.run_steps("TC03_04_10")
        logging.info(f"Testing completed for Cart Icon Visibility, Reset App state and Logout.")

    #Testcase5- Random selection of products and data extraction
    #Testcase6- Add selected products to cart and validate
    #Testcase7- Validate product details inside the cart
    #Testcase8- Complete checkout and validate order
    @pytest.mark.regression
    def test_case05_06_07_08(self):
        logging.info(f"--- Running test for test case 5, 6, 7 and 8--------")
        self.run_steps("TC05_06_07_08")
        logging.info("Testing completed for Random Selection of products, adding products, cart page validation and checkout.")

    #Testcase9- Validate sorting functionality on the products page
    @pytest.mark.regression
    def test_case09(self):
        logging.info(f"--- Running test for test case 9--------")
        self.run_steps("TC09")
        logging.info("Testing completed for Sorting functionality on the Product Page.")
