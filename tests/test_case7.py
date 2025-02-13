import os
from pathlib import Path

from SeleniumWait import Wait
from SingletonMeta import SeleniumDriver
from pages.uploadAndDownload_page import UploadAndDownloadPage
from content.menu import Menu, MenuItem
from content.main_content import MainPage


def test_Download_and_Upload(logger):
    main_page = MainPage()
    logger.info("Открытие главной страницы")
    SeleniumDriver().open("https://demoqa.com")
    try:
        assert main_page.is_opened() is True
    except AssertionError:
        logger.exception('Главная страница не открылась')
    logger.info('Переход на страницу "Elements"')
    main_page.enter_to_ElementsContent()

    menu = Menu()
    logger.info('Открытие формы "Upload And Download"')
    upload_and_download_page = UploadAndDownloadPage()
    try:
        menu.open(MenuItem.UPLOAD_AND_DOWNLOAD.value)
        assert upload_and_download_page.is_opened() is True, 'Форма с Date Picker не открылась'
    except Exception:
        logger.exception('Форма "Date Picker" не открылась')

    logger.info('Нажатие на кнопку "Download"')
    upload_and_download_page.download()

    path_to_file = f"{os.getcwd()}\\downloads\\sampleFile.jpeg"
    try:
        assert Wait().until_download(path_to_file) is True
        logger.info('Файл успешно скачан')
    except AssertionError:
        logger.exception('Файл не удалось скачать')

    logger.info('Нажатие на кнопку "Выберите файл" и отправка скачанного файла')
    upload_and_download_page.upload(path_to_file)

    try:
        assert upload_and_download_page.check_form_path() == f'C:\\fakepath\\{Path(path_to_file).name}'
        logger.info('В форме появился путь, содержащий в себе название файла')
    except AssertionError:
        logger.exception('В форме не появился путь, содержащий в себе название файла')


