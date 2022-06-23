Feature: Test Login
  Background:
    Given Launch Browser
  @smoke
  Scenario: Verify UI of Login page
    Given User On Login Page
    And Close Browser


  @sanity
  Scenario: Verify UI of Login page2
    Given Verify Login
    And Close Browser
