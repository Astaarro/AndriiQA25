from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CheckoutPage(BasePage):
    """
    This class represents the checkout page, a crucial part of the Page Object Model (POM) pattern.
    It encapsulates all the elements and actions required to complete the checkout process,
    such as filling in personal data and placing the order.
    """

    # Locators for input fields
    FIRST_NAME_INPUT = (By.ID, "billing_first_name")
    LAST_NAME_INPUT = (By.ID, "billing_last_name")
    PHONE_INPUT = (By.ID, "billing_phone")
    EMAIL_INPUT = (By.ID, "billing_email")
    TERMS_CHECKBOX = (By.ID, "terms") # Locator for the "Я прочитав і згоден з умовами" checkbox
    PLACE_ORDER_BUTTON = (By.ID, "place_order") # Locator for the "Підтвердити замовлення" button
    OVERLAY = (By.CSS_SELECTOR, "div.blockUI.blockOverlay")  # Locator for the overlay that blocks clicks

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Waits for the translucent overlay to disappear
    def wait_for_overlay_to_disappear(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.OVERLAY)
            )
        except:
            pass

    # Fills in the form fields with personal data
    def fill_in_data(self, first_name, last_name, phone, email):
        print("Filling in the data for the order.")
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
        print("Data has been filled in")

    # Clicks the 'Я погоджуюся з умовами' checkbox
    def accept_terms(self):
        print("Checking the 'Я погоджуюся з умовами' box.")
        self.wait_for_overlay_to_disappear()
        terms_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TERMS_CHECKBOX)
        )
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
            print("Checkbox is checked")

    # Clicks the 'Confirm order' button
    def place_order(self):
        print("Clicking the 'Confirm order' button.")
        self.wait_for_overlay_to_disappear()
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        )
        place_order_button.click()
        
        # Adding a delay to navigate to the confirmation page
        time.sleep(15)