# Sauce Demo Pages - Locators
from selenium.webdriver.common.by import By

# Login Page - Locators
class LoginLocators:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

# Inventory Page - Locators
class InventoryLocators:
    sauce_labs_backpack_img = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    menu_button = (By.ID, "react-burger-menu-btn")
    reset_app_state = (By.ID, "reset_sidebar_link")
    logout = (By.ID, "logout_sidebar_link")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    inventory_item = (By.CLASS_NAME, "inventory_item")
    inventory_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_price = (By.CLASS_NAME, "inventory_item_price")
    inventory_add_button = (By.XPATH, ".//button[contains(text(),'Add to cart')]")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")

# Cart Page - Locators
class CartLocators:
    continue_shopping= (By.ID, "continue-shopping")
    cart_items = (By.CLASS_NAME, "cart_item")
    inventory_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_price = (By.CLASS_NAME, "inventory_item_price")
    cart_quantity = (By.XPATH, "//div[@class='cart_quantity']")
    check_out = (By.ID, "checkout")

# Checkout - Locators
class CheckoutLocators:
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_postalcode = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    title = (By.CSS_SELECTOR, ".title")
    confirmation_message = (By.CSS_SELECTOR, ".complete-header")
    finish = (By.ID, "finish")
