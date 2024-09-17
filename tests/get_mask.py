def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты
    принимает на  вход  номер карты  и возвращает ее маску
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции"""

    #card_number_str = str(card_number)
    #replace_stars = f'{2 * "*"} {4 * "*"}'
    #return f"{card_number_str[0:4]} {card_number_str[4:6]}{replace_stars} {card_number_str[-4:]}"

    #card_number_str = str(card_number)
    #mask_card_number_list = []
    #mask_card_number_list.append(card_number_str[0:4])
    #mask_card_number_list.append(card_number_str[4:6] + '**')
    #mask_card_number_list.append('****')
    #mask_card_number_list.append(card_number_str[-4:])
    #return  " ".join(mask_card_number_list)

    card_number_str = str(card_number)
    return "{0} {1}** **** {2}".format(card_number_str[0:4], card_number_str[4:6], card_number_str[-4:])
    #return ' '.join(card_number_str[i:i + 4] for i in range(0, len(card_number_str), 4) )

def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета
    принимает на вход номер счета и возвращает его маску
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"



# для проверки
print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))