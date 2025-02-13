from SeleniumWait import Wait
from base.base_element import BaseElement
from components.Button import Button
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class UploadAndDownloadPage(BasePage):
    __DOWNLOAD_BUTTON = (By.ID, 'downloadButton')
    __UPLOAD_BUTTON = (By.ID, 'uploadFile')
    __FORM_PATH = (By.ID, 'uploadedFilePath')

    def __init__(self):
        super().__init__((By.XPATH, '//h1[text()="Upload and Download"]'))

    def download(self):
        download_button = Wait.element_to_be_clickable(self.__DOWNLOAD_BUTTON)
        download_button.click()

    def upload(self, path_to_file):
        upload_button = Button(self.__UPLOAD_BUTTON)
        upload_button.send_keys(path_to_file)

    def check_form_path(self):
        path = BaseElement(self.__FORM_PATH)
        return path.get_text()
