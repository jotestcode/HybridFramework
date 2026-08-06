import pytest
from selenium.webdriver.common.by import By

from base_pages.home_page import HomePage
from base_pages.shop_page import ShopPage
from utilities.custom_logger import LogMaker
from configurations.config import homepageurl


class Test02ShopPage:

    home_page_url = homepageurl
    loggerObj = LogMaker.log_gen()


    @pytest.mark.ui
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_shop(self, setup):
        self.loggerObj.info("*********** Test02ShopPage ***********")
        self.loggerObj.info("*********** SHOP link click from HomePage ***********")

        self.driver = setup
        self.driver.get(self.home_page_url)

        self.home_pageO = HomePage(self.driver)
        self.home_pageO.click_shop()

        self.loggerObj.info("*********** Shop Page *************")
        self.shopPageO = ShopPage(self.driver)

        self.loggerObj.info("*********** Selecting products from the list of items *************")
        self.loggerObj.info("*********** Adding items to cart ***************")
        self.shopPageO.click_products()
        self.shopPageO.click_shop_checkout()
        self.loggerObj.info("*********** Final checkout of items to purchase *************")
        self.shopPageO.click_final_checkout()

        self.loggerObj.info("*********** Enter country name for delivery location *************")
        self.shopPageO.enter_country_name("ind")

        self.loggerObj.info("*********** clicking the checkbox to I terms & conditions *************")
        self.shopPageO.click_terms_conditions()

        self.loggerObj.info("*********** Purchasing the items *************")
        self.shopPageO.click_purchase()

        self.loggerObj.info("*********** Success text message *************")
        success_message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        if "Success! Thank you!" in success_message:
            assert True
            print(f"Success text message: {success_message}")
            self.loggerObj.info("Text message appears successfully *************")
            self.driver.close()
        else:
            self.loggerObj.info("*********** Success text message does not appear *************")
            self.driver.save_screenshot("./screenshots/test_success_message_fail.png")
            self.driver.close()
            assert False



