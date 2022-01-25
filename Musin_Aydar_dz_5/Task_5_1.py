
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:


def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for odd in range(1, (number + 1), 2):
        yield odd


n = int(input())
generator = odd_nums(n)

for _ in range(1, n + 1, 2):
    print(f'$Next(Odd_to_{n})\n', f'{next(generator)}')
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration