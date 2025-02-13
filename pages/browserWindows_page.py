from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage


class BrowserWindowsPage(BasePage):
    __NEW_TAB_BUTTON = (By.ID, 'tabButton')
    __ELEMENTS_PAGE = (By.XPATH, '//div[contains(text(), "Elements")]')

    __NEW_TAB_TEXT = (By.XPATH, '//h1[text()="This is a sample page"]')

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Browser Windows']"))

    def clickOn_newTab_button(self):
        newTab_button = BaseElement(self.__NEW_TAB_BUTTON)
        newTab_button.click()

    def go_to_elementsPage(self):
        elements = BaseElement(self.__ELEMENTS_PAGE)
        elements.click()

