from config import PATH_HOME
import os
import json


def read_json_file(file_name: str) -> list:
    '''
    вход путь до JSON-файла
    :return:
    список словарей с данными.
    '''
    path_to_file = os.path.join(PATH_HOME, "data", file_name)
    try:
        with open(path_to_file, 'r', encoding="utf-8") as file:
            data_json = json.load(file)
    except:
        return []
    else:
        return data_json


if __name__ == "__main__":
    print(read_json_file('operations.json'))
