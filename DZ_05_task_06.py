"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран."""

file = open("file_task_06.txt")
onstring = file.read().split("\n")[:-1]
print(onstring)

dict = {}

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
print(dict)

print("\n<< Общее количество занятий по предметам >>")
for i in dict:
    list = dict[i]
    summ = 0
    for j in range(0, len(list)):
        summ += int(list[j])
    print(i, ":", summ)
file.close()
