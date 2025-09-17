from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage(BasePage):
    # Локатори для полів введення
    FIRST_NAME_INPUT = (By.ID, "billing_first_name")
    LAST_NAME_INPUT = (By.ID, "billing_last_name")
    PHONE_INPUT = (By.ID, "billing_phone")
    EMAIL_INPUT = (By.ID, "billing_email")
    
    # Локатор для чекбокса "Я прочитав і згоден з умовами"
    TERMS_CHECKBOX = (By.ID, "terms")
    
    # Локатор для кнопки "Підтвердити замовлення"
    PLACE_ORDER_BUTTON = (By.ID, "place_order")
    
    # Локатор для оверлею, який блокує кліки
    OVERLAY = (By.CSS_SELECTOR, "div.blockUI.blockOverlay")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def wait_for_overlay_to_disappear(self):
        """Чекає, поки напівпрозоре накладення зникне."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
        except:
            pass

    def fill_in_data(self, first_name, last_name, phone, email):
        """Заповнює поля форми особистими даними."""
        print("Крок 9: Заповнюємо дані для оформлення замовлення.")
        
        self.wait_for_overlay_to_disappear()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        
        self.wait_for_overlay_to_disappear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        
        self.wait_for_overlay_to_disappear()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        
        self.wait_for_overlay_to_disappear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        
        print("Дані заповнено. ✅")
        
    def accept_terms(self):
        """Натискає на чекбокс 'Я згоден з умовами'."""
        print("Крок 10: Ставимо позначку 'Я згоден з умовами'.")
        self.wait_for_overlay_to_disappear()
        
        terms_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TERMS_CHECKBOX)
        )
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
            print("Чекбокс відмічено. ✅")
        
    def place_order(self):
        """Натискає на кнопку 'Підтвердити замовлення'."""
        print("Крок 11: Натискаємо кнопку 'Підтвердити замовлення'.")
        self.wait_for_overlay_to_disappear()
        
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        )
        place_order_button.click()
        # Додаємо затримку для переходу на сторінку підтвердження
        time.sleep(15)