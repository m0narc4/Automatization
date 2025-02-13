from selenium.webdriver.common.by import By

from SingletonMeta import SeleniumDriver
from base.base_element import BaseElement
from base.base_page import BasePage


class FramesPage(BasePage):
    __first_frame_ID = 'frame1'
    __second_frame_ID = 'frame2'
    __FRAME_BODY = (By.TAG_NAME, 'body')

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Frames']"))

    def get_FirstAndSecondFrames_text(self, logger):
        logger.info('Переключение на первый фрейм')
        SeleniumDriver().switch_to('frame', self.__first_frame_ID)
        logger.info('Получение текста из первого фрейма')
        first_frame_text = BaseElement(self.__FRAME_BODY).get_text()

        logger.info('Переключение на дефолтный контент')
        SeleniumDriver().switch_to('default_content')
        logger.info('Переключение на второй фрейм')
        SeleniumDriver().switch_to('frame', self.__second_frame_ID)
        logger.info('Получение текста из второго фрейма')
        second_frame_text = BaseElement(self.__FRAME_BODY).get_text()
        return first_frame_text, second_frame_text