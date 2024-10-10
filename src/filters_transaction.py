import  re
from collections import Counter

def filter_tr_description(transactions: list, text_filter: str) -> list:
    '''
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    '''
    result = []
    for transaction in transactions:
        description = transaction.get('description', '')
        if re.search(text_filter, description, flags=re.IGNORECASE ):
            result.append(transaction)
    return result


def counter_category(transactions: list, category: list) -> dict:
    '''
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    '''
    return Counter(transaction.get('description', 'Error') for transaction in transactions)
