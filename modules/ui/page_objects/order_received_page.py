from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderReceivedPage(BasePage):
    """
    This class represents the order confirmation page.
    It's part of the Page Object Model pattern and contains the elements and methods necessary to interact with the page after a successful order has been placed.
    """
    
    # Locator for the successful order placement message
    ORDER_RECEIVED_MESSAGE = (By.CSS_SELECTOR, ".woocommerce-notice.woocommerce-notice--success.woocommerce-thankyou-order-received")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    #Retrieves the text of the successful order placement message
    def get_success_message(self):
        message_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ORDER_RECEIVED_MESSAGE)
        )
        return message_element.text