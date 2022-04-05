class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def calculator():
    try:
        number_1 = float(input('Введи первое число: '))
        operation = input('Введи операцию: ')
        number_2 = float(input('Введи второе число: '))
        if operation == '/' and number_2 == 0:
           raise MyError('ОШИБКА! Деление на 0')
        if operation == '+':
            res = number_1 + number_2
        elif operation == '-':
            res = number_1 - number_2
        elif operation == '*':
            res = number_1 * number_2
        elif operation == '/':
            res = number_1 / number_2
        print ('Результат:', res)
    except MyError as e:
        print(e)
    except UnboundLocalError:
        print('ОШИБКА! Неверно введена операция')
    except ValueError:
        print('ОШИБКА! Неверно введено число')



if __name__ == '__main__':
    calculator()