# BrowserStack Place Order - POM Maven Project

This project demonstrates a Page Object Model (PageFactory) implementation of the Place Order test
(https://www.demoblaze.com) running on BrowserStack Android Chrome.

## How to run

1. Edit credentials in `src/test/resources/config.properties` or `src/main/java/com/example/config/Constants.java`.
2. Build & run with Maven:
   mvn clean test

3. Allure results (if configured):
   mvn allure:serve

## Structure
- src/main/java/com/example/config - Constants & config
- src/main/java/com/example/pages  - Page objects (PageFactory)
- src/main/java/com/example/utils  - ExcelUtils (reads CSV)
- src/test/java/com/example/tests  - TestNG tests
