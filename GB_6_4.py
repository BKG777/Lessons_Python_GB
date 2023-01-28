# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем на {direction}')
        else:
            print(f'Не можем повернуть {direction} - мы стоим на месте')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('!!!Внимание! Превышение скорости, сбросьте скрорость до 60 км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print('!!!Внимание! Превышение скорости, сбросьте скрорость до 40 км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        self.is_police = True

def test_drive(test):
    print(f"Начинаем тест-драйв {'полицейского' if test.is_police else 'гражданского'} автомобиля {test.name}, цвет {test.color}")
    test.go(40)
    test.show_speed()
    test.turn('направо')
    test.stop()
    test.show_speed()
    test.turn('налево')
    test.go(60)
    test.show_speed()
    test.go(120)
    test.show_speed()
    test.stop()
    print("Тест-драйв окончен", end="\n\n")


car = Car('белый', 'Kia', False)
test_drive(car)

polo = TownCar('коричневый', 'Volkswagen Polo')
test_drive(polo)

veyron = SportCar('желтый', 'Bugatti Veyron')
test_drive(veyron)

largus = WorkCar('красный', 'Lada')
test_drive(largus)

mondeo = PoliceCar('синий', 'Ford')
test_drive(mondeo)