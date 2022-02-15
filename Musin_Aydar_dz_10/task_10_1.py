from typing import List
from numpy import sum


class Matrix:

    def reset_str(func):
        def wrapper(*args):
            result = func(*args)
            res = ''
            for el in result:
                res += f'|'
                for i in el:
                    res += f' {i}'
                res += f' |\n'
            return res
        return wrapper


    @classmethod
    def __set_len(cls, matrix):
        st = set()
        for i in matrix:
            st.add(len(i))
        return len(st) < 2


    def __init__(self, matrix: List[List[int]]):
        if type(matrix) == list and len(matrix) > 1 and Matrix.__set_len(matrix):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')


    @reset_str
    def __str__(self):
        return self.matrix

    @reset_str
    def __add__(self, other):
        sum_matrix = sum([self.matrix, other.matrix], axis=0)
        return sum_matrix


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