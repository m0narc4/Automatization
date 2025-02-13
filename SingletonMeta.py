import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config_manager import ConfigManager


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class SeleniumDriver(metaclass=SingletonMeta):
    __options_data = ConfigManager.get_browser_options()
    __initial_setup = ConfigManager.get_initial_setup()

    def __setup_driver(self):
        match self.__initial_setup.browser:
            case 'chrome':
                chrome_options = webdriver.ChromeOptions()
                chrome_prefs = {
                    "download.default_directory": f"{os.getcwd()}\downloads",
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "safebrowsing.enabled": True
                }
                chrome_options.add_argument(self.__options_data.window_size)
                chrome_options.add_experimental_option('prefs',chrome_prefs)
                chrome_options.page_load_strategy = "eager"
                self.__driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),
                                                 options=chrome_options)
            case 'firefox':
                firefox_options = Options()
                firefox_options.set_preference("browser.download.folderList", 2)
                firefox_options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
                firefox_options.page_load_strategy = "eager"
                self.__driver = webdriver.Firefox(options=firefox_options)

    def get_driver(self):
        if not hasattr(self, "_SeleniumDriver__driver"):
            self.__setup_driver()
        return self.__driver

    def get_handle(self, index):
        return self.get_driver().window_handles[index]

    def handles(self):
        return self.get_driver().window_handles

    def close(self):
        self.get_driver().close()

    def open(self, url):
        return self.get_driver().get(url)

    def switch_to(self, target, value=None):
        match target:
            case 'alert':
                self.get_driver().switch_to.alert
            case 'frame':
                self.get_driver().switch_to.frame(value)
            case 'parent_frame':
                self.get_driver().switch_to.parent_frame()
            case 'default_content':
                self.get_driver().switch_to.default_content()
            # case 'new_window':
            #     self.get_driver().switch_to.new_window('window')
            case 'new_tab':
                self.get_driver().switch_to.new_window('tab')
            case 'handle':
                self.get_driver().switch_to.window(value)
