from Project3_Sauce_Demo.pages.login_page import LoginPage
from Project3_Sauce_Demo.pages.inventory_page import InventoryPage
from Project3_Sauce_Demo.pages.cart_page import CartPage
from Project3_Sauce_Demo.pages.checkout_page import CheckoutPage
from Project3_Sauce_Demo.pages.checkoutoverview_page import CheckoutOverviewPage
from Project3_Sauce_Demo.pages.checkoutcomplete_page import CheckoutCompletePage


class KeywordEngine:
    """Keyword-driven engine using dispatch pattern"""
    # Page Mapping
    page_object_map = {
        "LoginPage": LoginPage,
        "InventoryPage": InventoryPage,
        "CartPage": CartPage,
        "CheckoutPage": CheckoutPage,
        "CheckoutOverviewPage": CheckoutOverviewPage,
        "CheckoutCompletePage": CheckoutCompletePage,
    }

    def __init__(self, driver):
        self.driver = driver
        self.current_page = None
        self.selected_products = []

        # Keyword - Method Mapping
        self.keyword_map = {
            "navigate": self._navigate,
            "set_page": self._set_page,
            "enter_text": self._enter_text,
            "click": self._click,
            "verify_login": self._verify_login,
            "verify_text": self._verify_text,
            "verify_element": self._verify_element,
            "verify_accessible": self._verify_accessible,
            "random_select_products": self._random_select_products,
            "extract_selected_products": self._extract_selected_products,
            "verify_selected_products": self._verify_selected_products,
            "verify_qty": self._verify_qty,
            "capture_screenshot": self._capture_screenshot,
            "verify_element_invisibility": self._verify_element_invisibility,
            "select_sort": self._select_sort,
            "verify_name_sort": self._verify_name_sort,
            "verify_price_sort": self._verify_price_sort,
        }


    # Executor

    def execute_step(self, keyword, page, element, data, expected):
        kw = (keyword or "").strip().lower()
        handler = self.keyword_map.get(kw)

        if not handler:
            raise Exception(f"Unknown keyword: '{keyword}'")

        handler(page , element, data, expected)

    # Helper Methods - To check current page and locator
    def _ensure_current_page(self):
        if self.current_page is None:
            raise Exception("current_page is None. Call set_page first.")

    def _get_locator(self, element):
        locator = self.current_page.locators.get(element)
        if locator is None:
            raise Exception(f"Locator '{element}' not found in page {type(self.current_page).__name__}")
        return locator


    # Keyword Handlers
    # navigating to url
    def _navigate(self, page, element, data, expected):
        url = str(data).strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.driver.get(url)

    # setting page before entering or verifying the element in the page
    def _set_page(self, page, element, data, expected):
        page_name = str(page).strip()
        page_class = self.page_object_map.get(page_name)
        if not page_class:
            raise Exception(f"Unknown PageName '{page_name}'")
        self.current_page = page_class(self.driver)

    # entering text in the element
    def _enter_text(self, page, element, data, expected):
        self._ensure_current_page()
        locator = self._get_locator(element)
        self.current_page.enter_text(locator, str(data or ""))

    # clicking the element
    def _click(self, page, element, data, expected):
        self._ensure_current_page()
        locator = self._get_locator(element)
        self.current_page.click(locator)

    # verifying login functionality result
    def _verify_login(self, page, element, data, expected):
        self._ensure_current_page()
        actual = self.current_page.verify_login_status()
        expected = str(data or "")

        if expected == "Success":
            assert actual == "Success", f"Expected Success but got '{actual}"
            self.current_page = InventoryPage(self.driver)
            assert self.current_page.verify_image() , f"Image mismatch on Inventory page"

        elif expected == "Image_Fail":
            if actual == "Success":
                inventory = InventoryPage(self.driver)
                assert inventory.verify_image() is False, f"Expected image failure but image is correct"

        else:
            assert expected == actual, f"Expected error message:{expected} but got error message {actual}"

    # verifying text on the page
    def _verify_text(self, page, element, data, expected):
        self._ensure_current_page()
        locator = self._get_locator(element)
        actual_text = self.current_page.get_text(locator)
        expected_text = str(data or "")

        assert expected_text in actual_text , f"Text mismatch. Expected to contain '{expected_text}', got '{actual_text}'"

    # verifying the element on the page
    def _verify_element(self, page, element, data, expected):
        self._ensure_current_page()
        locator = self._get_locator(element)
        assert self.current_page.is_visible(locator), f"{element} is not visible on the page"

    # verifying accessibility of the element
    def _verify_accessible(self, page, element, data, expected):
        self._ensure_current_page()
        locator = self._get_locator(element)
        assert (self.current_page.is_visible(locator) and self.current_page.is_clickable(locator)) , f"{element} is not accessible"

    # random selection of products
    def _random_select_products(self, page, element, data, expected):
        self._ensure_current_page()
        self.current_page.random_select_products(int(data))

    # extracting the information of selected products
    def _extract_selected_products(self, page, element, data, expected):
        self._ensure_current_page()
        self.selected_products = self.current_page.extract_selected_products()

    # verifying cart products with selected products information
    def _verify_selected_products(self, page, element, data, expected):
        self._ensure_current_page()
        cart_items = self.current_page.get_cart_products()
        assert self.selected_products == cart_items, f"Product mismatch between inventory and cart"

    # verifying quantity in the cart page
    def _verify_qty(self, page, element, data, expected):
        self._ensure_current_page()
        qty_list = self.current_page.get_all_quantities()
        assert sum(qty_list) == int(data) ,f"Cart quantities do not match selected products"

    # capturing screenshot during execution
    def _capture_screenshot(self, page, element, data, expected):
        self._ensure_current_page()
        self.current_page.take_screenshot(data)

    # verifying element invisibility
    def _verify_element_invisibility(self, page, element, data, expected):
        self._ensure_current_page()
        locator = self._get_locator(element)
        assert self.current_page.is_invisible(locator), f"{element} is visible but expected invisible"

    # selecting sort option
    def _select_sort(self, page, element, data, expected):
        self._ensure_current_page()
        self.current_page.select_sort_option(data)

    # performing and verifying sort on product name
    def _verify_name_sort(self, page, element, data, expected):
        self._ensure_current_page()
        order = str(data).upper()
        actual = self.current_page.get_product_names()
        expected_list = sorted(actual, reverse=(order != "ASC"))
        assert actual == expected_list, f"Name sort failed. Expected {expected_list}, got {actual}"

    # performing and verifying sort on product price
    def _verify_price_sort(self, page, element, data, expected):
        self._ensure_current_page()
        order = str(data).upper()
        actual = self.current_page.get_product_prices()
        expected_list = sorted(actual, reverse=(order != "ASC"))
        assert actual == expected_list, f"Price sort failed. Expected {expected_list}, got {actual}"