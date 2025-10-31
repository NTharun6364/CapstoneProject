# Converted Pytest BrowserStack Android (Appium) Project
This project is a **pytest** rewrite of the uploaded Java POM/Tests. It runs the Demoblaze site on **mobile Chrome via BrowserStack** (Android) using Appium-capable remote WebDriver.

Features:
- Page Object Model (pages/).
- Pytest fixtures (conftest.py) to create a Remote WebDriver session on BrowserStack or local Chrome.
- Reads test data from `tests/users.csv`.
- Allure reporting hooks.
- Python `logging` for logs.

Requirements:
- Python 3.8+
- `pip install -r requirements.txt`
- Set `BROWSERSTACK_USERNAME` and `BROWSERSTACK_KEY` env vars or edit `config.py`.

Run tests:
- `pytest -q --alluredir=allure-results`
- `allure serve allure-results` (to view report)
