# **Development of An Autonomous Healthcare Assistant**
ResQ Health Companion

**Under the Supervision of**

**PROF. TUFAN SAHA**

#

 Department of Computer Science &amp; Engineering Institute of Engineering and Management West Bengal, India

**November, 2020**

# Abstract

As life grows to be fast-paced, the focus on good health habits and provisions on healthcare gets less evident among the people and communities. Busy work schedules often lead to delay or skipping of healthy meals and medication, which are supposed to be taken regularly on time. As more and more professionals have to move to different workplaces, their parents and families, especially the elderlies often face mobility problems, forget to take their medicines and even during emergency situations face problems to manage themselves due to lack of a personal support.

The conclusion is, it is absolutely normal for humans to make errors. But in a sensitive domain of healthcare, the margin of error should optimally be zero.

It was necessary to develop a system which could provide support to ensure that healthcare routines are followed during a busy schedule by providing hand-in-hand. Detecting and handling emergencies should also be a real-time priority of the system. The problem of affordability for a helping hand is also considered along with its reliability. Our study and research will be oriented around these mentioned fields.

For this system, a working model able to comply and address to all the mentioned limitations will be developed. The basic working principle will utilize various concepts of Robotics and Near-Human Intelligence based on computer vision, sensory data, geo-positioning &amp; artificial intelligence algorithms to solve the various problems.

_ **Near Intelligence &amp; Human-Like Capabilities:** _ One of the fundamental necessities of the system will be the ability to operate across a wide variety of challenging workspaces. Precision movements not limited only to movement but to interact with the user efficiently upon call or autonomously is a major priority of the system. The design goals of the [LX17] TRINA which was related to hospital mobility with light-to-medium duty tasks were studied. However, the system was controlled remotely by an operator console with a low-level command interface. The ability to turn a compact system into autonomous was kept in mind.

_ **Computer Vision &amp; Object Recognition:** _ An array of sensory feedback was required for this system with adequate programming. Collision detection [WANG18], limitation of path, and possible 3D Environment Map [LX17] could be useful for the system. User addressing system as well as extra vanity features for the domain of mental healthcare was also proposed.

_ **Medicine Dispensing and Time Management** _: Generally, to ensure good health and also, for patients recovering from an illness, the requirement to consume medicines on a scheduled routine is of vital importance. The ability to carry and dispense medicines [LX17], the ability to detect when quantity of stock is low and also to ensure easy programming by the user for restocking the items in an inbuilt storage system is necessary. The time management can be utilized by programming into the system once by an user through a WebGUI-based software running on the local network.

_ **Power Systems &amp; Electronics:** _ The system will be capable of carrying medium loads with a scale of economic factors in mind. Thereby, the mainboard requires custom application-specific design with embedded microcontrollers. A lead-acid battery will be adequate to power the motors that is proposed to be utilized. The system software will have an algorithm that will allow it to automatically notify the user and charge, while keeping alert of the surrounding. A standby mode will also be utilized to improve user runtime. The chassis heat management will be mitigated using custom cooling solutions.

_ **System Architecture:** _ A complete utilization of electronics, path-finding algorithms [FINA89] and IOT Subsystems and Advanced Sensors is proposed to be utilized. The system is for use in medical domain so deployment will be possible upon successful reliability and stress-testing across a multitude of different environments.

_ **Assistant &amp; User Interaction:** _ We have envisioned the system to interact with the user using limited voice-communication commands in real-time. The system will also be able to support the user&#39;s mental health with intelligent communications on demand. The system will also be able to spot abnormal events and report to a guardian registered on the system domain or health authorities, in case it detects the user to be in a difficult state, so as to ensure it remains valid for users of different age categories, preferable when deployed for a family.


# Survey

This report surveys, analyzes and provides valuable insights for the project &quot;Development of An Autonomous Healthcare Assistant&quot;, an autonomous system which is deemed to be capable of addressing to human healthcare needs and offer various handsfree features.

So, various research was made into systems like this, and mostly, the ones deployed are in research and development stage, and includes extremely complex electronics and aren&#39;t in the production stage. Also, many systems were not capable of handsfree communication or motion in general.

For our project, we have made best use of what we have available in stock, and most of the items like PCB were manually designed and soldered, and all the power-supply and filtering system were made by standard components like capacitors and buck/boost-converter modules.

In our project, we have put effort and are addressing these issues, and mitigating a few difficulties that we faced during our current development stage, which we will discuss below.

We faced a few challenges during this development phase for our project which are being addressed:

- The unavailability of parts like LiDAR module, which was expensive, are being addressed with a 360Degree Ultrasonic Module Array, which is less accurate than the mentioned system.


- For the project, we used a Raspberry Pi Model 3B+ with 1GB of RAM and we faced difficulties to make the &#39; **face\_recognition&#39;** library work smoothly on this hardware. We are addressing this hardware limitation by experimenting on human face-detection only using standard **&#39;open-cv&#39;** library using HaaR Cascades.

- The medicine dispensing feature required powerful servo motors, generally used in mini-RC-Aero-planes and we are currently in the development stage for this feature.


- There are intermittent WIFI Drops in regions of low signal when the robot starts moving due to the high inrush current to the wheel-motors. We are rectifying this issue currently.


- All the handsfree features like medicine names, times, doctor appointments work smoothly and we are offering a smaller database for demonstration purpose, using a free instance of MongoDB Atlas deployed on the cloud and fetching it by simple voice authentication.

Our system, when compared to current projects under research address a multitude of problems:

 1) Handsfree communication allows every user of any age group to interact comfortably with this device using simple voice commands

2) Less development and manufacturing cost can give an end user significant benefit. The robot will cost less than a powerful smartphone in the market with all the sensors and better hardware like the Raspberry Pi 4 with 4GB or more RAM.

3) Various iterations of the voice-recognition system may be built on the same hardware for various purposes, for example, in children hospital, there should be a different type of voice assistant put to use, in comparison to a elderly person&#39;s hospital or home.

4) Emergency situation handling and general area patrolling systems will significantly boost the confidence of the users at home.


# References

**[LX17]** Zhi Li, Peter Moran, Qingyuan Dong, Ryan J. Shaw, Kris Hauser. Development of a Tele-Nursing Mobile Manipulator for Remote Care-giving in Quarantine Areas (TRINA),

2017 IEEE International Conference on Robotics and Automation, May 29 - June 3, 2017.

**[WANG18]** Weitian Wang, Rui Li, Longxiang Guo, Z.Max Diekel, Yunyi Jia. Hands-Free Maneuvers of Robotic Vehicles via Human Intentions Understanding Using Wearable Sensing, Dept. of Automotive Engineering - Clemson University, USA, Hindawi - Journal of Robotics, 17th April, 2018.

**[FINA89]** E.Y.Rodin, S.M. Amin. Intelligent Navigation for Autonomous Mobile Robot, Dept. of Systems Science &amp; Mathematics,Washington University,USA,IEEE 2016 Proceedings IEEE International Symposium on Intelligent Control 1988,Arlington, Virginia, USA.
