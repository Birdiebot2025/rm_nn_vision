from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='buff_tracker',
            executable='buff_tracker_node',
            name='buff_tracker_node',
            output='both',
            emulate_tty=True,
        ),
    ])
