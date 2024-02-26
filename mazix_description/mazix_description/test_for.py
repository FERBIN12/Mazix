import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot_node')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def move_forward(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.2  # Adjust linear velocity as needed

        self.cmd_pub.publish(twist_msg)
        
def main(args=None):
    rclpy.init(args=args)
    move_robot_node = MoveRobot()
    move_robot_node.move_forward()
    move_robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


