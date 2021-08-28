import os
import rosbag
import rospy
import cv2 as cv
# from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 

home_dir = os.getenv("HOME")
bag_dir = ("/bagfiles/")
bag_name = "15-08-2021 15:38:50.bag"
bag_full_path = home_dir + bag_dir + bag_name
bag = rosbag.Bag(bag_full_path)


bridge = CvBridge()

for topic, img_data, t in bag.read_messages(topics=['cam_imgs']):
    cv_img = bridge.imgmsg_to_cv2(img_data, "bgr8")
    cv.imshow("conv_img",cv_img)
    # print(t)
    cv.waitKey(60)  #after displaying the image adjust the wait time to match the capture fps

bag.close()