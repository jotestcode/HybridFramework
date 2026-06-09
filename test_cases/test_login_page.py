import pytest
from selenium.webdriver.common.by import By

from base_pages.login_page import LoginPage
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig


class Test03LoginPage:

    login_page_url = ReadConfig.get_login_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    loggerObj = LogMaker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.loggerObj.info("*********** Test03 Login Page **********")
        self.loggerObj.info("*********** test_valid_Login page Sign In started **********")

        self.driver = setup
        self.driver.get(self.login_page_url)

        self.login_pageO = LoginPage(self.driver)
        self.login_pageO.enter_username(self.username)
        self.login_pageO.enter_password(self.password)
        self.login_pageO.click_terms()
        self.login_pageO.click_login()


    @pytest.mark.regression
    def test_invalid_login(self, setup):
        self.loggerObj.info("*********** test_invalid_login started **********")

        self.driver = setup
        self.driver.get(self.login_page_url)

        self.login_pageO = LoginPage(self.driver)
        self.login_pageO.enter_username(self.invalid_username)
        self.login_pageO.enter_password(self.password)
        self.login_pageO.click_terms()
        self.login_pageO.click_login()

        self.login_pageO.extract_incorrect_username_password()

        incorrect_signin_error_msg = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-danger']").text
        if incorrect_signin_error_msg == "Incorrect username/password.":
            self.loggerObj.info("*********** test_invalid_login error message matched **********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/test_invalid_login.png")
            self.driver.close()
            assert False


    @pytest.mark.sanity
    def test_new_tab_link(self, setup):
        self.loggerObj.info("*********** test_new_tab_link click started **********")
        self.driver = setup
        self.driver.get(self.login_page_url)
        self.login_pageO = LoginPage(self.driver)
        self.login_pageO.click_new_tab_link()

        self.loggerObj.info("*********** switching the window handles to the new tab **********")
        window_open = self.driver.window_handles
        self.driver.switch_to.window(window_open[1])

        self.loggerObj.info("*********** New tab opened **********")
        self.loggerObj.info("********** Retrieving text from the newly opened tab **********")
        new_tab_text = self.driver.find_element(By.XPATH, "//div/p[2]").text
        if "mentor@rahulshettyacademy.com" in new_tab_text:
            assert True
            print(new_tab_text)
            self.loggerObj.info("*********** Text successfully retrieved from the newly opened tab **********")

            self.loggerObj.info("*********** Extracting substring from the retrieved text **********")
            substring_text = new_tab_text.split("at")[1].split("with")[0].strip()
            print(f"Extracted text: {substring_text}")
            self.driver.close()
        else:
            self.loggerObj.info("*********** Failed to retrieve text from the newly opened tab **********")
            self.driver.save_screenshot("./screenshots/test_new_tab_text_msg.png")
            self.driver.close()

        self.loggerObj.info("*********** Switch back to the original window tab **********")
        self.driver.switch_to.window(window_open[0])



