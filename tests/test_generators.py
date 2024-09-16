import pytest
from src.generators import filter_by_currency


@pytest.fixture
def transactions() -> list:  # Имя фикстуры — любое
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }, {
            "id": 939713450,
            "state": "EXECUTED",
            "date": "2018-06-29T02:08:58.425572",
            "operationAmount": {
                "amount": "782.67",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 11776614605963066702",
            "to": "Счет 75106830613657916952"
        }, ]


@pytest.fixture
def filter_transactions() -> list:  # Имя фикстуры — любое
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
            "id": 939713450,
            "state": "EXECUTED",
            "date": "2018-06-29T02:08:58.425572",
            "operationAmount": {
                "amount": "782.67",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 11776614605963066702",
            "to": "Счет 75106830613657916952"
        }, ]


@pytest.fixture
def transactions_no_code() -> list:  # Имя фикстуры — любое
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }]


def test_filter_by_currency(transactions: list, filter_transactions: list) -> None:
    """
    Функция filter_by_state:
    1. Тестирование работы фильтрации
    2. Тестирование на пустую строку или не найденную currency
    3. на отсутствие  ключей operationAmount, currency или code
    """
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == filter_transactions[0]
    assert next(generator) == filter_transactions[1]

    generator = filter_by_currency(transactions, "112")
    with pytest.raises(StopIteration):
        next(generator)

    generator = filter_by_currency(transactions_no_code, "USD")
    with pytest.raises(StopIteration):
       next(generator)
