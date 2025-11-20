"""
Learning: Browser interaction steps for Playwright automation
Learning: Steps define reusable actions that map to Gherkin keywords (Given, When, Then)
"""

from behave import given, when, then
from playwright.sync_api import expect


@given('I open the browser')
def step_open_browser(context):
    """
    Learning: @given decorator maps this function to 'Given I open the browser' step
    Learning: context object stores shared data between steps
    """
    # Browser and page are initialized in environment.py
    pass


@when('I navigate to "{url}"')
def step_navigate_to_url(context, url):
    """
    Learning: Parameters in quotes become function arguments
    Learning: context.page is the Playwright page object
    """
    context.page.goto(url)


@when('I navigate to the login page')
def step_navigate_to_login(context):
    """
    Learning: Hardcoded URLs can be moved to config for flexibility
    """
    context.page.goto("https://example.com/login")


@then('the page title should contain "{expected_text}"')
def step_verify_title(context, expected_text):
    """
    Learning: Assertions in Then steps verify expected outcomes
    Learning: expect() provides better async handling with Playwright
    """
    expect(context.page).to_have_title(expected_text, timeout=5000)