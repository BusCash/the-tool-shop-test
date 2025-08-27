# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
import os
from pages.utils.config import BROWSER, IMPLICIT_WAIT_TIME

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' and report.outcome in ('passed', 'failed'):
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')

        os.makedirs('screenshots', exist_ok=True)

        file_name = f'./screenshots/{item.name}_{timestamp}.png'
        driver.save_screenshot(file_name)

        extra.append(pytest_html.extras.image(file_name))
        report.extras = extra

@pytest.fixture(scope="function")
def browser():
    """Provides a WebDriver instance for each test function."""
    driver = None
    if BROWSER.lower() == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    if BROWSER.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif BROWSER.lower() == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)  # Set implicit wait globally
    yield driver
    driver.quit()
