import pytest
from selenium.webdriver.common.by import By

from base_pages.login_page import LoginPage
from utilities.custom_logger import LogMaker
from configurations.config import loginpageurl, username, password, invalid_username


class Test03LoginPage:

    login_page_url = loginpageurl

    username = username
    password = password
    invalid_username = invalid_username

    loggerObj = LogMaker.log_gen("UI")


    @pytest.mark.ui
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup):

        self.loggerObj.info("=" * 80)
        self.loggerObj.info("Test started: Valid login test")

        self.driver = setup

        self.loggerObj.info(
            f"Opening Login URL: {self.login_page_url}"
        )
        self.driver.get(self.login_page_url)

        self.login_pageO = LoginPage(self.driver)

        self.loggerObj.info("Entering valid username")
        self.login_pageO.enter_username(self.username)

        self.loggerObj.info("Entering password")
        self.login_pageO.enter_password(self.password)


        self.loggerObj.info("Accepting terms and conditions")
        self.login_pageO.click_terms()

        self.loggerObj.info("Clicking Login button")
        self.login_pageO.click_login()

        self.loggerObj.info(
            "Valid Login Test completed successfully"
        )


    @pytest.mark.ui
    @pytest.mark.regression
    def test_invalid_login(self, setup):

        self.loggerObj.info("=" * 80)
        self.loggerObj.info("Test started: Invalid login test")

        self.driver = setup

        self.loggerObj.info(
            f"Opening Login URL: {self.login_page_url}"
        )
        self.driver.get(self.login_page_url)

        self.login_pageO = LoginPage(self.driver)

        self.loggerObj.info("Entering invalid username")
        self.login_pageO.enter_username(self.invalid_username)

        self.loggerObj.info("Entering invalid password")
        self.login_pageO.enter_password(self.password)

        self.loggerObj.info("Accepting terms and conditions")
        self.login_pageO.click_terms()

        self.loggerObj.info("Clicking Login button")
        self.login_pageO.click_login()

        self.login_pageO.extract_incorrect_username_password()

        incorrect_signin_error_msg = self.driver.find_element(
            By.CSS_SELECTOR,
            "div[class*='alert-danger']"
        ).text

        self.loggerObj.info(
            f"Login error message displayed: {incorrect_signin_error_msg}"
        )

        expected_error_message = "Incorrect username/password."

        if incorrect_signin_error_msg == expected_error_message:

            self.loggerObj.info(
                "Invalid login error message validation PASSED"
            )

            assert True

        else:

            self.loggerObj.error(
                "Invalid login error message validation FAILED"
            )

            screenshot = "./screenshots/test_invalid_login.png"

            self.driver.save_screenshot(screenshot)

            self.loggerObj.info(
                f"Screenshot saved: {screenshot}"
            )

            assert False


    @pytest.mark.ui
    @pytest.mark.sanity
    def test_new_tab_link(self, setup):

        self.loggerObj.info("=" * 80)
        self.loggerObj.info("Test started: New tab link validation")

        self.driver = setup

        self.loggerObj.info(
            f"Opening Login URL: {self.login_page_url}"
        )
        self.driver.get(self.login_page_url)

        self.login_pageO = LoginPage(self.driver)

        self.loggerObj.info("Clicking new tab link")
        self.login_pageO.click_new_tab_link()

        self.loggerObj.info("Switching to newly opened tab")
        window_open = self.driver.window_handles

        self.driver.switch_to.window(window_open[1])

        self.loggerObj.info("New tab opened successfully")

        self.loggerObj.info("Retrieving text from the newly opened tab")

        new_tab_text = self.driver.find_element(
            By.XPATH, "//div/p[2]"
        ).text

        if "mentor@rahulshettyacademy.com" in new_tab_text:

            self.loggerObj.info("New tab text validation PASSED")

            substring_text = (
                new_tab_text
                .split("at")[1]
                .split("with")[0]
                .strip()
            )

            self.loggerObj.info(
                f"Extracted_text: {substring_text}"
            )

            assert True

        else:

            self.loggerObj.error("New tab text validation FAILED")

            screenshot = "./screenshots/test_new_tab_text_msg.png"

            self.driver.save_screenshot(screenshot)

            self.loggerObj.error(
                f"Screenshot saved: {screenshot}"
            )

            assert False

        self.loggerObj.info("Switching back to original tab")

        self.driver.switch_to.window(
            window_open[0]
        )

        self.loggerObj.info("New tab test opened Successfully")
