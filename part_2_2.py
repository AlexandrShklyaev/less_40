def decorate_method(method):
    def inner(*args, **kwargs):
        dict_numbers = {str(x): x for x in range(1, 6)}
        dict_numbers.update({'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5})

        if type(args[1]) == str:
            if args[1] in dict_numbers:
                other = dict_numbers[args[1]]
                args = [args[0], other]
                return method(*args, **kwargs)
            raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')
        return method(*args, **kwargs)
    return inner


class Int(int):

    @decorate_method
    def __add__(self, other):
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