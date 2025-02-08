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
import numpy as np
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

fig = plt.figure(figsize=(8, 8))

ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4])
x1 = np.linspace(1, 365, 365)
y1 = np.array(a)
ax1.plot(x1, y1, label="weather", color="green")
ax1.set_title("Погода по дням года")

for i in range(len(a)):

    if a[i] < 0:
        point1 = plt.Circle((i + 1, a[i]), 0.25, color="blue")
        ax1.add_patch(point1)

    elif a[i] > 25:
        point2 = plt.Circle((i + 1, a[i]), 0.25, color="red")
        ax1.add_patch(point2)

ax2 = fig.add_axes([0.1,0.03,0.8,0.4])
y2 = np.array(a)
ax2.hist(y2, 46)
ax2.set_title("Количество дней с одинаковой температурой")

plt.show()
