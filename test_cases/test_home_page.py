import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig
from base_pages.home_page import HomePage


class Test01HomePage:

    home_page_url = ReadConfig.get_home_page_url()
    loggerObj = LogMaker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.loggerObj.info("******** Test01HomePage **********")
        self.loggerObj.info("******* Verification of Home page TITLE *******")

        self.driver = setup
        self.driver.get(self.home_page_url)
        actual_title = self.driver.title
        expected_title = "ProtoCommerce"

        if actual_title == expected_title:
            self.loggerObj.info("******* TITLE matches *******")
            print(f'Home Page Title: {actual_title}')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/Test01HomePageTITLE.png")
            self.loggerObj.info("******* TITLE does not match *******")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_home_page(self, setup):
        self.loggerObj.info("******* Test_Home page info **********")
        self.driver = setup
        self.driver.get(self.home_page_url)

        self.home_pageO = HomePage(self.driver)
        self.home_pageO.enter_name("Emma Watson")
        self.home_pageO.enter_email("emmawatson@gmail.com")
        self.home_pageO.enter_password("Test@1234")
        self.home_pageO.select_gender("Female")
        self.home_pageO.click_employment_status()
        self.home_pageO.enter_dob("01/03/1990")
        self.home_pageO.click_submit()

        actual_success_message = "Success! The Form has been submitted successfully!."
        expected_success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

        if actual_success_message in expected_success_message:
            assert True
            self.loggerObj.info("******* SUCCESS message matches *******")
            print(f'Success message: {expected_success_message}')
            self.driver.close()
        else:
            self.loggerObj.info("******* SUCCESS message does not match *******")
            self.driver.screenshot("./screenshots/test_success_message_fail.png")
            self.driver.close()
            assert False






