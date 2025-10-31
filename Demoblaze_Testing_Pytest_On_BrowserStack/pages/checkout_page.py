import time
import logging
from selenium.webdriver.common.by import By
from config import PURCHASE_BUTTON, CONFIRMATION_OK_BUTTON

logger = logging.getLogger(__name__)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_order(self, name, country, city, card, month, year):
        """Fill the order form with given data"""
        fields = {
            "name": name,
            "country": country,
            "city": city,
            "card": card,
            "month": month,
            "year": year,
        }
        for field_id, value in fields.items():
            el = self.driver.find_element(By.ID, field_id)
            el.clear()
            el.send_keys(value)
        logger.info("✅ Order details filled successfully")

    def confirm_purchase(self):
        """Click Purchase button only"""
        self.driver.find_element(By.XPATH, PURCHASE_BUTTON).click()
        logger.info("🛒 Purchase button clicked")
        time.sleep(2)
