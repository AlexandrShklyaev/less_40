# перегрузка метода add
class Int(int):
    # расширяет класс int: добавлена возможность сложить число с числом в стоковом формате
    def __init__(self, other):
        super(Int, self).__init__()
        self.dict_numbers = {str(x): x for x in range(1, 6)}
        self.dict_numbers.update({'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5})

    def __add__(self, other) -> int:
        if type(other) == str:
            if other in self.dict_numbers:
                return super().__add__(self.dict_numbers[other])
            raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')
        return super().__add__(other)


if __name__ == '__main__':
    # использование
    x = Int(5)
    print(x + '5')  # 10
    print(x + 'один')  # 6
    print(x + 'пять')  # 10
    print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    # print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    # print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
