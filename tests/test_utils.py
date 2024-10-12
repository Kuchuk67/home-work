from unittest.mock import mock_open, patch

from src.utils import read_file

data_json = """[
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
]"""

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


# Mocking file open in Python


def test_read_file() -> None:
    m = mock_open(read_data=data_json)
    with patch("builtins.open", m):
        lines = read_file("my_file.json")
    assert lines == data_list


def test_read_file_not_file() -> None:
    lines = read_file("no_files.json")
    assert lines == []
