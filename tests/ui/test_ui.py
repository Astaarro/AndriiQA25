import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

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


# INDIVIDUAL WORK

# ROZETKA.COM.UA
# 1. Search "iphone".
# Test failed, cos site has antibot system Cloudflare

@pytest.mark.ui_rozetka
def test_search_product_rozetka():
    # Створення драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваємо Rozetka
    driver.get("https://rozetka.com.ua/")

    # Знаходимо поле пошуку
    search_box = driver.find_element(By.NAME, "search")

    # Вводимо текст "iPhone" і натискаємо Enter
    search_box.send_keys("iPhone")
    search_box.send_keys(Keys.RETURN)

    # Чекаємо десять секунд, щоб завантажились результати
    time.sleep(10)

    # Перевіряємо, що в заголовку сторінки є "iPhone"
    assert "iPhone" in driver.title

    # Перевіряємо, що є список товарів
    products = driver.find_elements(By.CLASS_NAME, "goods-tile__title")
    assert len(products) > 0, "Список товарів порожній!"

    # Закриваємо браузер
    driver.close()

# PROM.UA
# 2. Search "iphone".
# PASSED   100%                                                                                                   [100%]

@pytest.mark.ui_prom
def test_search_product_prom():
    # Створення драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваємо Prom.ua
    driver.get("https://prom.ua/")

    # Знаходимо поле пошуку
    search_box = driver.find_element(By.NAME, "search_term")

    # Вводимо текст "iPhone" і натискаємо Enter
    search_box.send_keys("iPhone")
    search_box.send_keys(Keys.RETURN)

    # Чекаємо десять секунд, щоб завантажились результати
    time.sleep(10)

    # Знаходимо заголовок h1
    page_h1 = driver.find_element(By.TAG_NAME, "h1").text

    # Перевіряємо, що в ньому є слово iPhone (без урахування регістру)
    assert "iphone" in page_h1.lower()

    # Закриваємо браузер
    driver.close()


