import os
import sys
from ament_index_python.packages import get_package_share_directory
sys.path.append(os.path.join(get_package_share_directory('rm_vision_bringup'), 'launch'))


def generate_launch_description():

    from common import node_params, launch_params, robot_state_publisher,buff_detector_node, armor_tracker_node, buff_tracker_node, auto_record_node
    from launch_ros.descriptions import ComposableNode
    from launch_ros.actions import ComposableNodeContainer, Node
    from launch.actions import TimerAction, Shutdown
    from launch import LaunchDescription

    cam_node = Node(
        package='hik_camera',
        executable='hik_camera_node',
        name='hik_camera',
        output='both',
        emulate_tty=True,
        parameters=[node_params],
        on_exit=Shutdown(),
    )

    armor_detector_node = Node(
    package='armor_detector',
    executable='armor_detector_node',
    output='both',
    emulate_tty=True,
    parameters=[node_params],
)
    serial_driver_node = Node(
        package='rm_serial_driver',
        executable='rm_serial_driver_node',
        name='serial_driver',
        output='both',
        emulate_tty=True,
        parameters=[node_params],
        on_exit=Shutdown(),
        ros_arguments=['--ros-args', '--log-level',
                       'serial_driver:='+launch_params['serial_log_level']],
    )

    delay_serial_node = TimerAction(
        period=1.5,
        actions=[serial_driver_node],
    )

    delay_buff_tracker_node = TimerAction(
        period=2.0,
        actions=[buff_tracker_node],
    )

    return LaunchDescription([
        robot_state_publisher,
        cam_node,
        buff_detector_node,       
        delay_serial_node,
        delay_buff_tracker_node,
        armor_detector_node
    ])
