import pytest
from selenium.webdriver.common.by import By

from base_pages.home_page import HomePage
from base_pages.shop_page import ShopPage
from utilities.custom_logger import LogMaker
from configurations.config import homepageurl


class Test02ShopPage:

    home_page_url = homepageurl

    loggerObj = LogMaker.log_gen("UI")


    @pytest.mark.ui
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_shop(self, setup):

        self.loggerObj.info("=" * 80)
        self.loggerObj.info("Test started: Shop Page Purchase Flow")

        self.driver = setup

        self.loggerObj.info(
            f"Opening Home Page URL: {self.home_page_url}"
        )
        self.driver.get(self.home_page_url)


        # Home Page
        self.loggerObj.info("Initializing Home Page Object")

        self.home_pageO = HomePage(self.driver)

        self.loggerObj.info("Clicking Shop Link Home Page")

        self.home_pageO.click_shop()

        # Shop Page
        self.loggerObj.info("Initializing Shop Page Object")

        self.shopPageO = ShopPage(self.driver)

        self.loggerObj.info("Selecting products from product list")

        self.shopPageO.click_products()

        self.loggerObj.info("Adding selected products to cart")

        self.shopPageO.click_shop_checkout()

        self.loggerObj.info("Proceeding to final checkout")

        self.shopPageO.click_final_checkout()

        self.loggerObj.info("Entering Delivery country")

        self.shopPageO.enter_country_name("ind")

        self.loggerObj.info("Accepting terms & conditions")

        self.shopPageO.click_terms_conditions()

        self.loggerObj.info("Clicking Purchase button")

        self.shopPageO.click_purchase()

        # Validation
        self.loggerObj.info("Validating purchase success message")

        success_message = self.driver.find_element(
            By.CLASS_NAME,
            "alert-success"
        ).text

        self.loggerObj.info(
            f"Success message: {success_message}"
        )

        if "Success! Thank you!" in success_message:

            self.loggerObj.info("Purchase flow completed successfully")

            assert True

        else:

            self.loggerObj.error("Purchase success message validation failed")

            screenshot = "./screenshots/test_success_message_fail.png"

            self.driver.save_screenshot(screenshot)

            self.loggerObj.error(
                f"Screenshot saved: {screenshot}"
            )

            assert False

        self.loggerObj.info("Test Completed: Shop Page Purchase Flow Completed")



