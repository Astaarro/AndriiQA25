from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Finding the field to enter the incorrect username or email address
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Entering the incorrect username or email address
        login_elem.send_keys(username)

        # Finding the field to enter the incorrect password
        pass_elem = self.driver.find_element(By.ID, "password")

        # Entering the incorrect password
        pass_elem.send_keys(password)

        # Finding the 'Sign in' button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulating a left mouse click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title





