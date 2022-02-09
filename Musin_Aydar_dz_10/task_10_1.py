from typing import List
from numpy import sum


class Matrix:

    @classmethod
    def set_len(cls, matrix):
        st = set()
        for i in matrix:
            st.add(len(i))
        return len(st) < 2

    def __init__(self, matrix: List[List[int]]):
        if type(matrix) == list and len(matrix) > 1 and Matrix.set_len(matrix):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    # def decor(func):
    #     def wrapper(self):
    #         result = func
    #         res = ''
    #         for el in self:
    #             res += f'|'
    #             for i in el:
    #                 res += f' {i}'
    #             res += f' |\n'
    #         return res
    #     return wrapper


    def __str__(self):
        res = ""
        for el in self.matrix:
            res += f'|'
            for i in el:
                res += f' {i}'
            res += f' |\n'
        return res

    def __add__(self, other):
        sum_matrix = sum([self.matrix, other.matrix], axis=0)
        res = ""
        for el in sum_matrix:
            res += f'|'
            for i in el:
                res += f' {i}'
            res += f' |\n'

        return res

    def reset_str(self, arg):
        res = ""
        for el in arg:
            res += f'|'
            for i in el:
                res += f' {i}'
            res += f' |\n'
        return res
if __name__ == '__main__':
    first_matrix = Matrix([[1, 2, 8], [3, 4, 7], [5, 6, 6]])
    second_matrix = Matrix([[6, 5, 1], [4, 3, 2], [2, 1, 3]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """