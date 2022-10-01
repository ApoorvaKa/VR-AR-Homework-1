import numpy as np

# matrix for position coordinates
#pos = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])


# arr = np.array([[1,2,3], [5,6,7], [8,9,10]])
# arr2 = np.array([[1,2,3,], [5,6,7], [8,9,10]])

# arr3 = np.matmul(arr, arr2)
# print(arr, arr2, arr3, sep='\n')

initial_camera_transformation = np.identity(4, dtype=np.float32)
print(initial_camera_transformation)