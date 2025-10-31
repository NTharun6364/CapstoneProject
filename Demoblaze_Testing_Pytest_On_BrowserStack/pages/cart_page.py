from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CART_LINK, PLACE_ORDER_BUTTON

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, CART_LINK)))
        cart.click()

    def place_order(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, PLACE_ORDER_BUTTON)))
        btn.click()
