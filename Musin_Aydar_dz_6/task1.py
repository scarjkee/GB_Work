from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    if 'GET' in line:
        r_a = line.split('- -')[0]
        r_t = line.split('] "')[1].split(' /')[0]
        r_r = line.split('GET ')[1].split(' HTTP')[0]
        return r_a, r_t, r_r
    elif 'HEAD' in line:
        r_a = line.split('- -')[0]
        r_t = line.split('] "')[1].split(' /')[0]
        r_r = line.split('HEAD ')[1].split(' HTTP')[0]
        return r_a, r_t, r_r


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line:
            break
        list_out.append(get_parse_attrs(line))

pprint(list_out)