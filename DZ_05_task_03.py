"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

with open('file_task_03.txt', 'r+') as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.rstrip().split(' '))    # Обрезаем каретку переноса строки и делим по пробелу
print(lst)

print("\nОклад меньше 20000 у сотрудников: ")
summ = 0
for i in range(1, len(lst), 2):
    a = int(lst[i])
    summ += a
    count = len(lst) / 2
    if a <= 20000:
        print(lst[i-1])
middle_profit = summ / count
print("\nСредняя величина дохода сотрудников: ", "%.1f" % middle_profit)

