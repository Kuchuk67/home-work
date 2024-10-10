from src import widget
from  data import text_ru

def choice_file()-> str:
    ''' Выбор пользователем файла транзакции '''
    print(text_ru['input_file'])
    while True:
        try:
            you_choice = int(input())
        except ValueError:
            print(text_ru['input_value_error'])
        else:
            break

    if you_choice == 1:
        file_transactions = 'operations.json'
    elif you_choice == 2:
        file_transactions = 'transactions.csv'
    elif you_choice == 3:
        file_transactions = 'transactions_excel.xlsx'
    else:
        file_transactions = ''
    return file_transactions

def choice_status() -> str:
    ''' Пользователь выбирает статус интересующих его операций.'''
    status_transactions = ''
    while True:
        you_choice_status = input(text_ru['input_status'])
        you_choice_status.upper()
        if you_choice_status in ['EXECUTED', 'CANCELED', 'PENDING']:
            print( f'{text_ru["filter_by_status"]} "{you_choice_status}"')
            break
        else:
            print(text_ru['filter_by_status_error'],'\n')
    return status_transactions

def main():
    print(text_ru['hey_title'],'\n')
    #file_transactions = choice_file()
    status_transactions = choice_status()




if __name__ == "__main__":
    main()
