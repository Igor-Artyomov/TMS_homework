import time

from functools import reduce


def hw_lection_5_decorator(func):
    """"
    Принимает 3 числа и выводит результат математического выражения
        обрамленный символами --- и ///
        
        a (int): первое число
        b (int): второе число
        c (int): третье число
    
    """
    def wrapper(*args):
        print('-----------------------')
        func(*args)
        print('///////////////////////')
    return wrapper

@hw_lection_5_decorator
def main_function(a, b, c):
    print((a + b) * c)



def lambda_func():
    """
    Lambda-функция, возвращает список, значение элементов которого
    на 12 больше каждого значения элементов исходного списка
    """
    print(list(map(lambda x: x + 12, [10, 166, 52, 48])))



def burger(func):
    """
    Декоратор, который возвращает список ингредиентов бургера
    
    ing1 (str): первый ингредиент
    ing2 (str): второй ингредиент
    ing3 (str): третий ингредиент
    ing4 (str): четвертый ингредиент
    """
    def wrapper(**kwargs):
       func(**kwargs)
    return wrapper


@burger
def ingredients(ing1 = 'помидор', ing2 = 'котлета', ing3 = 'салат', ing4 = 'булка'):
    print(ing1)
    print(ing2)
    print(ing3)
    print(ing4)



def function_name(func):
    """
    Декоратор, который возвращает имя декорируемой функции и ее аргументы
    """
    def wrapper(*args):
        print('Имя функции: ' + str(func.__name__), 'Аргументы функции: ' + str(args), sep = '\n')
        func(*args)
    return wrapper


@function_name
def funct(x, y):
    pass



def countdown(func):
    """
    Декоратор, который начинает обратный отсчет перед выполнением функции
    """
    def wrapper(num_of_secs):
        while num_of_secs:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(min_sec_format, sep = '/n')
            time.sleep(1)
            num_of_secs -= 1
        func(num_of_secs)
    return wrapper


@countdown
def main_func(a):
    print('Я просто функция')



def round_numbers():
    """
    Функция, которая принимает список дробных чисел и округляет их до целого значения
    """
    values = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
    round_number = map(lambda number: round(number), values)
    print(list(round_number))



def number_larger_80():
    """
    Функция, которая принимает список целых чисел и возвращает списко из
    чисел больше 80 на основании принятого
    """
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    filter_object = filter(lambda number: number > 80, scores)
    print(list(filter_object))



def palindrom():
    """
    Функция, которая принимает список слов и возвращает список из палиндромов,
    входящих в принятый список
    """
    values = ['demigod', 'rewire', 'madam', 'fortran', 'python', 'xamarin', 'salas', 'PHP']
    filter_object = filter(lambda word: word == word[::-1], values)
    print(list(filter_object))



def product_of_numbers():
    """
    Функция, которая принимает список из целых чисел и возвращает их произведение
    """
    values = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, values)
    print(product)



def max_number1():
    """
    Функция, которая принимает список из целых чисел и возвращает максимольное число
    из списка. Реализована с вомощью функции filter
    """
    values=[3, 5, 2, 4, 7, 1]
    filter_object = filter(lambda number: number == max(values), values)
    print(list(filter_object)[0])



def max_number2():
    """
    Функция, которая принимает список из целых чисел и возвращает максимольное число
    из списка. Реализована с вомощью функции reduce
    """
    values=[3, 5, 2, 4, 7, 1]
    max_number = reduce(lambda x, y: x if x > y else y, values)
    print(max_number)



def word_checking():
    """
    Функция, которая получает список и подсчитывает количество слов капитан в нем
    """
    sentences = ['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан']
    counter = map(lambda x: x.count('капитан'), sentences)
    print(sum(counter))



if __name__ == '__main__':
    main_func(5)