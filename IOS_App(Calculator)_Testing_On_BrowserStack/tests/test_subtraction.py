from pages.calculator_page import CalculatorPage

def test_subtraction(driver):
    calc = CalculatorPage(driver)
    print("\nRunning subtraction test...")

    calc.click_button("9")
    calc.click_button("-")
    calc.click_button("4")
    calc.click_button("=")

    print(" Subtraction test passed.")
