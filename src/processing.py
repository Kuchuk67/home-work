def filter_by_state(list_for_filter: list, key_state: str = "EXECUTED") -> list:
    """Функция  возвращает  список словарей,  у которых ключ state соответствует указанному значению.
    ключ state по умолчанию 'EXECUTED'
    filter_by_state(list_dict, state)"""
    return [dict_from_list for dict_from_list in list_for_filter if dict_from_list.get("state") == key_state]


def sort_by_date(list_for_sort: list, reverse_sort: bool = True) -> list:
    """Функция  возвращает  отсортированный список словарей по ключу "date".
    направление сортировки:
    True - по умолчанию — убывание
     False по возрастанию
    sort_by_date(list_for_sort, False)"""
    return sorted(list_for_sort, key=lambda x: x.get("date","0"), reverse=reverse_sort)


x = [
        {"id": 41428829, },
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
print(sort_by_date(x, False))

