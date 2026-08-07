import pytest
from selenium.webdriver.common.by import By

from utilities.custom_logger import LogMaker

from configurations.config import homepageurl

from base_pages.home_page import HomePage


class Test01HomePage:

    home_page_url = homepageurl

    loggerObj = LogMaker.log_gen("UI")

    @pytest.mark.ui
    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.loggerObj.info("=" * 80)
        self.loggerObj.info("******* Test Started: Home Page Title Verification *******")

        self.driver = setup

        self.loggerObj.info(f"Opening URL: {self.home_page_url}")
        self.driver.get(self.home_page_url)

        actual_title = self.driver.title
        expected_title = "ProtoCommerce"

        self.loggerObj.info(f"Actual Title: {actual_title}")
        self.loggerObj.info(f"Expected Title: {expected_title}")

        if actual_title == expected_title:

            self.loggerObj.info("******* Home Page Title matches *******")

            assert True

        else:

            self.loggerObj.error("Home Page Title Verification FAILED")

            screenshot = "./screenshots/Test01HomePageTITLE.png"
            self.driver.save_screenshot(screenshot)

            self.loggerObj.error(f"Screenshot saved: {screenshot}")

            assert False


    @pytest.mark.ui
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_home_page(self, setup):

        self.loggerObj.info("=" * 80)
        self.loggerObj.info("******* Test Started: Home Page Form Submission *******")

        self.driver = setup

        self.loggerObj.info(f"Opening URL: {self.home_page_url}")
        self.driver.get(self.home_page_url)

        self.home_pageO = HomePage(self.driver)

        self.loggerObj.info("Entering Name")
        self.home_pageO.enter_name("Emma Watson")

        self.loggerObj.info("Entering Email")
        self.home_pageO.enter_email("emmawatson@gmail.com")

        self.loggerObj.info("Entering Password")
        self.home_pageO.enter_password("Test@1234")

        self.loggerObj.info("Selecting Gender")
        self.home_pageO.select_gender("Female")

        self.loggerObj.info("Selecting Employment status")
        self.home_pageO.click_employment_status()

        self.loggerObj.info("Entering Date of Birth")
        self.home_pageO.enter_dob("01/03/1990")

        self.loggerObj.info("Clicking Submit button")
        self.home_pageO.click_submit()

        actual_success_message = (
            "Success! The Form has been submitted successfully!."
        )
        expected_success_message = self.driver.find_element(
            By.XPATH,
            "//div[@class='alert alert-success alert-dismissible']"
        ).text

        self.loggerObj.info(
            f"Expected Success Message: {actual_success_message}"
        )

        self.loggerObj.info(
            f"Actual Success Message: {expected_success_message}"
        )

        if actual_success_message in expected_success_message:

            self.loggerObj.info(
                "Home Page Form Submission PASSED"
            )

            assert True

        else:

            self.loggerObj.error(
                "Home Page Form Submission FAILED"
            )
            screenshot = "./screenshots/test_success_message_fail.png"
            self.driver.save_screenshot(screenshot)

            self.loggerObj.error(
                f"Screenshot saved: {screenshot}"
            )

            assert False




