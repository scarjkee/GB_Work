#Задание 3

import requests
from datetime import datetime


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    result_value = None  ## здесь должно оказаться результирующее значение float
    char_code = (
    'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT', 'CAD',
    'KGS', 'KGS', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK',
    'CHF', 'ZAR', 'KRW', 'JPY')
    num = 0
    end = 500

    cbr = "http://www.cbr.ru/scripts/XML_daily.asp"
    responce = requests.get(cbr).text.split('ID')

    p = [i for i in responce]

    for i in range(len(p)):
        p[i] = p[i].replace('<', ' ')
        p[i] = p[i].replace('>', ' ')
        p[i] = p[i].replace('/', '')
    d = ';\n'.join(p)
    d1 = d.split()
    if char_code.count(code) > 0:

        for i in d1:
            num += 1
            if i == code:
                end = num
                while num < (len(d1)):
                    if d1[num] == 'Value':
                        result_value = d1[num + 1]
                        break
                    num += 1
            elif end < num:
                break
    else:
        result_value = None
    return result_value

char = input(f'Введите значение валюты: ').upper()
print(currency_rates(char))