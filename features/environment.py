"""
Learning: environment.py defines hooks that run before/after scenarios and features
Learning: Hooks manage test setup and teardown for browser automation
"""

from playwright.sync_api import sync_playwright


def before_all(context):
    """
    Learning: before_all runs once before all tests
    Learning: Initialize Playwright at the test suite level
    """
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False,  # Set to True for CI/CD pipelines
        slow_mo=500      # Slows down operations for demo purposes
    )
    print("Browser launched successfully")


def before_scenario(context, scenario):
    """
    Learning: before_scenario runs before each scenario
    Learning: Create fresh browser context and page for test isolation
    """
    context.context = context.browser.new_context(
        viewport={'width': 1920, 'height': 1080}
    )
    context.page = context.context.new_page()
    print(f"\nStarting scenario: {scenario.name}")


def after_scenario(context, scenario):
    """
    Learning: after_scenario runs after each scenario
    Learning: Cleanup resources to prevent memory leaks
    """
    if hasattr(context, 'page'):
        context.page.close()
    if hasattr(context, 'context'):
        context.context.close()

    status = "PASSED" if scenario.status == "passed" else "FAILED"
    print(f"Scenario {scenario.name}: {status}")


def after_all(context):
    """
    Learning: after_all runs once after all tests
    Learning: Close browser and stop Playwright
    """
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
    print("\nBrowser closed and cleanup completed")