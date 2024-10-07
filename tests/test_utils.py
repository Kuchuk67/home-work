from unittest.mock import mock_open, patch

from src.utils import read_json_file, read_file

data_json = '''[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]'''

data_csv = '''id;state;date;amount;currency_name;currency_code;from;to;description
441945886;EXECUTED;2019-08-26T10:50:58.294041;31957.58;руб.;RUB;Maestro 1596837868705199;Счет 64686473678894779589;Перевод организации'''

data_list = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}]


# Mocking file open in Python


def test_read_file() -> None:
    m = mock_open(read_data=data_json)
    with patch("builtins.open", m):
        lines = read_file("my_file.json")
    assert lines == data_list

def test_read_file_not_file() -> None:
    lines = read_file("no_files.json")
    assert lines == []


def test_read_scv_file() -> None:
    m = mock_open(read_data=data_csv)
    with patch("builtins.open", m):
        lines = read_file("my_file.csv")
    assert lines == data_list