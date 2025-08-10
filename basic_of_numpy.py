# basic of NumPy.

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)

# numpy creating array

y = np.array([1,2,3])
print(y)
print(type(y))

# 0-D array

u = np.array(42)
print(u)
print(type(u))


# 1-D array

v = np.array([1, 2, 3, 4])
print(v)
print(type(v))  

# 2-D array

w = np.array([[1, 2, 3], [4, 5, 6]])
print(w)
print(type(w))  

# 3-D array

t = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t)
print(type(t))

# check number of dimensions
print("Number of dimensions of x:", x.ndim)
print("Number of dimensions of y:", y.ndim)
print("Number of dimensions of u:", u.ndim)
print("Number of dimensions of v:", v.ndim)
print("Number of dimensions of w:", w.ndim)
print("Number of dimensions of t:", t.ndim)

#higher dimensional arrays
a = np.array([1, 2, 3, 4, 5], ndmin=5)
print(a)
print("Number of dimensions of a:", a.ndim)


# access 2d array elements
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[1, 2])
print('2nd element on 1st row: ', arr[0, 2])

# access 3d array elements
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print('1st element on 2nd row of 1st array: ', arr3d[1, 1, 2])
print('2nd element on 1st row of 2nd array: ', arr3d[1, 0, 1])

# slicing 1d array
arr1d = np.array([1, 2, 3, 4, 5,6,7,8])
print('Elements from index 1 to 3:', arr1d[1:7:2])