# Course Overview — VEX Robotics + Computer Vision

## What This Course Is

A project-based high school course in which students use **VEX V5 + AI Vision Sensor + Python + Onshape + OpenCV** to build intelligent robotic systems.

The course is organized in three layers:

1. **VEX official robotics mainline** — build, code, sense, move, grab, navigate.
2. **Robotics-focused classical CV** — explain the vision pipeline with OpenCV.
3. **Modern learned CV theory** — introduce CNNs and object detection after the classical system is understood.

> **The robot is the main course. CV theory explains and extends what the robot already does.**

## Current Status

Students have already:
- built the TrainingBot;
- recreated it in Onshape;
- learned basic VEXcode V5 / Python;
- run the AI Vision Sensor successfully.

The next stage is **arm + claw + AI Vision**.

## Standard Platform

- VEX V5 Competition Starter Kit / equivalent V5 hardware
- V5 Brain
- Controller
- Smart Motors
- AI Vision Sensor
- arm + claw / V5 Clawbot structure
- VEXcode V5
- Python
- Onshape
- OpenCV

## Core Robotics Sequence

1. AI Vision Color Signature
2. centerX / centerY / width / height
3. Object Centering
4. Object Following
5. Add arm + claw
6. Vision-Guided Grab
7. AprilTag Navigation
8. Integrated autonomous task

Core feedback loop:

> **Camera → Perception Data → Decision Logic → Drivetrain / Arm / Claw → New Camera Data**

## Practical CV Sequence

Use selected sections from:

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Focus on:
- Color Spaces
- Thresholding
- Contours
- Morphology
- Object Tracking
- ArUco Marker
- optional Visual Servoing

The goal is not to finish all 110+ lectures. The goal is to explain the computer-vision concepts that directly map to the VEX projects.

## Modern CV Sequence

Use selected material from:

**Stanford CS231n — Deep Learning for Computer Vision**

https://cs231n.stanford.edu/

Focus on:
- CV overview
- CNNs
- architectures / transfer learning
- object detection

Students should understand the progression:

> **hand-written visual rules → learned features → modern object detection**

## Core Concept Mapping

| Robot experience | CV concept |
|---|---|
| Color Signature | HSV + thresholding |
| centerX / centerY | object / bounding-box center |
| width / height | object scale / bounding-box size |
| Following | tracking / visual servoing |
| AprilTag | fiducial markers |
| Grab | vision-guided manipulation |
| AI Classification | learned perception |

## Final Project

Recommended capstone:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

Students must explain:
- perception;
- decision logic;
- control;
- manipulator action;
- failure modes;
- test evidence;
- classical vs learned CV.

## CAD Role

Onshape remains a just-enough engineering tool.

Return to CAD only when real testing creates a design need such as:
- poor camera angle;
- occlusion by the arm;
- unstable sensor mount;
- claw interference;
- cable routing.

> **CAD → Build → Code → Vision → Test → Redesign**

## What Is No Longer Core

Not required as the main sequence:
- IBM CV course;
- previous Coursera OpenCV main-course plan;
- mandatory Andrew Ng CNN;
- mandatory Edge Impulse;
- separate traditional VEX sensor units before CV;
- full Onshape Fundamentals.
