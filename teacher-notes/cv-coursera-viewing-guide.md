# Current Coursera Viewing Guide

This guide defines how Coursera resources are used in the current VEX Robotics + Computer Vision course.

## Core Coursera Bridge

### IBM — Introduction to Computer Vision and Image Processing

https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Use this as a **short OpenCV bridge**, not as a full required course.

### Required / selected

**Module 1 — Introduction**
- select the videos needed to establish what computer vision is and what problems it solves.

**Module 2 — Image Processing with OpenCV and Pillow**
- this is the main required block;
- focus on digital images, pixels/channels, basic OpenCV operations, and image-processing concepts that help explain VEX AI Vision.

**Module 5 — Object Detection**
- select only the object-detection concepts that help bridge classical image processing to modern CV.

### Skip as core

- Module 3 — machine-learning image classification;
- Module 4 — CNN;
- Module 6 — transfer-learning project.

Reason: CNN / learned-CV theory is handled more cleanly through selected Stanford CS231n material later.

## Required local connection

Students must connect:

> **image → HSV / threshold → mask → object region → bounding box → center**

to:

> **VEX Color Signature → centerX / centerY / width / height**

## Optional Advanced Coursera

### University of Toronto — Visual Perception for Self-Driving Cars

https://www.coursera.org/learn/visual-perception-self-driving-cars

Status: **Optional Advanced / after-class enrichment.**

Recommended for stronger students who want deeper study in:
- camera models / calibration;
- feature detection / matching;
- visual odometry;
- object detection / tracking;
- semantic segmentation;
- mobile-platform perception.

Do not make this advanced course a whole-class requirement.

## Not Required

- full IBM completion;
- old Coursera OpenCV main-course plan;
- mandatory Andrew Ng CNN;
- mandatory Edge Impulse.

## Viewing Protocol

1. Give a prediction question before the clip.
2. Watch only the focused segment needed.
3. Apply the idea immediately in OpenCV or VEX.
4. Test and collect evidence.
5. Have students explain the concept from memory.

Coursera supports the project; it does not replace the project.