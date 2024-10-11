from language.ru import text_ru
from main_funtion import additionally_choice, choice_file, print_transactions, choice_status
from src.filters_transaction import filter_for_description, filter_for_rub
from src.processing import sort_by_date, filter_by_state
from src.utils import read_file



def main() -> None:
    print(text_ru["hey_title"], "\n")
    file_transactions = choice_file()  # выбрать тип файла
    status_transactions = choice_status()  # Выбрать статус для фильтрации
    additionally = additionally_choice()  # Получаем доп. настройки

    # получить список транзакций
    transactions_from_files = read_file(file_transactions)

    # Отфильтровать список транзакций по статус
    transactions_filter_by_state = filter_by_state(transactions_from_files, status_transactions)

    # Отфильтровать список транзакций по определенному слову
    filter_word = additionally.get("filter_word", "")
    if filter_word != "":
        transactions_filter_word = filter_for_description(transactions_filter_by_state, filter_word)
    else:
        transactions_filter_word = transactions_filter_by_state

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
