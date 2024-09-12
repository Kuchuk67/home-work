import pytest
# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def state(): # Имя фикстуры — любое
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},]
@pytest.fixture
def no_state(): # Имя фикстуры — любое
    return [{'id': 41428829,  'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},]
#@pytest.fixture
#def expected_for_state(): # Имя фикстуры — любое
    #return \

"""
Функция filter_by_state:
Тестирование фильтрации списка словарей по заданному статусу state.
Проверка работы функции при отсутствии словарей с указанным статусом state  в списке.
Параметризация тестов для различных возможных значений статуса state
"""
from src.processing import filter_by_state

def test_filter_by_no_state(no_state):
    assert filter_by_state(no_state, 'TEST') == []



@pytest.mark.parametrize("state_value, expected", [('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        ]),('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ]),])
def test_filter_by_state_value(state, state_value, expected):
    assert filter_by_state(state, state_value) == expected


"""
Функция sort_by_date:
Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
Проверка корректности сортировки при одинаковых датах.
Тесты на работу функции с некорректными или нестандартными форматами дат.
"""
from src.processing import sort_by_date
expected_for_sort_asc = [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    ]
expected_for_sort_desc = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]

def test_sort_by_date_empty(state):
    assert sort_by_date(state ) == expected_for_sort_desc

def test_sort_by_date_true(state):
    assert sort_by_date(state, True ) == expected_for_sort_desc

def test_sort_by_date_false(state):
    assert sort_by_date(state, False ) == expected_for_sort_asc