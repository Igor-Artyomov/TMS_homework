class Engine:
    def __init__(self, engine_type, horsepower, turbine):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.turbine = turbine
        self.acceleration = 0
        self.engine_power = 0
        

    def generate_power(self):
        if self.engine_type == 'v6':
            self.acceleration = 0.2
        elif self.engine_type == 'v8':
            self.acceleration = 0.4
        elif self.engine_type == 'v10':
            self.acceleration = 0.6

        if self.turbine == '+':
            self.engine_power = self.horsepower * self.acceleration / 0.8
        elif self.turbine == '-':
            self.engine_power = self.horsepower * self.acceleration
                   
            
        return self.engine_power

try:
    motor = Engine(input('Тип дв v6/v8/v10: '), int(input('Мощность дв, л.с.: ')), input('Наличие тур +/-: '))
    if motor.turbine != '+' and motor.turbine != '-' or motor.engine_type != 'v6' and motor.engine_type != 'v8' and motor.engine_type != 'v10':
        print('Неверный ввод параметров')
    else:
        print('Мощность мотора:', motor.generate_power())
except ValueError:
    print('Неверный ввод мощности двигателя')



class Wheel:
    def __init__(self, wheel_radius, wheel_weight):
        self.wheel_radius = wheel_radius
        self.wheel_weight = wheel_weight


wheel = Wheel(int(input('Радиус кол: ')), int(input('Вес кол: ')))

if wheel.wheel_radius < 16 or wheel.wheel_radius > 21:
    print('Неверный радиус колеса')



class Car(Engine, Wheel):
    def __init__(self, engine_type, horsepower, turbine, wheel_radius, wheel_weight, car_type, distance):
        
        self.distance = distance
        self.car_type = car_type
        self.race_time = 0

        if self.car_type == 'sedan':
            self.car_weight = 1200
        elif self.car_type == 'suv':
            self.car_weight = 1500
        elif self.car_type == 'truck':
            self.car_weight = 1800

    
    def start_engine(self):
        self.engine_status = input('Завести двигатель +/-: ')
        return self.engine_status


    def move(self):
        self.race_time = (self.car_weight + 4 * self.wheel_weight) / self.engine_power * self.distance
        return self.race_time


if __name__ == '__main__':
    my_car = Car(input('Тип двигателя v6/v8/v10: '), int(input('Мощность двигателя, л.с.: ')), input('Наличие турбины +/-: '), int(input('Радиус колеса: ')), int(input('Вес колеса: ')), input('Тип кузова: '), int(input('Дистанция: ')))
    print('Время заезда:', my_car.move())