# Teacher Start Here — Current Delivery Guide

Use [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md) as the authoritative sequence.

## Current Class Status

Students have already:
- built the TrainingBot / four-wheel V5 robot;
- completed the TrainingBot CAD model;
- completed basic VEXcode V5 / Python introduction;
- run the AI Vision Sensor successfully.

Therefore, do not restart a long hardware or basic programming sequence.

## Current Backbone

> **AI Vision → Centering → Following → Arm + Claw → Vision-Guided Grab → AprilTag → Robotics-Focused OpenCV → CS231n selected theory → Final Intelligent Robot**

## Next Teaching Steps

### 1. Confirm AI Vision reliability
Students should be able to:
- configure a Color Signature;
- read centerX / centerY / width / height;
- explain changing detection results;
- test lighting, distance, angle, and background.

### 2. Object Centering
Teach:
> **error = centerX - 160**

Build:
> **See → Measure → Decide → Turn → See Again**

### 3. Object Following
Use:
- centerX for steering;
- width / height as rough near/far evidence.

Target behavior:
> **Find → Center → Approach → Stop**

### 4. Add Arm + Claw
Official resources:
- AI Vision on V5 Clawbot: https://kb.vex.com/hc/en-us/articles/28385434989716-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Clawbot
- V5 Claw 3D instructions: https://kb.vex.com/hc/en-us/articles/15516473701524-Repairing-and-Reassembling-a-V5-Clawbot-Claw-V5-Claw-Kit-v2
- Robot Arm — Python: https://education.vex.com/stemlabs/v5/stem-labs/speedy-delivery/programming-the-robot-arm-python

Core project:
> **Detect → Center → Approach → Open → Grab → Lift**

### 5. AprilTag
Use after the basic claw project works:
https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

Possible extension:
> **Grab → find destination tag → navigate → deliver**

### 6. Robotics-Focused OpenCV
Use selected sections from:

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Assign only:
- Color Spaces
- Thresholding
- Contour Detection
- Morphology
- Object Tracking
- ArUco Marker
- optional Visual Servoing

Every video should connect to a VEX behavior.

### 7. Modern CV Theory
Use selected Stanford CS231n material:
https://cs231n.stanford.edu/

Focus on:
- CV overview;
- CNNs;
- transfer learning / architectures;
- object detection.

Do not assign the full Stanford course.

### 8. Final Project
Recommended behavior:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

### 9. Return to Onshape
Redesign only when test data shows a real problem.

Possible redesigns:
- camera angle;
- sensor height;
- arm occlusion;
- claw geometry;
- mount stiffness.

## Engineering Notebook

Every major session should leave:
- Goal
- Work
- Evidence
- Decision
- Next step

## Resource Priority

Use this order:
1. VEX official docs / videos for V5 and AI Vision;
2. VEX STEM Labs for Python / robot manipulation;
3. Udemy selected robotics-CV videos for classical CV;
4. OpenCV official docs for technical reference;
5. Stanford CS231n selected lectures for modern CV theory.

## No Longer the Main Path

Do not treat these as required core courses:
- IBM CV;
- previous Coursera OpenCV main-course plan;
- mandatory Andrew Ng CNN;
- mandatory Edge Impulse.

Older lesson files can still be mined for activities, but the sequence above controls delivery.
