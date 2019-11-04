"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class OfficeEquipmentWarehouse:
    """Класс, описывающий склад оргтехники"""
    # print("Класс, описывающий склад оргтехники")


class OfficeEquipment:
    """Базовый класс оргтехники"""
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    """Класс принтер"""

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type

    @staticmethod
    def name():
        print("<<Принтер>>", end=' ')

    def type_printer(self):
        return self.pr_type


class Scanner(OfficeEquipment):
    """Класс сканер"""

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor

    @staticmethod
    def name():
        print("<<Сканер>>", end='  ')

    def type_sensor(self):
        return self.sc_sensor


class Xerox(OfficeEquipment):
    """Класс ксерокс"""
    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi

    @staticmethod
    def name():
        print("<<Ксерокс>>", end=' ')

    def wi_fi_module(self):
        return self.xer_wi_fi


print("\n")
p = Printer('Canon', 'white', 'струйный')
p.name()
print("\tпроизводитель:", p.producer, "\tцвет:", p.color, "\tтип принтера: ", p.type_printer())

s = Scanner('Epson', 'black', 'CIS')
s.name()
print("\tпроизводитель:", s.producer, "\tцвет:", s.color, "\tтип сенсора: ", s.type_sensor() )

x = Xerox('Hanp', 'white', 'есть')
x.name()
print("\tпроизводитель:", x.producer, "\tцвет:", x.color, "\tWi-Fi модуль: ", x.wi_fi_module())