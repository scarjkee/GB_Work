from functools import wraps

# import sys
#
#
# def type_logger(func):
#     @wraps(func)
#     def wrapper(args):
#         program, args = args
#         print(args)
#         if args.isdigit():
#             args = int(args)
#             print(type(args))
#             result = func(args)
#         else:
#             err = f'введите цело численное значение int!!!'
#             raise ValueError(err)
#         return result
#     return wrapper
#
#
# @type_logger
# def calc_code(argv):
#     return argv ** 3
#
#
# if __name__ == '__main__':
#     a = calc_code(5)
#     print(calc_code.__name__)
#     exit(calc_code(sys.argv))

#
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        result = []
        for i in args:
            try:
                if i == int(i):
                    result2 = func(i)
                    result.append(f'{func.__name__} {i}:{type(i)}, {result2}')
            except:
                    ValueError('введенно не цело численное число!')
                    result.append(f'{func.__name__} {i}:{type(i)}')
        return result
    return wrapper


@type_logger
def calc_code(x):
    '''
    :param x: целочислноое значение
    :return: куб полученного аргумента
    '''
    return x ** 3


a = calc_code(5, 6, 7, 's', -5)
print(a)