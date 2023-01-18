# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [i for i in range(100, 1001, 2)]
print(my_list)
res_s = reduce(lambda i_1, i_2: i_1 * i_2, my_list)
print(res_s)

# Проверка
my_list_1 = [i for i in range(1, 4, 1)]
print(my_list_1)
res_s1 = reduce(lambda i_1, i_2: i_1 * i_2, my_list_1)
print(res_s1)
