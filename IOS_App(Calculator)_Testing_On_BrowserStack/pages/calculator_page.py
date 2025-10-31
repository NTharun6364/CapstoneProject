from appium.webdriver.common.appiumby import AppiumBy

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def button(self, name):
        return f'//XCUIElementTypeButton[@name="{name}"]'

    def click_button(self, name):
        self.driver.find_element(AppiumBy.XPATH, self.button(name)).click()
