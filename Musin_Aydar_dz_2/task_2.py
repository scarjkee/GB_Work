import string


def convert_list_in_str(list_in: list) -> str:

    for i in range(len(list_in)):
        if list_in[i].isdigit():
            list_in[i] = f'"{int(list_in[i]):02}"'
        elif list_in[i].startswith('+') or list_in[i].startswith('-'):
            list_in[i] = f'"{list_in[i][0]}{int(list_in[i]):02}"'
    str_out = ' '.join(list_in)

    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
