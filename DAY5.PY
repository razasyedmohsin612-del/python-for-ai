import numpy as np

arrays = [
    np.array([1,2,3]),
    np.array([[1,2],[3,4]]),
    np.ones((2,3,4)),
    np.zeros((5,2))
]

for arr in arrays:
    print("Array:")
    print(arr)
    print("ndim :", arr.ndim)
    print("shape:", arr.shape)
    print("size :", arr.size)
    print("-"*30)