from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name='armor_detector_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container_mt',  # 多线程组件容器
        composable_node_descriptions=[
            ComposableNode(
                package='armor_detector',
                plugin='rm_auto_aim::ArmorDetectorNode',
                name='armor_detector_node',
                parameters=[{
                    'debug': True,
                    'detect_color': 0  # 0=RED, 1=BLUE
                }]
            )
        ],
        output='screen'
    )

    return LaunchDescription([container])
