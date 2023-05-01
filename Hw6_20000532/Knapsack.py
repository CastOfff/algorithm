import random
import matplotlib.pyplot as plt
import numpy as np
import timeit
# size = random.randint(10, 15)
# print("size: ", size)
# weight = [0.5, 0.7, 1.1 ,1.6, 1.7, 2]
# value = [0 for i in range(len(weight))]
# for i in range(0, len(weight)):
#     value[i] = random.randint(10, 1000)
# print("weight: ", weight)
# print("value: ", value)

def knapknap(weight, size, value, condition):
    K = []
    arr = []
    for i in range(0, len(weight)):
        K.append(value[i] / weight[i])
    while condition < size and max(K) != 0:
        if (condition + weight[K.index(max(K))] > size):
            K[K.index(max(K))] = 0
        else :
            condition = condition + weight[K.index(max(K))]
            arr.append(weight[K.index(max(K))])
    return condition, arr
# print(knapknap(weight, size, value, 0))


data = np.arange(10, 100)
time = []
for n in data:
  value = [random.randint(10,1000) for i in range(n)]
  weight = [random.randint(1,10) for i in range(n)]
  t = timeit.timeit(lambda: knapknap(weight, n, value, 0), number = 10) / 10
  time.append(t)
# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time)
plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Thời gian")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài xếp balo")
plt.show()




