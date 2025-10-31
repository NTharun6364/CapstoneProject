package calculatorapk;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class browserstackWikipediaTest {

    AppiumDriver<MobileElement> driver;

    // ✅ BrowserStack credentials
    public static final String USERNAME = "charanreddyn_yOgNDh";
    public static final String ACCESS_KEY = "kiKQXu8xtzq3jEMJR8Xt";
    public static final String URL = "http://" + USERNAME + ":" + ACCESS_KEY + "@hub-cloud.browserstack.com/wd/hub";

    @BeforeTest
    public void setUp() {
        try {
            DesiredCapabilities caps = new DesiredCapabilities();

            // App uploaded on BrowserStack
            caps.setCapability("app", "bs://bd20f22c8ced00d997c4f163fd63503621647539");

            // BrowserStack device configuration
            Map<String, Object> bstackOptions = new HashMap<>();
            bstackOptions.put("deviceName", "Google Pixel 7");
            bstackOptions.put("osVersion", "13.0");
            bstackOptions.put("projectName", "Wikipedia Appium Test");
            bstackOptions.put("buildName", "BrowserStack Cloud Test");
            bstackOptions.put("sessionName", "Wikipedia - Search SpaceX Page");

            caps.setCapability("bstack:options", bstackOptions);
            caps.setCapability("platformName", "android");
            caps.setCapability("automationName", "UiAutomator2");

            driver = new AppiumDriver<>(new URL(URL), caps);
            System.out.println("✅ Connected to BrowserStack and Wikipedia app launched successfully!");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    public void wikipediaSearchTest() throws InterruptedException {
        String searchQuery = "SpaceX";
        System.out.println("🔍 Starting Wikipedia search for '" + searchQuery + "'...");

        // Wait for the app to load
        Thread.sleep(5000);

        // --- Dismiss onboarding if present ---
        try {
            MobileElement skipButton = driver.findElement(By.id("org.wikipedia.alpha:id/fragment_onboarding_skip_button"));
            skipButton.click();
            System.out.println("🟢 Dismissed onboarding screen");
        } catch (Exception e) {
            System.out.println("No onboarding screen present");
        }

        // Tap on the search bar
        MobileElement searchBar = driver.findElement(By.id("org.wikipedia.alpha:id/search_container"));
        searchBar.click();

        // Type the search query in the search box
        MobileElement searchInput = driver.findElement(By.id("org.wikipedia.alpha:id/search_src_text"));
        searchInput.sendKeys(searchQuery);
        System.out.println("✅ Search query entered: " + searchQuery);

        // Wait for search results
        Thread.sleep(3000);

        // Click on the first search result
        try {
            MobileElement firstResult = driver.findElement(By.xpath(
                "(//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_list_item_title'])[1]"
            ));
            firstResult.click();
            System.out.println("✅ Clicked on the first result for " + searchQuery);
        } catch (Exception e) {
            System.out.println("⚠️ No search results found for " + searchQuery);
            return;
        }

        // Wait until the article title is visible
        WebDriverWait wait = new WebDriverWait(driver, 15);
        try {
            MobileElement articleTitle = (MobileElement) wait.until(
                ExpectedConditions.visibilityOfElementLocated(
                    By.id("org.wikipedia.alpha:id/view_page_title_text")
                )
            );
            System.out.println("📘 Wikipedia article title opened: " + articleTitle.getText());
        } catch (Exception e) {
            System.out.println("⚠️ Unable to locate article title for " + searchQuery);
        }
    }

    @AfterTest
    public void tearDown() {
        if (driver != null) {
            driver.quit();
            System.out.println("✅ BrowserStack session closed successfully!");
        }
    }
}
