# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).

import numpy as np
import matplotlib.pyplot as plt
import random

from PIL.EpsImagePlugin import field

ind = [random.randint(1, 100) for i in range(15)]

while len(set(ind)) < 15:
    ind = [random.randint(1, 100) for i in range(15)]

field = [0 for i in range(100)]

for i in range(15):
    field[ind[i]] = -1

field = np.array(field)
np.matrix(field.reshape(10, 10))

fig, ax = plt.subplots()
plt.imshow(field, cmap="hot")
plt.show()