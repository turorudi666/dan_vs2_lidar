import math
import random

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class LidarSimulator(Node):

    def __init__(self):
        super().__init__('lidar_simulator')

        self.publisher = self.create_publisher(
            LaserScan,
            '/scan',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_scan)

        self.get_logger().info('LiDAR simulator elindult.')

    def publish_scan(self):
        scan = LaserScan()

        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = 'laser_frame'

        scan.angle_min = -math.pi
        scan.angle_increment = math.radians(1.0)
        scan.angle_max = math.pi - scan.angle_increment

        scan.range_min = 0.1
        scan.range_max = 10.0

        number_of_readings = 360

        # Alapesetben minden objektum messze van
        ranges = [
            random.uniform(4.0, 8.0)
            for _ in range(number_of_readings)
        ]

        state = random.choice(['CLEAR', 'WARNING', 'STOP'])

        if state == 'WARNING':
            obstacle_distance = random.uniform(1.0, 2.0)
            self.add_front_obstacle(ranges, obstacle_distance)

        elif state == 'STOP':
            obstacle_distance = random.uniform(0.3, 1.0)
            self.add_front_obstacle(ranges, obstacle_distance)

        scan.ranges = ranges

        self.publisher.publish(scan)

        self.get_logger().info(
            f'LiDAR meres publikalva - szimulalt allapot: {state}'
        )

    def add_front_obstacle(self, ranges, distance):
        center_index = 180 + random.randint(-20, 20)

        for offset in range(-3, 4):
            index = center_index + offset

            if 0 <= index < len(ranges):
                ranges[index] = distance


def main(args=None):
    rclpy.init(args=args)

    node = LidarSimulator()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()