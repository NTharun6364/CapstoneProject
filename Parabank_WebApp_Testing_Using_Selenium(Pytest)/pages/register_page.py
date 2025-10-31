from selenium.webdriver.common.by import By
import time
from utils.logger import logger

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def register_user(self, user):
        self.driver.find_element(By.ID, "customer.firstName").send_keys(user["first"])
        self.driver.find_element(By.ID, "customer.lastName").send_keys(user["last"])
        self.driver.find_element(By.ID, "customer.address.street").send_keys(user["street"])
        self.driver.find_element(By.ID, "customer.address.city").send_keys(user["city"])
        self.driver.find_element(By.ID, "customer.address.state").send_keys(user["state"])
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys(user["zip"])
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys(user["phone"])
        self.driver.find_element(By.ID, "customer.ssn").send_keys(user["ssn"])
        self.driver.find_element(By.ID, "customer.username").send_keys(user["username"])
        self.driver.find_element(By.ID, "customer.password").send_keys(user["password"])
        self.driver.find_element(By.ID, "repeatedPassword").send_keys(user["password"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@value='Register']").click()
        time.sleep(2)

        welcome_text = self.driver.find_element(By.XPATH, '//*[@id="leftPanel"]/p/b').text
        assert "Welcome" in welcome_text, "Registration failed"
        logger.info(f"✅ Registration Successful: {welcome_text}")

        
