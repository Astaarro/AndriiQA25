import pytest
from modules.api.clients.github import Github
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# A class to model a user with methods for creation and removal.
class User:  

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Andrii"
        self.second_name = "Savchenko"

    def remove(self):
        self.name = ""
        self.second_name = ""

# A pytest fixture that creates a user, yields it for the test, and then removes it.
@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.remove()

# A pytest fixture that provides an instance of the Github API client.
@pytest.fixture
def github_api():
    api = Github()
    yield api