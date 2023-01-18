# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

import sys

f_obj, name_v, rate, hours, bonus = sys.argv
print(f_obj)


def simple_calc(name_v, rate, hours, bonus):
    try:
        print(f'Сотрудник {name_v} заработал {int(rate) * int(hours) + int(bonus)}')
    except TypeError:
        print('Несоотвествующий тип данных')
        exit()


simple_calc(name_v, rate, hours, bonus)
