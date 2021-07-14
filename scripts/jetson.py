#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from adafruit_servokit import ServoKit

#Setup the Servo channels
myKit = ServoKit(channels=16)

#Setup the steering servo
min_range = 1000
max_range = 2000
myKit.servo[0].set_pulse_width_range(min_range,max_range)
myKit.servo[0].actuation_range = 180

#Setup the steering ranges
offset = 2
# myKit.servo[0].angle = 90 + offset      #90 deg --> neutral position
neutral_ang = 90 + offset
amp = 45

#Subscriber Function to process the xbox controller values
def convert(data):
    #Range of linear.x = -1 ... +1
    #Range of angular.z = -1 ... +1
    #Minus to match the steering orientation of the Xbox_ctr with the front axle direction
    veh_ang = neutral_ang - data.angular.z * amp
    veh_vel = data.linear.x

    print("Speed: {:.2f}\t Angle: {:.2f}".format(veh_vel, veh_ang))
    
    #Send the steering and speed values to the servo
    myKit.servo[0].angle = veh_ang
    myKit.continuous_servo[1].throttle = veh_vel  
    
def subs():
    #Declare the node to process the xbox-ctr values
    rospy.init_node('jetson')
    
    #Define the topic name and message type
    #CALL THE CONVERT FUNCTION !!!
    rospy.Subscriber('xbox2jetson', Twist, convert)
    rospy.spin()

if __name__ == '__main__':
    subs()