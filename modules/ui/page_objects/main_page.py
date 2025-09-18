from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time


class MainPage(BasePage):
    """
    This class represents the main page and category pages of the eros.in.ua website.
    It follows the Page Object Model (POM) pattern to encapsulate navigation,
    element locators, and interactions within these pages.
    """

    URL = 'https://eros.in.ua/'

    CATEGORY_PAGES = {
        'https://eros.in.ua/catalog/vahinalni_kulky/': 'вагінальні кульки',
        'https://eros.in.ua/catalog/vibratory/': 'вібратори',
        'https://eros.in.ua/catalog/vibroyajtsya/': 'віброяйця',
        'https://eros.in.ua/catalog/vakuumni-stymulyatory/': 'вакуумні стимулятори'
    }

    PAGINATION_CONTAINER = (By.CSS_SELECTOR, ".woocommerce-pagination.wd-pagination")  # Locator for the container holding the pagination links.
    LOADING_SPINNER = (By.CSS_SELECTOR, ".wd-preloader")  # Locator for the loading spinner that appears during page updates.
    ALL_PRODUCT_ITEMS = (By.CSS_SELECTOR, "ul.products li.product")  # Locator for all individual product items on a page.
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".wd-entities-title a")  # Locator for the link containing the product name.
    CART_LINK = (By.CSS_SELECTOR, ".wd-header-cart a[href*='cart']")  # Locator for the cart icon/link in the header.

    def __init__(self) -> None:
        super().__init__()

    # Navigates the browser to the main page URL.
    def go_to(self):
        self.driver.get(MainPage.URL)

    # Checks if the current page title is exactly the same as the expected title.
    def check_title(self, expected_title):
        
        return self.driver.title == expected_title

    # Checks if the current page title contains a specific substring within a given timeout period.
    def check_title_contains(self, expected_partial_title, timeout=10):
        expected_text_lower = expected_partial_title.lower()
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_title_lower = self.driver.title.lower()
            if expected_text_lower in current_title_lower:
                return True
            time.sleep(0.5)
        
        return False

    # Selects a random category URL from the defined list and navigates to it.
    def go_to_random_category(self):
        selected_url, expected_name = random.choice(list(self.CATEGORY_PAGES.items()))
        self.driver.get(selected_url)
        print("A category has been selected")

        return expected_name


    """
    def go_to_random_page(self):
        pagination = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PAGINATION_CONTAINER)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            pagination
        )
        page_number = random.randint(2, 4)
        print(f"Step 3.2: Random page number {page_number} has been selected.")
        page_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, str(page_number)))
        )
        try:
            page_link.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", page_link)
        print("Step 3.3: Waiting for the loading indicator to disappear...")
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(self.LOADING_SPINNER)
        )
        # Waiting for products to appear after AJAX loading
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.ALL_PRODUCT_ITEMS)
        )
        products = self.driver.find_elements(*self.ALL_PRODUCT_ITEMS)
        if not products:
            raise TimeoutException("No products found after navigating through pagination")
        print(f"Step 3.4: {len(products)} products have loaded on the page.")
        
        return page_number

    """




