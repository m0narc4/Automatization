import json
import os
from typing import Type, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


class DataLoader:
    __test_data_path = f'{os.path.dirname(os.getcwd())}\\data\\test_data.json'

    @staticmethod
    def load_data(file_path: str, model: Type[T]) -> T:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return model(**data)