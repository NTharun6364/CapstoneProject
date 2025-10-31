from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from utils.logger import logger

class TransferPage:
    def __init__(self, driver):
        self.driver = driver

    def transfer_funds(self, from_acc, to_acc, amount):
        self.driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "amount").send_keys(amount)
        Select(self.driver.find_element(By.ID, "fromAccountId")).select_by_visible_text(from_acc)
        Select(self.driver.find_element(By.ID, "toAccountId")).select_by_visible_text(to_acc)
        self.driver.find_element(By.XPATH, "//input[@value='Transfer']").click()
        time.sleep(2)
        assert "Transfer Complete!" in self.driver.page_source
        logger.info(f"✅ Transfer of ${amount} successful.")
