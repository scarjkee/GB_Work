from typing import List


class Matrix:

    # @classmethod
    # def __set_len(cls, matrix):
    #     st = set()
    #     for i in matrix:
    #         st.add(len(i))
    #     return len(st) < 2


    def __init__(self, matrix: List[List[int]]):
        if isinstance(matrix, list) and isinstance(matrix[0], list) and all(map(lambda l: len(matrix[0]) == len(l), matrix)):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')


    # @reset_str
    def __str__(self):
        res = ''
        for el in self.matrix:
            res += f'|'
            for i in el:
                res += f' {i}'
            res += f' |\n'
        return res

    # @reset_str
    def __add__(self, other):
        sum_matrix = ''
        for i, j in zip(self.matrix, other.matrix):
            el = ''
            sum_matrix += f'|'
            for el1 in zip(i, j):
                el = sum(el1)
                sum_matrix += f' {el}'
            sum_matrix += f' |\n'
        return sum_matrix


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2, 5], [3, 4, 5], [5, 6, 5]])
    second_matrix = Matrix([[6, 5, 5], [4, 3, 5], [2, 1, 5]])
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