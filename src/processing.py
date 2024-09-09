def filter_by_state(list_for_filter: list, key_state: str = "EXECUTED") -> list:
    """Функция  возвращает  список словарей,  у которых ключ state соответствует указанному значению.
    ключ state по умолчанию 'EXECUTED'
    filter_by_state(list_dict, state)"""
    return [
        dictionary_from_list for dictionary_from_list in list_for_filter if dictionary_from_list["state"] == key_state
    ]


def sort_by_date(list_for_sort: list, reverse_sort: bool = True) -> list:
    """Функция  возвращает  отсортированный список словарей по ключу "date".
    направление сортировки:
    True - по умолчанию — убывание
     False по возрастанию
    sort_by_date(list_for_sort, False)"""
    return sorted(list_for_sort, key=lambda x: x.get("date"), reverse=reverse_sort)
