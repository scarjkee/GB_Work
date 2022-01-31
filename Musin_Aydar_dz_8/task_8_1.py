import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r"(?P<username>\w+\S*?)@(?P<domain>\w+\.\w+)")
    dict_re_mail = RE_MAIL.search(email)
    if dict_re_mail:
        result = dict_re_mail.groupdict()
        return result
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
