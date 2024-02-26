import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan
from geometry_msgs.msg import Twist
import cv2
import time
from cv_bridge import CvBridge


class LidarCamauto(Node):
    def __init__(self):
        super().__init__('qr_auto_node')
        self.camera_sub = self.create_subscription(Image, '/camera/image_raw', self.camera_cb, 10)
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_cb, 10)

        self.bridge = CvBridge()
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10) 

    def camera_cb(self, data):
        self.frame = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        cv2.imshow('Frame', self.frame)
        cv2.waitKey(1)

    def lidar_cb(self, data):
        self.front_ray = min(data.ranges[179], 100)
        if self.front_ray <= 1.0: 
            self.qr_detector()
        else:  
            print('moving_forward, present_data==',self.front_ray)
            self.move_forward()  

    def qr_detector(self):
    
        decoder = cv2.QRCodeDetector()
        self.qr_data, points, _ = decoder.detectAndDecode(self.frame)
        print(f"QR code data: {self.qr_data}")
        self.move_based_on_qr()  

    def move_based_on_qr(self):
        if self.front_ray <= 1.0: 
            if self.qr_data == 'left':
                self.turn_left()
            elif self.qr_data == 'right':
                self.turn_right()
            else:
                self.stop()
                print(f"Unknown QR code: {self.qr_data}")  
        else:  
            print("Obstacle detected, taking evasive action!")

    def move_forward(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.4  # Adjust linear velocity as needed
        self.cmd_pub.publish(twist_msg)

    def turn_left(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.4
        time_front = 3.7
        self.cmd_pub.publish(twist_msg)
        time.sleep(time_front)
        twist_msg.angular.z = 0.5 

        turn_duration = 4.2  
        self.cmd_pub.publish(twist_msg)
        time.sleep(turn_duration)

        # Stop turning
        twist_msg.angular.z = 0.0
        self.cmd_pub.publish(twist_msg)

    def turn_right(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.4
        time_ryt_fron = 3.7
        self.cmd_pub.publish(twist_msg)
        time.sleep(time_ryt_fron)
        twist_msg.angular.z = -0.5  

        # Turn right
        turn_duration = 4.0  # Example: turn for 2 seconds
        self.cmd_pub.publish(twist_msg)
        time.sleep(turn_duration)

        # Stop turning
        twist_msg.angular.z = 0.0
        self.cmd_pub.publish(twist_msg)

    def stop(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
        self.cmd_pub.publish(twist_msg)


def main(args=None):
    rclpy.init(args=args)
    auto_sub = LidarCamauto()
    rclpy.spin(auto_sub)
    auto_sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()