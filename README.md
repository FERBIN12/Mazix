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

![image](https://github.com/FERBIN12/Mazix/assets/126778624/ee96c171-275d-4853-b59e-35214e0fac88)

In terminal 2:

    ros2 run mazix_description qr_auto_node.py

![image](https://github.com/FERBIN12/Mazix/assets/126778624/3950ca65-70db-4511-893c-5241cc793068)

