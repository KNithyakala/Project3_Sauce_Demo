from Project3_Sauce_Demo.pages.base_page import BasePage
from Project3_Sauce_Demo.pages.locators import CheckoutLocators

class CheckoutCompletePage(BasePage):

    # Checkout complete page - locators - getting from locator file
    locators = {
    "title" : CheckoutLocators.title,
    "confirmation_message": CheckoutLocators.confirmation_message
    }

