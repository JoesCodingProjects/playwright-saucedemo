Feature: Sauce Demo User Journey
  As a user
  I want to add an item to the cart and proceed to checkout

  @valid_login
  Scenario: User successfully completes a purchase
    Given the user is on the login page
    When the user logs in with valid credentials
    And the user adds an item to the cart
    And the user proceeds to checkout
    Then the purchase should be successful

  @invalid_login
  Scenario: User fails to log in with incorrect credentials
    Given the user is on the login page
    When the user logs in with invalid credentials
    Then an error message should be displayed
