import pytest

from base_pages.miscellaneous_ui_page import MiscellaneousUiPage
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig


class Test04MiscellaneousUiPage:

    misc_ui_page_url = ReadConfig.get_miscellaneous_ui_page_url()
    loggerObj = LogMaker.log_gen()

    @pytest.mark.sanity
    def test_miscellaneous_ui_interaction(self, setup):
        self.loggerObj.info("*********** Test Miscellaneous UI Interaction ***********")

        self.driver = setup
        self.driver.get(self.misc_ui_page_url)

        self.loggerObj.info("*********** Clicking on Radio button ***********")
        self.misc_pageO = MiscellaneousUiPage(self.driver)
        self.misc_pageO.click_radiobutton()

        self.loggerObj.info("*********** Entering a country name under 'Suggestion Class Example' ***********")
        self.misc_pageO.enter_countryname("ger")

        self.loggerObj.info("*********** Clicking on dropdown menu options ***********")
        self.misc_pageO.click_dropdown()

        self.loggerObj.info("*********** Clicking on checkbox options ************")
        self.misc_pageO.click_checkbox()

        self.loggerObj.info("*********** Opening a new window page ************")
        self.loggerObj.info("*********** Verifying if actual title matches with the expected title ************")
        self.loggerObj.info("*********** Close the child window and switch back to parent window ************")
        self.misc_pageO.click_switch_window()

        self.loggerObj.info("*********** Clicking on ALERT pop-up ************")
        self.loggerObj.info("*********** Retrieving 'Alert' pop-up text ************")
        self.misc_pageO.click_alert()

        self.loggerObj.info("*********** Clicking on CONFIRM pop-up ************")
        self.loggerObj.info("*********** Retrieving 'Confirm' pop-up text ************")
        self.misc_pageO.click_confirm()

        self.loggerObj.info("*********** Clicking on HIDE button ************")
        self.misc_pageO.click_hide()

        self.loggerObj.info("*********** Clicking on SHOW button ************")
        self.misc_pageO.click_show()
        self.loggerObj.info("*********** Enter random text on the textbox under HIDE/SHOW Example ************")
        self.misc_pageO.enter_hide_show_name("Emma")

        self.loggerObj.info("*********** Web table fixed header ************")
        self.loggerObj.info("*********** Selecting and printing rows that matches with the position of Engineer ************")
        self.misc_pageO.extract_web_table_rows()

        self.loggerObj.info("*********** Hover the mouse and select TOP option ************")
        self.loggerObj.info("*********** Scrolls to the top the top of the page ************")
        self.misc_pageO.action_mouse_hover()

        self.loggerObj.info("*********** Switch to iFrame Window ************")
        self.loggerObj.info("*********** Extract the internal iFrame page title ************")
        self.loggerObj.info("*********** Switch back to the main window ************")
        self.misc_pageO.action_iFrame_window()



