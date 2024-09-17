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
