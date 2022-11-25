import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

def open_widget(browser):
    ## Switch to the iframe that the widget lives on
    widget_iframe = wait_for_element_to_be_visible(browser, By.ID, "podium-bubble")
    browser.switch_to.frame(widget_iframe)
    widget = wait_for_element_to_be_visible(browser, By.ID, "podium-website-widget-button")
    widget.click()

    browser.switch_to.default_content()
    ## Switch to the chat iframe
    modal_iframe = wait_for_element_to_be_visible(browser, By.ID, "podium-modal")
    browser.switch_to.frame(modal_iframe)

def wait_for_element_to_be_visible(browser, by, path):
    start_time = time.time()
    while True:
        try:
            element = browser.find_element(by, path)
            return element
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
