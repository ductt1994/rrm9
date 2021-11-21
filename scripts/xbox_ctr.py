#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

#Publisher Function to send joystick values
def callback(data):
    twist = Twist()
    twist.linear.x = data.axes[1]
    twist.angular.z = data.axes[2]
    pub.publish(twist)

def start():
    #Declare the node to publish joystick values from
    rospy.init_node('xbox_ctr')
    
    #Define the topic name and message type
    global pub
    pub = rospy.Publisher('xbox2jetson', Twist, queue_size = 1)

    #Xbox_ctr node gets its values from the Joy-Node and publishes afterwards
    rospy.Subscriber("joy", Joy, callback)

    #Publish the msg with a rate of 60 Hz
    rospy.Rate(60)
    rospy.spin()

if __name__ == '__main__':
    start()