# coding=utf-8
__author__ = 'Macbook Pro'
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model
import matplotlib

# Ham make moon dung de tao du lieu ngau nhien cho ca bai toan phan lop, gom cum
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.80)
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
plt.show()


