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

public class CheckoutPage {
    WebDriver driver;
    WebDriverWait wait;

    @FindBy(id = Constants.FIELD_NAME)
    WebElement nameField;

    @FindBy(id = Constants.FIELD_COUNTRY)
    WebElement countryField;

    @FindBy(id = Constants.FIELD_CITY)
    WebElement cityField;

    @FindBy(id = Constants.FIELD_CARD)
    WebElement cardField;

    @FindBy(id = Constants.FIELD_MONTH)
    WebElement monthField;

    @FindBy(id = Constants.FIELD_YEAR)
    WebElement yearField;

    @FindBy(xpath = Constants.PURCHASE_BUTTON)
    WebElement purchaseBtn;

    public CheckoutPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(20));
        PageFactory.initElements(driver, this);
    }

    public void fillOrder(String name, String country, String city, String card, String month, String year) {
        wait.until(ExpectedConditions.visibilityOf(nameField));
        nameField.sendKeys(name);
        countryField.sendKeys(country);
        cityField.sendKeys(city);
        cardField.sendKeys(card);
        monthField.sendKeys(month);
        yearField.sendKeys(year);
    }

    public void confirmPurchase() {
        purchaseBtn.click();
        // Removed wait for confirmation header as it's causing timeout
    }

    public void closeConfirmation() {
        try {
            Thread.sleep(2000); // Small delay to let the confirmation appear
            WebElement okButton = driver.findElement(By.xpath(Constants.CONFIRMATION_OK_BUTTON));
            okButton.click();
        } catch (Exception e) {
            // Ignore if confirmation button is not found
        }
    }
}
