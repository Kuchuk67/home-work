from src import masks

def mask_account_card(customer_card: str) -> str:
    '''Возвращает строку с названием платежной системы или счета
    и с замаскированным номером.'''

    customer_card_list = customer_card.split(" ")
    # последний элемент списка customer_card_list это номер карты или счета
    number = int(customer_card_list.pop())
    if customer_card_list[0] == 'Счет':
        mask_number = masks.get_mask_account(number)
    else:
        mask_number = masks.get_mask_card_number(number)
    customer_card_list.append(mask_number)
    mask_customer_card = " ".join(customer_card_list)
    return mask_customer_card
