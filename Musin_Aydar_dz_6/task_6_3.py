import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    # Ваш код пишите здесь
    with open('users.csv', 'r', encoding='utf-8') as f:
        us_name = list()
        r = f.readline()
        while r:
            us_name.append(r.strip().replace(',', ' '))
            r = f.readline()
    with open('hobby.csv', 'r', encoding='utf-8') as fr:
        us_hobbi = list()
        r = fr.readline()
        while r:
            us_hobbi.append(r.strip().replace(',', ' '))
            r = fr.readline()
    if len(us_name) < len(us_hobbi):
        sys.exit(1)
    else:
        if len(us_name) > len(us_hobbi):
            add_in = len(us_name) - len(us_hobbi)
            for i in range(add_in):
                us_hobbi.append(None)
    user_hobbi_dict = {}

    for num, key in enumerate(us_name):
        user_hobbi_dict[key] = us_hobbi[num]
    return user_hobbi_dict




#    return  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)