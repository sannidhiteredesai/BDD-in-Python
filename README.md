# BDD for Flask application using Behave & Selenium

This is a very simple Flask application with only login feature. The login feature implemented here is just for demo purpose. The code demonstrates the use of Behave and Selenium for writing acceptance/e2e tests.

## Installation

Use the package manager pip to install dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

Here I am using the chrome web driver so that selenium can interact with Chrome browser. You can download the chrome webdriver compatible with your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the folder as *features/driver/chromedriver.exe*

## Execution
Execute this command on terminal:

```bash
behave
```

This will give the output like:
```shell
Feature: Login # features/login.feature:1
  """
  Login feature will test for successful and failed login attempts
  """
  Scenario: Success test for login          # features/login.feature:6
    Given I navigate to login page          # features/steps/login.py:4
    And I enter valid username and password # features/steps/login.py:13
    When I click on Submit button           # features/steps/login.py:24
    Then login is successful                # features/steps/login.py:33

  Scenario: Failure test for login           # features/login.feature:12
    Given I navigate to login page           # features/steps/login.py:4
    And I enter invalid username or password # features/steps/login.py:43
    When I click on Submit button            # features/steps/login.py:24
    Then login fails                         # features/steps/login.py:54

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
8 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m1.010s

```

If you want to see how actually the chrome window opens and the tests in feature file are executed comment this line from *features/environment.py* and add some *time.sleep()* if required:
```python
chrome_options.add_argument("--headless")
```