"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""


print("----- Программа поиска наибольшей цифры в числе -----")
number = input("Введите целое положительное число: ")
while not number.isdigit():
    number = input("Пожалуйста, введите целое положительное число: ")
else:
    number = int(number)
    max = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > max:
            max = number % 10
        number = number // 10
print("Максимальная цифра в ведёном числе:", max)
input()