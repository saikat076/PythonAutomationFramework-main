Feature: Google search functionality
    @search
    Scenario: Search for github and scroll to a target element
    Given I open Google homepage
    When I search for "Github"
    #Then I scroll to a target search result element
    #And I take a screenshot