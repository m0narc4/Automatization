from selenium.webdriver.common.by import By
from base.base_page import BasePage

import enum


class MenuItem(enum.Enum):
    WEB_TABLES = 'Web Tables'
    LINKS = 'Links'
    UPLOAD_AND_DOWNLOAD = 'Upload and Download'

    ALERTS = 'Alerts'
    FRAMES = 'Frames'
    NESTED_FRAMES = 'Nested Frames'
    BROWSER_WINDOWS = 'Browser Windows'

    DATE_PICKER = 'Date Picker'
    SLIDER = 'Slider'
    PROGRESS_BAR = 'Progress Bar'


class Menu(BasePage):
    __locator = '//span[contains(text(), "{0}")]'

    def __init__(self):
        super().__init__((By.XPATH, '//h1[text()="{0}"]'))

    def open(self, form):
        locator = (By.XPATH, self.__locator.format(form))
        self.open_form(locator)

