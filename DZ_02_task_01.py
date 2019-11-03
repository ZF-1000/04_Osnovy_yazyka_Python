"""Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

print("Привет, программист!")
name = input("Как Вас зовут?\n ")
print(name, ", добро пожаловать в мир Python!")

answer = ''
while answer != 'q':  # != - не равно
    answer = input("\nДавайте поработаем? (Y/N)")
    if answer == 'Y':
        print("Информация о типе данных какого элемента списка вы хотите узнать?")
        test = [5, 1.3, complex(4,6), "простая строка", [0, 1, 2, 3, 4, 5], (0, 1, 2, 3, 4, 5), {0, 1, 5, 0, 5, 2}]
        test.append({"key_1": 500, 2: 400, "key_3": True, 4: None})
        test.append(bool(20))
        test.append(bytes([10, 20, 30, 40]))
        test.append(None)
        print(test)

        do = int(input("\nУкажите индекс элемента списка: "))
        if do == 0:
            print(test[0], type(test[0]), "Тип данных: Целое число")
        elif do == 1:
            print(test[1], type(test[1]), "Тип данных: Вещественное число")
        elif do == 2:
            print(test[2], type(test[2]), "Тип данных: Комплексное число")
        elif do == 3:
            print(test[3], type(test[3]), "Тип данных: Строка")
        elif do == 4:
            print(test[4], type(test[4]), "Тип данных: Список")
        elif do == 5:
            print(test[5], type(test[5]), "Тип данных: Кортеж")
        elif do == 6:
            print(test[6], type(test[6]), "Тип данных: Множество")
        elif do == 7:
            print(test[7], type(test[7]), "Тип данных: Словарь")
        elif do == 8:
            print(test[8], type(test[8]), "Тип данных: Логический")
        elif do == 9:
            print(test[9], type(test[9]), "Тип данных: Байтовые строки")
        elif do == 10:
            print(test[10], type(test[10]), "Тип данных: NoneType")


    elif answer == 'N':
        print("До свидания!")
        input()
        exit(0)
    else:
        print("Неверный символ. Завершение работы программы")
        input()
        exit(0)






