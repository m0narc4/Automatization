import pytest

from content.main_content import MainPage
from pages.webTables_page import WebTablesPage
from SingletonMeta import SeleniumDriver
from content.menu import Menu, MenuItem
from test_data_manager import TestDataManager

test_case_data = TestDataManager.get_test_case_data().test_case3
user_data = TestDataManager.get_users(test_case_data)


@pytest.mark.parametrize("user", user_data)
def test_WebTable(user, logger):
    main_page = MainPage()
    logger.info('Открытие главной страницы')
    SeleniumDriver().open("https://demoqa.com/")
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переход на страницу "Elements"')
    main_page.enter_to_ElementsContent()

    menu = Menu()
    logger.info('Открытие формы "Web Tables"')
    webTables_page = WebTablesPage()
    try:
        menu.open(MenuItem.WEB_TABLES.value)
        assert webTables_page.is_opened() is True
    except Exception:
        logger.exception('Форма "Web Tables" не открылась')

    logger.info(f'Добавление пользователя {user.first_name} в таблицу')
    webTables_page.addUser(user, logger)
    logger.info('Удаление пользователя из таблицы')
    webTables_page.deleteUser(user.first_name, logger)

