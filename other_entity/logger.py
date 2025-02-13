import logging
import os


class Logger:
    __logger = logging.getLogger(__name__)

    def setup(self, moduleName):
        self.__logger.setLevel(logging.INFO)
        if self.__logger.hasHandlers():
            self.__logger.handlers.clear()
        handler = logging.FileHandler(f'{os.path.dirname(os.getcwd())}/logs/{moduleName}.log', encoding='utf-8')
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def get_logger(self):
        return self.__logger

    def info(self, message):
        self.__logger.info(message)

    def exception(self, message):
        self.__logger.exception(message)