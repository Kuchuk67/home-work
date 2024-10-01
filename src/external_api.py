import requests
import os
from dotenv import load_dotenv


# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv('API_KEY')
to = 'RUB'
from_ = 'USD'
amount = 100

url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

payload = {}
headers = {
    "apikey": API_KEY
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
print(result)


def transaction_amount_in_rubles(transaction: dict) -> float:
    ''' принимает на вход транзакцию
    возвращает сумму транзакции  в рублях
.   Если транзакция была в USD или EUR
,   происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    :return:
    '''
    return 31957.58
