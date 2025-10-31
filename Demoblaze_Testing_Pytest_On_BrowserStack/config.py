import os

# BrowserStack credentials (defaults can be overridden with env vars)
BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME', 'madhavreddy_pXoxYK')
BROWSERSTACK_KEY = os.getenv('BROWSERSTACK_KEY', 'q8LSNTHK4WyFVxQzQdoT')

BROWSERSTACK_URL = f"http://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_KEY}@hub-cloud.browserstack.com/wd/hub"

BASE_URL = "https://www.demoblaze.com/"

# XPaths / IDs used in the pages (converted from Java Constants)
HOME_FIRST_PRODUCT = "(//a[@class='hrefch'])[1]"
ADD_TO_CART = "//a[text()='Add to cart']"
CART_LINK = "//a[text()='Cart']"
PLACE_ORDER_BUTTON = "//button[text()='Place Order']"
PURCHASE_BUTTON = "//button[text()='Purchase']"
CONFIRMATION_HEADER_XPATH = "//h2[contains(text(),'Thank you')]"
CONFIRMATION_OK_BUTTON = "//button[text()='OK']"

FIELD_NAME = "name"
FIELD_COUNTRY = "country"
FIELD_CITY = "city"
FIELD_CARD = "card"
FIELD_MONTH = "month"
FIELD_YEAR = "year"

# ✅ Added missing locators for checkout modal (keep naming pattern consistent)
NAME_INPUT = f"//input[@id='{FIELD_NAME}']"
COUNTRY_INPUT = f"//input[@id='{FIELD_COUNTRY}']"
CITY_INPUT = f"//input[@id='{FIELD_CITY}']"
CARD_INPUT = f"//input[@id='{FIELD_CARD}']"
MONTH_INPUT = f"//input[@id='{FIELD_MONTH}']"
YEAR_INPUT = f"//input[@id='{FIELD_YEAR}']"


