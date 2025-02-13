import os

from Models.Data_models import User, TestCaseData, UserData, Alert, IFrames, Engineer
from data_loader import DataLoader


class TestDataManager:
    __test_data_path = f'{os.path.dirname(os.getcwd())}\\data\\test_data.json'

    @staticmethod
    def get_users(dictionary: dict):
        return [User(**nested_dictionary) for nested_dictionary in dictionary.values()]

    @staticmethod
    def get_user_data(dictionary: dict):
        return UserData(**dictionary)

    @staticmethod
    def get_test_case_data():
        return DataLoader.load_data(TestDataManager.__test_data_path, TestCaseData)

    @staticmethod
    def get_alerts(dictionary: dict):
        return [Alert(**nested_dictionary) for nested_dictionary in dictionary.values()]

    @staticmethod
    def get_frames_data(dictionary: dict):
        return IFrames(**dictionary)

    @staticmethod
    def get_engineer_age():
        return Engineer(**TestDataManager.get_test_case_data().test_case5)


