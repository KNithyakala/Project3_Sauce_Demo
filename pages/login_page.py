from Project3_Sauce_Demo.pages.base_page import BasePage
from Project3_Sauce_Demo.pages.locators import LoginLocators

class LoginPage(BasePage):

    # Login page - locators - getting from locator file
    locators = {
    "username" : LoginLocators.username,
    "password" : LoginLocators.password,
    "login_button" : LoginLocators.login_button,
    "error_message" : LoginLocators.error_message
    }

    # Login page - Actions

    def verify_login_status(self):
        try:
            if self.find_element(self.locators["error_message"]).is_displayed():
                error_msg = self.get_text(self.locators["error_message"])
                return error_msg
        except:
            pass

        if "inventory" in self.driver.current_url:
            return "Success"
        else:
            return "unknown"