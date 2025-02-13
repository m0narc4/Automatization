from selenium.webdriver.common.by import By

from SingletonMeta import SeleniumDriver
from base.base_element import BaseElement
from base.base_page import BasePage


class NestedFramesPage(BasePage):
    __first_frame_ID = 'frame1'
    __child_frame_ID = 0
    __FRAME_BODY = (By.TAG_NAME, 'body')

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Nested Frames']"))

    def get_ParentAndChildFrames_text(self, logger):
        logger.info('Переключение на родительский фрейм')
        SeleniumDriver().switch_to('frame', self.__first_frame_ID)
        logger.info('Получение текста из родительского фрейма')
        parent_frame_text = BaseElement(self.__FRAME_BODY).get_text()

        logger.info('Переключение на дочерний фрейм')
        SeleniumDriver().switch_to('frame', self.__child_frame_ID)
        logger.info('Получение текста из дочернего фрейма')
        child_frame_text = BaseElement(self.__FRAME_BODY).get_text()

        logger.info('Переключение на родительский фрейм')
        SeleniumDriver().switch_to('parent_frame')
        logger.info('Переключение на дефолтный контент')
        SeleniumDriver().switch_to('default_content')
        return parent_frame_text, child_frame_text

