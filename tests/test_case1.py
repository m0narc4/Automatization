from other_entity.alert import Alert
from content.main_content import MainPage
from content.menu import Menu, MenuItem
from pages.alerts_page import AlertsPage
from SingletonMeta import SeleniumDriver
from test_data_manager import TestDataManager
from faker import Faker
fake = Faker()


def is_opened(text, logger):
    Alert().switch()
    try:
        assert Alert().is_displayed() is True
        assert Alert().get_text() == text
    except AssertionError:
        logger.exception('Alert не открылся или не появился нужный текст')


def is_closed(logger):
    try:
        assert Alert().is_closed() is True
    except AssertionError:
        logger.exception('Alert не закрылся')


def compare_text(text1, text2):
    try:
        assert text1 == text2
    except AssertionError:
        pass


def test_Alerts(logger):
    test_data = TestDataManager.get_test_case_data().test_case1
    alerts = TestDataManager.get_alerts(test_data)


    main_page = MainPage()
    logger.info("Открытие главной страницы")
    SeleniumDriver().open("https://demoqa.com")
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переход на страницу "Alerts"')
    main_page.enter_to_AlertsContent()

    menu = Menu()
    logger.info("Открытие формы Alerts")
    alerts_page = AlertsPage()
    try:
        menu.open(MenuItem.ALERTS.value)
        assert alerts_page.is_opened() is True
    except Exception:
        logger.exception('Форма "Alerts" не открылась')

    logger.info("Нажатие на кнопку 'Показать алерт'")
    alerts_page.clickOn_alert_button()
    is_opened(alerts[0].text, logger)
    logger.info("Закрытие алерта")
    Alert().accept()
    is_closed(logger)

    logger.info("Нажатие на кнопку 'Показать алерт с окном подтверждения'")
    alerts_page.clickOn_confirm_button()
    is_opened(alerts[1].text, logger)
    logger.info("Закрытие алерта")
    Alert().accept()
    is_closed(logger)
    text_in_site = alerts_page.get_confirmResult_text()
    logger.info(f"Сверка текста '{text_in_site}' на странице рядом с кнопкой 'Показать алерт с окном подтверждения'")
    compare_text(text_in_site, alerts[1].comparable_text)

    logger.info("Нажатие на кнопку 'Показать алерт с запросом'")
    alerts_page.clickOn_prompt_button()
    is_opened(alerts[2].text, logger)
    name = fake.name()
    logger.info(f"Отправка случайно сгенерированного имени: {name}")
    Alert().send_keys(name)
    logger.info("Закрытие алерта")
    Alert().accept()
    is_closed(logger)
    text_in_site = alerts_page.get_promprResult_text()
    logger.info(f"Сверка текста '{text_in_site}' на странице рядом с кнопкой 'Показать алерт с запросом'")
    compare_text(text_in_site, alerts[2].comparable_text + name)
