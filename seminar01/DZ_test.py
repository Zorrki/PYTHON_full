Не все тесты пройдены, есть ошибки :(


Количество затраченных попыток: 6

Время выполнения: 1.9937 сек

Общая статистика

Всего тестов: 6. Пройдено: 1. Не пройдено: 5.

Подробную информацию по каждому тесту смотрите ниже.
Тест 1
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            element = operation(row, col)
            print(element, end=" ")
        print()
        
#print_operation_table(lambda x, y: x * y, 2, 1) 

print_operation_table(lambda x, y: x * y, 3, 3)



Ожидаемый ответ:

1 2 3
2 4 6
3 6 9

Ваш ответ:

1 2 3 
2 4 6 
3 6 9
Тест 2
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            element = operation(row, col)
            print(element, end=" ")
        print()
        
#print_operation_table(lambda x, y: x * y, 2, 1) 

print_operation_table(lambda x, y: x + y, 4, 4)



Ожидаемый ответ:

2 3 4 5
3 4 5 6
4 5 6 7
5 6 7 8

Ваш ответ:

2 3 4 5 
3 4 5 6 
4 5 6 7 
5 6 7 8
Тест 3
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            element = operation(row, col)
            print(element, end=" ")
        print()
        
#print_operation_table(lambda x, y: x * y, 2, 1) 

print_operation_table(lambda x, y: x - y, 5, 5)



Ожидаемый ответ:

0 -1 -2 -3 -4
1 0 -1 -2 -3
2 1 0 -1 -2
3 2 1 0 -1
4 3 2 1 0

Ваш ответ:

0 -1 -2 -3 -4 
1 0 -1 -2 -3 
2 1 0 -1 -2 
3 2 1 0 -1 
4 3 2 1 0
Тест 4
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            element = operation(row, col)
            print(element, end=" ")
        print()
        
#print_operation_table(lambda x, y: x * y, 2, 1) 

print_operation_table(lambda x, y: x * y, 1, 2)

Тест 5
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            element = operation(row, col)
            print(element, end=" ")
        print()
        
#print_operation_table(lambda x, y: x * y, 2, 1) 

print_operation_table(lambda x, y: x / y, 4, 4)



Ожидаемый ответ:

1.0 0.5 0.3333333333333333 0.25
2.0 1.0 0.6666666666666666 0.5
3.0 1.5 1.0 0.75
4.0 2.0 1.3333333333333333 1.0

Ваш ответ:

1.0 0.5 0.3333333333333333 0.25 
2.0 1.0 0.6666666666666666 0.5 
3.0 1.5 1.0 0.75 
4.0 2.0 1.3333333333333333 1.0
Тест 6
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки.

import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            element = operation(row, col)
            print(element, end=" ")
        print()
        
#print_operation_table(lambda x, y: x * y, 2, 1) 

print_operation_table(lambda x, y: x * y)



Ожидаемый ответ:

1 2 3 4 5 6 7 8 9
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81

Ваш ответ:

1 2 3 4 5 6 7 8 9 
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36 
5 10 15 20 25 30 35 40 45 
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81