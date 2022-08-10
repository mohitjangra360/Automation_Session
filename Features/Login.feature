# Created by Mohit at 10-08-2022
Feature: Login
  verify login UI and functionality

  @LP_01
  Scenario: Verify user able to login with valid data
    Given Open Browser
    And Click On Login Link
    Then User Enter Username
    And I wait 2 seconds
    Then User Enter Password
    And I wait 2 seconds
    Then click on login button
    Then I wait 10 seconds



