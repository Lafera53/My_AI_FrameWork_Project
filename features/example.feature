Feature: Web Application Testing
  As a QA engineer
  I want to test web applications
  So that I can ensure quality

  Scenario: Navigate to a website and verify title
    Given I open the browser
    When I navigate to "https://example.com"
    Then the page title should contain "Example"

  Scenario: Search functionality
    Given I open the browser
    When I navigate to "https://www.google.com"
    And I enter "Playwright Python" in the search box
    And I click the search button
    Then I should see search results
    # change for commit