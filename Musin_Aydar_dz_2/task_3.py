
def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = [i.split(' ') for i in list_in]
    for i in range(len(list_out)):
        list_out[i] = f'Привет, {(list_out[i][-1]).title()}!'

    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)