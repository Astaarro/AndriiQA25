from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderReceivedPage(BasePage):
    # Локатор для повідомлення про успішне оформлення замовлення
    ORDER_RECEIVED_MESSAGE = (By.CSS_SELECTOR, ".woocommerce-notice.woocommerce-notice--success.woocommerce-thankyou-order-received")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def get_success_message(self):
        """Отримує текст повідомлення про успішне оформлення замовлення."""
        message_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ORDER_RECEIVED_MESSAGE)
        )
        return message_element.text