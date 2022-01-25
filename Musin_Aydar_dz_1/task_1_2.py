
number = int(input("dataset: "))


def sum_list_1(dataset: list) -> int:
    answer = 0
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    for n in dataset:
        z = []
        j = 0
        x = n
        z = [int(i) for i in str(x)]
        for i in z:
            j += int(i)
        if j % 7 == 0:
            answer += x

    return answer

def sum_list_2(dataset: list) -> int:
    answer_2 = 0
    """К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7"""
    for n in dataset:
        z = []
        j = 0
        x = n + 17
        z = [int(i) for i in str(x)]
        for i in z:
            j += int(i)
        if j % 7 == 0:
            answer_2 += x

    return answer_2
my_list = [i**3 for i in range(number) if i % 2 != 0]

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)
