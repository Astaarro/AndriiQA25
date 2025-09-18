from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BasePage:
    """
    A base class for page objects that contains common methods and driver initialization
    """

    # Initializes the browser driver or uses an existing one
    def __init__(self, driver=None) -> None:
        if driver is None:
            options = Options()
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.maximize_window()
            print("New Chrome driver initialized.")
        else:
            self.driver = driver

    # Closes the browser window
    def close(self):
        if self.driver:
            self.driver.close()
