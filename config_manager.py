import os

from Models.Data_models import ConfigData, InitialSetup, BrowserOptions
from data_loader import DataLoader


class ConfigManager:
    __config_path = f'{os.path.dirname(os.getcwd())}\\data\\config.json'

    @staticmethod
    def get_browser_options():
        return BrowserOptions(**DataLoader.load_data(ConfigManager.__config_path, ConfigData).options)

    @staticmethod
    def get_initial_setup():
        return InitialSetup(**DataLoader.load_data(ConfigManager.__config_path, ConfigData).initial_setup)

    @staticmethod
    def get_config_data():
        return DataLoader.load_data(ConfigManager.__config_path, ConfigData)