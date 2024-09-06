from src import masks


def mask_account_card(customer_card: str) -> str:
    """Возвращает строку с названием платежной системы или счета
    и с замаскированным номером."""

    customer_card_list = customer_card.split(" ")
    # последний элемент списка customer_card_list это номер карты или счета
    number = int(customer_card_list.pop())
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

    date_format_dd_mm_yyyy = f"{date_format_full[5:7]}.{date_format_full[8:10]}.{date_format_full[:4]}"
    return date_format_dd_mm_yyyy
