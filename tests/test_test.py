import pytest

from main import add

def test_add():
    assert add(-2, 2) == 0



from src.masks import get_mask_card_number

@pytest.mark.parametrize("number, expected", [(1234567890123456, '1234 56** **** 3456'),
                                              (12345678901234567890, '1234 56** **** 7890'),
                                              (1234567890123456789012345, '1234 56** **** 2345'),
                                              (1234567890123, '1234 56** **** 0123'),
                                              (12345678, 'Error'),
                                              (0, 'Error'),
                                              ])

print(get_mask_card_number(1234567890123456))
def test_get_mask_card_number():
    assert get_mask_card_number(1234567890123456) == '1234 56** **** 3456'


