import math


def calculate(task_name: str, args: dict) -> str:
    try:
        result = globals()[task_name](**args)
        return str(result)
    except AssertionError as error:
        return str(error)


def task_23(x, y) -> float:
    """
    Даны действительные числа x,y. Вычислить значение функции z=ln(x)-x/y.
    """
    assert x > 0, "X должен быть положительным"
    assert y != 0, "Y должен быть не нулём"
    return math.log(x) - x / y


def task_26(x, y) -> float:
    """
    Даны действительные числа x,y. Вычислить значение функции z=arcsin(x)-y.
    """
    assert abs(x) <= 1, "X должен быть по модулю меньше или равен 1"
    return math.asin(x) - y


def task_29(k1, k2, x) -> str:
    """
    На каком из интервалов (-oo;k1),(k1;k2),(k2;+oo)
    лежит точка x? Где k1, k2,
    x – вводимые произвольные числа, причем k1<k2.
    """
    if x < k1:
        return f"(-oo; {k1})"
    elif k1 < x < k2:
        return f"({k1}; {k2})"
    elif k2 < x:
        return f"({k2}; +oo)"
    return f"x = {k1} or x = {k2}"


def task_2(x: float, y: float, z: float) -> float:
    """
    Даны действительные числа x, y, z. Найти минимальное из них.
    """
    return min(x, y, z)


def task_5(
        x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
) -> float:
    """
    Выяснить, существует ли треугольник с координатами вершин А(x1,y1),
    В(x2,y2), C(x3,y3), если да, то найти его площадь.
    """
    square = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    assert square != 0, "Такого треугольника не существует"
    return square
