import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math
from turtlesim.msg import Pose

class DistancePublisher(Node):

    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher = self.create_publisher(String, 'turtle1/distance_from_origin', 10)
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.calculate,
            10
        )
        self.subscription

        self.prevCoords = None


    def calculate(self, msg):
        x , y = msg.x, msg.y
        if self.prevCoords is not None and (x,y) == self.prevCoords  : return
        d = math.sqrt(x**2 + y**2)
        output = String()
        output.data = (f"Distance from origin of the turtle is : {d:.2f}")
        self.publisher.publish(output)
        self.get_logger().info(f"Publishing to topic distance_from_origin : {d:.2f}")
        self.prevCoords = (x, y)


def main(args = None):
    rclpy.init(args = args)
    distance_publisher = DistancePublisher()
    rclpy.spin(distance_publisher)
    distance_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()