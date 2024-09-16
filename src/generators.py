def filter_by_currency(transactions, currency):
    for dict_transaction in transactions:
        #if   dict_transaction.get('operationAmount'['currency']['code']) == currency:
        if   dict_transaction.get('operationAmount', {}).get('currency', {}).get('code')  == currency:

            yield dict_transaction
    #return []



