# VR and AR: Homework 1
# Apoorva Kaushik

import matplotlib.pyplot as plt
import numpy as np
import math

# In the beginning, the camera's local coordinate system coincides with the world coordinate system.
initial_camera_transformation = np.identity(4, dtype=np.float32)

# First rotate the camera around the z axis by 120 degrees, then move it by a translation of (dx, dy, dz) = (2.0, 3.0, 1.0), finally rotate it around the x axis by 30 degrees.
# TODO: compute the 4 x 4 matrix corresponding to each transformation described above and composite them into a single transformation matrix, i.e., the camera transformation matrix.

# 1. rotate the camera around the z axis by 120 degrees
cosine_120 = math.cos(math.radians(120))
sine_120 = math.sin(math.radians(120))

rotation1 = np.array([[cosine_120, -sine_120, 0, 0],
                        [sine_120, cosine_120, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]], dtype=np.float32)

# 2. move camera by a translation of (dx, dy, dz) = (2.0, 3.0, 1.0)
translation = np.array([[1, 0, 0, 2],
                        [0, 1, 0, 3],
                        [0, 0, 1, 1],
                        [0, 0, 0, 1]], dtype=np.float32)

# 3. rotate camera around the x axis by 30 degrees
cosine_30 = math.cos(math.radians(30))
sine_30 = math.sin(math.radians(30))

rotation2 = np.array([[1, 0, 0, 0],
                        [0, cosine_30, -sine_30, 0],
                        [0, sine_30, cosine_30, 0],
                        [0, 0, 0, 1]], dtype=np.float32)

# composite them into a single transformation matrix, i.e., the camera transformation matrix.
current_camera_transformation = np.matmul(np.matmul(rotation2, translation), rotation1)

# Object position in the world space.
object_position_world = np.array([2, 3, 4], dtype=np.float32)

# TODO: compute the object's position in the camera space using the camera transformation matrix.
# use the inverse of the camera transformation matrix to transform the object position from the world space to the camera space.
composite_object_transformation = np.linalg.inv(current_camera_transformation)
object_position_camera = np.matmul(composite_object_transformation, np.append(object_position_world, 1))
object_position_camera = object_position_camera[:3]

print("Object Position in the camera space:")
print(object_position_camera)

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
