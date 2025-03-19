"""
Домашнее задание №1. Функции и структуры данных
"""
"""
    Функция, которая принимает N целых чисел, 
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""    
def power_numbers(input):
    input = input.split(', ')
    return [int(x) ** 2 for x in input]
    
print(power_numbers('1, 2, 4'))

    
"""
    функция, которая на вход принимает список из целых чисел, 
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""    
def filter_numbers(x, str):
    ODD = "odd"
    EVEN = "even"
    PRIME = "prime"
    c = []
    if str == ODD:
        c = filter(odd, x)
    if str == EVEN:
        c = filter(even, x)
    if str == PRIME:
        c = filter(prime, x)
    return list(c)

def even(n):
    return n % 2 == 0
    
def odd(n):
    return n % 2 != 0
    
def prime(a):
    if a == 1: return False
    test = True
    b = a - 1
    while b > 1:
        if not a % b:
            test = False
            break
        b = b - 1
    return a if test else False
    
print(filter_numbers([1, 2, 3, 4, 5], ODD))
print(filter_numbers([1, 2, 3, 4, 5], EVEN))
print(filter_numbers([1, 2, 3, 4, 5], PRIME))