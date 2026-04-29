
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MiscellaneousUiPage:

    radiobutton_radio_xpath = "//input[@value='radio2']"
    textbox_suggestion_id = "autocomplete"
    dropdown_select_id = "dropdown-class-example"
    checkbox_option_id = "checkBoxOption3"
    button_window_id = "openwindow"
    button_alert_id = "alertbtn"
    button_confirm_id = "confirmbtn"
    button_hide_id = "hide-textbox"
    button_show_id = "show-textbox"
    textbox_hide_show_name_id = "displayed-text"
    webtable_table_xpath = "//div[@class='tableFixHead']//table//tbody/tr"
    action_mousehover_id = "mousehover"
    action_top_linktext = "Top"
    iFrame_window_id = "courses-iframe"


    def __init__(self, driver):
        self.driver = driver

    def click_radiobutton(self):
        self.driver.find_element(By.XPATH, self.radiobutton_radio_xpath).click()


    def enter_countryname(self, suggestionname):
        self.driver.find_element(By.ID, self.textbox_suggestion_id).send_keys(suggestionname)
        wait = WebDriverWait(self.driver, 10)
        listed_countries = wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.ui-menu-item")))
        for option in listed_countries:
            if option.text == "Germany":
                option.click()
                break


    def click_dropdown(self):
        self.driver.find_element(By.ID, self.dropdown_select_id).click()


    def click_checkbox(self):
        self.driver.find_element(By.ID, self.checkbox_option_id).click()


    def click_switch_window(self):
        self.driver.find_element(By.ID, self.button_window_id).click()
        windowO = self.driver.window_handles
        self.driver.switch_to.window(windowO[1])
        actual_title = self.driver.title
        if "Foundations of Modern " in actual_title:
            assert True
            print(f"New window TITLE: {actual_title}")
            self.driver.close()
        self.driver.switch_to.window(windowO[0])


    def click_alert(self):
        self.driver.find_element(By.ID, self.button_alert_id).click()
        alert_popup = self.driver.switch_to.alert
        text_alert = alert_popup.text
        print(f"ALERT text: {text_alert}")
        alert_popup.accept()


    def click_confirm(self):
        self.driver.find_element(By.ID, self.button_confirm_id).click()
        confirm_popup = self.driver.switch_to.alert
        text_confirm = confirm_popup.text
        print(f"CONFIRM text: {text_confirm}")
        confirm_popup.dismiss()


    def click_hide(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.driver.find_element(By.ID, self.button_hide_id).click()


    def click_show(self):
        self.driver.find_element(By.ID, self.button_show_id).click()


    def enter_hide_show_name(self, hide_show_name):
        self.driver.find_element(By.ID, self.textbox_hide_show_name_id).send_keys(hide_show_name)


    def extract_web_table_rows(self):
        web_table = self.driver.find_elements(By.XPATH, self.webtable_table_xpath)
        for row in web_table:
            if "Engineer" in row.text:
                columns = row.find_elements(By.TAG_NAME, "td")
                row_data = [col.text for col in columns]
                print(f"No. of columns: {len(row_data)}")
                print(row_data)


    def action_mouse_hover(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.ID, self.action_mousehover_id))
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, self.action_mousehover_id)).perform()
        action.click(self.driver.find_element(By.LINK_TEXT, self.action_top_linktext)).pause(2).perform()


    def action_iFrame_window(self):
        iFrame = self.driver.find_element(By.ID, self.iFrame_window_id)
        ActionChains(self.driver).scroll_to_element(iFrame).pause(3).perform()

        self.driver.switch_to.frame(iFrame)
        iFrame_title = self.driver.find_element(By.TAG_NAME, "title").get_attribute("textContent")
        print(f"Internal iFrame title: {iFrame_title}")

        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, 0);")










