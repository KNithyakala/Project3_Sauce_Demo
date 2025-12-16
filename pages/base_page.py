from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
import os, time

class BasePage:
    # Reusable Actions
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver,timeout)

    def is_visible(self, locator):
        """To check visibility"""
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_invisible(self,locator):
        """To check invisibility"""
        return self.wait.until(ec.invisibility_of_element(locator))

    def is_clickable(self, locator):
        """To check clickability"""
        return self.wait.until(ec.element_to_be_clickable(locator))

    def enter_text(self, locator, text):
        """To enter the text"""
        element = self.is_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """To click the element"""
        self.is_clickable(locator).click()

    def get_text(self, locator):
        """To get the text"""
        return self.is_visible(locator).text

    def find_element(self,locator):
        """To find the element in web page"""
        return self.driver.find_element(*locator)

    def find_elements(self,locator):
        """To find the elements in the web page"""
        return self.driver.find_elements(*locator)

    def take_screenshot(self, file_name=None):
        """
        Takes screenshot during execution (check points) and stores it under /Snapshots_during_test folder
        """
        screenshots_dir = os.path.join(os.getcwd(), "test_reports/snapshots_during_test")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = time.strftime("%Y%m%d_%H%M%S")

        if not file_name:
            file_name = f"screenshot_{timestamp}.png"
        else:
            if not file_name.endswith(".png"):
                file_name = f"{file_name}_{timestamp}.png"

        file_path = os.path.join(screenshots_dir, file_name)

        self.driver.save_screenshot(file_path)

    def select_dropdown_by_text(self, locator, visible_text):
        """Select the dropdown by visible text"""
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_visible_text(visible_text)