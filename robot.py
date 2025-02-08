# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
import matplotlib.pyplot as plt
import numpy as np
import random

x = [0]
y = [0]
steps_up = 0
steps_down = 0
steps_left = 0
steps_right = 0

for i in range(100):
    a = random.randint(1,4)

    if a == 1:
        x.append(x[-1] + 1)
        y.append(y[-1])
        steps_up += 1

    elif a == 2:
        x.append(x[-1] - 1)
        y.append(y[-1])
        steps_down += 1

    elif a == 3:
        y.append(y[-1] + 1)
        x.append(x[-1])
        steps_right += 1

    elif a == 4:
        y.append(y[-1] - 1)
        x.append(x[-1])
        steps_left += 1

print('end location:', 'x =', x[-1], 'y =', y[-1])
print(' steps up:', steps_up, '\n', 'steps down:', steps_down, '\n','steps left:', steps_left, '\n','steps right:', steps_right)
print("range is:", ((x[0] - x[-1]) ** 2 + (y[2] - y[-1]) ** 2) ** 0.5)
x1 = np.array(x)
y1 = np.array(y)
fig, ax = plt.subplots()
plt.plot(x1, y1, color="blue")
plt.show()




