import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup(request):
    browser = request.param
    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService())
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver, browser   # ✅ return browser name too
    driver.quit()
