#!/usr/bin/env python
import os
import cv_bridge
import rospy
import numpy as np
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 
from sensor_msgs.msg import Joy
from datetime import datetime
import rosbag

home_dir = os.getenv("HOME")
bag_dir = ("/bagfiles/")

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
bag_name = dt_string + ".bag"
bag_full_path = home_dir + bag_dir + bag_name
bag = rosbag.Bag(bag_full_path, 'w')

class ImageConverter:
    def __init__(self):
        # self.capstate = 0
        rospy.init_node("cam_sub",anonymous=True)
        self.sub_ctr = rospy.Subscriber("joy", Joy, self.checkstate)
        rospy.spin()

        # while not rospy.is_shutdown():
        #     # print(self.capstate)
        #     if self.capstate == 1:
        #         self.bridge = CvBridge()
        #         self.sub_img = rospy.Subscriber("cam_imgs", Image, self.convert)
        #     elif self.capstate == 2:
        #         break

    def checkstate(self,data):
        # print(data.buttons[0], data.buttons[1])
        if data.buttons[0] == 1:
            #A-Button
            # self.capstate = 1
            self.bridge = CvBridge()
            self.sub_img = rospy.Subscriber("cam_imgs", Image, self.convert)
        elif data.buttons[1] == 1: 
            #B-Button
            # self.capstate = 2
            bag.close()
            rospy.signal_shutdown("User pressed 'B'")
        
    def convert(self,img_data):
        # cv_img = self.bridge.imgmsg_to_cv2(img_data, "bgr8")
        # cv.imshow("conv_img",cv_img)
        # cv.waitKey(1)

        bag.write("cam_imgs",img_data)

if __name__ == "__main__":
    img_sub = ImageConverter()
    # cv.destroyAllWindows()
