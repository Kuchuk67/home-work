import json
import os
from typing import Any

from config import PATH_HOME


def read_json_file(file_name: str) -> Any:
    """
    вход путь до JSON-файла
    :return:
    список словарей с данными.
    """
    path_to_file = os.path.join(PATH_HOME, "data", file_name)
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data_json = json.load(file)
    except Exception:
        return []
    else:
        return data_json


if __name__ == "__main__":
    print(read_json_file("operations.json"))
