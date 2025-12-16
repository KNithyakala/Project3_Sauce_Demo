from Project3_Sauce_Demo.pages.locators import CheckoutLocators
from Project3_Sauce_Demo.pages.base_page import BasePage

class CheckoutPage(BasePage):

    # Checkout page - locators - getting from locator file
    locators = {
    "first_name" : CheckoutLocators.first_name ,
    "last_name" : CheckoutLocators.last_name,
    "zip_postalcode" : CheckoutLocators.zip_postalcode,
    "continue" : CheckoutLocators.continue_button
    }
