import numpy as np

A = np.arange(0,100,10)
B = np.arange(0,50,5)

C = np.vstack((A, B))
D = np.hstack((A, B))

AB_intersection = np.intersect1d(A,B)

indices = np.where((A >= 5) & (A <= 25))

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, 'float', delimiter=',', usecols=(0, 1, 2))
iris_filter = np.where((iris_2d[:,0] < 5.0) & (iris_2d[:,2] > 1.5))

if __name__ == '__main__':
    print('Numpy array A:', A)
    print('Numpy array B:', B)
    print('Vertical stack of A and B: ', C)
    print('Horizontal stack of A and B: ', D)
    print('Intersection of A and B:', AB_intersection)
    print('Values of A in range 5 to 25:', A[indices])
    print('Values of iris_2D with petallength >1.5 and sepallength < 5.0:', iris_2d[iris_filter])