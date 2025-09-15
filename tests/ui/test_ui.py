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


# Eros.in.ua
# 3. Test 'add to cart', 'cart' and 'cheсkout'

@pytest.mark.ui_eros
def test_checkout_eros():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Щоб елементи не перекривались мобільними меню
    
    
    # 1. Відкриваємо головну сторінку
    driver.get("https://eros.in.ua/")

    # 2. Знаходимо картку товару
    # Ми використовуємо CSS-селектор для пошуку елемента-контейнера,
    # що містить посилання з назвою товару.
    product_card = driver.find_element(
        By.CSS_SELECTOR,
        "div.product-element-bottom:has(a[href*='pretty-love-robert'])"
    )

    # 3. Знаходимо кнопку "Купити" поруч із товаром
    buy_button = product_card.find_element(By.CLASS_NAME, "add_to_cart_button")
    # Скролимо до кнопки та натискаємо
    driver.execute_script("arguments[0].scrollIntoView();", buy_button)
    time.sleep(1)
    buy_button.click()

    # 4. Чекаємо AJAX, щоб товар додався
    time.sleep(5)

    # 5. Переходимо на сторінку кошика
    driver.get("https://eros.in.ua/cart/")

    # 6. Перевіряємо заголовок сторінки кошика
    WebDriverWait(driver, 10).until(EC.title_contains("Кошик"))
    assert "Кошик 💘 Інтим-Бутік ЕРОС" == driver.title

    # 7. Перевіряємо, що товар присутній у кошику і має правильну назву
    cart_item = driver.find_element(
    By.PARTIAL_LINK_TEXT,
    "Hi-tech вібратор Pretty Love Robert"
    )
    assert cart_item.is_displayed()

    # 8. Натискаємо кнопку "Перейти до оформлення"
    checkout_button = driver.find_element(By.CLASS_NAME, "checkout-button")
    checkout_button.click()

    # 9. Чекаємо, поки заголовок сторінки оформлення стане правильним
    WebDriverWait(driver, 10).until(EC.title_contains("Оформлення замовлення"))
    assert "Оформлення замовлення 💘 Інтим-Бутік ЕРОС" == driver.title

    # 10. Натискаємо "Підтвердити замовлення" (очікувано виникне повідомлення про обов’язкові поля)

    time.sleep(5)
    place_order_button = driver.find_element(By.ID, "place_order")
    place_order_button.click()
    time.sleep(10)
    # Перевіряємо повідомлення про обов’язкове поле
    error_message = driver.find_element(By.ID, "billing_first_name_description")
    assert "обов'язкове поле" in error_message.text


    # Закриваємо браузер
    driver.quit()

# 4. Test 'search'

@pytest.mark.ui_eros2
def test_search_vibrator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
 
    driver.get("https://eros.in.ua/")

    # 1. Чекаємо на повне завантаження сторінки
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'wd-header-search') and @title='Пошук']"))
    )

    # 2. Знаходимо іконку пошуку і наводимо на неї мишу
    search_icon = driver.find_element(By.XPATH, "//div[contains(@class,'wd-header-search') and @title='Пошук']")
    ActionChains(driver).move_to_element(search_icon).perform()

    # 3. Чекаємо, поки з'явиться випадаюче меню 
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "wd-search-dropdown"))
    )

    # 4. Чекаємо, поки поле введення стане клікабельним
    search_input = WebDriverWait(dropdown, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//input[@name='s']"))
    )

    # 5. Вводимо текст і натискаємо Enter
    search_input.click()
    search_input.send_keys("вібратор")
    search_input.send_keys(Keys.ENTER)

    # 6. Чекаємо поки завантажиться сторінка результатів і перевіряємо її назву
    WebDriverWait(driver, 10).until(
        EC.title_contains("Ви шукали вібратор")
    )
    assert "Ви шукали вібратор | Інтим-Бутік ЕРОС" == driver.title

    # 7. Перевіряємо, що товари присутні
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrapper"))
    )
    assert len(products) > 0, "Не знайдено жодного вібратора на сторінці"

    # 8. Додаємо затримку, щоб побачити результат перед закриттям
    print("Тест успішно завершено! Браузер закриється через 5 секунд.")
    time.sleep(10) 

    # 9. Закриваємо браузер
    driver.quit()