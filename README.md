
## Elastiq.AI Framework




## Introduction

* A test script built with Pytest and Selenium.
* Automates a test case for the Table Search Demo on the Selenium Playground.
* Verifies that searching for "New York" returns 5 entries out of 24 total entries.

## Prerequisites

* Python: Version 3.7 or higher.
* Selenium WebDriver: Installed via pip (pip install selenium).
* Pytest: Installed via pip (pip install pytest).
* Driver: ChromeDriver (ensure the version matches your Chrome browser).

## Test Details

* Purpose: Validate the table search functionality for the query "New York".
Steps:-
* Navigate to the Selenium Playground Table Search Demo.
* Locate the search box and input "New York".
* Verify that the search results display 5 entries out of 24 total entries.


## About Framework

* First Python package 'Pageobject' - Inside this package i have stored Page object model used in Testcase "qa_selenium_test.py".
* Second Python package 'Testcase' - Inside this package i have created 'conftest.py' file to store fixtures. 
* In 'Testcase' package i have created 'qa_selenium_test.py' python file. Under this file i have writen testcase to validate search functionality for Selenium Playground Table Search Demo.

## Querry to run code
* You can use following pytest querry.
( pytest -v -s -p no:warnings )