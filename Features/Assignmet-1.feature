# Created by Mohit at 10-08-2022
Feature: Assignment-1
  1. Login with Valid Credentials
  2. Login with Invalid Credentials & Verify Error Message
  3. After Login switch lightning to classic and classic to lightning
  4. Verify user able to edit any object
  5. Verify user able to add or create custom object

Background:
    Given Open Browser With Salesforce

  @AS01_01
  Scenario: 1. Login with Valid Credentials
    When User Enter Username "msjangra2021@gmail.com"
    And User Enter Password "Salesforce@2804."
    And Click On Login Button
    And I wait 10 seconds

  @AS01_02
  Scenario: 2. Login with Invalid Credentials & Verify Error Message
    When User Enter Username "msjangra2021@gmail.com"
    And User Enter Password "Salesfoczxcrce@2804."
    And Click On Login Button
    Then Verify Error Msg Visible
    And I wait 10 seconds


  @AS01_03
  Scenario: After Login switch lightning to classic and classic to lightning
    When User Enter Username "msjangra2021@gmail.com"
    And User Enter Password "Salesforce@2804."
    And Click On Login Button
    And I wait 10 seconds
    Then Switch Salesforce
    And I wait 10 seconds
