# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, par0):
        self.par0 = par0


def del_na_nol(par1, par2):
    try:
        if par2 == 0:
            raise OwnError("Деление на ноль недопустимо")
        print(par1 / par2)
    except OwnError as err:
        print(err)


del_na_nol(10, 0)
