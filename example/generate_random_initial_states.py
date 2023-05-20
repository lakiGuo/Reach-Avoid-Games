import numpy as np
x = np.random.uniform(6.7, 8.4, 10)
# 随机生成10个y坐标，范围在0到14之间
y = np.random.uniform(0, 14, 10)
# 将x和y合并为一个二维矩阵
matrix = np.column_stack((x, y))
