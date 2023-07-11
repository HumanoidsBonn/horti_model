#!/usr/bin/env python3
import time
import rospy
from gazebo_msgs.srv import SetModelConfiguration
from gazebo_msgs.srv import SetModelConfigurationRequest
from std_srvs.srv import Empty, EmptyRequest
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
pub_head_command = rospy.Publisher("/head_controller/command", JointTrajectory, queue_size=1, latch=True)

def set_model_config():
    time.sleep(1)
    rospy.logwarn("Setting model configuration")
    reset_joints =  rospy.ServiceProxy('/gazebo/set_model_configuration', SetModelConfiguration)

    reset_req = SetModelConfigurationRequest()
    reset_req.model_name = 'robot'
    reset_req.urdf_param_name = 'robot_description'
    reset_req.joint_names = ['head_joint1', 'head_joint2', 'head_joint3', 'head_joint4', 'head_joint5', 'head_joint6']
    reset_req.joint_positions = [0.0, -2.3038, 0.2037, 0.0, 0.0, -0.81]
    reset_res = reset_joints(reset_req)
    rospy.logwarn("Unpausing physics...")
    unpause_physics = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
    unpause_req = EmptyRequest()
    unpause_res = unpause_physics(unpause_req)
    rospy.logwarn("...Unpaused physics")

def publish_command():
    

    traj = JointTrajectory()
    traj.header.stamp = rospy.Time.now()
    traj.joint_names = ['head_joint1', 'head_joint2', 'head_joint3', 'head_joint4', 'head_joint5', 'head_joint6']
    traj_point = JointTrajectoryPoint()
    traj_point.positions = [0.0, -2.3038, 0.2037, 0.0, 0.0, -0.81]
    traj_point.time_from_start = rospy.Duration.from_sec(0.5)

    traj.points.append(traj_point)
    i = 0

    while i < 5:
        rospy.logwarn("Publishing command")
        traj.header.stamp = rospy.Time.now()
        pub_head_command.publish(traj)
        i = i +1
        time.sleep(1)

if __name__ == '__main__':
    rospy.init_node('set_model_config')
    set_model_config()
    publish_command()
    rospy.logwarn("Set model config done")
