from selenium.webdriver.support import expected_conditions as EC

from SeleniumWait import Wait
from base.base_element import BaseElement


class BasePage:
    def __init__(self, unique_locator):
        self.unique_locator = unique_locator

    @staticmethod
    def open_form(locator):
        form = BaseElement(locator)
        form.click()

    def is_opened(self):
        try:
            Wait.presence(self.unique_locator)
            return True
        except Exception as e:
            print(e)
            return False


