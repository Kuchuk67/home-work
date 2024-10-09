import  re

def filter_tr_description(transactions: list, text_filter: str) -> list:
    result = []
    for transaction in transactions:
        description = transaction.get('description', '')
        if re.search(text_filter, description, flags=re.IGNORECASE ):
            result.append(transaction)
    return result

