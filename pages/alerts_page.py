from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage
from components.Button import Button


class AlertsPage(BasePage):
    __ALERT_BUTTON = (By.ID, 'alertButton')
    __CONFIRM_BUTTON = (By.ID, 'confirmButton')
    __CONFIRM_RESULT = (By.ID, 'confirmResult')
    __PROMPT_BUTTON = (By.ID, 'promtButton')
    __PROMPT_RESULT = (By.ID, 'promptResult')

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Alerts']"))

    def clickOn_alert_button(self):
        alert_button = Button(self.__ALERT_BUTTON)
        alert_button.click()

    def clickOn_confirm_button(self):
        confirm_button = Button(self.__CONFIRM_BUTTON)
        confirm_button.click()

    def get_confirmResult_text(self):
        confirm_result = BaseElement(self.__CONFIRM_RESULT)
        return confirm_result.get_text()

    def clickOn_prompt_button(self):
        prompt_button = Button(self.__PROMPT_BUTTON)
        prompt_button.click()

    def get_promprResult_text(self):
        prompt_result = BaseElement(self.__PROMPT_RESULT)
        return prompt_result.get_text()
