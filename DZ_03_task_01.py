"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def division_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Делить на "ноль" нельзя!')
        return 0.0

print("Программа деления чисел a / b")
var_1 = float(input("Введите число a: "))
var_2 = float(input("Введите число b: "))

print("a / b = ", division_func(var_1, var_2))
