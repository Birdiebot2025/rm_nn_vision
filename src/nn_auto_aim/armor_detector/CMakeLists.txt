cmake_minimum_required(VERSION 3.10)
project(armor_detector LANGUAGES CXX)

# -------------------- C++ --------------------
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

# -------------------- ament auto --------------------
find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

# -------------------- 第三方库 --------------------
find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(fmt REQUIRED)
find_package(OpenVINO REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)

# -------------------- 构建库 --------------------
ament_auto_add_library(${PROJECT_NAME} SHARED
    src/detector_nn_node.cpp
    src/detector.cpp
    src/number_classifier.cpp
    src/pnp_solver.cpp
    tasks/yolo.cpp
    tasks/yolos/yolov8.cpp
    tasks/classifier.cpp
    tasks/detector.cpp
    tasks/armor.cpp
)

# 头文件
target_include_directories(${PROJECT_NAME} PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/tasks>
)

# -------------------- plain-style 链接 --------------------
# 注意：这里不能用 PRIVATE/PUBLIC，否则会和 ament_target_dependencies 冲突
ament_target_dependencies(${PROJECT_NAME}
    rclcpp
    rclcpp_components
    OpenCV
    OpenVINO
    Eigen3
    fmt
)

# 如果需要额外链接第三方库（OpenVINO plain-style）
if(TARGET openvino::runtime)
    target_link_libraries(${PROJECT_NAME} openvino::runtime)
elseif(TARGET openvino)
    target_link_libraries(${PROJECT_NAME} openvino)
endif()

# -------------------- 注册 ROS2 组件节点 --------------------
rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN rm_auto_aim::ArmorDetectorNode
  EXECUTABLE armor_detector_node
)

# -------------------- 安装 --------------------
ament_auto_package(
  INSTALL_TO_SHARE
  model
)
