"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк."""

seconds = input("Введите количество секунд для перевода в формат <<hour : min : sec>>:\n")
while not seconds.isdigit():
    seconds = input("Пожалуйста, введите целое положительное число: ")
else:
    seconds = int(seconds)
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
input()
