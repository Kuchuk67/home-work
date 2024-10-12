import csv
from typing import Any, Union

import pandas as pd


def read_csv_file(file_name: str) -> Any:
    """
    вход путь до CSV-файла
    :return:
    список словарей с данными.
    """
    data_csv = []
    data_csv_dict: dict[str, Union[str, int, dict]] = {}
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        for row in reader:
            if row[0].isdigit():
                data_csv_dict["id"] = int(row[0])
            else:
                continue
            data_csv_dict["state"] = row[1]
            data_csv_dict["date"] = row[2]
            data_csv_dict["operationAmount"] = {"amount": row[3], "currency": {"name": row[4], "code": row[5]}}
            data_csv_dict["from"] = row[6]
            data_csv_dict["to"] = row[7]
            data_csv_dict["description"] = row[8]

            data_csv.append(data_csv_dict)
            data_csv_dict = {}

    return data_csv


def read_xls_file(file_name: str) -> Any:
    """
    вход путь до XLS-файла
    :return:
    список словарей с данными.
    """
    data_xls = []
    data_xls_dict: dict[str, Any] = {}
    excel_data = pd.read_excel(file_name)
    excel_data = excel_data.fillna('') #замена NAN на ""
    df_dict = excel_data.to_dict(orient="records")
    for item in df_dict:
        data_xls_dict["id"] = item.get("id")
        data_xls_dict["state"] = item.get("state")
        data_xls_dict["date"] = item.get("date")
        data_xls_dict["operationAmount"] = {
            "amount": str(item.get("amount")),
            "currency": {"name": item.get("currency_name"), "code": item.get("currency_code")},
        }
        data_xls_dict["from"] = item.get("from")
        data_xls_dict["to"] = item.get("to")
        data_xls_dict["description"] = item.get("description")

        data_xls.append(data_xls_dict)
        data_xls_dict = {}

    return data_xls
