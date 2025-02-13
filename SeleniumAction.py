from selenium.webdriver import ActionChains
from SingletonMeta import SeleniumDriver


class Action:
    __action = ActionChains(SeleniumDriver().get_driver())

    @staticmethod
    def send_keys(text):
        Action.__action.send_keys(text).perform()
