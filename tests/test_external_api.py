import pytest
from unittest.mock import Mock
from unittest.mock import patch
from src.external_api import transaction_amount_in_rubles



@pytest.fixture
def transactions_0() -> dict:
    return {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "code": "RUB"
            }
        },

    }

@pytest.fixture
def transactions_1() -> dict:
    return {
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "code": "USD"
            }
        },

    }


def test_transaction_amount_from_RUB(transactions_0) -> None:
    result = transaction_amount_in_rubles(transactions_0)
    assert result == 31957.58

@patch('requests.get')
def test_transaction_amount_from_USD(mocked_get,transactions_1) -> None:

    mocked_get.return_value.status_code = 200
    mocked_get.return_value.text = '''{
    "success": true,
    "result": 12345.67
}'''
    result = transaction_amount_in_rubles(transactions_1)
    assert result == 12345.67

@patch('requests.get')
def test_transaction_amount_from_500(mocked_get, transactions_1) -> None:
    mocked_get.return_value.status_code = 500
    with pytest.raises(SystemError) as exc_info:
        transaction_amount_in_rubles(transactions_1)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "ОПИСАНИЕ:Ошибка при запроcе API"

@patch('requests.get')
def test_transaction_amount_from_500(mocked_get, transactions_1) -> None:
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.text = '''{
        
        "result": 12345.67
    }'''
    with pytest.raises(SystemError) as exc_info:
        transaction_amount_in_rubles(transactions_1)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "ОПИСАНИЕ: API вернул False"

@patch('requests.get')
def test_transaction_amount_from_no(mocked_get, transactions_1) -> None:
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.text = '''{
    "success": true,
    "_result": 12345.67
}'''
    #with pytest.raises(SystemError) as exc_info:
    result =  transaction_amount_in_rubles(transactions_1)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert result == 0
