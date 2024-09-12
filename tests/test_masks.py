import pytest

"""  # проверяем get_mask_card_number
Тестирование правильности маскирования номера карты.
Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
"""
from src.masks import get_mask_card_number


# card_client(number_user_card: int)
@pytest.mark.parametrize("number, expected", [(1234567890123456, '1234 56** **** 3456'),
                                              (12345678901234567890, '1234 56** **** 7890'),
                                              (1234567890123456789012345, '1234 56** **** 2345'),
                                              (1234567890123, '1234 56** **** 0123'),
                                              (12345678, 'Error'),
                                              (0, 'Error'),
                                              ])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


''' # account_client
Тестирование правильности маскирования номера счета.
Проверка работы функции с различными форматами и длинами номеров счетов.
Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины.
'''

from src.masks import get_mask_account


@pytest.mark.parametrize("number_account, expected_account", [(1234567890123456, '**3456'),
                                                              (12345678901234567890, '**7890'),
                                                              (1234567890123456789012345, '**2345'),
                                                              (1234567890123, '**0123'),
                                                              (12345678, '**5678'),
                                                              (678434, 'Error'),
                                                              (0, 'Error'),
                                                              ])
def test_get_mask_account(number_account, expected_account):
    assert get_mask_account(number_account) == expected_account
