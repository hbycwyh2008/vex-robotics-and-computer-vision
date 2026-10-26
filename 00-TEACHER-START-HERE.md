# Teacher Start Here — Current Delivery Guide

Use this file with [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md). The current course has been intentionally simplified around VEX AI Vision + formal OpenCV learning.

## Important 2026 Update

The current class has already:
- built the VEX V5 TrainingBot / four-wheel robot;
- driven it with an existing Controller program;
- completed the TrainingBot in Onshape.

Therefore, do **not** restart with a long TrainingBot build, full Controller programming, or separate Distance/Optical/Inertial sensor sequence.

The current backbone is:

> **Minimum VEXcode → AI Vision → Object Centering → Object Following → OpenCV → AprilTag → Integrated Vision Robot → Onshape Redesign**

## What Is Authoritative

Use these files first:
1. [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md)
2. [syllabus.md](syllabus.md)
3. [pacing-guide.md](pacing-guide.md)
4. [resources.md](resources.md)

Older anchor lessons and the 72-meeting playbook remain useful as a resource bank, but parts of them reflect the previous broader curriculum. If they conflict with CURRENT-COURSE-PATH.md, follow CURRENT-COURSE-PATH.md.

## Next Teaching Sequence

### 1. VEXcode V5 basics

Use:
- Lesson 1 — Coding with VEXcode V5: https://pd.vex.com/hu/node/1479
- Lesson 2a — Code Viewer in VEXcode V5 (Python): https://pd.vex.com/training/v5/vex-v5-introductory-training-course/lesson-2a-using-the-code-viewer-in-vexcode-v5

Teach only enough for students to perform:

> **Forward → Turn → Stop → Forward**

Students need:
- drive / drive_for
- turn / turn_for
- stop
- set_drive_velocity
- variables
- conditionals
- while loops
- simple functions

### 2. Mount AI Vision Sensor

Use the simple four-wheel V5 Advanced Trainingbot-style platform.

Resource:
https://kb.vex.com/hc/en-us/articles/28385212896916-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Advanced-Trainingbot

Do not require a custom CAD mount before students have real vision-testing evidence.

### 3. Camera feed and Color Signature

Resources:
- https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5
- https://kb.vex.com/hc/en-us/articles/24067512493972-Configuring-Color-Signatures-with-the-AI-Vision-Sensor-in-VEXcode-V5

Students should test lighting, distance, angle, and background.

### 4. Vision data

Focus on:
- exists
- centerX
- centerY
- width
- height
- take_snapshot()

Resources:
- https://kb.vex.com/hc/en-us/articles/24068869007636-Understanding-the-Data-in-the-AI-Vision-Utility-in-VEXcode-V5
- https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python

### 5. Object Centering

Teach:

> **error = centerX - 160**

Students build:

> **See → Measure → Decide → Turn → See Again**

### 6. Object Following

Use:
- centerX for steering
- width/height as rough near/far evidence

Target behavior:

> **Find → Center → Approach → Stop**

### 7. Formal OpenCV course

Core course:

**Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Required concepts:
- image/pixel
- RGB/BGR
- HSV
- thresholding
- masks
- contours
- bounding boxes
- center/centroid
- real-time frames

Face-recognition-specific material is optional.

### 8. AprilTag

Teach after color tracking is reliable.

Resource:
https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

### 9. Final integrated project

Core behavior:

> **Search → Detect → Center → Approach → Stop / Perform Task**

### 10. Return to Onshape

Only after real testing reveals a camera-placement problem, redesign the mount.

> **CAD → Build → Code → Vision → Test → Redesign**

## Onshape Scope

Do not continue full Onshape Fundamentals.

Core scope:
- Part Studio essentials
- Introduction to Onshape Assemblies
- VEX V5 Parts Library
- TrainingBot CAD
- later AI Vision mount redesign

Skip:
- Drawings
- Detailed Drawings
- Inspection and Repair
- advanced surfacing
- sheet metal
- certification preparation

## Engineering Notebook

Use the notebook every major work session.

Minimum evidence:
- Goal
- Work
- Evidence
- Decision
- Next Step

Useful files:
- student-handouts/engineering-notebook-guide.md
- student-handouts/engineering-notebook-template.md
- student-handouts/individual-engineering-learning-log.md
- student-handouts/test-record-template.md

## What Is Now Optional

The following no longer belong in the required core path:
- separate Distance Sensor unit
- separate Optical Sensor unit
- separate Inertial Sensor unit
- dedicated PID unit
- long competition-autonomy unit
- required Andrew Ng CNN sequence
- required Edge Impulse sequence

Use them only as extensions after the core vision robot works.