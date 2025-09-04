import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui 
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваю сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне імя користувача або поштову адресу
    login_elem.send_keys("andriisavinov@mastakeinemail.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong_password")

    # Знаходимо кнопку Sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Виконуємо клік лівою кнопкою миші
    btn_elem.click()

    # Перевіряємо, що назва сторінка така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    
    # Закриваю браузер
    driver.close()