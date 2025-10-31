import pytest
from utils.browserstack_driver import create_browserstack_driver

@pytest.fixture(scope="function")
def driver():
    driver = create_browserstack_driver()
    yield driver
    driver.quit()
