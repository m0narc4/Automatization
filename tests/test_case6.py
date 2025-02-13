from SingletonMeta import SeleniumDriver
from pages.datePicker_page import DatePickerPage
from content.main_content import MainPage
import datetime

from content.menu import Menu, MenuItem


def test_DatePicker(logger):
    main_page = MainPage()
    logger.info("Открытие главной страницы")
    SeleniumDriver().open("https://demoqa.com")
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переход на страницу "Widgets"')
    main_page.enter_to_WidgetsContent()

    menu = Menu()
    logger.info('Открытие формы "DatePicker"')
    datePicker_page = DatePickerPage()
    try:
        menu.open(MenuItem.DATE_PICKER.value)
        assert datePicker_page.is_opened() is True, 'Форма с Date Picker не открылась'
    except Exception:
        logger.exception('Форма "Date Picker" не открылась')


    system_date = datetime.datetime.now()
    logger.info('Сверка текущей даты и даты в поле "Select Date"')
    try:
        assert f'{system_date.strftime("%m")}/{system_date.strftime("%d")}/{system_date.year}' == datePicker_page.getDateInfo()
    except AssertionError:
        logger.exception('Текущая дата и дата в поле "Select Date" не совпадают')

    logger.info('Сверка текущей даты и даты в поле "Date And Time"')
    try:
        assert f"{system_date.strftime('%B %#d, %Y %#I:%M %p')}" == datePicker_page.getDateAndTimeInfo()
    except AssertionError:
        logger.exception('Текущая дата и дата в поле "Date And Time" не совпадают')

    logger.info('Начат процесс "задать дату ближайшего 29 февраля"')
    try:
        assert datePicker_page.select_nearestFebruary(logger) == datePicker_page.getDateInfo()
    except AssertionError:
        logger.exception('Данные в поле "Select Date" не поменялись')

    try:
        assert datePicker_page.select_nearestFebruary_DaT(logger) == datePicker_page.getDateAndTimeInfo()
    except AssertionError:
        logger.exception('Данные в поле "Date And Time" не поменялись')