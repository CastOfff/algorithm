import matplotlib.pyplot as plt
import numpy as np
import timeit

def change(arr, money, i):
    while (i < n and money > 0 ):
        k[i] = money // arr[i]
        money = money - (k[i] * arr[i])
        i += 1
    if money > 0:
        return -1
    else:
        return 0
n = 9
k = [0 for i in range(n)]
arr = [500, 200, 100, 50, 20, 10, 5, 2, 1]



data = np.arange(1, 10000)
time = []
for money in data:
  t = timeit.timeit(lambda: change(arr,money,0), number = 10) / 10
  time.append(t)

# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time)
plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Thời gian")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài change coins")
plt.show()


