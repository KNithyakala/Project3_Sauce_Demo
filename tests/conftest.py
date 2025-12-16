import logging
import os
import time

import pytest
import configparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


# Reading config file
config = configparser.ConfigParser()
config.read("config.ini")

@pytest.fixture(scope="function")
def setup(request):
    browser = config.get("browser_settings", "browser").lower()

    # Setup driver options
    driver_options = Options()
    driver_options.add_argument("--incognito")
    # driver Setup
    if browser == "chrome":
        driver_instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)
    elif browser == "firefox":
        driver_instance = webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        driver_instance = webdriver.Edge(service=EdgeService())
    elif browser == "safari":
        driver_instance = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser in config.ini:{browser}.\n"
                         f"Only chrome/firefox/edge/safari are allowed")

    driver_instance.maximize_window()
    request.cls.driver = driver_instance
    yield driver_instance
    # driver Tear down
    driver_instance.quit()


# defining log file
def pytest_configure():
    logger = logging.getLogger() # Debug,Info,Warning,Error,Critical,Fatal
    logger.setLevel(logging.INFO) # from where we need report
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ---- LOG FOLDER ----
    log_dir = os.path.join(os.getcwd(), "test_reports", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "test_logs.log")

    file_handler = logging.FileHandler(log_file,mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


#Hook to capture screenshots after each test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    if report.when == "call": # only after the test function runs

        driver_instance = None

        # try to get driver for class - based test
        if hasattr(item,"instance") and hasattr(item.instance,"driver"):
            driver_instance = getattr(item.instance,"driver",None)
            # function-based test
        elif "driver" in item.funcargs:
            driver_instance = item.funcargs["driver"]

        # Take screenshot  if driver available

        if driver_instance:
            status = "PASSED" if report.passed else "FAILED"
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            # create folder per test class
            class_name = item.cls.__name__ if item.cls else "FunctionTests"
            screenshot_dir = "test_reports/screenshots"
            os.makedirs(screenshot_dir,exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir,f"{item.name}-{status}-{timestamp}.png")
            WebDriverWait(driver_instance,10)
            driver_instance.save_screenshot(screenshot_path)
            print(f"Screenshot saved:{screenshot_path}")
