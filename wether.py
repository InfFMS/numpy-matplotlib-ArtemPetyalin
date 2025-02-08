# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import random
import matplotlib.pyplot as plt
a = [random.randint(-10, 35) for i in range(365)]
av_temp = 0
heat_counter = 0
colds = []
prev = 0
cold_counter = 0

for i in range(len(a)):
    av_temp += a[i]

    if a[i] > 25:
        heat_counter += 1

    if prev < 0 and a[i] < 0:
        cold_counter += 1

    else:
        colds.append(cold_counter)
        cold_counter = 0

    prev = a[i]

av_temp = av_temp / 365

max_cold = 0
for i in range(len(colds)):

    if max_cold < colds[i]:
        max_cold = colds[i]

print(av_temp, max_cold, heat_counter)