import os.path
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from SingletonMeta import SeleniumDriver
from config_manager import ConfigManager
from selenium.webdriver.support import expected_conditions as EC


class Wait:
    __wait = WebDriverWait(SeleniumDriver().get_driver(), ConfigManager.get_initial_setup().wait_time, ConfigManager.get_initial_setup().poll_frequency)

    @staticmethod
    def until_download(path):
        t = ConfigManager.get_initial_setup().wait_time
        for i in range(t-1):
            time.sleep(1)
            if os.path.exists(path):
                return True
        return False

    @staticmethod
    def presence(locator):
        return Wait.__wait.until(EC.presence_of_element_located(locator))

    @staticmethod
    def visibility(locator):
        return Wait.__wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def element_to_be_clickable(locator):
        return Wait.__wait.until(EC.element_to_be_clickable(locator))

    @staticmethod
    def alert_present():
        return Wait.__wait.until(EC.alert_is_present())

    @staticmethod
    def text_to_be_present_in_element(locator, text):
        return Wait.__wait.until(EC.text_to_be_present_in_element(locator, text))

    @staticmethod
    def get_wait():
        return Wait.__wait