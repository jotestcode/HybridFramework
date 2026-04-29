from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:

    link_productLists_xpath = "//div[@class='card h-100']"
    link_checkout_css = "a[class*='btn-primary']"
    button_checkout_css = "button[class='btn btn-success']"
    input_dropdown_id = "country"
    checkbox_terms_conditions_xpath = "//div[@class='checkbox checkbox-primary']"
    button_purchase_xpath = "//input[@value='Purchase']"
    message_success_classname = "alert-success"

    targetItems = ['iphone X', 'Blackberry']


    def __init__(self, driver):
        self.driver = driver


    def click_products(self):
        product_list = self.driver.find_elements(By.XPATH, self.link_productLists_xpath)
        for phones in product_list:
            product_names = phones.find_element(By.XPATH, "div/h4").text
            if product_names in self.targetItems:
                phones.find_element(By.XPATH, "div/button").click()


    def click_shop_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link_checkout_css).click()


    def click_final_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_checkout_css).click()


    def enter_country_name(self, country):
        self.driver.find_element(By.ID, self.input_dropdown_id).send_keys(country)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()


    def click_terms_conditions(self):
        self.driver.find_element(By.XPATH, self.checkbox_terms_conditions_xpath).click()


    def click_purchase(self):
        self.driver.find_element(By.XPATH, self.button_purchase_xpath).click()





