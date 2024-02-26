**MAZIX - AUTONOMOUS MAZE SOLVING USING 2DLIDAR AND QR SCANNING**

OS AND SOFTWARE USED:

UBUNTU 22.04

ROS2 -HUMBLE

OPENCV
            
Packages needed:
        
        sudo apt install ros-humble-xacro
        sudo apt install ros-humble-joint-state-publisher-gui
        sudo apt install ros-humble-gazebo-ros-pkgs

LAUNCHING COMMANDS:

In terminal 1:
                        
    ros2 launch mazix_description launch_sim.launch.py 
In terminal 2:
                        ros2 run mazix_description qr_auto_node


