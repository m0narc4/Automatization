from other_entity.tab import Tab
from pages.links_page import LinksPage
from pages.browserWindows_page import BrowserWindowsPage
from content.main_content import MainPage
from SingletonMeta import SeleniumDriver
from content.menu import Menu, MenuItem


def test_Tabs(logger):
    main_page = MainPage()
    logger.info('Открытие главной страницы')
    SeleniumDriver().open("https://demoqa.com")
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переход на страницу "Alerts"')
    main_page.enter_to_AlertsContent()

    menu = Menu()
    logger.info('Открытие формы "Browser Windows"')
    browserWindows_page = BrowserWindowsPage()
    try:
        menu.open(MenuItem.BROWSER_WINDOWS.value)
        assert browserWindows_page.is_opened() is True
    except Exception:
        logger.exception('Форма "Browser Windows" не открылась')

    logger.info('Нажатие на кнопку "New Tab"')
    browserWindows_page.clickOn_newTab_button()
    logger.info('Переключение на новую вкладку')

    tab = Tab()
    tab.switch_to_newTab()
    try:
        assert tab.is_opened() is True
    except AssertionError:
        logger.exception('Новая вкладка с надписью "Sample Page" не открылась')

    logger.info('Закрытие вкладки')
    tab.close_tab()
    logger.info('Переключение на предыдущую вкладку')
    tab.switch_to_original()
    try:
        assert browserWindows_page.is_opened() is True
        logger.info('Форма Browser Windows открылась')
    except AssertionError:
        logger.exception('Форма Browser Windows не открылась')
    logger.info('Переход на страницу "Elements"')
    browserWindows_page.go_to_elementsPage()

    menu.open(MenuItem.LINKS.value)
    logger.info('Открытие формы "Links"')
    links_page = LinksPage()
    try:
        assert links_page.is_opened() is True
    except AssertionError:
        logger.exception('Форма Links не открылась')

    logger.info('Нажатие на кнопку "Home Link"')
    links_page.clickOn_homeLink()
    logger.info('Переключение на новую вкладку')
    tab.switch_to_newTab()
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переключение на предыдущую вкладку')
    tab.switch_to_original()

    try:
        assert links_page.is_opened() is True
    except AssertionError:
        logger.exception('Форма Links не открылась')