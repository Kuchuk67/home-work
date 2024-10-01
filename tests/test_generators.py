import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

#Тест функции filter_by_currency
@pytest.fixture
def test_transactions()-> list:
    transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб."}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб."}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
    ]
    return transactions

@pytest.fixture
def my_code()-> str:
    return "USD"

@pytest.fixture
def my_code_rub()-> str:
    return "RUB"

def test_filter_by_currency(test_transactions: list,my_code: str):
    usd_transactions = filter_by_currency(test_transactions, my_code)
    assert next(usd_transactions) == {'id': 939719570,
                                     'state': 'EXECUTED',
                                     'date': '2018-06-30T02:08:58.425572',
                                     'operationAmount': {'amount': '9824.07','currency': {'name': 'USD', 'code': 'USD'}},
                                     'description': 'Перевод организации',
                                     'from': 'Счет 75106830613657916952',
                                     'to': 'Счет 11776614605963066702'}


def test_filter_by_currency_not_key(test_transactions: list,my_code: str):
    rub_transactions = filter_by_currency(test_transactions, my_code)
    assert next(rub_transactions) == {}


def test_filter_by_currency_not_data(test_transactions: list,my_code_rub: str):
    rub_transactions = filter_by_currency(test_transactions, my_code_rub)
    assert next(rub_transactions) == None


#Тест функции transaction_descriptions

@pytest.mark.parametrize("transactions, expected", [(test_transactions, "Перевод организации"),
(test_transactions, "Перевод со счета на счет"),
(test_transactions, "Перевод со счета на счет"),
(test_transactions, "Перевод с карты на карту"),
(test_transactions,"Перевод организации")])
def test_transaction_descriptions(transactions: list, expected: str):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == expected
    assert next(descriptions) == expected


def test_transaction_descriptions_not():
    descriptions = transaction_descriptions([], "")
    assert next(descriptions) == None


#Тест функции card_number_generator

@pytest.mark.parametrize("start, end, expected", [(1, 2, ("0000 0000 0000 0001" "0000 0000 0000 0002") ),
                                                  (0,1, ("StopIteration"))])
def test_card_number_generator(start: int, end: int, expected: str):
    generator = card_number_generator(start, end)
    assert next(generator) == expected
    assert next(generator) == expected