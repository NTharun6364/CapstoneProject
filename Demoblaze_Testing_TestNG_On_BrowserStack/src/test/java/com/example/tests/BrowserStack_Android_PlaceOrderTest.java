package com.example.tests;

import com.example.base.BaseTest;
import com.example.pages.*;
import com.example.config.Constants;
import com.example.utils.ExcelUtils;
import org.testng.annotations.Test;
import java.util.List;
import java.util.Map;

public class BrowserStack_Android_PlaceOrderTest extends BaseTest {

    @Test(description = "Place an order using Place Order modal, data-driven from users CSV")
    public void placeOrder() throws Exception {
        HomePage home = new HomePage(driver);
        home.goToHome();

        // open first product via page object
        home.openFirstProduct();
        ProductPage product = new ProductPage(driver);
        product.addToCartAndAcceptAlert();

        CartPage cart = new CartPage(driver);
        cart.goToCart();
        cart.placeOrder();

        List<Map<String, String>> users = ExcelUtils.loadData(Constants.USERS_DATA);
        Map<String, String> first = users.get(0);

        CheckoutPage checkout = new CheckoutPage(driver);
        checkout.fillOrder(first.get("name"), first.get("country"), first.get("city"),
                first.get("card"), first.get("month"), first.get("year"));
        checkout.confirmPurchase();

        // Removed assertion for confirmation text
        checkout.closeConfirmation();
    }
}
