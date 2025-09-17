from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from conftest import driver

class BasePage:

 
    PATH = r"C:\Users\AMD\AndriiQA25\AndriiQA25"
    DRIVER_NAME = "chromedriver"

    


    def close(self):
        self.driver.close()
    """Базовий клас для об'єктів сторінок, який містить загальні методи та ініціалізацію драйвера."""
    
    # Локатор для іконки/посилання кошика в хедері
    CART_LINK = (By.CSS_SELECTOR, ".wd-header-cart a[href*='cart']")

  
    def __init__(self, driver=None):
        if driver is None:
            options = Options()
            options.add_argument("--start-maximized")
            # webdriver-manager завантажує правильний драйвер
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
        else:
            self.driver = driver
        
    def close(self):
        """Закриває вікно браузера."""
        if self.driver:
            self.driver.close()

    def go_to_cart_from_header(self):
        """Переходить на сторінку кошика, натискаючи на посилання в хедері."""
        print("Перехід до кошика через хедер...")
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()