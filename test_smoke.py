from selenium.webdriver.common.by import By
from utility import setUp, tearDown, wait_for_element_to_be_visible, open_widget


# Smoke Tests
# Test - the web page loads and the widget can be opened and closed
def test_widget_can_be_opened_and_closed():
    browser = setUp()

    # I open the test website
    browser.get("https://demo.podium.tools/qa-webchat-lorw/")
    ## Switch to the iframe that the widget lives on
    widget_iframe = wait_for_element_to_be_visible(browser, By.ID, "podium-bubble")
    browser.switch_to.frame(widget_iframe)

    # I can see the widget
    widget = wait_for_element_to_be_visible(browser, By.ID, "podium-website-widget-button")
    
    # I can open the widget
    widget.click()
    ## Switch back to default content so we can find the iframe the search screen lives on
    browser.switch_to.default_content()
    ## Switch to the chat iframe
    modal_iframe = wait_for_element_to_be_visible(browser, By.ID, "podium-modal")
    browser.switch_to.frame(modal_iframe)

    # I see a search bar
    search_input = wait_for_element_to_be_visible(browser, By.NAME, "Search Locations")
    assert search_input.is_displayed()
    ## Switch back to the default browser
    browser.switch_to.default_content()

    # and I can close the widget
    browser.switch_to.frame(widget_iframe)
    widget.click()
    assert len(browser.find_elements(By.NAME, "Search Locations")) < 1

    tearDown(browser)

# Test - User input happy path
# leave unfinished per requested spec
def test_required_contact_fields_activate_send_button():
    browser = setUp()

    # I open the test website
    open_widget(browser)

    # Select the first search result to see the compose message screen
    search_results = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_results.click()

    wait_for_element_to_be_visible(browser, By.ID, 'ComposeMessage')
    # The "send" button should be disabled 

    tearDown(browser)


# Test - terms link works
# purely a compliance-based test


# Test - user can return to location search
# this one will fail
# def test_user_can_return_to_search_and_search_again():


    # Bugs - define expected behavior vs. actual
    # 1. Back button does not work from contact view
    # 2. Pressing enter on the search view clears search field and doesn't perform search
    # 3. I don't think the 'Send' button should be clickable until required fields are filled in
    # 4. Closing and reopening the widget resets progress (based on functionality from other chat widgets)
