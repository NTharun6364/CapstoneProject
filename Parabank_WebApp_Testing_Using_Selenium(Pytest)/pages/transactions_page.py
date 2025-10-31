from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from utils.logger import logger

class TransactionsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_transaction(self, account, amount):
        self.driver.find_element(By.LINK_TEXT, "Find Transactions").click()
        time.sleep(2)
        Select(self.driver.find_element(By.ID, "accountId")).select_by_visible_text(account)
        self.driver.find_element(By.ID, "amount").send_keys(amount)
        self.driver.find_element(By.ID, "findByAmount").click()
        time.sleep(3)

        title = self.driver.find_element(By.XPATH, "//div[@id='resultContainer']/h1").text
        assert title == "Transaction Results", "Transaction Results not shown!"
        logger.info("✅ Transaction Results page verified.")

        table = self.driver.find_element(By.ID, "transactionTable")
        rows = table.find_elements(By.XPATH, ".//tbody/tr")
        assert len(rows) > 0
        logger.info("✅ Transaction record(s) found.")
