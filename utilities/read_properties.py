import configparser

config = configparser.RawConfigParser()

config.read('./configurations/config.ini')

class ReadConfig:
    @staticmethod
    def get_home_page_url():
        homepageurl = config.get('home page info', 'home_page_url')
        return homepageurl


    @staticmethod
    def get_login_page_url():
        loginpageurl = config.get('login page info', 'login_page_url')
        return loginpageurl

    @staticmethod
    def get_username():
        username = config.get('login page info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login page info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('login page info', 'invalid_username')
        return invalid_username


    @staticmethod
    def get_miscellaneous_ui_page_url():
        miscellaneouspageurl = config.get('miscellaneous UI page info', 'miscellaneous_ui_page_url')
        return miscellaneouspageurl






