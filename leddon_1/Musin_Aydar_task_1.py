# ДЗ № 1


def convert_time(duration: int) -> str:
    timeout = []
    spisok = []
    day = duration // 86400
    spisok.append(day)
    hour = (duration - (day * 86400)) // 3600
    spisok.append(hour)
    minutes = (duration - (3600 * (duration // 3600))) // 60
    spisok.append(minutes)
    seconds = (duration - (3600 * (duration // 3600))) - (minutes * 60)
    spisok.append(seconds)

    for i in spisok:
        if i > 0 or len(timeout) > 0 :
            timeout.append(i)
    spisok = timeout

    if len(spisok) > 3:
        answer = (f"""{str(spisok[0])} дн {spisok[1]} час {spisok[2]} мин {spisok[3]} сек""")
    elif len(spisok) > 2:
        answer = (f"""{spisok[0]} час {spisok[1]} мин {spisok[2]} сек""")
    elif len(spisok) > 1:
        answer = (f"""{spisok[0]} мин {spisok[1]} сек""")
    else:
        answer = (f"""{spisok[0]} сек""")
    return answer




duration = int(input("duration: "))
result = convert_time(duration)
print(result)
