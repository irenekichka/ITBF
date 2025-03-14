"""
Домашнее задание №1
Функции и структуры данных
"""
 """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    
def power_numbers(n):
    for a in range(0, len(n)):
        n[a] = n[a]**2
        print(n)
power_numbers ([1, 2, 5, 7])


    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
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
    
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(x, str):
    c = []
    if str == ODD:
        for i in x:
            if i%2!=0:
                c.append(i)
    if str == EVEN:
        for i in x:
            if i%2==0:
                c.append(i)
    if str == PRIME:
        for i in x:
            if prime(i):
                c.append(i)
    print(c)

x = [1, 2, 3, 4, 5]
filter_numbers(x, PRIME)



