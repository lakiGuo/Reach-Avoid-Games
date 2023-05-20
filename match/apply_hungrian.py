# import numpy as np
# from scipy.optimize import linear_sum_assignment

# def apply_hungarian(matrix):
#     row_ind, col_ind = linear_sum_assignment(matrix)
#     return matrix[row_ind, col_ind]

# matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# result = apply_hungarian(matrix)
# print(result)
import matplotlib.pyplot as plt
from hungarian import Hungarian
from hungarian import HungarianError
import numpy as np
import time
from scipy.optimize import linear_sum_assignment
import math
# design O(Nlog(N)) algorithm


def NlogN_algorithm(N: int):
    count = 0
    # 对logN上取整
    M = math.ceil(math.log(N))
    for i in range(N):
        for j in range(M):
            count += 1
    return count
# design O(N^2) algorithm


def N2_algorithm(N: int):
    count = 0
    for i in range(N):
        for j in range(N):
            count += 1
    return count

# design O(N^3) algorithm


def N3_algorithm(N: int):
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                count += 1
    return count


def test_N3_algorithm():
    sizes1 = list(range(10, 100, 10))
    times1 = []
    for size in sizes1:
        start_time = time.time()
        count = N3_algorithm(size)
        end_time = time.time()
        times1.append(end_time - start_time)

    sizes2 = list(range(100, 1001, 100))
    times2 = []
    for size in sizes2:
        start_time = time.time()
        count = N3_algorithm(size)
        end_time = time.time()
        times2.append(end_time - start_time)

    sizes = sizes1+sizes2
    times = times1+times2
    return sizes, times


def test_NlogN_algorithm():
    sizes1 = list(range(10, 100, 10))
    times1 = []
    for size in sizes1:
        start_time = time.time()
        count = NlogN_algorithm(size)
        end_time = time.time()
        times1.append(end_time - start_time)

    sizes2 = list(range(100, 1001, 100))
    times2 = []
    for size in sizes2:
        start_time = time.time()
        count = NlogN_algorithm(size)
        end_time = time.time()
        times2.append(end_time - start_time)

    sizes = sizes1+sizes2
    times = times1+times2
    return sizes, times


def test_N2_algorithm():
    sizes1 = list(range(10, 100, 10))
    times1 = []
    for size in sizes1:
        start_time = time.time()
        count = N2_algorithm(size)
        end_time = time.time()
        times1.append(end_time - start_time)

    sizes2 = list(range(100, 1001, 100))
    times2 = []
    for size in sizes2:
        start_time = time.time()
        count = N2_algorithm(size)
        end_time = time.time()
        times2.append(end_time - start_time)

    sizes = sizes1+sizes2
    times = times1+times2
    return sizes, times


def test_algorithm():
    sizes1 = list(range(10, 100, 10))
    times1 = []
# for size in sizes1:
#     matrix = np.random.randint(0, 100, size=(size, size))

#     hungarian = Hungarian(matrix, is_profit_matrix=False)
#     start_time = time.time()
#     try:
#         hungarian.calculate()
#     except HungarianError as e:
#         print(e)
#     end_time = time.time()
#     times1.append(end_time - start_time)

    for size in sizes1:
        matrix = np.random.randint(0, 100, size=(size, size))
        try:
            start_time = time.time()
            row_ind, col_ind = linear_sum_assignment(matrix)
            end_time = time.time()
            times1.append(end_time - start_time)
        except:
            print("error")

    sizes = list(range(100, 1001, 100))
    times = []
    for size in sizes:
        matrix = np.random.randint(0, 100, size=(size, size))
        try:
            start_time = time.time()
            row_ind, col_ind = linear_sum_assignment(matrix)
            end_time = time.time()
            times.append(end_time - start_time)
        except:
            print("error")
# for size in sizes:
#     matrix = np.random.randint(0, 100, size=(size, size))

#     hungarian = Hungarian(matrix, is_profit_matrix=False)
#     start_time = time.time()
#     try:
#         hungarian.calculate()
#     except HungarianError as e:
#         print(e)
#     end_time = time.time()
#     times.append(end_time - start_time)

    return sizes1+sizes, times1+times


# 10*10 matrix
# matrix_10 = np.random.randint(0, 100, size=(10, 10))
# row_ind, col_ind = linear_sum_assignment(matrix_10)
# print(row_ind, col_ind)

sizes1, times1 = test_N2_algorithm()
sizes2, times2 = test_algorithm()
sizes3, times3 = test_NlogN_algorithm()
#sizes3, times3 = test_N3_algorithm()
plt.plot(sizes1, times1, linewidth=2.5, label="O(N^2)")
plt.plot(sizes2, times2, linewidth=2.5,
         color="#C93300", label="Hungarian Algorithm")
plt.plot(sizes3, times3, linewidth=2.5, color="g", label="O(NlogN)")
#plt.plot(sizes3, times3, linewidth=2, label="O(N^3) algorithm")
# plt.title("Hungarian Algorithm Running Time")
# 取消label的框框
plt.legend(frameon=False)
plt.xlabel("Matrix Size")
plt.ylabel("Time (seconds)")

# 保存图片为eps格式
plt.savefig("HungarianAlgorithmRunningTime.eps", format="eps")
plt.show()
