#!/usr/bin/env python

import cv_bridge
import rospy
import numpy as np
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 

class ImageConverter:
    def __init__(self):
        rospy.init_node("cam_sub",anonymous=True)
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber("cam_imgs", Image, self.convert)
        rospy.spin()

    def convert(self,img_data):
        cv_img = self.bridge.imgmsg_to_cv2(img_data, "bgr8")
        cv.imshow("conv_img",cv_img)
        cv.waitKey(1)

if __name__ == "__main__":
    img_sub = ImageConverter()
    cv.destroyAllWindows()
