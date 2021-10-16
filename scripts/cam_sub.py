#!/usr/bin/env python
import os
import cv2 as cv
import cv_bridge
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 
from sensor_msgs.msg import Joy
from datetime import datetime
import rosbag

home_dir = os.getenv("HOME")
bag_dir = ("/bagfiles/")

now = datetime.now()
dt_string = now.strftime("%Y:%m:%d-%H:%M:%S")
bag_name = dt_string + ".bag"
bag_full_path = home_dir + bag_dir + bag_name
bag = rosbag.Bag(bag_full_path, 'w')

class ImageConverter:
    def __init__(self):
        rospy.init_node("cam_sub",anonymous=True)
        self.sub_ctr = rospy.Subscriber("joy", Joy, self.checkstate)
        rospy.spin()

    def checkstate(self,data):
        if data.buttons[0] == 1:
            #A-Button
            self.bridge = CvBridge()
            self.sub_img = rospy.Subscriber("cam_imgs", Image, self.write2bag)
        elif data.buttons[1] == 1: 
            #B-Button
            bag.close()
            rospy.signal_shutdown("User pressed 'B'")
        
    def write2bag(self,img_data):
        bag.write("cam_imgs",img_data)

if __name__ == "__main__":
    img_sub = ImageConverter()