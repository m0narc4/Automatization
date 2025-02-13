from SingletonMeta import SeleniumDriver
from base.base_element import BaseElement
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class LinksPage(BasePage):
    __HOME_LINK = (By.ID, 'simpleLink')

    def __init__(self):
        super().__init__((By.XPATH, '//h1[text()="Links"]'))

    def clickOn_homeLink(self):
        homeLink = BaseElement(self.__HOME_LINK)
        homeLink.click()
        SeleniumDriver().switch_to('window', SeleniumDriver().get_handle(1))

    def switch_back(self):
        SeleniumDriver().switch_to('window', SeleniumDriver().get_handle(0))
