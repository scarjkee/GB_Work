
def convert_time(duration: int) -> str:
    day = duration // 86400
    hour = (duration - (day * 86400)) // 3600
    minutes = (duration - (3600 * (duration // 3600))) // 60
    seconds = (duration - (3600 * (duration // 3600))) - (minutes * 60)


    if day > 0:
        result = f'{day} дн {hour} час {minutes} мин {seconds} сек'
    elif hour > 0:
        result = f'{hour} час {minutes} мин {seconds} сек'
    elif minutes > 0:
        result = f'{minutes} мин {seconds} сек'
    else:
        result = f'{seconds} сек'
    return result

duration = int(input("duration: "))
result = convert_time(duration)
print(result)
