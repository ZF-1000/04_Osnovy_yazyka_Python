"""Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input() ."""

n = input("Введите количество элементов в списке: ")
while not n.isdigit():
    print("Пожалуйста, введите положительное число")
    n = input("Введите количество элементов в списке: ")
else:
    print("Введите через <<enter>> элементы списка: ")
    n = int(n)
    list = []
    for i in range(0, n):
        elem = input()
        list.append(elem)
    print("Вы ввели список: ", list)
    for j in range(0, len(list)-1):
        if j % 2 == 0:
            list[j], list[j+1] = list[j+1], list[j]

print("Измененный список: ", list)