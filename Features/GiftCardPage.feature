# Created by rupal at 14/08/2022
Feature: Add to cart btn on gift page
  enter valid recipient name and email and click on add to cart btn

  Scenario: Verify user is able to click on add to cart button of gift page
    Given Open Browser
    And Click On Login Link
    Then User Enter Username
    Then User Enter Password
    Then click on login button
    Then Click on Add to Cart
    And I wait 5 seconds
    Then Click on Add to Cart button of gift card page
    And I wait 10 seconds
