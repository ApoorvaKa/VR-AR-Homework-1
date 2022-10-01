import matplotlib.pyplot as plt
import numpy as np
import math

# In the beginning, the camera's local coordinate system coincides with the world coordinate system.
# this is the initial camera transformation matrix
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
initial_camera_transformation = np.identity(4, dtype=np.float32)

# First rotate the camera around the z axis by 120 degrees, then move it by a translation of (dx, dy, dz) = (2.0, 3.0, 1.0), finally rotate it around the x axis by 30 degrees.
# TODO: compute the 4 x 4 matrix corresponding to each transformation described above and composite them into a single transformation matrix, i.e., the camera transformation matrix.

# 1. rotate the camera around the z axis by 120 degrees
# [[cos(120). -sin(120). 0. 0.]
#  [sin(120). cos(120).  0. 0.]
#  [0.          0.       1. 0.]
#  [0.          0.       0. 1.]]

cosine_120 = math.cos(math.radians(120))
sine_120 = math.sin(math.radians(120))

rotation1 = np.array([[cosine_120, -sine_120, 0, 0],
                        [sine_120, cosine_120, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]], dtype=np.float32)

# 2. move it by a translation of (dx, dy, dz) = (2.0, 3.0, 1.0)
# [[1. 0. 0. 2.]
#  [0. 1. 0. 3.]
#  [0. 0. 1. 1.]
#  [0. 0. 0. 1.]]
translation = np.array([[1, 0, 0, 2],
                        [0, 1, 0, 3],
                        [0, 0, 1, 1],
                        [0, 0, 0, 1]], dtype=np.float32)

# 3. rotate it around the x axis by 30 degrees
# [[1.      0.           0.          0.  ]
#  [0.      cos(30).  -sin(30).      0.  ]
#  [0.      sin(30).   cos(30).      0.  ]
#  [0.      0.           0.          1.  ]]
cosine_30 = math.cos(math.radians(30))
sine_30 = math.sin(math.radians(30))

rotation2 = np.array([[1, 0, 0, 0],
                        [0, cosine_30, -sine_30, 0],
                        [0, sine_30, cosine_30, 0],
                        [0, 0, 0, 1]], dtype=np.float32)

# composite them into a single transformation matrix, i.e., the camera transformation matrix.
current_camera_transformation = np.matmul(np.matmul(rotation1, translation), rotation2)

# Debugs for the camera transformation matrix step 1
print("Initial camera transformation matrix:")
print(initial_camera_transformation)
print("Rotation 120 around z axis:")
print(rotation1)
print("Translation (2, 3, 1):")
print(translation)
print("Rotation 30 around x axis:")
print(rotation2)
print("Current camera transformation matrix:")
print(current_camera_transformation)

# Object position in the world space.
object_position_world = np.array([2, 3, 4], dtype=np.float32)

# TODO: compute the object's position in the camera space using the camera transformation matrix.
object_position_camera = np.matmul(current_camera_transformation, np.append(object_position_world, 1))
object_position_camera = object_position_camera[:3]
print(object_position_camera)

#object_position_camera = None

# TODO: visualize the object's position in the world space and the camera space.
fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title("World space")
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title("Camera space")
ax1.scatter(*object_position_world, color='blue', marker='o')
ax2.scatter(*object_position_camera, color='red', marker='x')
ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")
ax1.set_zlabel("Z Axis")
ax2.set_xlabel("X Axis")
ax2.set_ylabel("Y Axis")
ax2.set_zlabel("Z Axis")
plt.show()
