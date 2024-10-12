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

