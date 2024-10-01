from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[dict, None, None]:
    """
    :param transactions: список транзакций
    :param currency: код валюты
    :return: список транзакций по определенной валюты
    """
    for dict_transaction in transactions:
        # if   dict_transaction.get('operationAmount'['currency']['code']) == currency:
        if dict_transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield dict_transaction


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """
    :param transactions: список транзакций
    :return: название операции
    """
    for dict_transaction in transactions:
        description = dict_transaction.get("description")
        if description:
            yield description


def card_number_generator(start_card: int, end_card: int) -> Generator[str, None, None]:
    """
    :param start_card: начало нумерации
    :param end_card: конец нумерации
    :return:  номера карт в формате **** **** **** ****
    """
    if start_card < 0 or end_card < start_card:
        raise ValueError("Parameters 'card_number_generator' does not the desired range")
    while True:
        if start_card > end_card:
            break
        start_card += 1
        number_card_full = "{:016}".format(start_card - 1)
        number_card = (
            f"{number_card_full[0:4]} {number_card_full[4:8]} {number_card_full[8:12]} {number_card_full[12:]}"
        )
        yield number_card


x = [
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

q = (filter_by_currency(x, "USD"))
print(next(q))
print(next(q))
print(next(q))
