# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def calc(*args):
    try:
        arg_1 = float(input("Укажите аргумент 1: "))
        arg_2 = float(input("Укажите аргумент 2: "))
        calc_1 = arg_1 / arg_2
    # calc_2 = calc_1 / arg_1
    # calc_3 = calc_2 * arg_2
    except ValueError:
        return "Ошибка значения"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return calc_1


# calc_1_val, calc_3_val = calc()
print(f"Результат= {calc()}")
# print(f"Деление = {calc_1_val}; 2-й пример = {calc_3_val}")
