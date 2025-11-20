# Test Automation Framework

A behavior-driven development (BDD) test automation framework using Python, Playwright, and Behave.

## Overview

This framework provides a structured approach to writing and executing automated browser tests using:
- **Python** - Programming language
- **Playwright** - Modern browser automation
- **Behave** - BDD testing framework with Gherkin syntax
- **Poetry** - Dependency management

## Project Structure

```
test-automation-framework/
├── features/                   # BDD feature files and step definitions
│   ├── steps/                 # Step definition files
│   │   ├── __init__.py
│   │   ├── browser_steps.py   # Browser navigation steps
│   │   └── interaction_steps.py # User interaction steps
│   ├── environment.py         # Behave hooks (setup/teardown)
│   ├── example.feature        # Sample web testing scenarios
│   └── login.feature          # Sample login scenarios
├── tests/                     # Additional test utilities
│   └── __init__.py
├── reports/                   # Test execution reports (generated)
├── behave.ini                 # Behave configuration
├── pyproject.toml            # Poetry dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Prerequisites

- Python 3.9 or higher
- Poetry (for dependency management)
- Git

## Installation

### 1. Install Dependencies

```bash
# Install project dependencies using Poetry
poetry install
```

### 2. Install Playwright Browsers

```bash
# Activate the Poetry virtual environment
poetry shell

# Install Playwright browsers
playwright install chromium
```

## Usage

### Running Tests

**Run all tests:**
```bash
poetry run behave
```

**Run specific feature:**
```bash
poetry run behave features/example.feature
```

**Run specific scenario by name:**
```bash
poetry run behave -n "Navigate to a website"
```

**Run with tags:**
```bash
# Add @smoke tag to scenarios in feature files
poetry run behave --tags=@smoke
```

**Run with custom format:**
```bash
# JSON output
poetry run behave -f json -o reports/results.json

# JUnit XML (for CI/CD)
poetry run behave --junit
```

### Writing Tests

#### 1. Create Feature Files

Feature files use Gherkin syntax and are stored in `features/` directory:

```gherkin
Feature: User Login
  As a user
  I want to log into the application
  So that I can access my account

  Scenario: Successful login
    Given I open the browser
    When I navigate to the login page
    And I enter username "testuser"
    And I enter password "testpass123"
    And I click the login button
    Then I should be redirected to the dashboard
```

#### 2. Create Step Definitions

Step definitions are Python functions in `features/steps/` that implement the Gherkin steps:

```python
from behave import given, when, then

@given('I open the browser')
def step_open_browser(context):
    # Browser is already initialized in environment.py
    pass

@when('I navigate to "{url}"')
def step_navigate(context, url):
    context.page.goto(url)

@then('the page title should contain "{text}"')
def step_verify_title(context, text):
    assert text in context.page.title()
```

#### 3. Use Behave Hooks

The `environment.py` file contains hooks for test setup and teardown:

- `before_all()` - Runs once before all tests
- `before_scenario()` - Runs before each scenario
- `after_scenario()` - Runs after each scenario
- `after_all()` - Runs once after all tests

## Configuration

### Behave Configuration (behave.ini)

```ini
[behave]
format = pretty
color = true
show_timings = true
junit = true
junit_directory = reports
```

### Browser Configuration

Modify `features/environment.py` to customize browser settings:

```python
context.browser = context.playwright.chromium.launch(
    headless=True,      # Run headless for CI/CD
    slow_mo=0,          # Remove delay for faster execution
    args=['--start-maximized']
)
```

## Best Practices

1. **Step Reusability** - Write generic, reusable steps
2. **Page Objects** - Consider implementing Page Object Model for complex applications
3. **Test Data** - Externalize test data using context tables or config files
4. **Reporting** - Use JUnit XML format for CI/CD integration
5. **Parallel Execution** - Use `behave --processes N` for parallel test execution

## Troubleshooting

**Issue: Browser not launching**
```bash
# Reinstall Playwright browsers
poetry run playwright install --force chromium
```

**Issue: Module not found**
```bash
# Ensure you're in the Poetry shell
poetry shell
```

**Issue: Tests failing due to timeouts**
- Increase timeout in step definitions
- Check network connectivity
- Verify element selectors are correct

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Automation

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Poetry
        run: pip install poetry
      - name: Install dependencies
        run: poetry install
      - name: Install Playwright
        run: poetry run playwright install chromium
      - name: Run tests
        run: poetry run behave
      - name: Upload reports
        uses: actions/upload-artifact@v3
        with:
          name: test-reports
          path: reports/
```

## Learning Resources

- [Behave Documentation](https://behave.readthedocs.io/)
- [Playwright Python Documentation](https://playwright.dev/python/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
- [Poetry Documentation](https://python-poetry.org/docs/)

## Contributing

1. Create a feature branch
2. Write tests for new functionality
3. Ensure all tests pass
4. Submit a pull request

## License

MIT License