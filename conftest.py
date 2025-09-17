import pytest
from modules.api.clients.github import Github

class User:

    def _init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Andrii"
        self.second_name = "Savchenko"

    def remove(self):
        self.name = "" 
        self.second_name = ""

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

@pytest.fixture
def github_api():
    api = Github()
    yield api


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """Фікстура для ініціалізації та завершення роботи драйвера браузера."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()