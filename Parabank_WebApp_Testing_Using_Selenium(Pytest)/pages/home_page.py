from selenium.webdriver.common.by import By
from utils.logger import logger

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://parabank.parasoft.com/parabank/index.htm"

    def open_homepage(self):
        self.driver.get(self.url)
        assert "ParaBank" in self.driver.title
        logger.info("✅ ParaBank homepage opened successfully.")

    def go_to_register(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
