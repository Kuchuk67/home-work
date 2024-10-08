# Проект card_client
## Описание:
Это серверная часть виджета банковских операций. Виджет имеет возможность отображать операции клиента.

## Реализация функций
### Модуль masks
- Функция mask_account_card принимает на вход строку формата Visa Platinum 7000792289606361, или Maestro 7000792289606361, или Счет 73654108430135874305.
Для маскировки номера карты/счета используются ранее написанные функции из модуля masks.
- Функция get_date принимает на вход строку и отдает корректный результат в формате 11.07.2018.

### Модуль processing
- функция filter_by_state, которая принимает список словарей и опционально значение для ключа state
 (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.
-  функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).  Функция должна возвращать новый список, отсортированный по дате (date).

### Модуль widget
- функция mask_account_card, возвращает строку с названием платежной системы или счета и с замаскированным номером.
- функция get_date, переводит дату из формата "Y-m-dTH:M:S.f" в "d.m.Y"

### Модуль generators
- функция filter_by_currency, возвращает словари по определенной валюте
- функция transaction_descriptions, возвращает проведенные операции
- функция card_number_generator, генерирует номера карт

### Декоратор log
Декоратор позволяет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
@log(filename="mylog.txt") имя файла для логов
Если filename не задан, логи выводятся в консоль.


## Установка:
Клонируйте репозиторий:
git clone https://github.com/Kuchuk67/Home_work.git

Установите зависимости:

poetry env use python

poetry install

## Тестирование:

### Модуль masks 
- mask_account_card 
Тестирование правильности маскирования номера карты.
Проверка работы функции на различных входных форматах номеров карт,
включая граничные случаи и нестандартные длины номеров.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
- get_date
Тестирование правильности маскирования номера счета.
Проверка работы функции с различными форматами и длинами номеров счетов.
Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины.


### Модуль processing
- filter_by_state 
Тестирование фильтрации списка словарей по заданному статусу state.
Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
Параметризация тестов для различных возможных значений статуса state.
- sort_by_date
Тестирование сортировки списка словарей по датам в порядке убывания и возрастания. проверка на отсутствие даты

### Модуль widget
- mask_account_card
Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
- get_date
Тестирование правильности преобразования даты.

### Модуль generators
- Функция filter_by_state:
Тестирование работы фильтрации
Тестирование на пустую строку или не найденную currency
на отсутствие  ключей operationAmount, currency или code
- Функция card_number_generator
Тестирование работы выдачи номеров нужного формата
Тестирование прохода через end_card
Тест ValueError
- Функция transaction_descriptions
Тестирование работы выдачи списка проводок
Тестирование отсутствия ключа


Отчет по тестам https://github.com/Kuchuk67/Home_work/tree/feature/homework_10_2/htmlcov