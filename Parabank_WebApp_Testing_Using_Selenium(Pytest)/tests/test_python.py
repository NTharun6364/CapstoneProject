import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.logger import logger
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage
from pages.billpay_page import BillPayPage
from pages.transactions_page import TransactionsPage


def read_users_from_csv(file_path):
    """Reads all users from CSV and returns as a list of dicts"""
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def test_python(setup):
    driver, browser = setup

    # ✅ Load all users
    users = read_users_from_csv("data/user.csv")

    # ✅ Assign one user per browser
    browser_index_map = {"chrome": 0, "firefox": 1, "edge": 2}
    user_index = browser_index_map.get(browser, 0)
    user = users[user_index]
    logger.info(f"🧾 Running on {browser.upper()} with user: {user['username']}")

    # ✅ Initialize pages
    home = HomePage(driver)
    register = RegisterPage(driver)
    login = LoginPage(driver)
    transfer = TransferPage(driver)
    billpay = BillPayPage(driver)
    transactions = TransactionsPage(driver)

    # Step 1: Open homepage and go to register
    home.open_homepage()
    home.go_to_register()

    # Step 2: Register new user
    register.register_user(user)
    driver.find_element(By.LINK_TEXT, "Log Out").click()

    # Step 3: Login
    login.login(user["username"], user["password"])

    # Step 4: Open New Account
    driver.find_element(By.LINK_TEXT, "Open New Account").click()
    time.sleep(1)
    select_account_type = Select(driver.find_element(By.ID, "type"))
    select_account_type.select_by_visible_text("SAVINGS")
    driver.find_element(By.XPATH, '//*[@id="openAccountForm"]/form/div/input').click()
    time.sleep(2)

    account_number = driver.find_element(By.ID, "newAccountId").text
    logger.info(f"✅ New account number ({browser}): {account_number}")
    assert account_number.isdigit(), "Account number invalid!"

    # Step 5: Accounts Overview
    driver.find_element(By.LINK_TEXT, "Accounts Overview").click()
    time.sleep(1)
    accounts = driver.find_elements(By.XPATH, "//table[@id='accountTable']//a")
    account_numbers = [a.text for a in accounts]
    logger.info(f"💰 Available accounts on {browser}: {account_numbers}")

    # Step 6: Transfer Funds
    transfer.transfer_funds(account_numbers[0], account_numbers[1], "100")

    # Step 7: Bill Payment
    payee = {
        "name": "ABC Power Co",
        "address.street": "Green Street",
        "address.city": "Bangalore",
        "address.state": "KA",
        "address.zipCode": "560001",
        "phoneNumber": "9876543210",
    }
    billpay.pay_bill(payee, account_numbers[0], "50")

    # Step 8: Verify Transaction
    transactions.verify_transaction(account_numbers[0], "100")

    logger.info(f"🎯 {browser.upper()} test completed successfully for {user['username']}")
