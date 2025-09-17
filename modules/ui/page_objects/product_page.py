from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    URL = 'https://eros.in.ua/product/nabir-lubrykantiv-just-glide-3x50-ml/'
    
    # Локатор для назви товару
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product_title.entry-title.wd-entities-title")
    # Локатор для кнопки "Купити"
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".single_add_to_cart_button")
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
        
    def go_to(self):
        self.driver.get(ProductPage.URL)
        
    def get_product_title(self):
        # Чекаємо, поки назва товару стане видимою і повертаємо її текст
        title_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_TITLE)
        )
        return title_element.text.strip()
        
    def add_to_cart(self):
        # Чекаємо, поки кнопка "Купити" стане клікабельною
        buy_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        buy_button.click()