import pytest

'''
Функция  mask_account_card

Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
'''
from src.widget import mask_account_card


@pytest.mark.parametrize("number, expected", [('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                              ('Счет 35383033474447895560', 'Счет **5560'),
                                              ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                              ('Visa  Classic  6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                              ('MasterCard 7158R300734726758', 'MasterCard 7158 30** **** 6758'),
                                              ('MasterCard 34 7158300734726758', 'MasterCard 34 7158 30** **** 6758'),
                                              ('', 'Error'),
                                              ('Master Card', 'Error'),
                                              ('343254544354', 'Error'),
                                              ])
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


'''
Функция get_data

Тестирование правильности преобразования даты.
Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
'''
from src.widget import get_date
data_for_test = '21.11.1977'
def test_get_date():
    with pytest.raises(ValueError) as exc_info:
        get_date(data_for_test)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "time data '"+data_for_test+"' does not match format '%Y-%m-%dT%H:%M:%S.%f'"