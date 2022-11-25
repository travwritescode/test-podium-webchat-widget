import time
from selenium.webdriver.common.by import By
from utility import setUp, tearDown, wait_for_element_to_be_visible, open_widget

# Test - No name
def test_name_required():
    browser = setUp()

    # I open the test website
    open_widget(browser)

    # Select the first search result to see the compose message screen
    search_results = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_results.click()

    wait_for_element_to_be_visible(browser, By.ID, 'ComposeMessage')
    # input_name = browser.find_element(By.ID, 'Name')
    input_phone = browser.find_element(By.ID, 'Mobile Phone')
    input_phone.send_keys("12345678901")
    input_message = browser.find_element(By.ID, 'Message')
    input_message.send_keys("Hello its me I was wondering if you'd like to meet")
    button_send = browser.find_element(By.CLASS_NAME, 'SendButton')
    button_send.click()

    # I should see an error message notifying me a name is required
    error_message = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'TextInput__TextInputError')
    assert error_message.text == 'Name is required'

    tearDown(browser)

# Test - No phone number
def test_phone_number_required():
    browser = setUp()

    # I open the test website
    open_widget(browser)

    # Select the first search result to see the compose message screen
    search_results = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_results.click()

    wait_for_element_to_be_visible(browser, By.ID, 'ComposeMessage')
    input_name = browser.find_element(By.ID, 'Name')
    input_name.send_keys("Travis Anderson")
    input_message = browser.find_element(By.ID, 'Message')
    input_message.send_keys("Hello its me I was wondering if you'd like to meet")
    button_send = browser.find_element(By.CLASS_NAME, 'SendButton')
    button_send.click()

    # I should see an error message notifying me a phone number is required
    error_message = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'TextInput__TextInputError')
    assert error_message.text == 'Mobile phone is required'

    tearDown(browser)

    
# Test - No message
def test_message_required():
    browser = setUp()

    # I open the test website
    open_widget(browser)

    # Select the first search result to see the compose message screen
    search_results = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_results.click()

    wait_for_element_to_be_visible(browser, By.ID, 'ComposeMessage')
    input_name = browser.find_element(By.ID, 'Name')
    input_name.send_keys("Travis Anderson")
    input_phone = browser.find_element(By.ID, 'Mobile Phone')
    input_phone.send_keys("12345678901")
    button_send = browser.find_element(By.CLASS_NAME, 'SendButton')
    button_send.click()

    # I should see an error message notifying me a message is required
    error_message = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'TextInput__TextInputError')
    assert error_message.text == 'Message is required'

    tearDown(browser)


# Test - searching shows best result at top of results
# Should have a test case that fails (pressing enter 
# clears search term but doesn't search)
def test_search_returns_best_result():
    browser = setUp()

    # I open the test website
    open_widget(browser)
    search_reset = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'SearchInput__Reset')
    search_reset.click()
    search_field = browser.find_element(By.NAME, 'Search Locations')
    search_field.send_keys("765")
    # Explicit wait here to allow for search to be processed. Three seconds should be enough
    # time for the spinner to display and then I wait for the results
    time.sleep(3)

    # The first search result should be Scoreboard Sports - Orem
    search_result = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'LocationContainer')
    search_result.click()

    location_name = wait_for_element_to_be_visible(browser, By.CLASS_NAME, 'SendSmsPage__CurrentLocationName')
    assert location_name.text == 'Scoreboard Sports - Orem'

