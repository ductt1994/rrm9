#!/usr/bin/env python

import rospy
import numpy as np
import cv2 as cv
import rrm9.cam_params as cp
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 

#Chose camera and color settings
camera = 2      #camera 1: Acer swift 3 webcam
                #camera 2: IMX219
clr_mode = 0    #0->gray
                #1->color

#Create camera settings as formatted string
if camera == 1:
    camSet = ("v4l2src "
          "! videoconvert "
          "! video/x-raw, width={}, height={}, framerate={}/1 "
          "! appsink").format(cp.capture_width,cp.capture_height,cp.capture_fps)
elif camera == 2:
    camSet = ("nvarguscamerasrc "
            "! video/x-raw(memory:NVMM), width={}, height={}, format=NV12, framerate={}/1 "
            "! nvvidconv "
            "! video/x-raw, width={}, height={}, framerate={}/1, format=BGRx "
            "! videoconvert "
            "! video/x-raw, format=BGR "
            "! appsink").format(cp.capture_width,cp.capture_height,cp.capture_fps,
                                cp.display_width,cp.display_height,cp.display_fps)

class CameraPublisher:
    def __init__(self,params):
        self.pub = rospy.Publisher("cam_imgs", Image, queue_size=1)
        self.bridge = CvBridge()
        rospy.init_node("camera", anonymous=True)
        self.rate = rospy.Rate(params.capture_fps)

    def set_cam(self,Settings):
        self.camSettings = Settings

    def publish(self):
        self.cap = cv.VideoCapture(self.camSettings)

        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Convert image with ROS compability and display the stream
            if clr_mode == 0:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                img_msg = self.bridge.cv2_to_imgmsg(gray,"mono8")
            elif clr_mode == 1:
                img_msg = self.bridge.cv2_to_imgmsg(frame,"bgr8")

            self.pub.publish(img_msg)
            # cv.imshow("frame",frame)
            # if cv.waitKey(1) == ord('q'):
                # break

            self.rate.sleep()

        #Release resources
        self.cap.release()
        # cv.destroyAllWindows()

if __name__ == "__main__":
    cam = CameraPublisher(cp)
    cam.set_cam(camSet)
    cam.publish()