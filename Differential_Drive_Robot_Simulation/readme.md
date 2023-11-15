Modeling, simulation and controlling a four-wheeled diferential drive robot in ROS Rviz.

Q. CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package): Could not find a package configuration file provided by "amcl" with any of the following names: amclConfig.cmake amcl-config.cmake
solve:
sudo apt-get install ros-(your ros distribution)-(package name)`

Q. CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "dwa_local_planner"
  with any of the following names:
    dwa_local_plannerConfig.cmake
    dwa_local_planner-config.cmake
solve: 
sudo apt-get install ros-noetic-dwa-local-planner

Q. CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "gmapping" with any
  of the following names:
    gmappingConfig.cmake
    gmapping-config.cmake
solve:
sudo apt-get install ros-noetic-slam-gmapping

More installation:
sudo apt-get install ros-noetic-map-server
sudo apt-get install ros-noetic-move-base

****************************************************************************************

Checking gazebo : 

$gazebo
$gazebo --version

Robot_Model_Packages:
sudo apt-get install ros-noetic-gazebo-ros-pkgs
sudo apt-get install ros-noetic-gazebo-msgs
sudo apt-get install ros-noetic-gazebo-plugins
sudo apt-get install ros-noetic-gazebo-ros-control
sudo apt-get install ros-noetic-teleop-twist-keyboard

---creating new directories (urdf, launch)---

Additional packages installation:
catkin_create_pkg robot_model_pkg gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control

$catkin_make

$source ~/<directory_name>/devel/setup.bash

checking source:
echo $ROS_PACKAGE_PATH

roscore
roslaunch robot_model_pkg robot_xacro.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
