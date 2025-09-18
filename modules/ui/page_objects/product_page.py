from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    """
    This class represents the product page within the Page Object Model (POM) pattern.
    It encapsulates the elements and actions related to the product page on the eros.in.ua website for automated testing.
    """

    URL = 'https://eros.in.ua/product/probnyk-masazhnoi-olii-exsens-strawberry-3ml/'
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product_title.entry-title.wd-entities-title") # Locator for the product title
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".single_add_to_cart_button") # Locator for the "Купити" button
    CART_LINK = (By.CSS_SELECTOR, ".wd-header-cart a[href*='cart']")  # Locator for the cart icon/link in the header.

    def __init__(self) -> None:
        super().__init__()

    # Navigates to the product page.
    def go_to(self):
        self.driver.get(ProductPage.URL)

    # Retrieves the text of the product title from the page. It waits up to 10 seconds for the element to become visible.
    def get_product_title(self):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_TITLE)
        )
        
        return title_element.text.strip()

    # Clicks the "Купити" button. It waits up to 10 seconds for the button to become clickable before interacting with it.
    def add_to_cart(self):
        buy_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        buy_button.click()

    # Navigates to the cart page by clicking the link in the header.
    def go_to_cart_from_header(self):
        print("Navigating to cart via header...")
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()