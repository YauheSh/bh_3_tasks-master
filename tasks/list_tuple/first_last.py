"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
вернуть первый и последний элемент в списке
"""


def get_first_last(collection: list) -> tuple:
    first = collection[0]
    last = collection[-1]
    return first, last


if __name__ == '__main__':
    assert (1, 7) == get_first_last([1, 2, 3, 4, 5, 6, 7])
    print('Решено!')
