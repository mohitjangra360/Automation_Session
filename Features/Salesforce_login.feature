# Created by Mohit at 05-08-2022
Feature: Login Page
  user verify logo


@sanity
  Scenario: User able to see logo is visible
    Given Open Browser
    Then  click on login

@smoke
  Scenario: User able to see logo is visible
    Given Open Browser
    Then logo is visible

    # Enter steps here