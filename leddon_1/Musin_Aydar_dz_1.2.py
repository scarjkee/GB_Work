number = int(input("dataset: "))


def sum_list_1(dataset: list) -> int:
    answer = []

    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    for n in my_list:
        x = n ** 3
        z = [int(i) for i in str(x)]
        if sum(z) % 7 == 0:
            answer.append(sum(z))

    return sum(answer)


def sum_list_2(dataset: list) -> int:
    answer = []

    for n in my_list:
        x = n ** 3
        z = [int(i) for i in str(x) + "17"]
        if sum(z) % 7 == 0:
            answer.append(sum(z))

    return sum(answer)


my_list = [i for i in range(number) if i % 2 != 0]

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)
