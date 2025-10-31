from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import HOME_FIRST_PRODUCT

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_home(self):
        self.driver.get(self.driver.current_url)
        self.wait.until(EC.presence_of_element_located((By.ID, 'nava')))

    def open_first_product(self):
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, HOME_FIRST_PRODUCT)))
        el.click()
