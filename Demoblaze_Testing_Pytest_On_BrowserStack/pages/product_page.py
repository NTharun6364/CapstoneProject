from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import ADD_TO_CART


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def add_to_cart_and_accept_alert(self):
        """
        Clicks the 'Add to cart' button and handles the alert popup on Demoblaze.
        Waits explicitly for the alert to be present (important for BrowserStack mobile).
        """
        # Wait for Add to Cart button
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, ADD_TO_CART)))
        add_button.click()

        # Wait for alert (Demoblaze may delay this by a few seconds)
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            raise AssertionError("❌ Alert did not appear after clicking 'Add to cart'. "
                                 "Possible UI delay or test environment issue.")
