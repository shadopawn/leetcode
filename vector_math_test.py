import numpy as np
import vectormath as vmath

# Single Vectors
v = vmath.Vector3(5, 0, 0)
v.normalize()
print(v)                          # >> [1, 0, 0]
print(v.x)                        # >> 1.0

x = vmath.Vector3(0,1,0)
print(x.cross(v))

# VectorArrays are much faster than a for loop over Vectors
v_array = vmath.Vector3Array([[4, 0, 0], [0, 2, 0], [0, 0, 3]])
print(v_array.x)                  # >> [4, 0, 0]
print(v_array.length)             # >> [4, 2, 3]
print(v_array.normalize())        # >> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Vectors can be accessed individually or in slices
print(type(v_array[1:]))          # >> vectormath.Vector3Array
print(type(v_array[2]))           # >> vectormath.Vector3

# All these classes are just numpy arrays
print(isinstance(v, np.ndarray))  # >> True
print(type(v_array[1:, 1:]))      # >> numpy.ndarray