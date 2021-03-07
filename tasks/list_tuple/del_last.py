"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая удалит последний элемент
"""
from copy import deepcopy


def del_last(collection: list) -> list:
    collection_copy = deepcopy(collection)
    collection_copy.pop()
    return collection_copy


if __name__ == '__main__':
    assert 2 not in del_last([1, 3, 5, 2])
    print('Решено!')
