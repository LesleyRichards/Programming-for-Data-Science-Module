import numpy as np

# array creation

a = np.array([2, 3, 4])
print(a)

# to print: array ([2, 3, 4])
print(a.dtype)

# to print: dtype('int64')
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

# to print: dtype('float64')
# example of WRONG code: a = np.array(1, 2, 3, 4)
a = np.array([1, 2, 3, 4])  # RIGHT code, missing the [] to make it 1 sequence

# to print: array([[1.5, 2. , 3. ], [4. , 5. , 6. ]])
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

# to print: array([10, 15, 20, 25])
np.arange(10, 30, 5)
print(np.arange(10, 30, 5))

# to print: array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
np.arange(0, 2, 0.3)  # it accepts float arguments
print(np.arange(0, 2, 0.3))


from numpy import pi  # should be at top of page, but for just here in instance
np.linspace(0, 2, 9)  # 9 numbers from 0 to 2
print(np.linspace(0, 2, 9))

x = np.linspace(0, 2 * pi, 100)  # useful to evaluate function at lots of points
f = np.sin(x)
print(x)
print(f)

# basic operations
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)

c = a - b
print(c)

print(b**2)
print(10 * np.sin(a))
print(a < 35)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)  # elementwise product

print(A @ B)  # matrix product

print(A.dot(B))  # another matrix product

# Some operations, such as += and *=, act in place to modify an existing array rather than
# create a new one.
rg = np.random.default_rng(1)  # create instance of default random number generator
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a)

b += a
print(b)

# When operating with arrays of different types, the type of the resulting array corresponds to
# the more general or precise one (a behavior known as upcasting)

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)

c = a + b
print(c)

print(c.dtype.name)

d = np.exp(c * 1j)
print(d)

print(d.dtype.name)

a = rg.random((2, 3))
print(a)

print(a.sum())
print(a.min())
print(a.max())

b = np.arange(12).reshape(3, 4)
print(b)

b.sum(axis=0)  # sum of each column

b.min(axis=1)  # min of each row

b.cumsum(axis=1)  # cumulative sum along each row


# universal functions

# NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy,
# these are called “universal functions” (ufunc). Within NumPy, these functions operate
# elementwise on an array, producing an array as output.

B = np.arange(3)
print(B)

print(np.exp(B))

print(np.sqrt(B))

C = np.array([2., -1., 4.])
print(np.add(B, C))


# Indexing, Slicing and Iterating

# One-dimensional arrays can be indexed, sliced and iterated over, much like lists and
# other Python sequences.

a = np.arange(10)**3
print(a)

print(a[2])

print(a[2:5])

# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000

a[:6:2] = 1000
print(a)

print(a[::-1])  # reversed a

for i in a:
    print(i**(1 / 3.))

# Multidimensional arrays can have one index per axis. These indices are given in a
# tuple separated by commas:


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

print(b[2, 3])
print(b[0:5, 1])  # each row in the second column of b
print(b[:, 1])  # equivalent to the previous example
print(b[1:3, :])  # each column in the second and third row of b

# When fewer indices are provided than the number of axes, the missing indices are
# considered complete slices:
print(b[-1])  # the last row. Equivalent to b[-1, :]

# The expression within brackets in b[i] is treated as an i followed by as many instances
# of : as needed to represent the remaining axes. NumPy also allows you to write this
# using dots as b[i, ...].

# The dots (...) represent as many colons as needed to produce a complete indexing
# tuple. For example, if x is an array with 5 axes, then

# • x[1, 2, ...] is equivalent to x[1, 2, :, :, :],
# • x[..., 3] to x[:, :, :, :, 3] and
# • x[4, ..., 5, :] to x[4, :, :, 5, :].

c = np.array([[[0, 1, 2],  # a 3D array (two stacked 2D arrays)
... [10, 12, 13]],
... [[100, 101, 102],
... [110, 112, 113]]])

print(c.shape)
print(c[1, ...])  # same as c[1, :, :] or c[1]
print(c[..., 2])  # same as c[:, :, 2])
