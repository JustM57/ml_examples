import numpy as np
x = np.random.normal(loc=1, scale=50, size=(100, 50))
m = np.mean(x, axis=0)
o = np.std(x, axis=0)
x_norm = (x - m) / o

z = np.array([[4, 5, 0],
             [1, 9, 3],
             [5, 1, 1],
             [3, 3, 3],
             [9, 9, 9],
             [4, 7, 1]])
s = np.sum(z, axis=1)
t = np.nonzero(s > 10)
a = np.eye(3)
b = np.eye(3)
ab = np.vstack((a, b))
