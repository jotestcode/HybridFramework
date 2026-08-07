import pytest

from base_pages.miscellaneous_ui_page import MiscellaneousUiPage
from utilities.custom_logger import LogMaker
from configurations.config import miscellaneouspageurl


class Test04MiscellaneousUiPage:

    misc_ui_page_url = miscellaneouspageurl

    loggerObj = LogMaker.log_gen("UI")


    @pytest.mark.ui
    @pytest.mark.sanity
    def test_miscellaneous_ui_interaction(self, setup):

        self.loggerObj.info("=" * 80)
        self.loggerObj.info("Test started: Miscellaneous UI Interaction")

        self.driver = setup

        self.loggerObj.info(
            f"Opening miscellaneous URL: {self.misc_ui_page_url}"
        )
        self.driver.get(self.misc_ui_page_url)

        self.misc_pageO = MiscellaneousUiPage(self.driver)

        self.loggerObj.info("Clicking Radio button")

        self.misc_pageO.click_radiobutton()

        # Auto Suggestion
        self.loggerObj.info("Entering country name under Suggestion Class Example")

        self.misc_pageO.enter_countryname("ger")

        # Dropdown
        self.loggerObj.info("Selecting Dropdown option")

        self.misc_pageO.click_dropdown()

        # Checkbox
        self.loggerObj.info("Selecting checkbox option")

        self.misc_pageO.click_checkbox()

        # Window Handling
        self.loggerObj.info("Opening child window")

        self.loggerObj.info("Verifying child window title")

        self.misc_pageO.click_switch_window()

        # Alert Popup
        self.loggerObj.info("Opening ALERT pop-up")
        self.loggerObj.info("Retrieving 'Alert' pop-up text")

        self.misc_pageO.click_alert()

        # Confirm Popup
        self.loggerObj.info("Opening CONFIRM pop-up")
        self.loggerObj.info("Retrieving 'Confirm' pop-up text")

        self.misc_pageO.click_confirm()

        # HIde / Show Example
        self.loggerObj.info("Clicking on HIDE button")

        self.misc_pageO.click_hide()

        self.loggerObj.info("Clicking on SHOW button")

        self.misc_pageO.click_show()

        self.loggerObj.info("Entering random text in HIDE/SHOW textbox")

        self.misc_pageO.enter_hide_show_name("Emma")

        # Web Table
        self.loggerObj.info("Extracting Web Table rows")
        self.loggerObj.info("Filtering rows based on Engineer position")

        self.misc_pageO.extract_web_table_rows()

        # Mouse Hover
        self.loggerObj.info("Performing Mouse Hover action")
        self.loggerObj.info("Scrolls to the TOP/BEGINNING of the page")

        self.misc_pageO.action_mouse_hover()

        # iFrame
        self.loggerObj.info("Switching to iFrame Window")
        self.loggerObj.info("Extracting iFrame page title")

        self.misc_pageO.action_iFrame_window()

        screenshot = "./screenshots/test_iFrame__window_page.png"
        self.driver.save_screenshot(screenshot)

        self.loggerObj.info(
            f"Screenshot saved to: {screenshot}"
        )

        self.loggerObj.info("Switching back to main window")

        self.loggerObj.info("Miscellaneous UI Page Interaction Test PASSED")






