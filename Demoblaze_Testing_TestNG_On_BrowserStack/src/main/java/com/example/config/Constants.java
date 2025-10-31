package com.example.config;

public class Constants {
    // BrowserStack credentials (can also be loaded from properties)
    public static final String BROWSERSTACK_USERNAME = "madhavreddy_pXoxYK";
    public static final String BROWSERSTACK_KEY = "q8LSNTHK4WyFVxQzQdoT";
    public static final String BROWSERSTACK_URL = "http://" + BROWSERSTACK_USERNAME + ":" + BROWSERSTACK_KEY + "@hub-cloud.browserstack.com/wd/hub";

    // Test data path (CSV)
    public static final String USERS_DATA = "src/test/resources/users.csv";

    // Reusable locators (as XPaths / IDs)
    public static final String HOME_FIRST_PRODUCT = "(//a[@class='hrefch'])[1]";
    public static final String ADD_TO_CART = "//a[text()='Add to cart']";
    public static final String CART_LINK = "//a[text()='Cart']";
    public static final String PLACE_ORDER_BUTTON = "//button[text()='Place Order']";
    public static final String ORDER_MODAL_HEADER_ID = "orderModalLabel";
    public static final String PURCHASE_BUTTON = "//button[text()='Purchase']";
    public static final String CONFIRMATION_HEADER_XPATH = "//h2[contains(text(),'Thank you')]";
    public static final String CONFIRMATION_OK_BUTTON = "//button[text()='OK']";

    // Form field IDs inside modal
    public static final String FIELD_NAME = "name";
    public static final String FIELD_COUNTRY = "country";
    public static final String FIELD_CITY = "city";
    public static final String FIELD_CARD = "card";
    public static final String FIELD_MONTH = "month";
    public static final String FIELD_YEAR = "year";
}
