class Clothes:

    def calculate(self):
        pass


class Coat(Clothes):

    def __init__(self, size: float):
        if isinstance(size, float) or isinstance(size, int) and size > 0:
            self.size = size
        else:
            raise ValueError

    @property
    def calculate(self):
        return f'{self.size / 6.5 + 0.5 : .2f}'

class Costume(Clothes):

    def __init__(self, height: float):
        if isinstance(height, float) or isinstance(height, int) and height > 0:
            self.height = height
        else:
            raise ValueError

    @property
    def calculate(self):
        return f'{2 * self.height + 0.3: .2f}'

if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3