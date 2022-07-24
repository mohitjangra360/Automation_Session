Feature: Logout
  User able to logout
  Background:
    Given Verify Login

  Scenario: Verify user able to logout
    Given Logout
    And User On Login Page