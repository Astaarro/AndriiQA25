from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage(BasePage):
    URL = 'https://eros.in.ua/cart/'
    CHECKOUT_URL = 'https://eros.in.ua/checkout/'

    # Локатор для назви товару в кошику
    PRODUCT_IN_CART_TITLE = (By.CSS_SELECTOR, ".product-name a")
    # Локатор для кнопки "Перейти до оформлення"
    # Використовуємо більш надійний локатор за класом 'checkout-button'
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout-button")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def get_product_name_in_cart(self):
        product_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_IN_CART_TITLE)
        ).text
        return product_title
    
    def proceed_to_checkout(self):
        print("Крок 7: Натискаємо кнопку 'Перейти до оформлення'.")
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
        # Чекаємо, поки URL-адреса сторінки зміниться на адресу сторінки оформлення замовлення
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.CHECKOUT_URL)
        )
        print("Перехід на сторінку оформлення замовлення завершено. ✅")