from src import widget

# для проверки
def add(x, y):
    return x + y

print(widget.mask_account_card('Visa Platinum 7000792289606361'))
print(widget.mask_account_card('Счет f73654108430135874305'))

print(widget.get_date('2024-03-11T02:26:18.671407'))
