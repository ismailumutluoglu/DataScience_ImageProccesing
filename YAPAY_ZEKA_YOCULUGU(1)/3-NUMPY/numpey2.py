import numpy as np 

# 1D arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)       # Element-wise addition
print(a - b)       # Element-wise subtraction
print(a ** 2)      # Square of each element
print(np.sin(a))   # Sine of each element
print(a < 2)       # Element-wise comparison

# 2D arrays
array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2= np.array([[1,2,3],[4,5,6],[7,8,9]])

#element wise product
print(array1*array2)

#matrix product

array1.dot(array2.T)

print(np.exp(array1))

array = np.random.random((5,5))
print(array)

print(array.sum())
print(array.max())
print(array.min())

print(array.sum(axis=0))
print(array.sum(axis=1))

print(np.sqrt(array))   
print(np.square(array))



#indexing and slicing
