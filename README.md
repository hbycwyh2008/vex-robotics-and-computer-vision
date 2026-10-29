# VEX Robotics + Computer Vision

A project-based high school course using **VEX V5 + VEX AI Vision Sensor + Python + Onshape + OpenCV**.

> **Current architecture:** VEX official robotics mainline → Robotics-focused OpenCV → Modern CV theory → Integrated intelligent robot

Start here:
- [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md)
- [syllabus.md](syllabus.md)
- [pacing-guide.md](pacing-guide.md)
- [resources.md](resources.md)

## Current Classroom Status

Students have already:
- built the VEX V5 TrainingBot / simple four-wheel robot;
- completed the TrainingBot in Onshape;
- learned the basic VEXcode V5 / Python workflow;
- connected and run the VEX AI Vision Sensor successfully.

The next step is **vision-guided manipulation with an arm + claw**, followed by robotics-focused OpenCV and selected modern-CV theory.

## Main Learning Path

> **V5 Python → AI Vision → Centering → Following → Claw → Vision-Guided Grab → AprilTag → OpenCV Robotics Vision → CS231n selected theory → Final Intelligent Robot**

## Robotics Mainline

The VEX robot remains the center of the course.

Students use:
- VEX V5 Competition Starter Kit / compatible V5 hardware;
- V5 Brain, Controller, Smart Motors;
- AI Vision Sensor;
- VEXcode V5 + Python;
- V5 Clawbot / Clawbot-style arm + claw for manipulation.

Core VEX projects:
1. Reliable Color Detection
2. Object Centering Robot
3. Object Following Robot
4. Vision-Guided Grab
5. AprilTag Navigation
6. Integrated autonomous task

## Practical CV Course

The current external CV video resource is:

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Use selected sections only:
- Color Spaces
- Thresholding
- Contour Detection
- Morphological Operations
- Object Tracking
- ArUco Marker
- optional Visual Servoing

The purpose is to explain the CV behind the robot:

| VEX AI Vision | CV concept |
|---|---|
| Color Signature | HSV + thresholding |
| centerX / centerY | contour / bounding-box center |
| width / height | bounding-box size |
| Object Following | tracking / visual servoing |
| AprilTag | fiducial marker concepts |
| Claw + AI Vision | vision-guided manipulation |

## Modern CV Theory

After students understand the classical CV pipeline, use selected material from:

**Stanford CS231n — Deep Learning for Computer Vision**

https://cs231n.stanford.edu/

Focus on:
- CV overview;
- CNNs;
- architectures / transfer learning;
- object detection / YOLO-style concepts.

Do not require the full Stanford course.

## Final Integrated Project

Recommended capstone:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

Students should be able to explain:
- what the camera sees;
- how perception data is represented;
- how decision logic uses that data;
- how the drivetrain and manipulator act;
- how classical CV differs from learned CV;
- what failure evidence justifies redesign.

## Engineering Iteration

After real testing, students return to Onshape only when necessary to redesign:
- AI Vision mount;
- camera angle / height;
- arm occlusion;
- claw geometry;
- mounting stiffness.

> **CAD → Build → Code → Vision → Test → Redesign**

## Important Note About Older Materials

Older lesson/playbook files remain useful as references, but if they conflict with [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md), follow the current course path.

IBM CV, the previous Coursera OpenCV main-course plan, mandatory Andrew Ng CNN, and mandatory Edge Impulse are no longer the required core sequence.
