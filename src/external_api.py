import requests
import json
import os
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv('API_KEY')


def transaction_amount_in_rubles(transaction: dict) -> float:
    ''' принимает на вход транзакцию
    возвращает сумму транзакции  в рублях
.   Если транзакция была в USD или EUR
,   происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    :return:
    '''
    # получаем код валюты
    currency_code = transaction.get('operationAmount').get('currency').get('code')
    # получаем сумму транзакции
    amount_transaction = float(transaction.get('operationAmount').get('amount'))
    if currency_code == 'RUB':
        return amount_transaction
    else:

        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount_transaction}'

        payload = {}
        headers = {
            'apikey': API_KEY
        }

        response = requests.get(url, headers=headers, data=payload)

        status_code = response.status_code



        if status_code != 200:
            pass # тут ошибка, пока не понятно как обработать

            raise SystemError  ("ОПИСАНИЕ:Ошибка при запроcе API")

        json_data = response.text

        print(json_data)
        result = json.loads(json_data)
        #result = json_data
        if not result.get('success'):
            raise SystemError  ("ОПИСАНИЕ: API вернул False")
        print(result)

        return round(result.get('result', 0),2)

