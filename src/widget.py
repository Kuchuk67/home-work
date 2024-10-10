import re
from datetime import datetime

from src import masks


def mask_account_card(customer_card: str) -> str:
    """Возвращает строку с названием платежной системы или счета
    и с замаскированным номером."""

    customer_card = re.sub(r"\s+", " ", customer_card)
    customer_card_list = customer_card.split(" ")
    if len(customer_card_list) < 2:
        return "Error"
    # последний элемент списка customer_card_list это номер карты или счета
    number_str = customer_card_list.pop()
    number_str = "".join(re.findall("[0-9]+", number_str))
    if number_str == "":
        return "Error"
    number = int(number_str)

    if customer_card_list[0] == "Счет":
        mask_number = masks.get_mask_account(number)
    else:
        mask_number = masks.get_mask_card_number(number)

    customer_card_list.append(mask_number)
    mask_customer_card = " ".join(customer_card_list)
    return mask_customer_card


def get_date(date_format_full: str) -> str:
    """возвращает строку с датой в формате  "ДД.ММ.ГГГГ"
    ввод  2024-03-11T02:26:18.671407"""

    format = "%Y-%m-%dT%H:%M:%S.%f"
    try:
        date_format_date = datetime.strptime(date_format_full, format)

        date_format_date = date_format_date.strftime("%d.%m.%Y")
    except Exception:
        date_format_date = ''

    return date_format_date

#print(get_date ('2019-01-05T00:52:30.108534'))