from pages.calculator_page import CalculatorPage

def test_addition(driver):
    calc = CalculatorPage(driver)
    print("\nRunning addition test...")

    calc.click_button("2")
    calc.click_button("+")
    calc.click_button("3")
    calc.click_button("=")

    print(" Addition test passed.")
