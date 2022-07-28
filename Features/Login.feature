Feature: Test Login
  Background:
    Given Open Browser

  @smoke
  Scenario: Verify UI of Login page
    Given User On Login Page
    Then I should see sliding image
    And Close Browser

#  @sanity
#  Scenario: Verify UI of Login page 2
#    Given Verify Login
#    And Close Browser



