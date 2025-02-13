from pages.frames_page import FramesPage
from pages.nestedFrames_page import NestedFramesPage
from content.main_content import MainPage
from SingletonMeta import SeleniumDriver
from content.menu import Menu, MenuItem
from test_data_manager import TestDataManager


def test_Frames(logger):
    test_data = TestDataManager.get_test_case_data().test_case2
    iframes = TestDataManager.get_frames_data(test_data)

    main_page = MainPage()
    logger.info("Открытие главной страницы")
    SeleniumDriver().open("https://demoqa.com/")
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переход на страницу "Alerts"')
    main_page.enter_to_AlertsContent()

    menu = Menu()
    logger.info('Открытие формы "Nested Frames"')
    nestedFrames_page = NestedFramesPage()
    try:
        menu.open(MenuItem.NESTED_FRAMES.value)
        assert nestedFrames_page.is_opened() is True
    except Exception:
        logger.exception('Форма "Nested Frames" не открылась')

    logger.info('Получение текста из двух фреймов')
    value1, value2 = nestedFrames_page.get_ParentAndChildFrames_text(logger)
    try:
        assert value1 == iframes.ParentFrameText and value2 == iframes.Child_IFrameText
    except AssertionError:
        logger.exception('Данные не совпадают с теми, что представлены в parent frame и child iframe')

    logger.info('Открытие формы "Frames"')
    frames_page = FramesPage()
    try:
        menu.open(MenuItem.FRAMES.value)
        assert frames_page.is_opened() is True
    except Exception:
        logger.exception('Страница не открылась')

    logger.info('Получение текста из двух фреймов')
    value3, value4 = frames_page.get_FirstAndSecondFrames_text(logger)
    try:
        assert value3 == value4
    except AssertionError:
        logger.exception('Текст у двух фреймов должен быть одинаковым')