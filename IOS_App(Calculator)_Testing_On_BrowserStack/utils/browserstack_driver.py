import os
from appium import webdriver
from appium.options.common import AppiumOptions
from dotenv import load_dotenv

def create_browserstack_driver():
    load_dotenv()

    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    app_url = os.getenv("BROWSERSTACK_APP_URL")

    if not username or not access_key or not app_url:
        raise Exception("Missing BrowserStack credentials or app URL in .env file")

    options = AppiumOptions()
    options.set_capability("platformName", "iOS")
    options.set_capability("deviceName", "iPhone 15")
    options.set_capability("platformVersion", "17")
    options.set_capability("app", app_url)
    options.set_capability("build", "Calculator-iOS-Pytest")
    options.set_capability("name", "Calculator Test Run")
    options.set_capability("browserstack.debug", True)
    options.set_capability("browserstack.networkLogs", True)

    driver = webdriver.Remote(
        command_executor=f"http://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    return driver
