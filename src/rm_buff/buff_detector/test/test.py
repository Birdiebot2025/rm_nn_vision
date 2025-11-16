import numpy as np
import cv2

# 假设的原始点
points = np.float32([
    [120, 106],  # 点1
    [105, 150],  # 点2
    [155, 98],  # 点3
    [155, 146]   # 点4
])

# 计算质心
centroid = np.mean(points, axis=0)

# 假设的平均长度的一半
half_length = 25

# 定义理想正方形的顶点
ideal_points = np.float32([
    [centroid[0] - half_length, centroid[1] - half_length],  # 左上角
    [centroid[0] - half_length, centroid[1] + half_length],  # 左下角
    [centroid[0] + half_length, centroid[1] - half_length],  # 右上角
    [centroid[0] + half_length, centroid[1] + half_length]   # 右下角
])

# 计算透视变换矩阵
perspective_matrix = cv2.getPerspectiveTransform(points, ideal_points)

# 应用透视变换
transformed_points = cv2.perspectiveTransform(np.array([points]), perspective_matrix)

print("原始点:")
print(points)
print("变换后的点:")
print(transformed_points)
