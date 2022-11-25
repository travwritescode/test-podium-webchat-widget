import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--log-level=3")
    browser = webdriver.Chrome(options=options)
    browser.get("https://demo.podium.tools/qa-webchat-lorw/")

    yield browser

    browser.quit()
