def iss(object_first, object_second) -> None:
    """ выводит для двух объектов сравнения по значению и по ссылке"""
    equal_value = "разные"
    equal_address = "разные адреса"
    if object_first == object_second:  # сравниваем значения
        equal_value = "одинаковые"
    if object_first is object_second:  # сравниваем ссылки
        equal_address = "один и тот же адрес"

    print(f"Две переменные ссылаются на {equal_address} в памяти, имеют {equal_value} значения.")
    print(f"id первой переменной: {id(object_first)}")
    print(f"id второй переменной: {id(object_second)}")
    print(f"Значение первой переменной: {object_first}")
    print(f"Значение второй переменной: {object_second}")