#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from adafruit_servokit import ServoKit
import time

#Subscriber Function to process the xbox controller values
def convert(data):
    # rospy.loginfo(data.linear.x, data.angular.z)
    print("Speed: {}\t Angle: {}".format(data.linear.x, data.angular.z))
    # rospy.loginfo(data)
    # print(data)

    
def subs():
    #Declare the node to process the xbox-ctr values
    rospy.init_node('jetson')
    
    #Define the topic name and message type
    #CALL THE CONVERT FUNCTION !!!
    rospy.Subscriber('xbox2jetson', Twist, convert)
    rospy.spin()

if __name__ == '__main__':
    subs()