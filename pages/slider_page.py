import random

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from components.InputField import InputField
from components.Slider import Slider


class SliderPage(BasePage):
    __SLIDER = (By.XPATH, '//input[@type]')
    __SLIDER_INFO = (By.ID, 'sliderValue')

    __slider = Slider(__SLIDER)

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Slider']"))

    def slide(self, logger):
        number = random.randint(1, 100)
        logger.info('Нажатие на слайдер')
        self.__slider.click()
        logger.info(f'Установка слайдеру значения {number}')
        self.__slider.slide_to(self.__SLIDER_INFO, number)
        return number

    def get_sliderText(self):
        return int(InputField(self.__SLIDER_INFO).get_attribute('value'))