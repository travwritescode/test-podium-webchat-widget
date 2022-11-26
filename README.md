# Podium Webchat Widget Test Suite
Below I have outlined my test suite for the Podium webchat widget. I have broken the test cases into smoke and regression cases.
The smoke tests will test the basic functionality of the widget, making sure each screen can be reached and happy path (incomplete in this case) is
satisfied. The regression tests break down into finer details testing more in depth like required fields and the search functionality.

## Smoke Tests
1. Widget Can Be Opened and Closed
   - This test is the most basic functionality, making sure the widget loads, it can be opened, and it can be closed.
2. Happy Path
   - The basic happy path test of filling out all required fields and submitting the form. I am leaving this one unfinishedaccording to the spec document.
   - This is a failing test on purpose representing an unfinished test case.
3. Use Terms Link Works
   - I am unsure of the compliance implications for this section being required or not, so I have included this test to ensurethe link to the use terms works.
4. User Can Navigate Between Widget Windows
   - This test verifies the user can get to and from each window on the widget
   - This is a failing test due to a bug. Maintaining TDD principles I would leave this as a failing test until it is fixed on the development side.

## Regression Tests
1. Name Required
   - Ensure the user cannot submit a form without including their name.
2. Phone Number Required
   - Ensure the user cannot submit a form without including their phone number.
3. Message Required
   - Ensure the user cannot submit a form without including a message.
4. Search Returns Best Result First
   - Searching for a term which is included in part of the location data should return that location as the first search result.

### Bugs
1. Back button on compose message window does not work
   - Expected Behavior: When I am on the compose message window and I click the back arrow I should return to the search window.
   - Actual Behavior: When I click the back arrow, the window refreshes but remains on the compose message window.
2. Pressing enter on location search window does not perform search
   - Expected Behavior: When I type a search term in the location search field and press enter, the location is searched and the best result is returned at the top of the search results
   - Actual Behavior: When I type a search term in the location search field and press enter, the search field is cleared and the search is not performed
3. Incomplete phone number is submittable
   - Expected Behavior: I must fill in a complete, 10-digit phone number in order to submit a message.
   - Actual Behavior: I am able to submit a message with a phone number containing only 9 digits
4. Minor: Send button should be disabled until all required fields are filled
   - Expected Behavior: On the compose message window, the Send button is disabled until all required fields are filled
   - Actual Behavior: The Send button has a faded style but is still clickable
   - This is simply to maintain a consistent user experience
5. Minor: Closing and reopening the widget resets progress
   - Expected Behavior: When I close and reopen the chat widget I should return to the screen I was previously on
   - Actual Behavior: When I close and reopen the chat widget my progress is reset
   - Expected behavior based on investigation of other chat widgets in use on other websites

# Running the Tests
I built these tests to run on Chrome. I don't have experience Dockerizing Selenium tests and the more I researched this the less I felt confident handing off a Dockerized test job. I have included steps for running these tests locally below:
#### Prerequisites:
  - If you don't have Google Chrome installed, install it. Check your Chrome version by typing `chrome://system/` into the address bar in Chrome
  - Download the ChromeDriver version that is the same as your Chrome version from [this page](https://sites.google.com/chromium.org/driver/?pli=1)
  - Put ChromeDriver in your System's PATH. For Mac users the `/usr/local/bin` folder will work. For Windows the `C:\Windows` folder is good.
#### With the Repo
  - Clone the repo
  - Open you terminal and navigate to the parent directory
  - Run pip install for requirements file: `pip install -r requirements.txt`
  - To execute the tests run: `pytest -v -s --reruns 3`. I encountered some flaky tests and use a pytest plugin to rerun failed tests 3 times.
  - I have included code for running the tests against Firefox in the file `conftest.py`. This is also where you may flip the boolean that controls headless execution.
