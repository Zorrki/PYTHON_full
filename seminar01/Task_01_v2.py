# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# 1 вариант
# import math
# speed = int(input("Введите скорость: "))
# distance = int(input("Введите расстояние: "))
# days = math.ceil(distance / speed)
# print("Количество дней: ", days)


# 2 вариант
# speed = int(input("Введите скорость: "))
# distance = int(input("Введите расстояние: "))
# days = distance / speed
# days2 = (distance + (speed - 1)) // speed
# print("Количество дней: ", days2)

# 3 вариант
speed = int(input("Введите скорость: "))
distance = int(input("Введите расстояние: "))
days = distance / speed
days2 = (distance + (speed - 1)) // speed
days3 = (distance//speed)+bool(distance%speed)
print("Количество дней: ", days3)