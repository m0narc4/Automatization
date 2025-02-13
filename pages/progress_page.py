from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from base.base_element import BaseElement
from base.base_page import BasePage


class ProgressBarPage(BasePage):
    __PROGRESS_BAR = (By.CSS_SELECTOR, 'div[role="progressbar"]')
    __START_STOP_BUTTON = (By.ID, 'startStopButton')

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Progress Bar']"))

    def check_progress(self, age, logger):
        button = BaseElement(self.__START_STOP_BUTTON)
        logger.info('Нажатие на кнопку "Start"')
        button.click()

        try:
            while BaseElement(self.__PROGRESS_BAR).get_text() != '100%':
                if BaseElement(self.__PROGRESS_BAR).get_text() == str(age) + '%':
                    logger.info('Нажатие на кнопку "Stop"')
                    button.click()
                    break
            if BaseElement(self.__PROGRESS_BAR).get_text() == '100%':
                raise TimeoutException
        except TimeoutException:
            logger.exception('Шкала не остановилась на нужном значении')

        progress_bar = BaseElement(self.__PROGRESS_BAR)
        logger.info('Получение результата')
        result = int(progress_bar.get_text()[:-1])
        return result

