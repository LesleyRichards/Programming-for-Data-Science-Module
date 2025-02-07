import numpy as np

# array creation

a = np.array([2, 3, 4])
print(a)

# array ([2, 3, 4])
print(a.dtype)

# dtype('int64')
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

# dtype('float64')
# example of WRONG code: a = np.array(1, 2, 3, 4)
a = np.array([1, 2, 3, 4])  # RIGHT code, missing the [] to make it 1 sequence

# to print array([[1.5, 2. , 3. ], [4. , 5. , 6. ]])
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)

# to print: array([[1.+0.j, 2.+0.j], [3.+0.j, 4.+0.j]])
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

# zeros function
np.zeros((3, 4))
print(np.zeros((3, 4)))

# ones function
np.ones((2, 3, 4), dtype=np.int16)
print(np.ones((2, 3, 4)))

# empty function, creates an array with random content
np.empty((2, 3))
print(np.empty((2, 3)))
