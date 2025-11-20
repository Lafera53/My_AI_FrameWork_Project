Feature: User Login
  As a user
  I want to log into the application
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I open the browser
    When I navigate to the login page
    And I enter username "testuser"
    And I enter password "testpass123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see welcome message