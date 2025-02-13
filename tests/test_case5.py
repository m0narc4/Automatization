from pages.progress_page import ProgressBarPage
from pages.slider_page import SliderPage
from content.main_content import MainPage
from SingletonMeta import SeleniumDriver
from data_loader import DataLoader
from content.menu import Menu, MenuItem
from test_data_manager import TestDataManager


def test_ProgressBar_and_Slider(logger):
    age = TestDataManager.get_engineer_age().age

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
    logger.info('Открытие формы "Slider"')
    slider_page = SliderPage()
    try:
        menu.open(MenuItem.SLIDER.value)
        assert slider_page.is_opened() is True
    except Exception:
        logger.exception('Форма "Slider" не открылась')

    try:
        assert slider_page.is_opened() is True
    except AssertionError:
        logger.exception('Форма "Slider" не открылась')

    try:
        assert slider_page.slide(logger) == slider_page.get_sliderText()
        logger.info("Нужное значение установлено")
    except AssertionError:
        logger.exception('Значения не совпадают')

    logger.info('Открытие формы "Progress Bar"')
    progressBar_page = ProgressBarPage()
    try:
        menu.open(MenuItem.PROGRESS_BAR.value)
        assert progressBar_page.is_opened() is True, 'Форма Progress Bar не открылась'
    except Exception:
        logger.exception(logger.exception('Форма "Progress Bar" не открылась'))


    result = progressBar_page.check_progress(age, logger)
    try:
        assert age - 2 <= result <= age + 2
        logger.info('Результат в пределах допустимого')
    except AssertionError:
        logger.exception('Некорректный ответ')
