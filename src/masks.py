def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты
    принимает на  вход  номер карты  и возвращает ее маску
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции"""

    card_number_str = str(card_number)
    if len(card_number_str) < 9:
        return "Error"
    return "{0} {1}** **** {2}".format(card_number_str[0:4], card_number_str[4:6], card_number_str[-4:])


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета
    принимает на вход номер счета и возвращает его маску
    73654108430135874305  # входной аргумент
    **4305  # выход функции"""

    account_number_str = str(account_number)
    if len(account_number_str) < 7:
        return "Error"
    return f"**{account_number_str[-4:]}"
