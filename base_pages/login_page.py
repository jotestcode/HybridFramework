from io import BytesIO

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    textbox_username_id = "username"
    textbox_password_id = "password"
    checkbox_terms_css = "#terms"
    button_login_id = "signInBtn"
    link_new_tab_xpath = "//a[contains(text(), 'Free Access to')]"


    def __init__(self, driver):
        self.driver = driver


    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)


    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)


    def click_terms(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox_terms_css).click()


    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()


    def click_new_tab_link(self):
        self.driver.find_element(By.XPATH, self.link_new_tab_xpath).click()








