# Podium Webchat Widget Test Suite
Below I have outlined my test suite for the Podium webchat widget. I have broken the test cases into smoke and regression cases.
The smoke tests will test the basic functionality of the widget, making sure each screen can be reached and happy path (incomplete in this case) is
satisfied. The regression tests break down into finer details testing more in depth like required fields and the search functionality.

## Smoke Tests
**1. Widget Can Be Opened and Closed**
    - This test is the most basic functionality, making sure the widget loads, it can be opened, and it can be closed.
**2. Happy Path**
    - The basic happy path test of filling out all required fields and submitting the form. I am leaving this one unfinishedaccording to the spec document.
**3. Use Terms Link Works**
    - I am unsure of the compliance implications for this section being required or not, so I have included this test to ensurethe link to the use terms works.

## Regression Tests
**1. Name Required**
    - Ensure the user cannot submit a form without including their name.
**2. Phone Number Required**
    - Ensure the user cannot submit a form without including their phone number.
**3. Message Required**
    - Ensure the user cannot submit a form without including a message.
**4. Search Returns Best Result First**
    - Searching for a term which is included in part of the location data should return that location as the first search result.

### Bugs
**1. Back button on compose message window does not work**
    - Expected Behavior: When I am on the compose message window and I click the back arrow I should return to the search window.
    - Actual Behavior: When I click the back arrow, the window refreshes but remains on the compose message window.
**2. Pressing enter on location search window does not perform search**
   - Expected Behavior: When I type a search term in the location search field and press enter, the location is searched and the best result is returned at the top of the search results
    - Actual Behavior: When I type a search term in the location search field and press enter, the search field is cleared and the search is not performed
**3. Minor: Send button should be disabled until all required fields are filled**
    - Expected Behavior: On the compose message window, the Send button is disabled until all required fields are filled
    - Actual Behavior: The Send button has a faded style but is still clickable
    - This is simply to maintain a consistent user experience
**4. Minor: Closing and reopening the widget resets progress**
    - Expected Behavior: When I close and reopen the chat widget I should return to the screen I was previously on
    - Actual Behavior: When I close and reopen the chat widget my progress is reset
    - Expected behavior based on investigation of other chat widgets in use on other websites
