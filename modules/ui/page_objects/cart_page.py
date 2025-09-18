from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CartPage(BasePage):
    """
    This class represents the cart page within the Page Object Model (POM) pattern.
    It encapsulates the elements and actions related to the shopping cart, allowing tests to interact with products in the cart and proceed to the checkout page.
    """

    URL = 'https://eros.in.ua/cart/'
    CHECKOUT_URL = 'https://eros.in.ua/checkout/'
    PRODUCT_IN_CART_TITLE = (By.CSS_SELECTOR, ".product-name a") # Locator for the product name in the cart
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout-button") # Locator for the "Оформити замовлення" button

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Retrieves the text of the product's title from the cart page.
    def get_product_name_in_cart(self):
        product_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_IN_CART_TITLE)
        ).text
        
        return product_title

    # Clicks the "Оформити замовлення" button and waits for the page to navigate.
    def proceed_to_checkout(self):
        print("Clicking the 'Оформити замовлення' button")
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.CHECKOUT_URL)
        )
        print("Navigation to the checkout page completed")