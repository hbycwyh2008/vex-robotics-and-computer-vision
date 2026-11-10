# CURRENT COURSE PATH — VEX Robotics + Computer Vision

> **Status:** authoritative current course path. If older lesson files conflict with this document, follow this document.

## Current Classroom Status

The current class has already:
- built the VEX V5 TrainingBot / simple four-wheel robot;
- completed the TrainingBot in Onshape;
- learned the basic VEXcode V5 / Python workflow;
- completed the official VEX AI Vision Sensor project sequence, including the main color, vision-data, classification/tracking, and AprilTag activities used in this course.

There is **no mechanical arm / manipulator unit in the current course**. Do not add a claw, pick-and-place, or industrial robot-arm pathway just to match an external CV course.

## Current Course Architecture

> **VEX AI Vision completed → Short OpenCV Bridge → Independent VEX Vision Challenge → Selected CS231n theory → Final Autonomous Vision Robot**

Optional advanced after-school / homework enrichment:

> **University of Toronto — Visual Perception for Self-Driving Cars**

---

# Phase 1 — Engineering Notebook (ongoing)

Students continue to record:
- Goal
- Work / change
- Evidence
- Test result
- Decision
- Next step

Use the notebook throughout independent robot challenges, OpenCV bridge labs, testing, and redesign.

---

# Phase 2 — Essential Onshape

Current status: **TrainingBot CAD completed.**

Onshape remains a just-enough engineering tool. Return to CAD only when real testing creates a need such as camera angle, sensor height, field of view, vibration, cable routing, or mount stiffness.

Do not require full Onshape Fundamentals.

---

# Phase 3 — VEXcode V5 / Python

Current status: **basic VEXcode/Python foundation completed.**

Students should already understand the drivetrain basics, variables, conditionals, loops, and simple functions needed for vision-based control.

---

# Phase 4 — VEX AI Vision Sensor

Current status: **official AI Vision project sequence completed.**

Students should now be able to use and explain:
- Color Signature
- exists
- centerX / centerY
- width / height
- repeated visual feedback
- AI Classification
- AprilTags
- perception → decision → action

Do not spend the next unit repeating official sensor tutorials.

---

# Phase 5 — OpenCV Bridge (Core, Short)

OpenCV is not a full semester course here. Its purpose is to reveal what is happening underneath the VEX AI Vision abstraction and improve debugging / competition reasoning.

## Core Coursera resource

**IBM — Introduction to Computer Vision and Image Processing**

https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

### Required scope

- **Module 1 — selected introduction material**
  - what computer vision is
  - applications / perception pipeline
- **Module 2 — core OpenCV / image-processing material**
  - digital images and pixels
  - image arrays / channels
  - basic OpenCV operations
  - selected image transformations / filtering as useful
- **Module 5 — selected object-detection concepts only**
  - use only enough to bridge from classical image processing to modern detection

### Skip as core

- Module 3 — ML image classification
- Module 4 — CNN material
- Module 6 — transfer-learning project

Those topics are better handled later through selected CS231n material.

## Local OpenCV bridge labs

Students should understand this pipeline:

> **image → HSV / threshold → mask → contour / object region → bounding box → center**

and explicitly connect it to:

> **VEX AI Vision → Color Signature → centerX / centerY / width / height**

Recommended duration: **3–5 hours of selected Coursera/video/lab work, not the full IBM course.**

---

# Phase 6 — Independent VEX Vision Challenge

After the OpenCV bridge, students stop following tutorials and design a robot behavior with no step-by-step solution.

Recommended challenge:

> **Search → Detect → Center → Approach → Identify Marker → Choose Action → Navigate → Stop**

Possible requirements:
- use at least two perception states;
- use AprilTag or target identity for a decision;
- use repeated visual feedback rather than one-shot movement;
- document failure cases under different conditions;
- justify thresholds / stopping conditions;
- use a simple state machine if appropriate.

This is the main transition from tutorial-following to engineering.

---

# Phase 7 — Modern CV Theory: Stanford CS231n (Selected)

Course:
- https://cs231n.stanford.edu/
- https://cs231n.stanford.edu/schedule

Use selected material only:
- Computer Vision overview
- convolution / CNNs
- feature learning / pooling
- architectures and transfer learning at overview level
- object detection
- bounding boxes / IoU / NMS / YOLO-style concepts

Do not require the full Stanford course or full assignment sequence.

Purpose:

> **VEX AI Vision use → classical OpenCV understanding → modern learned-CV understanding**

---

# Phase 8 — Optional Advanced Coursera Study

**University of Toronto — Visual Perception for Self-Driving Cars**

https://www.coursera.org/learn/visual-perception-self-driving-cars

Status: **Optional Advanced / after-class enrichment. Not required for core assessment.**

Recommended for stronger students who want deeper work in:
- camera models / calibration
- feature detection and matching
- visual odometry
- object detection / tracking
- semantic segmentation
- mobile-robot / autonomous-vehicle perception

Do not slow the whole class down to complete this advanced course.

---

# Phase 9 — Final Autonomous Vision Robot

Recommended capstone behavior:

> **Search → Detect → Center → Approach → Identify → Choose Route / Action → Navigate → Stop**

Required integration:
- VEX V5 drivetrain
- VEXcode Python
- AI Vision Sensor
- visual perception data
- decision logic
- repeated feedback
- autonomous mobile behavior
- testing evidence
- engineering notebook
- explanation of classical vs learned CV

Possible extensions:
- state machine
- multi-target behavior
- route choice based on AprilTag
- robustness testing
- competition-style timing / reliability
- optional learned object detection off-robot as an enrichment study

---

# What Is Not Core

The following are **not** part of the current required pathway:
- mechanical arm / claw / pick-and-place
- industrial robot-arm simulation
- Udemy Hands on Robotic Vision course
- full IBM CV course
- full CS231n course
- full University of Toronto advanced course
- required Andrew Ng CNN sequence
- required Edge Impulse sequence

Udemy may be referenced individually if a specific clip solves a teaching need, but it is not a planned course component.

# Current Core Sequence

1. Engineering Notebook — ongoing
2. Onshape / VEXcode foundations — completed
3. Official VEX AI Vision projects — completed
4. IBM OpenCV Bridge — selected Module 1 + core Module 2 + selected Module 5
5. Independent VEX Vision Challenge
6. Stanford CS231n — selected modern-CV theory
7. Final Autonomous Vision Robot
8. University of Toronto Visual Perception — optional advanced after-class study

That is the current curriculum backbone.