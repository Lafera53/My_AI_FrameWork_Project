"""
Learning: User interaction steps for form inputs and button clicks
Learning: Separate step files by functionality for better maintainability
"""

from behave import when, then
from playwright.sync_api import expect


@when('I enter "{text}" in the search box')
def step_enter_search_text(context, text):
    """
    Learning: Use descriptive selectors for better test readability
    Learning: Playwright auto-waits for elements to be actionable
    """
    context.page.fill('input[name="q"]', text)


@when('I click the search button')
def step_click_search(context):
    """
    Learning: Clicking triggers navigation, Playwright waits automatically
    """
    context.page.click('button[type="submit"]')


@when('I enter username "{username}"')
def step_enter_username(context, username):
    """
    Learning: Store selectors as constants for reusability
    """
    context.page.fill('input[name="username"]', username)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    """
    Learning: Sensitive data should be externalized in real tests
    """
    context.page.fill('input[name="password"]', password)


@when('I click the login button')
def step_click_login(context):
    """
    Learning: Wait for navigation after login clicks
    """
    context.page.click('button[type="submit"]')


@then('I should see search results')
def step_verify_search_results(context):
    """
    Learning: Verify elements exist using locators
    """
    expect(context.page.locator('#search')).to_be_visible()


@then('I should be redirected to the dashboard')
def step_verify_dashboard_redirect(context):
    """
    Learning: URL verification ensures proper navigation
    """
    expect(context.page).to_have_url('https://example.com/dashboard', timeout=5000)


@then('I should see welcome message')
def step_verify_welcome_message(context):
    """
    Learning: Text content verification validates UI feedback
    """
    expect(context.page.locator('text=Welcome')).to_be_visible()