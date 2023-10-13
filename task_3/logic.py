import math


def calculate(task_name: str, args: str) -> str:
    try:
        result = globals()[task_name](args)
        return str(result)
    except Exception as error:
        return str(error)


def task_23(args: str) -> list[float]:
    """
    Вывести на печать значения функции z=sin(x)+cos(x),
    находящиеся в интервале (-0,3;0,7)
    для x изменяющегося на отрезке [-4,6] с шагом 0,91
    """
    y_bounds = (-0.3, 0.7)
    x_values = [x / 100 for x in range(-400, 601, 91)]
    z_list = [math.sin(x) + math.cos(x) for x in x_values]
    z_list = list(filter(lambda z: y_bounds[0] <= z <= y_bounds[1], z_list))
    return z_list


def task_26(args: str) -> tuple[int, float]:
    """
    Hайти пеpвый член последовательности ln(9n/(n*n+1), меньший 0,
    для n изменяющегося на следующим обpазом: n=1,2,3...
    """
    def seq(n: int) -> float:
        return math.log((9 * n) / (n * n + 1))

    i = 1
    while (x_i := seq(i)) >= 0:
        i += 1
    return i, x_i


def task_29(args: str) -> list[float]:
    """
    Напечатать значения функции Y=sqrt(2*x^2 - x^3) для произвольных x,
    вводимых с клавиатуры.
    При вводе числа, не входящего в область определения функции,
    ввод и печать прекратить.
    """
    numbers: list[float] = [float(x) for x in args.split()]
    result = []
    for x in numbers:
        if not (0 <= x <= 2):
            break
        y = math.sqrt(2 * x ** 2 - x ** 3)
        result.append(y)
    return result


def task_2(args: str) -> list[float]:
    """
    Вывести на печать значения функции z=tg(2x)-sin(x)
    для x изменяющегося на отрезке [-3, 3] с шагом 0,3.
    """
    x_values = [x / 10 for x in range(-30, 31, 3)]
    z_list = [math.tan(2 * x) - math.sin(x) for x in x_values]
    return z_list


def task_5(args: str) -> bool:
    """
    Определить, является ли натуpальное число N степенью числа 5 или нет.
    """
    n = int(args)
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 5 != 0:
        return False
    return task_5(str(n // 5))
