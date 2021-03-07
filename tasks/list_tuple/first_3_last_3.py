"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает первые 3 и последние 3 элемента в списке
"""


def get_first_3_last_3(collection: list) -> tuple:

    first_3 = collection[:3]
    last_3 = collection[4:]
    return first_3, last_3


if __name__ == '__main__':
    assert ([1, 2, 3], [5, 6, 7]) == get_first_3_last_3([1, 2, 3, 4, 5, 6, 7])
    print('Решено!')
