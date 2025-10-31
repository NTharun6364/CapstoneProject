from selenium.webdriver.common.by import By
import time
from utils.logger import logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Log In']").click()
        time.sleep(1)
        assert "Welcome" in self.driver.page_source
        logger.info("✅ Login successful.")
