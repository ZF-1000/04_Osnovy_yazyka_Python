"""Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools ."""

from itertools import cycle

list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
for i in cycle(list):
    print(i, end=' ')
