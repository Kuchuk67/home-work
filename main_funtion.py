from typing import Union
from language.ru import text_ru, yes_
from src.widget import get_date, mask_account_card


def choice_file() -> str:
    """Выбор пользователем файла транзакции"""
    print(text_ru["input_file"])
    while True:
        try:
            you_choice = int(input())
        except ValueError:
            print(text_ru["input_value_error"])
        else:
            break

    if you_choice == 1:
        file_transactions = "operations.json"
    elif you_choice == 2:
        file_transactions = "transactions.csv"
    elif you_choice == 3:
        file_transactions = "transactions_excel.xlsx"
    else:
        file_transactions = ""
    return file_transactions


def choice_status() -> str:
    """Пользователь выбирает статус интересующих его операций."""
    status_transactions = ""
    while True:
        you_choice_status = input(text_ru["input_status"])
        you_choice_status.upper()
        if you_choice_status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'{text_ru["filter_by_status"]} "{you_choice_status}"')
            return you_choice_status
            break
        else:
            print(f'{text_ru["filter_by_status_error_1"]} "{you_choice_status}" {text_ru["filter_by_status_error_2"]}')
    return status_transactions


def additionally_choice() -> dict:
    """:return: Получаем доп. настройки для фильтрации dict[str_key, bool] \n\n
    'sorting_data' Отсортировать операции по дате\n
    'sort_order' Отсортировать по возрастанию\n
    'transactions_only_rub' Выводить только рублевые транзакции\n
    'filter_word'  str Отфильтровать список транзакций по определенному слову\n
    """

    def input_data(text: str) -> bool:
        x = input(text)
        if not x.lower() in yes_:
            return False
        else:
            return True

    additionally: dict[str, Union[bool, str]] = {}
    additionally["sorting_data"] = input_data(text_ru["sorting_data"])
    if additionally["sorting_data"]:
        additionally["sort_order"] = input_data(text_ru["sort_order"])
    additionally["transactions_only_rub"] = input_data(text_ru["all_or_rub"])
    additionally["filter_word"] = input(text_ru["filter_word"])

    print("\n", text_ru["print_transactions"])
    return additionally


def print_transactions(transactions: list) -> None:
    len_tr = len(transactions)
    if len_tr > 0:
        print("\n", text_ru["counter_transactions"], len_tr)
        for transaction in transactions:
            date_trans = transaction.get("date", "")
            date_transaction = get_date(date_trans)
            print(f"\n{date_transaction} {transaction.get('description')}")
            separator_to_from = ""
            to_ = mask_account_card(transaction.get("to", ""))
            from_ = mask_account_card(transaction.get("from", ""))
            if to_ != "" and from_ != "":
                separator_to_from = " -> "
            print(f"{from_} {separator_to_from} {to_}")
            print(
                text_ru["sum"],
                transaction.get("operationAmount", {}).get("amount", ""),
                transaction.get("operationAmount", {}).get("currency", {}).get("name"),
                "",
            )
    else:
        print("\n", text_ru["not_transactions"])
