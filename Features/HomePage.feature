# Created by Mohit at 10-08-2022
Feature: Home Page
  # Enter feature description here
  Background:
    Given Open Browser
    And Click On Login Link
    Then User Enter Username
    Then User Enter Password
    Then click on login button
    And I wait 5 seconds

  Scenario: Verify user able to click on Book link after login
    Then click on Book Link

  Scenario: Verify user able to see on Book link after login
    Then click on Book Link