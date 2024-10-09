import pytest
from src.filters_transaction import filter_tr_description

@pytest.fixture
def transactions() -> list:  # Имя фикстуры — любое
    return [
        {
            "id": 125719345,
            "state": "CANCELED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "584.07", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719570,
            "state": "PENDING",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие счета",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 939713450,
            "state": "EXECUTED",
            "date": "2018-06-29T02:08:58.425572",
            "operationAmount": {"amount": "782.67", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 11776614605963066702",
            "to": "Счет 75106830613657916952",
        },
    ]

@pytest.fixture
def transactions_description() -> list:  # Имя фикстуры — любое
    return [
        {
            "id": 125719345,
            "state": "CANCELED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "584.07", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]



def test_filter_tr_description(transactions: list, transactions_description: list) -> None:
    result = filter_tr_description(transactions, 'Органи')
    assert result == transactions_description