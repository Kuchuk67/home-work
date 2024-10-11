import re
from collections import Counter


def filter_for_description(transactions: list, text_filter: str) -> list:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    result = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if re.search(text_filter, description, flags=re.IGNORECASE):
            result.append(transaction)
    return result


def counter_category(transactions: list, category: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    if len(category) == 0:
        x = Counter(transaction.get("description", "Error") for transaction in transactions if transaction.get("description", "Error"))
        return x
    return Counter(transaction.get("description", "Error") for transaction in transactions if transaction.get("description", "Error")  in category)


def filter_for_rub(transactions: list) -> list:
    """
    Принимает список словарей с данными о банковских операциях,
    а возвращать список словарей, у которых только рубблевые операции.
    """
    result = []
    for transaction in transactions:
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if code == "RUB":
            result.append(transaction)
    return result


x = [
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
            "operationAmount": {"amount": "9824.07", "currency": {"name": "руб.", "code": "USD"}},
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
            "operationAmount": {"amount": "782.67", "currency": {"name": "руб.", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 11776614605963066702",
            "to": "Счет 75106830613657916952",
        },
    ]
print(counter_category(x,[]))