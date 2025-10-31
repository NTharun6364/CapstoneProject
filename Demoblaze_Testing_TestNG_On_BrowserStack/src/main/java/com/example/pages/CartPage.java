package com.example.pages;

import com.example.config.Constants;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class CartPage {
    WebDriver driver;
    WebDriverWait wait;

    @FindBy(xpath = Constants.CART_LINK)
    WebElement cartLink;

    @FindBy(xpath = Constants.PLACE_ORDER_BUTTON)
    WebElement placeOrderBtn;

    public CartPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(20));
        PageFactory.initElements(driver, this);
    }

    public void goToCart() {
        wait.until(ExpectedConditions.elementToBeClickable(cartLink));
        cartLink.click();
        wait.until(ExpectedConditions.elementToBeClickable(placeOrderBtn));
    }

    public void placeOrder() {
        wait.until(ExpectedConditions.elementToBeClickable(placeOrderBtn));
        placeOrderBtn.click();
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id(Constants.ORDER_MODAL_HEADER_ID)));
    }
}
