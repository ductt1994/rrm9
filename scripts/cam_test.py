#!/usr/bin/env python
import rospy
import numpy as np
import cv2 as cv
import rrm9.cam_params as cp 

#Chose camera
#camera 1: Acer swift 3 webcam
#camera 2: IMX219
camera = 2

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
# print(camSet)

#Create OpenCV capture object
cap = cv.VideoCapture(camSet)

#Check if camera data can be accessed
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Check for return value errors and read each frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Display frame until "q" is pressed
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

#Release resources
cap.release()
cv.destroyAllWindows()