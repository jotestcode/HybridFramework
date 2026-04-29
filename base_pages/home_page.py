from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    textbox_name_xpath = "(//input[@name='name'])[1]"
    textbox_email_css = "input[name='email']"
    textbox_password_id = "exampleInputPassword1"
    dropdown_gender_male_xpath = "//select[@class='form-control']/option[text()='Male']"
    dropdown_gender_female_xpath = "//select[@class='form-control']/option[text()='Male']"
    rdo_employment_status_css = "#inlineRadio2"
    textbox_dob_xpath = "//input[@name='bday']"
    button_submit_xpath = "//input[@type='submit']"

    link_shop_linktext = "Shop"


    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, self.textbox_name_xpath).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_css).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)


    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.dropdown_gender_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.dropdown_gender_female_xpath).click()
        else:
            self.driver.fnd_element(By.XPATH, self.dropdown_gender_male_xpath).click()

    def click_employment_status(self):
        self.driver.find_element(By.CSS_SELECTOR, self.rdo_employment_status_css).click()

    def enter_dob(self, dob):
        self.driver.find_element(By.XPATH, self.textbox_dob_xpath).send_keys(dob)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def click_shop(self):
        self.driver.find_element(By.LINK_TEXT, self.link_shop_linktext).click()






