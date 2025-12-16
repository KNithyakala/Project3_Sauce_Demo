from Project3_Sauce_Demo.pages.base_page import BasePage
from Project3_Sauce_Demo.pages.locators import CartLocators

class CartPage(BasePage):
    # Cart page - locators - getting from locator file
    locators = {
        "continue_shopping" : CartLocators.continue_shopping ,
        "cart_items" : CartLocators.cart_items,
        "inventory_name": CartLocators.inventory_name,
        "inventory_price": CartLocators.inventory_price,
        "cart_quantity": CartLocators.cart_quantity,
        "check_out": CartLocators.check_out
    }

    # Cart page - Actions
    def get_quantity_elements(self):
        return self.find_elements(self.locators["cart_quantity"])

    def get_all_quantities(self):
        qty_elements = self.get_quantity_elements()
        qty_list=[]
        for element in qty_elements:
            qty_text = element.text.strip()
            qty_list.append(int(qty_text))
        return qty_list

    def get_cart_products(self):
        cart_items = self.find_elements(self.locators["cart_items"])
        result = []
        for item in cart_items:
            name = item.find_element(*self.locators["inventory_name"]).text
            price = item.find_element(*self.locators["inventory_price"]).text
            result.append({"name": name, "price": price})
        return result
