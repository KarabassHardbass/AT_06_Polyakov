from PIL import Image
import numpy as np
import time

print('Картинка')
img = Image.open(input())
print('Сохранить как')
name = input()
print('Серый цвет')
modifier = int(input())
print('Размер')
size = int(input())

start_time = time.time()

array = np.array(img)
height = len(array)
width = len(array[1])

def find_grayscale(x, y):
    scale = 0
    for cur_y in range(y, y + size):
        for cur_x in range(x, x + size):
            if cur_y >= height or cur_x >= width:
                print('Введён неправильный шаг')
            scale += (array[cur_y][cur_x].sum()) // 3
    return int(scale // (size * size))

def fill_array(x, y, scale):
    for cur_y in range(y, y + size):
        for cur_x in range(x, x + size):
            if cur_y >= height or cur_x >= width:
                print('Введён неправильный шаг')
            array[cur_y][cur_x] = np.repeat(int(scale // modifier) * modifier, 3)

for y in range(0, height, size):
    for x in range(0, width, size):
        fill_array(x, y, find_grayscale(x, y))

res = Image.fromarray(array)
res.save(name)
print("Время выполнения: {:.2f}s".format(time.time() - start_time))