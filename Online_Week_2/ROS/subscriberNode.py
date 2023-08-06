import rospy
from turtlesim.msg import Pose


def pose_callback(msg):
    rospy.loginfo(msg)


if __name__ == '__main__':
    rospy.init_node("turtlePoseSubscriber")
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.info("Node has already started working")

    rospy.spin()