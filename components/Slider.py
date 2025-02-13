from selenium.webdriver import Keys

from SeleniumAction import Action
from base.base_element import BaseElement
from components.InputField import InputField


class Slider(BaseElement):
    @staticmethod
    def slide_to(locator, endPoint):
        sliderInfo = InputField(locator).get_attribute('value')

        if int(sliderInfo) > endPoint:
            while int(InputField(locator).get_attribute('value')) != endPoint:
                Action.send_keys(Keys.ARROW_LEFT)
        else:
            while int(InputField(locator).get_attribute('value')) != endPoint:
                Action.send_keys(Keys.ARROW_RIGHT)
