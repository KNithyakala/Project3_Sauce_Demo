from Project3_Sauce_Demo.pages.base_page import BasePage
from Project3_Sauce_Demo.pages.locators import CheckoutLocators

class CheckoutOverviewPage(BasePage):

    # Checkout overview page - locators - getting from locator file
    locators = {
    "finish" : CheckoutLocators.finish
    }
