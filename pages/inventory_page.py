from Project3_Sauce_Demo.testdata.image_data import sauce_labs_backpack_src
from Project3_Sauce_Demo.pages.base_page import BasePage
from Project3_Sauce_Demo.pages.locators import InventoryLocators
import random

class InventoryPage(BasePage):
    # Inventory page - locators - getting from locator file
    locators = {
    "sauce_labs_backpack_img" : InventoryLocators.sauce_labs_backpack_img,
    "menu_button"             : InventoryLocators.menu_button,
    "reset_app_state"         : InventoryLocators.reset_app_state,
    "logout"                  : InventoryLocators.logout,
    "cart_icon"               : InventoryLocators.cart_icon,
    "inventory_item"          : InventoryLocators.inventory_item,
    "inventory_name"          : InventoryLocators.inventory_name,
    "inventory_price"         : InventoryLocators.inventory_price,
    "inventory_add_button"    : InventoryLocators.inventory_add_button,
    "shopping_cart_badge"     : InventoryLocators.shopping_cart_badge,
    "sort_dropdown"           : InventoryLocators.sort_dropdown
    }

    # Inventory Page - Actions

    def verify_image(self):
        image_element = self.find_element(self.locators["sauce_labs_backpack_img"])
        image_source = image_element.get_attribute("src")
        return image_source == sauce_labs_backpack_src

    def random_select_products(self, count):
        all_products = self.find_elements(self.locators["inventory_item"])
        selected = random.sample(all_products, count)
        self.selected = []
        for item in selected:
            name = item.find_element(*self.locators["inventory_name"]).text
            price = item.find_element(*self.locators["inventory_price"]).text
            item.find_element(*self.locators["inventory_add_button"]).click()

            self.selected.append({"name": name, "price": price})


    def extract_selected_products(self):
        return self.selected

    def select_sort_option(self,option_text):
        self.select_dropdown_by_text(self.locators["sort_dropdown"], option_text)

    def get_product_names(self):
        product_names = []
        for product in self.find_elements(self.locators["inventory_item"]):
            text = product.text.strip()
            product_names.append(text)
        return product_names

    def get_product_prices(self):
        prices = []
        for product in self.find_elements(self.locators["inventory_price"]):
            text = product.text.strip()
            try:
                prices.append(float(text.replace("$", "")))
            except ValueError:
                raise ValueError(f"Invalid price format: '{text}'")
        return prices