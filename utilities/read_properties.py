
from configurations.config import (
homepageurl,
loginpageurl,
miscellaneouspageurl,
username,
password,
invalid_username,
apipageUrl,
api_token
)

class ReadConfig:
    @staticmethod
    def get_home_page_url():
        return homepageurl


    @staticmethod
    def get_login_page_url():
        return loginpageurl

    @staticmethod
    def get_username():
        return username

    @staticmethod
    def get_password():
        return password

    @staticmethod
    def get_invalid_username():
        return invalid_username


    @staticmethod
    def get_miscellaneous_ui_page_url():
        return miscellaneouspageurl


    @staticmethod
    def get_api_page_url():
        return apipageUrl


    @staticmethod
    def get_api_token():
        return api_token






