from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time

class MainPage(BasePage):
    URL = 'https://eros.in.ua/'

    CATEGORY_PAGES = {
        'https://eros.in.ua/catalog/vahinalni_kulky/': 'вагінальні кульки',
        'https://eros.in.ua/catalog/vibratory/': 'вібратори',
        'https://eros.in.ua/catalog/vibroyajtsya/': 'віброяйця',
        'https://eros.in.ua/catalog/vakuumni-stymulyatory/': 'вакуумні стимулятори'
    }

    PAGINATION_CONTAINER = (By.CSS_SELECTOR, ".woocommerce-pagination.wd-pagination")
    LOADING_SPINNER = (By.CSS_SELECTOR, ".wd-preloader")
    
    # Оновлені локатори
    ALL_PRODUCT_ITEMS = (By.CSS_SELECTOR, "ul.products li.product")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, ".wd-entities-title a")

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(MainPage.URL)

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def check_title_contains(self, expected_partial_title, timeout=10):
        expected_text_lower = expected_partial_title.lower()
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_title_lower = self.driver.title.lower()
            if expected_text_lower in current_title_lower:
                return True
            time.sleep(0.5)
        return False
    
    def go_to_random_category(self):
        selected_url, expected_name = random.choice(list(self.CATEGORY_PAGES.items()))
        self.driver.get(selected_url)
        
        # Виконуємо скрол на 500 пікселів вниз
        self.driver.execute_script("window.scrollBy(0, 500);")
        print("Крок 2.1: Вибрано категорію. Виконано скрол вниз на 500 пікселів.")
        
        return expected_name
    
    def go_to_random_page(self):
        pagination = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PAGINATION_CONTAINER)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            pagination
        )

        page_number = random.randint(2, 4)
        print(f"Крок 3.2: Вибрано випадкову сторінку №{page_number}.")
        page_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, str(page_number)))
        )

        try:
            page_link.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", page_link)

        print("Крок 3.3: Очікування зникнення індикатора завантаження...")
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(self.LOADING_SPINNER)
        )

        # Чекаємо, поки товари з’являться після AJAX-завантаження
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.ALL_PRODUCT_ITEMS)
        )

        products = self.driver.find_elements(*self.ALL_PRODUCT_ITEMS)
        if not products:
            raise TimeoutException("Не знайдено жодного товару після переходу по пагінації")

        print(f"Крок 3.4: Завантажилось {len(products)} товарів на сторінці.")
        return page_number



