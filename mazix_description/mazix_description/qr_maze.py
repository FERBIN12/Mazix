from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image #thats how ros2 receives image information
from sensor_msgs.msg import LaserScan

import cv2

class lidar_cam_sub(Node):

    def __init__(self):
        super().__init__('camera_lidar_node')
        self.camera_sub = self.create_subscription(Image,'/camera/image_raw',self.camera_cb,10)
        self.lidar_sub = self.create_subscription(LaserScan,'/scan',self.lidar_cb,10)

        self.bridge=CvBridge()
        self.frame=0


    def camera_cb(self, data):
        self.frame = self.bridge.imgmsg_to_cv2(data,'bgr8')
        cv2.imshow('Frame',self.frame)
        cv2.waitKey(1)

    def lidar_cb(self, data):
        front_ray = min(data.ranges[179], 100 )
        if(front_ray <= 0.9):
            self.qr_detector()
        else:
            print(front_ray)

    def qr_detector(self):
        decoder = cv2.QRCodeDetector()
        data, points, _ = decoder.detectAndDecode(self.frame)
        print(data)

def main(args=None):
    rclpy.init(args=args)

    sensor_sub = lidar_cam_sub()

    rclpy.spin(sensor_sub)
    sensor_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()