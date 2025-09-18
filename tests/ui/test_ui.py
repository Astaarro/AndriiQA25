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
from selenium.common.exceptions import NoSuchElementException


# QA AUTOMATION COURSE TEST without PAGE OBGECT

# GitHub.com тест введення неправильного логіну і пароля
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


# PERSONAL WORK without PAGE OBGECT

# 1. ROZETKA.COM.UA
# Search "iphone". Test failed, cos site has antibot system Cloudflare

@pytest.mark.ui_rozetka
def test_search_product_rozetka():
    # Creating the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Opening Rozetka
    driver.get("https://rozetka.com.ua/")

    # Finding the search field
    search_box = driver.find_element(By.NAME, "search")

    # Entering "iPhone" and pressing Enter
    search_box.send_keys("iPhone")
    search_box.send_keys(Keys.RETURN)

    # Waiting ten seconds for the results to load
    time.sleep(10)

    # Verifying that "iPhone" is in the page title
    assert "iPhone" in driver.title

    # Checking that there is a list of products
    products = driver.find_elements(By.CLASS_NAME, "goods-tile__title")
    assert len(products) > 0, "Список товарів порожній!"

    # Closing the browser
    driver.close()


# 2. PROM.UA
# Search "iphone". Test Complited 100%

@pytest.mark.ui_prom
def test_search_product_prom():
    # Creating the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Opening Prom.ua
    driver.get("https://prom.ua/")

    # Finding the search field
    search_box = driver.find_element(By.NAME, "search_term")

    # Entering "iPhone" and pressing Enter
    search_box.send_keys("iPhone")
    search_box.send_keys(Keys.RETURN)

    # Waiting ten seconds for the results to load
    time.sleep(10)

    # Finding the h1 heading
    page_h1 = driver.find_element(By.TAG_NAME, "h1").text

    # Checking that the word "iPhone" is in it (case-insensitive)
    assert "iphone" in page_h1.lower()

    # Closing the browser
    driver.close()


# 3. Eros.in.ua
# Test 'add to cart', 'cart' and 'cheсkout'

@pytest.mark.ui_eros_checkout
def test_checkout_eros():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Opening the main page
    driver.get("https://eros.in.ua/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-element-bottom"))
    )

    # Finding the first product card on the page
    try:
        product_card = driver.find_element(By.CSS_SELECTOR, ".product-element-bottom")
    except NoSuchElementException:
        print("Failed to find a product card on the main page. The test will be skipped")
        driver.quit()
        pytest.skip("No products available for testing")

    # Finding the product's name and its link
    product_link = product_card.find_element(By.CSS_SELECTOR, "a[href]")
    product_name = product_link.text

    if not product_name:
        print("Found a product card without a name. Skipping this product")
        driver.quit()
        pytest.skip("Product without a name")

    print(f"Found product: '{product_name}'")

    # Finding the "Buy" button next to the product
    buy_button = product_card.find_element(By.CLASS_NAME, "add_to_cart_button")

    driver.execute_script("arguments[0].scrollIntoView();", buy_button)
    time.sleep(1)
    buy_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-cart-link"))
    )
    print("Product has been added to the cart")

    # Navigating to the cart page
    driver.get("https://eros.in.ua/cart/")

    WebDriverWait(driver, 10).until(EC.title_contains("Кошик"))
    assert "Кошик 💘 Інтим-Бутік ЕРОС" == driver.title

    # Verifying that the product is in the cart and has the correct name
    cart_item_locator = (By.PARTIAL_LINK_TEXT, product_name)
    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(cart_item_locator)
    )
    assert cart_item.is_displayed()
    assert product_name in cart_item.text
    print(f"Product '{product_name}' found in the cart")

    # Clicking the "Proceed to checkout" button
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))
    )
    checkout_button.click()
    print("Proceeding to checkout.")

    # Waiting for the checkout page title to become correct
    WebDriverWait(driver, 10).until(EC.title_contains("Оформлення замовлення"))
    assert "Оформлення замовлення 💘 Інтим-Бутік ЕРОС" == driver.title

    # Clicking "Confirm order"
    try:
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.blockUI.blockOverlay"))
        )
    except:
        pass

    place_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "place_order"))
    )
    place_order_button.click()
    print("Clicked the 'Confirm order' button")

    # Verifying the required field error message
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".woocommerce-error"))
    )
    assert "обов'язкове поле" in error_message.text
    print("Required field message found. Test successfully completed")

    # Closing the browser
    driver.quit()

    
# Test 'search'

@pytest.mark.ui_eros_search
def test_search_vibrator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://eros.in.ua/")

    # 1. Waiting for the page to fully load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'wd-header-search') and @title='Пошук']"))
    )

    # 2. Finding the search icon and hovering the mouse over it
    search_icon = driver.find_element(By.XPATH, "//div[contains(@class,'wd-header-search') and @title='Пошук']")
    ActionChains(driver).move_to_element(search_icon).perform()

    # 3. Waiting for the dropdown menu to appear
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "wd-search-dropdown"))
    )

    # 4. Waiting for the input field to become clickable
    search_input = WebDriverWait(dropdown, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//input[@name='s']"))
    )

    # 5. Entering text and pressing Enter
    search_input.click()
    search_input.send_keys("вібратор")
    search_input.send_keys(Keys.ENTER)

    # 6. Waiting for the results page to load and checking its title
    WebDriverWait(driver, 10).until(
        EC.title_contains("Ви шукали вібратор")
    )
    assert "Ви шукали вібратор | Інтим-Бутік ЕРОС" == driver.title

    # 7. Verifying that products are present
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "product-wrapper"))
    )
    assert len(products) > 0, "No vibrators found on the page"

    # 8. Adding a delay to see the result before closing
    print("Test successfully completed! The browser will close in 5 seconds.")
    time.sleep(10)

    # 9. Closing the browser
    driver.quit()