#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse 
import rospy

try:
    rospy.wait_for_service('/go_to_kitchen')
    go_to_kitchen_service = rospy.ServiceProxy('/go_to_kitchen', Empty)
    go_to_kitchen_service() 
except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

try:
    rospy.wait_for_service('/stop')
    stop_service = rospy.ServiceProxy('/stop', Empty)
    stop_service()
except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

try:
    rospy.wait_for_service('/go_home')
    go_home_service = rospy.ServiceProxy('/go_home', Empty)
    go_home_service()
except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

try:
    rospy.wait_for_service('/stop')
    stop_service = rospy.ServiceProxy('/stop', Empty)
    stop_service()
except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

