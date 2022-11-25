# Podium Webchat Widget Test Suite
Below I have outlined my test suite for the Podium webchat widget. I have broken the test cases into smoke and regression cases.
The smoke tests will test the basic functionality of the widget, making sure each screen can be reached and happy path (incomplete in this case) is
satisfied. The regression tests break down into finer details testing more in depth like required fields and the search functionality.

## Smoke Tests
1. Widget Can Be Opened and Closed
This test is the most basic functionality, making sure the widget loads, it can be opened, and it can be closed.
2. Happy Path
The basic happy path test of filling out all required fields and submitting the form. I am leaving this one unfinished
according to the spec document.
3. Use Terms Link Works
I am unsure of the compliance implications for this section being required or not, so I have included this test to ensure
the link to the use terms works.

## Regression Tests
1. Name Required
Ensure the user cannot submit a form without including their name.
2. Phone Number Required
Ensure the user cannot submit a form without including their phone number.
3. Message Required
Ensure the user cannot submit a form without including a message.
4. Search Returns Best Result First
Searching for a term which is included in part of the location data should return that location as the first search result.

### Bugs
