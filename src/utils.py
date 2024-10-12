import json
import os
from typing import Any

from config import PATH_HOME
from src.logs_init import logger_init
from src.read_csv_xls import read_csv_file, read_xls_file

named_logger = logger_init("utils")


def read_json_file(file_name: str) -> Any:
    """
    вход путь до JSON-файла
    :return:
    список словарей с данными.
    """

    named_logger.info(f"Попытка чтения файла JSON: {file_name}")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data_json = json.load(file)
            named_logger.info("Возвращаем JSON")
    except FileNotFoundError:
        named_logger.error(f"Не найден файл: {file_name}")
        return []
    except json.JSONDecodeError:
        named_logger.error(f"Не верный формат файла: {file_name}")
        return []
    else:
        return data_json


def read_file(file_name: str) -> Any:
    """
    вход путь до JSON, CSV, XLS-файла
    :return:
    список словарей с данными.
    """
    name_file_list = file_name.split(".")
    path_to_file = os.path.join(PATH_HOME, "data", file_name)
    if name_file_list[-1] == "json":

        return read_json_file(path_to_file)

    elif name_file_list[-1] == "csv":
        return read_csv_file(path_to_file)

    elif name_file_list[-1] in ["xls", "xlsx"]:
        return read_xls_file(path_to_file)

    else:
        pass  # Неизвестный формат, ЧТо делать?
        named_logger.error(f"Не верный тип файла (json,csv,xls,xlsx): {file_name}")
    return []



