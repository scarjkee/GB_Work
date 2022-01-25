#Задание 5

def get_uniq_numbers(src: list):
    # надо создать множество не повторяющихся чисел из списка
    ch = []
    # for i in src:
    #     if src.count(i) == 1: #ищем количество повторений равное 1
    #         ch.append(i)      # записываем его в ноый список *порядок сохранится
    ch = [i for i in src if src.count(i) == 1]
    return ch


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))