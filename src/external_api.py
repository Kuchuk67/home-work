import json
import os
import requests
from dotenv import load_dotenv
from typing import Any

# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount_in_rubles(transaction: dict) -> float:
    """принимает на вход транзакцию
        возвращает сумму транзакции  в рублях
    .   Если транзакция была в USD или EUR
    ,   происходит обращение к внешнему API для получения текущего курса валют
        и конвертации суммы операции в рубли.
        :return:
    """
    # получаем код валюты
    cur_code = transaction.get("operationAmount", None).get("currency", None).get("code", None)
    # получаем сумму транзакции
    amount_transaction = float(transaction.get("operationAmount", None).get("amount", None))
    if cur_code == "RUB":
        return amount_transaction
    else:

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={cur_code}&amount={amount_transaction}"

        payload: dict[Any]  = {}
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, data=payload)

        status_code = response.status_code

        if status_code != 200:
            pass  # тут ошибка, пока не понятно как обработать

            raise SystemError("ОПИСАНИЕ:Ошибка при запроcе API")

        json_data = response.text

        print(json_data)
        result = json.loads(json_data)
        # result = json_data
        if not result.get("success"):
            raise SystemError("ОПИСАНИЕ: API вернул False")
        #print(result)

        return float(round(result.get("result", 0), 2))
