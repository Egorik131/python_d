# Задача 2
# Взять любую задачу и настроить в ней запуск скрипта с параметрами. (используем Пайчарм и модуль argparse)

import argparse

def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        quadratic_root_1 = (-b + discriminant ** 0.5) / (2 * a)
        quadratic_root_2 = (-b - discriminant ** 0.5) / (2 * a)
        return quadratic_root_1, quadratic_root_2
    if discriminant == 0:
        return -b / (2 * a)
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Решение квадратного уравнения.")
    parser.add_argument('-a', metavar='a', type=float, help='Ввод коэффициента a.')
    parser.add_argument('-b', metavar='b', type=float, help='Ввод коэффициента b.')
    parser.add_argument('-c', metavar='c', type=float, help='Ввод коэффициента c.')
    args = parser.parse_args()
    print(quadratic_equation(args.a, args.b, args.c))