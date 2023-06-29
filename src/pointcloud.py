import rospy
from sensor_msgs.msg import PointCloud2



if __name__ == '__main__':
    try:
        rospy.init_node('point_cloud', anonymous=True)
        point = rospy.wait_for_message("/zed2/zed_node/point_cloud/cloud_registered",PointCloud2)
        print(len(point.data),'\n',point.height,point.width)
        p = (point.fields)
        print(p)
        data = point.data
    except rospy.ROSInterruptException:
        pass
