import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from config import BROWSERSTACK_URL, BASE_URL

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def _browserstack_capabilities():
    """
    Returns the desired capabilities for BrowserStack session.
    Includes project name, build name, and test metadata.
    """
    caps = {
        "browserName": "Chrome",
        "device": "Google Pixel 8",
        "realMobile": "true",
        "os_version": "14.0",
        "name": "Demoblaze PlaceOrder Pytest",  # Test name
        "build": "Demoblaze-Pytest-1",          # Build name
        "project": "capstone_project_python",   # ✅ Added project name
    }
    return caps


@pytest.fixture(scope='function')
def driver(request):
    """
    Pytest fixture to initialize BrowserStack Remote or local Chrome driver.
    Controlled by env var USE_BROWSERSTACK (default: true)
    """
    use_bs = os.getenv('USE_BROWSERSTACK', 'true').lower() in ('1', 'true', 'yes')

    if use_bs:
        caps = _browserstack_capabilities()
        logger.info('🚀 Starting BrowserStack remote session...')
        options = Options()
        for key, value in caps.items():
            options.set_capability(key, value)

        driver = Remote(command_executor=BROWSERSTACK_URL, options=options)
        logger.info(f"✅ BrowserStack session started under project: {caps['project']}")
    else:
        # Local Chrome fallback
        logger.info('🧩 Starting local Chrome browser...')
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    driver.implicitly_wait(10)
    driver.get(os.getenv('BASE_URL', BASE_URL))
    logger.info(f"🌐 Navigated to: {BASE_URL}")

    yield driver

    logger.info('🧹 Quitting WebDriver...')
    try:
        driver.quit()
    except Exception as e:
        logger.warning(f"⚠️ Error quitting driver: {e}")
