import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.headless = True
    chromeOptions.add_argument("--log-level=3")
    browser = webdriver.Chrome(options=chromeOptions)

    # Below code for Firefox testing
    # firefoxOptions = webdriver.FirefoxOptions()
    # firefoxOptions.headless = True
    # firefoxOptions.add_argument("--log-level=3")
    # browser = webdriver.Firefox()

    browser.get("https://demo.podium.tools/qa-webchat-lorw/")

    yield browser

    browser.quit()
