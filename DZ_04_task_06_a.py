"""Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools ."""

from itertools import count

print("<<Бесконечный итератор целых чисел, начиная с указанного>>")
n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')
