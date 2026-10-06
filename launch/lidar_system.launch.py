from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dan_vs2_lidar',
            executable='lidar_simulator',
            name='lidar_simulator',
            output='screen'
        ),
        Node(
            package='dan_vs2_lidar',
            executable='obstacle_detector',
            name='obstacle_detector',
            output='screen'
        ),
    ])