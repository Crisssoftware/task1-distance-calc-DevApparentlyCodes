import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class DistanceSubscriber(Node):
	def __init__(self):
		super().__init__('distance_subscriber')
		self.subscriber = self.create_subscription(
			String,
			'turtle1/distance_from_origin',
			self.listener,
			10
		)
		self.subscriber
	
	def listener(self, msg):
		self.get_logger().info(msg.data)




def main(args=None):

    rclpy.init(args=args)
    distance_subscriber = DistanceSubscriber()
	
    rclpy.spin(distance_subscriber)
    distance_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
