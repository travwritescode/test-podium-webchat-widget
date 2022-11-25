import pytest
from selenium.webdriver.common.by import By
from utils import wait_for_element_to_be_visible, open_widget


# Smoke Tests
# Test - the web page loads and the widget can be opened and closed
def test_widget_can_be_opened_and_closed(browser):
    # I open the test website
    browser.get("https://demo.podium.tools/qa-webchat-lorw/")
    ## Switch to the iframe that the widget lives on
    widget_iframe = wait_for_element_to_be_visible(browser, By.ID, 'podium-bubble')
    browser.switch_to.frame(widget_iframe)

    # I can see the widget
    widget = wait_for_element_to_be_visible(browser, By.ID, 'podium-website-widget-button')
    
    # I can open the widget
    widget.click()
    ## Switch back to default content so we can find the iframe the search screen lives on
    browser.switch_to.default_content()
    ## Switch to the chat iframe
    modal_iframe = wait_for_element_to_be_visible(browser, By.ID, 'podium-modal')
    browser.switch_to.frame(modal_iframe)

    # I see a search bar
    search_input = wait_for_element_to_be_visible(browser, By.NAME, 'Search Locations')
    assert search_input.is_displayed()
    ## Switch back to the default browser
    browser.switch_to.default_content()

    # and I can close the widget
    browser.switch_to.frame(widget_iframe)
    widget.click()
    assert len(browser.find_elements(By.NAME, 'Search Locations')) < 1

# Test - User input happy path
# leave unfinished per requested spec
def test_hapy_path(browser):
    # I open the test website
    open_widget(browser)

    # Select the first search result to see the compose message screen
    search_results = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_results.click()

    # I fill in the required fields
    wait_for_element_to_be_visible(browser, By.ID, 'ComposeMessage')
    input_name = browser.find_element(By.ID, 'Name')
    input_name.send_keys("Travis Anderson")
    input_phone = browser.find_element(By.ID, 'Mobile Phone')
    input_phone.send_keys("12345678901")
    input_message = browser.find_element(By.ID, 'Message')
    input_message.send_keys("Hello its me I was wondering if you'd like to meet")
    # I do not submit the form per the spec
    button_send = browser.find_element(By.CLASS_NAME, 'SendButton')
    pytest.fail("Finish me!")

# Test - terms link works
# purely a compliance-based test
def test_terms_link_works(browser):
    # I open the test website and open the widget
    open_widget(browser)

    # I click on the terms link
    terms_link = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'terms')
    terms_link.click()
    browser.switch_to.window(browser.window_handles[1])

    assert browser.current_url == 'https://legal.podium.com/#aup-us'


# Test - user can return to location search
# this one will fail
# def test_user_can_return_to_search_and_search_again():
def test_user_can_navigate_between_widget_windows(browser):
    # I open the test website and open the widget
    open_widget(browser)

    # I open the compose message window by clicking a location
    search_results = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_results.click()

    # I can see the compose message window
    back_button = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'SendSmsPage__ArrowIcon')
    assert browser.find_element(By.ID, 'ComposeMessage').isDisplayed()

    # I can return to the search page
    back_button.click()
    wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    assert browser.find_element(By.NAME, 'Search Locations').isDisplayed()
