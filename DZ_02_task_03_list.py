"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict."""


list = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
season = ('Зима', 'Весна', 'Лето', 'Осень')

month = input("Выберите месяц: ")

while (not month.isdigit()) or (int(month) > 12) or (int(month) == 0):
    print("Пожалуйста, введите положительное число от 1 до 12")
    month = input("Выберите месяц: ")
else:
    month = int(month)
    # i = 0
    for i in range(0, len(season)):
        if month in list[i]:
            print(season[i])
            break
