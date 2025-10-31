package com.example.base;

import com.example.config.Constants;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Optional;
import org.testng.annotations.Parameters;
import java.net.URL;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

public class BaseTest {
    protected WebDriver driver;
    protected final Logger log = LogManager.getLogger(this.getClass());

    @Parameters({ "browser", "deviceName", "osVersion" })
    @BeforeMethod(alwaysRun = true)
    public void setUp(@Optional("chrome") String browser,
                      @Optional("Samsung Galaxy S23") String deviceName,
                      @Optional("13.0") String osVersion) throws Exception {
        if ("browserstack".equalsIgnoreCase(browser)) {
            DesiredCapabilities caps = new DesiredCapabilities();
            caps.setCapability("browserName", "chrome");

            Map<String, Object> bstackOptions = new HashMap<>();
            bstackOptions.put("deviceName", deviceName);
            bstackOptions.put("osVersion", osVersion);
            bstackOptions.put("realMobile", "true");
            bstackOptions.put("projectName", "Capstone_Project1");
            bstackOptions.put("buildName", "PlaceOrder-POM-Build");
            bstackOptions.put("sessionName", "PlaceOrder-POM-Session");
            caps.setCapability("bstack:options", bstackOptions);

            driver = new RemoteWebDriver(new URL(Constants.BROWSERSTACK_URL), caps);
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
            log.info("Launched remote driver on BrowserStack");
        } else {
            // Local Chrome fallback (user should have chromedriver on PATH)
            System.setProperty("webdriver.chrome.silentOutput", "true");
            driver = new org.openqa.selenium.chrome.ChromeDriver();
            driver.manage().window().maximize();
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
            log.info("Launched local Chrome driver");
        }
        driver.get(System.getProperty("base.url", "https://www.demoblaze.com/"));
    }

    @AfterMethod(alwaysRun = true)
    public void tearDown() {
        if (driver != null) {
            driver.quit();
            log.info("Session closed");
        }
    }
}
