from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from SeleniumWait import Wait
from base.base_element import BaseElement
from base.base_page import BasePage
from components.InputField import InputField


class DatePickerPage(BasePage):
    __SELECT_DATE = (By.ID, 'datePickerMonthYearInput')
    __DATE_AND_TIME = (By.ID, 'dateAndTimePickerInput')
    __SELECT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    __DAT_YEAR_SELECT_ARROW = (By.XPATH, "//span[contains(@class, 'year') and contains(@class, 'arrow')]")
    __FEBRUARY_29 = (By.XPATH, "//div[@role='option' and text()='29']")

    __select_date_field = InputField(__SELECT_DATE)
    __date_and_time_field = InputField(__DATE_AND_TIME)

    def __init__(self):
        super().__init__((By.XPATH, "//h1[text()='Date Picker']"))
        self.__nearestFebruary = None

    def is_leapYear(self, year):
        if year % 4 == 0:
            return True
        else:
            return False

    def get_nearestFebruary(self):
        year = int(self.__select_date_field.get_attribute('value')[-4:])
        while True:
            year += 1
            if self.is_leapYear(year):
                return year

    def select_nearestFebruary(self, logger):
        logger.info('Расчёт ближайшего 29 февраля')
        self.__nearestFebruary = self.get_nearestFebruary()
        logger.info('Нажатие на поле "Select Date"')
        self.__select_date_field.click()
        logger.info('Выбор ближайшего года, где есть 29 февраля, в поле "Select Date"')
        year_select = Select(Wait.element_to_be_clickable(self.__SELECT_YEAR))
        year_select.select_by_value(f'{self.__nearestFebruary}')
        logger.info('Выбор дня')
        BaseElement(self.__FEBRUARY_29).click()
        logger.info('Нажатие на поле "Date And Time"')
        return self.__select_date_field.get_attribute('value')

    
    def select_nearestFebruary_DaT(self, logger):
        self.__date_and_time_field.click()
        DaT_year_select = BaseElement(self.__DAT_YEAR_SELECT_ARROW)
        logger.info('Клик на выбор года')
        DaT_year_select.click()
        DAT_SELECT_YEAR = (By.XPATH, f"//div[@class='react-datepicker__year-option' and text()='{self.__nearestFebruary}']")
        select_year = BaseElement(DAT_SELECT_YEAR)
        logger.info('Выбор ближайшего года, где есть 29 февраля')
        select_year.click()

        BaseElement(self.__FEBRUARY_29).click()
        logger.info('Выбор случайного времени суток')
        BaseElement((By.XPATH, "//li[text()='19:00']")).click()
        return self.__date_and_time_field.get_attribute('value')

    def getDateInfo(self):
        return self.__select_date_field.get_attribute('value')

    def getDateAndTimeInfo(self):
        return self.__date_and_time_field.get_attribute('value')
