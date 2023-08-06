import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("Draw Circle")
    rospy.loginfo("Successfully started new publisher node")

    pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate=rospy.Rate(2) # keeping the while loop in 2 unit rate
    while not rospy.is_shutdown():
        msg=Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        pub.publish(msg)
        rate.sleep()
