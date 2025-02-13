from Models.Data_models import User
from base.base_element import BaseElement
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from components.InputField import InputField


class Table(BasePage):
    def __init__(self):
        super().__init__((By.ID, 'registration-form-modal'))

    __FIRST_NAME_FIELD = (By.ID, 'firstName')
    __LAST_NAME_FIELD = (By.ID, 'lastName')
    __EMAIL_FIELD = (By.ID, 'userEmail')
    __AGE_FIELD = (By.ID, 'age')
    __SALARY_FIELD = (By.ID, 'salary')
    __DEPARTMENT_FIELD = (By.ID, 'department')

    __SUBMIT_BUTTON = (By.ID, 'submit')
    __DELETE = (By.XPATH, '//div[text()=\'{0}\']/..//span[contains(@id, "delete")]')

    def addUser(self):
        submit_button = BaseElement(self.__SUBMIT_BUTTON)
        submit_button.click()

    def deleteUser(self, user_name):
        DELETE_USER_BUTTON = (By.XPATH, self.__DELETE[1].format(user_name))
        delete_button = BaseElement(DELETE_USER_BUTTON)
        delete_button.click()

    def fill_fields(self, user: User):
        fName_field = InputField(self.__FIRST_NAME_FIELD)
        lName_field = InputField(self.__LAST_NAME_FIELD)
        email_field = InputField(self.__EMAIL_FIELD)
        age_field = InputField(self.__AGE_FIELD)
        salary_field = InputField(self.__SALARY_FIELD)
        department_field = InputField(self.__DEPARTMENT_FIELD)

        fName_field.send_keys(user.first_name)
        lName_field.send_keys(user.last_name)
        email_field.send_keys(user.email)
        age_field.send_keys(user.age)
        salary_field.send_keys(user.salary)
        department_field.send_keys(user.department)
