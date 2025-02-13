from Models.Data_models import User
from base.base_element import BaseElement
from base.base_page import BasePage
from selenium.webdriver.common.by import By

from components.Table import Table


class WebTablesPage(BasePage):
    __FIRST_NAME_FIELD = (By.ID, 'firstName')
    __LAST_NAME_FIELD = (By.ID, 'lastName')
    __EMAIL_FIELD = (By.ID, 'userEmail')
    __AGE_FIELD = (By.ID, 'age')
    __SALARY_FIELD = (By.ID, 'salary')
    __DEPARTMENT_FIELD = (By.ID, 'department')

    __ADD_BUTTON = (By.ID, 'addNewRecordButton')
    __SUBMIT_BUTTON = (By.ID, 'submit')

    __DELETE = (By.XPATH, '//div[text()=\'{0}\']/..//span[contains(@id, "delete")]')

    __table = Table()

    def __init__(self):
        super().__init__((By.XPATH, '//h1[text()="Web Tables"]'))

    def addUser(self, user: User, logger):
        add_button = BaseElement(self.__ADD_BUTTON)
        logger.info('Нажатие на кнопку "Add"')
        add_button.click()
        logger.info('Заполнение полей')
        try:
            self.__table.fill_fields(user)
        except Exception:
            logger.exception('Ошибка при заполнении полей')
        logger.info(f'Добавление пользователя {user.first_name} в таблицу')
        try:
            self.__table.addUser()
        except:
            logger.exception('Не удалось добавить пользователя')

    def deleteUser(self, user_name, logger):
        logger.info('Удаление пользователя')
        try:
            self.__table.deleteUser(user_name)
        except Exception:
            logger.exception('Не удалось удалить пользователя')

