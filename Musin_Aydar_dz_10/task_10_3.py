class Cell:

    def __init__(self, cells: int):
        if not isinstance(cells, int) and cells > 0:
            raise TypeError('Не верное значение')
        self.cells = cells

    def make_order(self, number: int) -> str:
        full = self.cells // number
        out = self.cells % number
        res = "'''\n"
        for _ in range(full):
            res += f'{number * "*"}\n'
        if out != 0:
            res += f'{"*" * out}\n'
        res += "'''"
        return res

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')
        ot = other
        if isinstance(other, Cell):
            ot = other.cells
        return Cell(self.cells + ot)

    def __sub__(self, other):
        ot = other
        if not isinstance(other, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')
        ot = other.cells
        if not self.cells >= ot:
            raise ValueError('Не допустимая операция')
        return Cell(int(self.cells - ot))

    def __mul__(self, other):
        ot = other
        if not isinstance(other, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')
        ot = other.cells
        if ot == 0:
            raise ZeroDivisionError('Не допустимая операция')
        return Cell(int(self.cells * ot))

    def __truediv__(self, other):
        ot = other
        if not isinstance(other, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')
        ot = other.cells
        if ot == 0:
            raise ZeroDivisionError('Не допустимая операция')
        return Cell(int(self.cells / ot))

    def __floordiv__(self, other):
        ot = other
        if not isinstance(other, (int, Cell)):
            raise TypeError('действие допустимо только для экземпляров того же класса')
        ot = other.cells
        if ot == 0:
            raise ZeroDivisionError('Не допустимая операция')
        return Cell(int(self.cells // ot))


# реализация других магических методов по заданию


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса
