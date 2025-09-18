from modules.ui.page_objects.main_page import MainPage
from modules.ui.page_objects.product_page import ProductPage
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.cart_page import CartPage
from modules.ui.page_objects.checkout_page import CheckoutPage
from modules.ui.page_objects.order_received_page import OrderReceivedPage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# QA AUTOMATION COURSE TEST with PAGE OBGECT

# Тест github невірний логін/пароль

@pytest.mark.ui 
def test_check_incorrect_usermane_page_object():
    # Стрворення обєкту сторніки
    sign_in_page = SignInPage()
    
    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # Виконуємо спробу увійти в GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong_password")

    # Перевіряємо чи назва стоірнки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Зариваємо браузер
    sign_in_page.close()


# PERSONAL WORK with PAGE OBGECT

# Test for navigating to a random eros.in.ua category
@pytest.mark.ui_eros_cat
def test_open_random_for_her_category():
    # Opening the main page
    main_page = MainPage()
    expected_main_page_title = "Секс-шоп «Ерос»💘Онлайн магазин інтимних товарів в Україні"
    main_page.go_to()
    assert main_page.check_title(expected_main_page_title)
    print("The main page is open. The title matches the expected one.")

    # Selecting a random category and navigating to it
    selected_category_name = main_page.go_to_random_category()
    print(f"The category '{selected_category_name}' has been selected.")
    assert main_page.check_title_contains(selected_category_name)
 

# Test for ordering a product on eros.in.ua
@pytest.mark.ui_eros_prod
def test_product_title_and_add_to_cart():
    # Step 1: Initializing the product page and a new driver instance
    product_page = ProductPage()
        
    # Step 2: Navigating to the product page
    product_page.go_to()
    print("Step 1: Navigating to the product page")

    # Step 3: Getting the product title from the page
    product_name_on_page = product_page.get_product_title()

    # Step 4: Verifying that the product title is part of the page's title
    page_title = product_page.driver.title
    assert product_name_on_page in page_title
    print(f"Step 2: The product title ('{product_name_on_page}') is in the page title")

    # Step 5: Clicking the "Buy" button
    product_page.add_to_cart()
    print("Step 3: The 'Buy' button has been clicked.")

    time.sleep(2)

    # Step 6: Navigating to the cart via the header link
    product_page.go_to_cart_from_header()

    # Step 7: Initializing the cart page with the existing driver from product_page
    cart_page = CartPage(product_page.driver)
    print("Step 4: Navigating to the cart")

    # Step 8: Checking the cart page's title
    expected_cart_title = "Кошик 💘 Інтим-Бутік ЕРОС"
    assert cart_page.driver.title == expected_cart_title
    print(f"Step 5: The cart page title ('{cart_page.driver.title}') matches the expected one")

    # Step 9: Verifying the product title in the cart
    product_name_in_cart = cart_page.get_product_name_in_cart()
    assert product_name_in_cart == product_name_on_page.strip()
    print(f"Step 6: The product title in the cart ('{product_name_in_cart}') matches the title on the product page")

    # Step 10: Proceeding to checkout
    cart_page.proceed_to_checkout()

    # Step 11: Verifying the checkout page's title
    expected_checkout_title = "Оформлення замовлення 💘 Інтим-Бутік ЕРОС"
    assert product_page.driver.title == expected_checkout_title
    print(f"Step 8: The checkout page title ('{product_page.driver.title}') matches the expected one")

    # Step 12: Initializing the checkout page
    checkout_page = CheckoutPage(product_page.driver)

    # Step 13: Filling out the order form
    checkout_page.fill_in_data("Андрій", "Сав", "096 1111111", "tessssst@ukr.net")

    # Step 14: Checking the "I agree to the terms" checkbox
    checkout_page.accept_terms()

    # Step 15: Clicking the "Confirm order" button
    checkout_page.place_order()

    # Step 16: Initializing the order received page
    order_received_page = OrderReceivedPage(product_page.driver)

    # Step 17: Verifying the order confirmation message
    expected_message = "Дякуємо. Ваше замовлення було отримано."
    actual_message = order_received_page.get_success_message()
    assert actual_message.strip() == expected_message.strip()


    # Step 18: Closing the browser
    product_page.close()