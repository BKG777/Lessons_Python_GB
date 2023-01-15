# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    try:
        arg_1 = float(input("Укажите аргумент 1: "))
        arg_2 = float(input("Укажите аргумент 2: "))
        arg_3 = float(input("Укажите аргумент 3: "))
    except ValueError:
        print("Ошибка значения")
    x = [arg_1, arg_2, arg_3]
    x.remove(min(x))
    return sum(x)


print(my_func())
