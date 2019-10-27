"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Время перехода между
режимами должно составлять 7 и 2 секунды. Проверить работу примера, создав экземпляр и
вызвав описанный метод."""

import time

class TrafficLight:

    __traffic_light_color = "Светофор"

    def running(self):
        while True:
            print("Red light")
            time.sleep(7)
            print("Yellow light")
            time.sleep(2)
            print("Green light")
            time.sleep(7)


a = TrafficLight()
a.running()
