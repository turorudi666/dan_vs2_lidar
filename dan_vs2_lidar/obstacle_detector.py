import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String


class ObstacleDetector(Node):

    def __init__(self):
        super().__init__('obstacle_detector')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            '/obstacle_status',
            10
        )

        self.get_logger().info('Obstacle detector elindult.')

    def scan_callback(self, scan):
        front_ranges = []

        for index, distance in enumerate(scan.ranges):
            angle = scan.angle_min + index * scan.angle_increment

            # Csak a robot előtti +/- 30 fokos területet vizsgáljuk
            if -math.radians(30) <= angle <= math.radians(30):
                if (
                    math.isfinite(distance)
                    and scan.range_min <= distance <= scan.range_max
                ):
                    front_ranges.append(distance)

        if not front_ranges:
            return

        closest_distance = min(front_ranges)

        if closest_distance < 1.0:
            status = 'STOP'
        elif closest_distance < 2.0:
            status = 'WARNING'
        else:
            status = 'CLEAR'

        message = String()
        message.data = status

        self.publisher.publish(message)

        self.get_logger().info(
            f'Legkozelebbi akadaly: {closest_distance:.2f} m -> {status}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ObstacleDetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()