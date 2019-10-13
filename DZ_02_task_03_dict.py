"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict."""

seasons = {'Зима' : (1, 2, 12),
           'Весна' : (3, 4, 5),
           'Лето' : (6, 7, 8),
           'Осень' : (9, 10, 11)}

month = input("Выберите месяц: ")

while (not month.isdigit()) or (int(month) > 12) or (int(month) == 0):
    print("Пожалуйста, введите положительное число от 1 до 12")
    month = input("Выберите месяц: ")
else:
    month = int(month)
    for key in seasons.keys():
        if month in seasons[key]:
            print(key)
