import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list:  # Имя фикстуры — любое
    return [
        {
            "id": 125719345,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
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
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 939713450,
            "state": "EXECUTED",
            "date": "2018-06-29T02:08:58.425572",
            "operationAmount": {"amount": "782.67", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 11776614605963066702",
            "to": "Счет 75106830613657916952",
        },
    ]


@pytest.fixture
def right_descriptions() -> list:
    return [
        "Перевод организации",
        "Перевод организации",
        "Перевод со счета на счет",
    ]


@pytest.fixture
def filter_transactions() -> list:  # Имя фикстуры — любое
    return [
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
            "id": 939713450,
            "state": "EXECUTED",
            "date": "2018-06-29T02:08:58.425572",
            "operationAmount": {"amount": "782.67", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 11776614605963066702",
            "to": "Счет 75106830613657916952",
        },
    ]


def test_filter_by_currency(transactions: list, filter_transactions: list) -> None:
    """
    Функция filter_by_state:
    1. Тестирование работы фильтрации
    2. Тестирование на пустую строку или не найденную currency
    3. на отсутствие  ключей operationAmount, currency или code
    """
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == filter_transactions[0]
    assert next(generator) == filter_transactions[1]
    with pytest.raises(StopIteration):
        next(generator)

    generator = filter_by_currency(transactions, "112")
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(transactions: list, right_descriptions: list) -> None:
    """
    transaction_descriptions
        1. Тестирование работы выдачи списка проводок
        2. Тестирование отсутствия ключа
    """
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == right_descriptions[0]
    assert next(descriptions) == right_descriptions[1]
    assert next(descriptions) == right_descriptions[2]

    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator() -> None:
    """
    1. Тестирование работы выдачи номеров нужного формата
    2. Тестирование прохода через end_card
    3. Тест ValueError
    """
    start_card = 123456788998
    end_card = 123456789002
    generator_card_number = card_number_generator(start_card, end_card)
    assert next(generator_card_number) == "0000 1234 5678 8998"
    assert next(generator_card_number) == "0000 1234 5678 8999"
    assert next(generator_card_number) == "0000 1234 5678 9000"
    assert next(generator_card_number) == "0000 1234 5678 9001"
    assert next(generator_card_number) == "0000 1234 5678 9002"

    with pytest.raises(StopIteration):
        next(generator_card_number)

    generator_card_number = card_number_generator(8, 3)
    with pytest.raises(ValueError) as exc_info:
        next(generator_card_number)

    assert str(exc_info.value) == "Parameters 'card_number_generator' does not the desired range"
