import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.headless = True
    chromeOptions.add_argument("--log-level=3")
    browser = webdriver.Chrome(options=chromeOptions)

    browser.get("https://demo.podium.tools/qa-webchat-lorw/")

    yield browser

    browser.quit()
