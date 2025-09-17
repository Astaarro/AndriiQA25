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



# ІНДИВІДУАЛЬНІ ТЕСТИ з PAGE OBGECT

# Тест переходу на рандомну категорію
@pytest.mark.ui_eros_cat
def test_open_random_for_her_category():
    # Етап 1: Відкриття головної сторінки
    main_page = MainPage()
    expected_main_page_title = "Секс-шоп «Ерос»💘Онлайн магазин інтимних товарів в Україні"
    main_page.go_to()
    assert main_page.check_title(expected_main_page_title)
    print("Крок 1: Головна сторінка відкрита. Назва відповідає очікуваній.")

    # Етап 2: Вибір випадкової категорії та перехід
    selected_category_name = main_page.go_to_random_category()
    print(f"Крок 2.1: Вибрано категорію '{selected_category_name}'.")
    assert main_page.check_title_contains(selected_category_name)
    print("Крок 2.2: Перевірка назви сторінки успішна. Вона містить назву категорії.")


# Тест замовлення товару
@pytest.mark.ui_eros_prod
def test_product_title_and_add_to_cart(driver):
    # Етап 1: Ініціалізація сторінок з використанням фікстури 'driver'
    product_page = ProductPage(driver)
    
    # Етап 2: Перехід на сторінку товару
    product_page.go_to()
    print("Крок 1: Перехід на сторінку товару")
    
    # Етап 3: Отримання назви товару зі сторінки
    product_name_on_page = product_page.get_product_title()
    
    # Етап 4: Перевірка, що назва товару є частиною заголовка сторінки
    processed_product_name = product_name_on_page.replace("×", "x")
    page_title = product_page.driver.title
    assert processed_product_name in page_title
    print(f"Крок 2: Назва товару ('{product_name_on_page}') є в заголовку сторінки")
    
    # Етап 5: Натискаємо кнопку "Купити"
    product_page.add_to_cart()
    print("Крок 3: Натиснуто кнопку 'Купити'.")
    
    time.sleep(2)
    
    # Етап 6: Переходимо в кошик через посилання в хедері
    product_page.go_to_cart_from_header()
    
    # Етап 7: Ініціалізація сторінки кошика з існуючим драйвером
    cart_page = CartPage(driver)
    print("Крок 4: Перехід до кошика")
    
    # Етап 8: Перевіряємо назву сторінки кошика
    expected_cart_title = "Кошик 💘 Інтим-Бутік ЕРОС"
    assert cart_page.driver.title == expected_cart_title
    print(f"Крок 5: Назва сторінки кошика ('{cart_page.driver.title}') відповідає очікуваній")
    
    # Етап 9: Перевіряємо назву товару в кошику
    product_name_in_cart = cart_page.get_product_name_in_cart()
    
    assert product_name_in_cart.replace("x", "×").strip() == product_name_on_page.strip()
    
    print(f"Крок 6: Назва товару в кошику ('{product_name_in_cart}') відповідає назві на сторінці товару. ✅")
    
    # Етап 10: Переходимо до оформлення замовлення
    cart_page.proceed_to_checkout()
    
    # Етап 11: Перевіряємо назву сторінки оформлення замовлення
    expected_checkout_title = "Оформлення замовлення 💘 Інтим-Бутік ЕРОС"
    assert driver.title == expected_checkout_title
    print(f"Крок 8: Назва сторінки оформлення замовлення ('{driver.title}') відповідає очікуваній")
    
    # Етап 12: Ініціалізуємо сторінку оформлення замовлення
    checkout_page = CheckoutPage(driver)
    
    # Етап 13: Заповнюємо форму замовлення
    checkout_page.fill_in_data("Андрій", "Сав", "096 1111111", "tessssst@ukr.net")
    
    # Етап 14: Ставимо чекбокс "Я згоден з умовами"
    checkout_page.accept_terms()
    
    # Етап 15: Натискаємо кнопку "Підтвердити замовлення"
    checkout_page.place_order()
    
    # Етап 16: Ініціалізуємо сторінку підтвердження замовлення
    order_received_page = OrderReceivedPage(driver)
    
    # Етап 17: Перевіряємо текст підтвердження замовлення
    expected_message = "Дякуємо. Ваше замовлення було отримано."
    actual_message = order_received_page.get_success_message()
    assert actual_message.strip() == expected_message.strip()
    print(f"Крок 12: Повідомлення про успішне замовлення ('{actual_message}') відповідає очікуваному")

    print("Тест оформлення замовлення завершено успішно")