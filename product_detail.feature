
Feature: Test for product page

  Scenario: User can select colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can click through colors


  Scenario Outline: Verify that every product on Amazon search results page has a product name and image
    Given Open amazon page
    When Input <product> into Amazon search field
    And Click on the search icon
    Then Verify that every product has a name and image
    Examples:
      |product |
      |mug     |
