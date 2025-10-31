import csv
import os
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_place_order_flow(driver):

    # Load test user data
    data_file = os.path.join(os.path.dirname(__file__), 'users.csv')
    with open(data_file, newline='') as f:
        reader = csv.DictReader(f)
        users = list(reader)
    user = users[0]

    # Start test flow
    home = HomePage(driver)
    home.open_first_product()

    product = ProductPage(driver)
    alert_text = product.add_to_cart_and_accept_alert()

    cart = CartPage(driver)
    cart.go_to_cart()
    cart.place_order()

    checkout = CheckoutPage(driver)
    checkout.fill_order(
        user['name'],
        user['country'],
        user['city'],
        user['card'],
        user['month'],
        user['year']
    )
    checkout.confirm_purchase()

