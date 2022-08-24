# Created by rupali at 14/08/2022
Feature: Shopping Cart

  Scenario: Verify user is able to click on add to cart button on home page
    Given Open Browser
    And Click On Login Link
    Then User Enter Username
    Then User Enter Password
    Then click on login button
    And I wait 5 seconds
    Then Click on Add to Cart
    And I wait 15 seconds

