# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2


n = int(input("Введите расстояние проходимое за день: "))
print("Расстояние в день: ", n, "км")
m = int(input("Введите необходимое расстояние: "))
print("Необходимое расстояние: ", m, "км")
# result = int((m - 1) / n) + 1
result = -(-m // n)
print("Необходимое количество дней: ", result)