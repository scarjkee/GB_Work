# *задание 2

def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""

    for odd in range(1, (number + 1), 2):
        nums_list.append(odd)
    return nums_list

nums_list = []
n = int(input())
generator = iter(odd_nums(n))

for _ in range(1, n + 1, 2):
    print(next(generator))
