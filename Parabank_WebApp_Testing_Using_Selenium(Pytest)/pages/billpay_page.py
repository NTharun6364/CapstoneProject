from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from utils.logger import logger

class BillPayPage:
    def __init__(self, driver):
        self.driver = driver

    def pay_bill(self, payee, account, amount):
        self.driver.find_element(By.LINK_TEXT, "Bill Pay").click()
        time.sleep(1)
        for field, value in payee.items():
            self.driver.find_element(By.NAME, f"payee.{field}").send_keys(value)
        self.driver.find_element(By.NAME, "payee.accountNumber").send_keys(account)
        self.driver.find_element(By.NAME, "verifyAccount").send_keys(account)
        self.driver.find_element(By.NAME, "amount").send_keys(amount)
        Select(self.driver.find_element(By.NAME, "fromAccountId")).select_by_visible_text(account)
        self.driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
        time.sleep(2)
        assert "Bill Payment Complete" in self.driver.page_source
        logger.info(f"✅ Bill Payment of ${amount} complete.")
