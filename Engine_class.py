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
    motor = Engine(input('Тип двигателя v6/v8/v10: '), int(input('Мощность двигателя, л.с.: ')), input('Наличие турбины +/-: '))
    if motor.turbine != '+' and motor.turbine != '-' or motor.engine_type != 'v6' and motor.engine_type != 'v8' and motor.engine_type != 'v10':
        print('Неверный ввод параметров')
    else:
        print('Мощность мотора: = ', motor.generate_power())
except ValueError:
    print('Неверный ввод мощности двигателя')