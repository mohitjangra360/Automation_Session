# Created by rupal at 15/08/2022
Feature: After adding items click on shopping cart btn

  Background:
      Given Open Browser
      And Click On Login Link
      Then User Enter Username
      Then User Enter Password
      Then click on login button
      And I wait 5 seconds
@TC_01
  Scenario: Verify user is able to remove one product from cart
    Then Click on Add to Cart
    And I wait 10 seconds
    Then Click on Add to Cart button of gift card page
    And I wait 5 seconds
    Then Click on shopping cart button
    And I wait 10 seconds
    Then Click on remove checkbox
    And I wait 5 seconds
    Then Click on update cart button
    And I wait 5 seconds

@TC_02
  Scenario: Verify user is able to remove product from cart by directly clicking on shopping cart
    Then Click on shopping cart button
    And I wait 5 seconds
    Then Click on remove checkbox
    And I wait 5 seconds
    Then Click on update cart button
    And I wait 5 seconds


@TC_03
  Scenario: Verify user is able to remove multiple product from cart by directly clicking on shopping cart
    Then Click on shopping cart button
    And I wait 5 seconds
    Then Click on multiple checkbox of product
    And I wait 5 seconds
    Then Click on update cart button
    And I wait 5 seconds