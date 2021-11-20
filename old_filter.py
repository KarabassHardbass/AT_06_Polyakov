from PIL import Image
import numpy as np
import time
start_time = time.time()
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                b1 = arr[n][n1][0]
                b2 = arr[n][n1][1]
                b3 = arr[n][n1][2]
                M = (int(b1) + int(b2) + int(b3)) / 3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
print("Время выполнения: {:.2f}s".format(time.time() - start_time))
