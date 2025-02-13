from base.base_page import BasePage
from base.base_element import BaseElement
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    __ALERTS = (By.XPATH, '//h5[contains(text(),"Alerts")]')
    __ELEMENTS = (By.XPATH, '//h5[contains(text(),"Elements")]')
    __WIDGETS = (By.XPATH, '//h5[contains(text(),"Widgets")]')

    def __init__(self):
        super().__init__((By.CSS_SELECTOR, 'div.home-banner'))

    def enter_to_AlertsContent(self):
        alerts_link = BaseElement(self.__ALERTS)
        alerts_link.click()

    def enter_to_ElementsContent(self):
        elements_link = BaseElement(self.__ELEMENTS)
        elements_link.click()

    def enter_to_WidgetsContent(self):
        widgets_link = BaseElement(self.__WIDGETS)
        widgets_link.click()