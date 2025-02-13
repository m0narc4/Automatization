from selenium.common import TimeoutException, NoAlertPresentException

from SeleniumWait import Wait
from SingletonMeta import SeleniumDriver


class Alert:
    def accept(self):
        self.find_element().accept()

    def send_keys(self, text):
        self.find_element().send_keys(text)

    @staticmethod
    def find_element():
        try:
            alert = Wait.alert_present()
            return alert
        except TimeoutException:
            return None

    @staticmethod
    def switch():
        try:
            SeleniumDriver().switch_to('alert')
        except NoAlertPresentException as e:
            print(e)

    def get_text(self):
        return self.find_element().text

    @staticmethod
    def is_displayed():
        try:
            Wait.alert_present()
            return True
        except TimeoutException:
            return False

    @staticmethod
    def is_closed():
        try:
            SeleniumDriver().switch_to('alert')
            return False
        except NoAlertPresentException:
            return True