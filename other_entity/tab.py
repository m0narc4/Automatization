from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from SingletonMeta import SeleniumDriver
from base.base_page import BasePage


class Tab(BasePage):
    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='This is a sample page']"))

    def switch_to_newTab(self):
        handles = SeleniumDriver().get_driver().window_handles
        SeleniumDriver().switch_to('handle', handles[1])

    def switch_to_original(self):
        handles = SeleniumDriver().get_driver().window_handles
        SeleniumDriver().switch_to('handle', handles[0])

    def close_tab(self):
        SeleniumDriver().close()
        handles = SeleniumDriver().get_driver().window_handles
        SeleniumDriver().get_driver().switch_to.window(handles[0])
