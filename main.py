from language.ru import text_ru, yes_
from src.filters_transaction import filter_for_description, filter_for_rub
from src.processing import sort_by_date
from src.utils import read_file
from src.widget import get_date, mask_account_card
from typing import Union


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
            break
        else:
            print(text_ru["filter_by_status_error"], "\n")
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
            to_ = transaction.get("to", "")
            from_ = transaction.get("from", "")
            if to_ != "" and from_ != "":
                separator_to_from = " -> "
            print(f"{mask_account_card(to_)}{separator_to_from}{mask_account_card(from_)}")
            print(
                text_ru["sum"],
                transaction.get("operationAmount", {}).get("amount", ""),
                transaction.get("operationAmount", {}).get("currency", {}).get("name"),
                "",
            )
    else:
        print("\n", text_ru["not_transactions"])


def main() -> None:
    print(text_ru["hey_title"], "\n")
    file_transactions = choice_file()  # выбрать тип файла
    # status_transactions = choice_status()  # Выбрать статус для фильтрации
    additionally = additionally_choice()  # Получаем доп. настройки

    transactions_from_files = read_file(file_transactions)

    # Отфильтровать список транзакций по определенному слову
    filter_word = additionally.get("filter_word", "")
    if filter_word != "":
        transactions_filter_word = filter_for_description(transactions_from_files, filter_word)
    else:
        transactions_filter_word = transactions_from_files

    # Отсортировать операции по дате
    if additionally["sorting_data"]:
        transactions_filter_word_and_data = sort_by_date(transactions_filter_word, additionally["sort_order"])
    else:
        transactions_filter_word_and_data = transactions_filter_word

    # Выводить только рублевые транзакции
    if additionally["transactions_only_rub"]:
        transactions_filter_word_and_data_rub = filter_for_rub(transactions_filter_word_and_data)
    else:
        transactions_filter_word_and_data_rub = transactions_filter_word_and_data

    print_transactions(transactions_filter_word_and_data_rub)


if __name__ == "__main__":
    main()
