import json
import os
from typing import Any

from config import PATH_HOME
from src.logs_init import logger_init

named_logger = logger_init('utils')


def read_json_file(file_name: str) -> Any:
    """
    вход путь до JSON-файла
    :return:
    список словарей с данными.
    """
    path_to_file = os.path.join(PATH_HOME, "data", file_name)
    named_logger.info(f'Попытка чтения файла: {path_to_file}')
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data_json = json.load(file)
            named_logger.info('Возвращаем JSON')
    except FileNotFoundError:
        named_logger.error(f'Не найден файл: {path_to_file}')
        return []
    except json.JSONDecodeError:
        named_logger.error(f'Не верный формат файла: {path_to_file}')
        return []
    else:
        return data_json


if __name__ == "__main__":
    print(read_json_file("operations.json"))
