# Syllabus — VEX Robotics + Computer Vision

## Course Description

This project-based high school course uses **VEX V5 robotics, the VEX AI Vision Sensor, Python, Onshape, and OpenCV** to teach engineering design, robot control, computer vision, and intelligent behavior.

The VEX robot is the main learning platform. External CV material is used to explain and extend what students already build on the robot.

> **Perception → Decision → Action → Testing → Improvement**

Current curriculum architecture:

> **VEX official robotics mainline → Robotics-focused OpenCV → Modern CV theory → Integrated intelligent robot**

See [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md).

## Current Classroom Starting Point

The current class has already:
- built the TrainingBot / four-wheel V5 robot;
- completed the TrainingBot in Onshape;
- learned basic VEXcode V5 / Python;
- run the AI Vision Sensor successfully.

The next major step is adding **arm + claw** for vision-guided manipulation.

## Standard Hardware and Software

### Robotics
- VEX V5 Competition Starter Kit or equivalent V5 hardware
- V5 Brain
- Controller
- Smart Motors
- VEX AI Vision Sensor
- V5 Claw / arm + claw structure

### Software
- VEXcode V5
- Python
- Onshape
- OpenCV
- GitHub + Markdown

### External CV Learning
- **Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation** — selected robotics-relevant sections
- **Stanford CS231n — Deep Learning for Computer Vision** — selected modern-CV lectures

## Learning Outcomes

By the end of the course, students will be able to:
1. maintain an engineering notebook with evidence and decisions;
2. use essential Onshape skills for robot structures and mounts;
3. control a VEX drivetrain with Python;
4. use variables, loops, conditionals, and functions in robot programs;
5. configure and test the AI Vision Sensor;
6. interpret exists, centerX, centerY, width, and height;
7. build object-centering and object-following behavior;
8. control a robot arm and claw;
9. combine AI Vision with the claw for vision-guided pickup;
10. use AprilTags for tag-based navigation/decisions;
11. explain images, pixels, RGB/BGR, HSV, thresholding, masks, contours, and bounding boxes;
12. connect VEX Color Signature to classical OpenCV thresholding;
13. connect centerX / centerY to contour/bounding-box centers;
14. connect Object Following to tracking / visual servoing;
15. explain the basic role of CNNs, learned features, transfer learning, and object detection;
16. distinguish classical rule-based CV from learned computer vision;
17. build and test an integrated autonomous vision robot;
18. redesign robot structures from test evidence.

## Core Units

### Unit 1 — Engineering Notebook and Design Process
Ongoing through the course.

### Unit 2 — Essential Onshape
Part Studio essentials, Assemblies, VEX V5 Parts Library, later evidence-based mount/manipulator redesign.

### Unit 3 — VEXcode V5 / Python Foundation
Drivetrain control, variables, conditionals, loops, functions.

### Unit 4 — VEX AI Vision Core
Color Signature, camera data, centerX / centerY / width / height, reliable detection.

### Unit 5 — Closed-Loop Vision Control
Object Centering and Object Following.

### Unit 6 — Arm + Claw
Mechanical claw/arm build and Python control.

Core project:

> **Detect → Center → Approach → Open → Grab → Lift**

### Unit 7 — AprilTag Navigation
Tag ID, target position, orientation/angle, tag-based behavior.

### Unit 8 — Robotics-Focused OpenCV
Use selected sections from:

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Required topics:
- Color Spaces
- Thresholding
- Contour Detection
- Morphological Operations
- Object Tracking
- ArUco Marker

Optional:
- Image-Based Visual Servoing

### Unit 9 — Modern CV Theory
Use selected Stanford CS231n lectures:
- Computer Vision overview
- CNNs
- architectures / transfer learning
- object detection

https://cs231n.stanford.edu/

### Unit 10 — Integrated Intelligent Robot
Recommended final behavior:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

### Unit 11 — Evidence-Based CAD Redesign
Use real test evidence to redesign the AI Vision mount, camera placement, claw geometry, or robot structure.

## Major Projects

1. Reliable Color Detection
2. Object Centering Robot
3. Object Following Robot
4. Vision-Guided Grab
5. AprilTag Navigation
6. OpenCV Robotics Vision Labs
7. Final Integrated Vision Robot
8. Evidence-Based Onshape Redesign

## Not Required Core Material

The following are optional/reference rather than the current core:
- separate Distance Sensor unit;
- separate Optical Sensor unit;
- separate Inertial Sensor unit;
- dedicated PID unit;
- long competition-autonomy sequence;
- full Onshape Fundamentals;
- IBM Computer Vision course;
- previous Coursera OpenCV course as the main CV course;
- mandatory Andrew Ng CNN sequence;
- mandatory Edge Impulse sequence.

## Assessment Emphasis

Suggested weighting:
- Engineering evidence / portfolio: 20%
- Formative checks / quizzes: 15%
- Projects and challenges: 40%
- Final integrated project: 20%
- Presentation / reflection: 5%

The priority is working systems, test evidence, explanation, and iteration—not simply finishing videos.
