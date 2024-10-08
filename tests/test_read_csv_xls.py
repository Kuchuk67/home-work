from unittest.mock import Mock, mock_open, patch

import pandas as pd

from src.utils import read_file

data_csv = """id;state;date;amount;currency_name;currency_code;from;to;description
441945886;EXECUTED;2019-08-26T10:50:58.294041;31957.58;руб.;RUB;Maestro 1596837868705199;Счет 64686473678894779589;Перевод организации"""


data_xls = pd.DataFrame(
    {
        "id": [441945886],
        "state": ["EXECUTED"],
        "date": ["2019-08-26T10:50:58.294041"],
        "amount": ["31957.58"],
        "currency_name": ["руб."],
        "currency_code": ["RUB"],
        "from": ["Maestro 1596837868705199"],
        "to": ["Счет 64686473678894779589"],
        "description": ["Перевод организации"],
    },
)

data_list = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
]


def test_read_scv_file() -> None:
    m = mock_open(read_data=data_csv)
    with patch("builtins.open", m):
        lines = read_file("my_file.csv")
    assert lines == data_list


def test_read_xls_file() -> None:
    mock_random = Mock(return_value=data_xls)
    pd.read_excel = mock_random
    lines = read_file("my_file.xls")
    assert lines == data_list
