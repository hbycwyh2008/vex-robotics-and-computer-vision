# Lessons — Current Use

Use [../CURRENT-COURSE-PATH.md](../CURRENT-COURSE-PATH.md) as the authoritative sequence.

## Important

This repository contains lesson material from an earlier broader VEX curriculum. Some of those lessons remain useful, but the current course no longer requires students to complete every sensor/autonomy/mechanism topic before computer vision.

The current class has already built and CAD-modeled the TrainingBot. The current path is:

> **Minimum VEXcode → AI Vision → Object Centering → Object Following → OpenCV → AprilTag → Integrated Vision Robot → Onshape Redesign**

## Use These Existing Lesson Areas Selectively

### 01-trainingbot

Reference only for hardware/build troubleshooting. The current class has already completed the physical TrainingBot and Onshape TrainingBot model.

### 02-driver-control

Use only the minimum material needed for:
- VEXcode device setup
- Python/Code Viewer bridge
- drivetrain motion
- variables / functions / conditionals / loops

Do not require a long Controller-programming sequence before AI Vision.

### 03-sensors-autonomy

**Extension/reference, not required core.**

Distance Sensor, Optical Sensor, Inertial Sensor, and long autonomous-navigation work should not delay AI Vision. Use individual lessons only if a later project creates a real need.

### 04-engineering-design

Use engineering iteration/testing ideas as needed. Mechanism/competition lessons are optional until after the core vision robot works.

### 05-computer-vision

OpenCV concepts remain important, but teach them after students have first used the VEX AI Vision Sensor enough to understand the practical meaning of target position and size.

Core OpenCV concepts:
- image/pixel
- RGB/BGR and HSV
- thresholding
- masks
- contours
- bounding boxes
- center/centroid
- real-time frames

Core structured course:

**Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

### 06-ai-robotics-integration

Use for perception → decision → action concepts, especially closed-loop alignment and robustness.

However, the current implementation should first use the VEX AI Vision Sensor:
- Color Signature
- centerX / centerY
- width / height
- Object Centering
- Object Following
- AprilTag

### 07-capstone

Use the capstone structure after students can build a working vision-guided robot.

Core final behavior:

> **Search → Detect → Center → Approach → Stop / Perform Task**

## New Current Sequence

1. VEXcode V5 intro videos
2. Drivetrain mini-task
3. mount/connect AI Vision Sensor
4. camera feed
5. Color Signature
6. vision data
7. Object Centering Robot
8. Object Following Robot
9. Coursera OpenCV Fundamentals
10. OpenCV HSV/mask/contour/bounding-box labs
11. AprilTag
12. final integrated vision robot
13. Onshape camera-mount redesign based on real test evidence

## Deep Learning

Older lesson/resource references to required Andrew Ng CNN and Edge Impulse work should now be treated as optional advanced extension material.

The current required CV core is VEX AI Vision + classical OpenCV.