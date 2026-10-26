# CURRENT COURSE PATH — VEX Robotics + Computer Vision

> **Status:** authoritative 2026 course path. This file supersedes older sequencing that required a long traditional VEX sensor/autonomy track before computer vision.

## Current Classroom Starting Point

- Students already built the basic VEX V5 TrainingBot / four-wheel drive robot.
- Students already completed the TrainingBot in Onshape.
- The robot already has a working Controller program and can be driven.
- The course will use the **VEX AI Vision Sensor** as the primary perception sensor.
- The course does **not** require separate Distance Sensor, Optical Sensor, or Inertial Sensor units before computer vision.

## Course Goal

The course is not "complete all VEX topics, then learn CV." The robot is the physical platform for learning perception, decision, and action.

> **CAD → Robot Control → AI Vision → Vision-Based Control → Formal CV Course → Integrated Vision Robot**

Engineering Notebook work runs through the entire sequence.

---

# Phase 1 — Engineering Notebook (ongoing)

Students document:
- Goal
- Design / change
- Evidence
- Test result
- Decision
- Next step

Use the VEX digital notebook approach throughout CAD, programming, AI Vision, CV, and redesign.

Resources:
- VEX Getting Started with Engineering Notebooks: https://kb.vex.com/hc/en-us/articles/49010276056596-Getting-Started-with-Engineering-Notebooks
- VEX Digital Engineering Notebook Templates: https://kb.vex.com/hc/en-us/articles/49020662150676-Digital-Engineering-Notebook-Templates

---

# Phase 2 — Essential Onshape Only

Onshape is now an enabling skill, not a separate full CAD course.

## Required Onshape learning

1. **Part Studio essentials**
   - Sketch
   - dimensions and basic constraints
   - Extrude
   - Add / Remove
   - Hole
   - Fillet
   - Pattern / Mirror as needed

2. **Introduction to Onshape Assemblies only**
   - Create Assembly
   - Insert Part
   - position components
   - Mate Connector
   - Fastened Mate
   - Revolute Mate

3. **VEX V5 Parts Library**
   - use existing VEX standard parts rather than redrawing motors, wheels, channels, shafts, Brain, battery, etc.

## Required CAD application

- Rebuild the real TrainingBot in Onshape — **completed in the current class**.
- Later, after AI Vision testing exposes a real mounting problem, redesign the AI Vision Sensor mount in Onshape.

## Stop point

Do **not** require the rest of Onshape Fundamentals:
- Introduction to Drawings
- Detailed Drawings
- Inspection and Repair
- advanced surfacing
- sheet metal
- certification preparation

Resources:
- Onshape Fundamentals: CAD: https://learn.onshape.com/learning-paths/onshape-fundamentals-cad
- VEX V5 Parts Libraries in Onshape: https://www.onshape.com/en/blog/vex-iq-vex-v5-parts-libraries
- Using Onshape to Design a VEX Robot in the Cloud: https://www.onshape.com/en/resource-center/videos/using-onshape-to-design-a-vex-robot-in-the-cloud

---

# Phase 3 — Standard Robot Platform

Use the **V5 Advanced Trainingbot / simple four-wheel drivetrain + AI Vision Sensor** as the standard CV platform.

Why this platform:
- simple drivetrain
- stable mobile base
- no unnecessary arm/claw complexity during CV introduction
- official VEX AI Vision mounting guidance exists

Do not move to a complex Clawbot or manipulator before students can complete basic vision-guided movement.

Resource:
- Mounting and Wiring AI Vision Sensor on V5 Advanced Trainingbot: https://kb.vex.com/hc/en-us/articles/28385212896916-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Advanced-Trainingbot

---

# Phase 4 — Minimum VEXcode V5 Needed for Vision

Do not turn this into a full traditional VEX programming unit.

## Required VEXcode platform learning

Students learn only enough to connect code to robot motion:
- create/open a VEXcode V5 project
- configure/use the Drivetrain
- download/run/stop
- understand Blocks ↔ Python using Code Viewer

Required videos:
- Lesson 1 — Coding with VEXcode V5: https://pd.vex.com/hu/node/1479
- Lesson 2a — Using the Code Viewer in VEXcode V5 (Python): https://pd.vex.com/training/v5/vex-v5-introductory-training-course/lesson-2a-using-the-code-viewer-in-vexcode-v5

## Minimum Drivetrain API

Students need to recognize and use:
- drive()
- drive_for()
- turn()
- turn_for()
- stop()
- set_drive_velocity()

Programming concepts needed for CV:
- variables
- if / elif / else
- while loops
- simple functions

Mini-task:

> **Forward → Turn → Stop → Forward**

Once students can make the robot move by code, move immediately to AI Vision.

VEXcode V5: https://codev5.vex.com/

---

# Phase 5 — AI Vision Sensor Fundamentals

## Step 1 — Setup and camera feed

Students connect the sensor, add it in VEXcode V5, open the AI Vision Utility, and see a live image.

Resource:
- Getting Started with the AI Vision Sensor with VEX V5: https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5

## Step 2 — Color Signature

Students learn:
- Color Signature
- Hue Range
- Saturation Range
- lighting effects
- background interference
- repeated detection tests at different distances and angles

Resource:
- Configuring Color Signatures: https://kb.vex.com/hc/en-us/articles/24067512493972-Configuring-Color-Signatures-with-the-AI-Vision-Sensor-in-VEXcode-V5

## Step 3 — Understand vision data

Students focus on:
- exists
- centerX
- centerY
- width
- height

The AI Vision Sensor image is 320 × 240, so the approximate image center is (160, 120).

Resources:
- Understanding the Data in the AI Vision Utility: https://kb.vex.com/hc/en-us/articles/24068869007636-Understanding-the-Data-in-the-AI-Vision-Utility-in-VEXcode-V5
- Coding with the AI Vision Sensor in VEXcode V5 Python: https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python

Useful VEX AI Vision videos:
- Detecting a Color with the AI Vision Sensor: https://pd.vex.com/videos/exp/detecting-a-color-with-the-ai-vision-sensor
- Adjusting a Color Signature: https://pd.vex.com/videos/exp/adjusting-a-color-signature
- Using Data from the AI Vision Utility in a Project: https://pd.vex.com/videos/exp/using-data-from-the-ai-vision-utility-in-a-project

Note: the PD+ examples may use EXP/Blocks, but centerX, centerY, width, height, color-signature, and closed-loop ideas transfer directly to the V5 AI Vision workflow.

---

# Phase 6 — Vision-Based Robot Control

## Project 1 — Object Centering Robot

Core idea:

> error = centerX - 160

Behavior:
- target left of center → turn left
- target right of center → turn right
- target near center → stop turning

Students should repeatedly take snapshots and update movement, forming a visual feedback loop:

> **See → Measure → Decide → Move → See Again**

## Project 2 — Object Following Robot

Use:
- centerX for steering
- width / height as a rough near/far proxy

Behavior:
- find target
- center target
- approach target
- stop when target appears sufficiently large
- continue updating the snapshot

This is the first major integrated robotics + vision milestone.

---

# Phase 7 — Formal Computer Vision Course

Students should not only use the VEX AI Vision API. They also need a structured CV course so they understand how vision works.

## Core Coursera course

**Master OpenCV Fundamentals for Real-Time Computer Vision**
https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Use it as the main structured CV course because it is short, practical, beginner-oriented, Python/OpenCV based, and includes real-time video work.

### Required

- Module 1 — OpenCV foundations and image basics
- Module 2 — image transformations / geometry as relevant
- Module 3 — real-time webcam/video-processing portions

### Skip or make optional

- face-recognition-specific workflow unless needed for an extension

## OpenCV concepts students must understand

- image as pixel data
- RGB / BGR
- HSV
- thresholding
- binary masks
- contours
- bounding boxes
- center / centroid
- real-time frames

Official OpenCV references:
- Python tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Color spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- Contour features / bounding box: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

Students explicitly connect the two pipelines:

> **OpenCV: image → HSV → mask → contour → bounding box → center**

and

> **VEX AI Vision: snapshot → detected object → centerX / centerY / width / height**

## Deep-learning CV

Andrew Ng CNN and Edge Impulse material are **optional extensions**, not required core content for the current course path. Add them only after students can build and explain the classical CV + VEX AI Vision system.

---

# Phase 8 — AprilTag

After color tracking and object following work reliably, add AprilTags.

Students learn:
- Tag ID
- center / size data
- angle/orientation data
- tag-based robot decisions

Example behaviors:
- Tag 1 → turn left
- Tag 2 → turn right
- Tag 3 → stop
- later: station-to-station navigation

Resource:
- Using AprilTags with the AI Vision Sensor in VEXcode V5: https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

---

# Phase 9 — Final Integrated Vision Robot

Core final behavior:

> **Search → Detect → Center → Approach → Stop / Perform Task**

Required integration:
- VEX drivetrain
- VEXcode Python
- AI Vision Sensor
- perception data
- decision logic
- closed-loop movement
- formal CV understanding
- engineering notebook evidence

After students observe real camera-placement problems, return to Onshape for a genuine redesign cycle:

> **CAD → Build → Code → Vision → Test → Redesign**

Optional advanced extension after the core course:
- state machine
- multi-target behavior
- vision-guided claw/intake
- sorting/delivery challenge
- learned object detection / CNN / Edge Impulse

---

# What Is No Longer Core

The following are not required before CV and should not consume the main sequence:
- separate Distance Sensor unit
- separate Optical Sensor unit
- separate Inertial Sensor unit
- full controller-programming unit
- advanced drivetrain API coverage
- PID as a dedicated unit
- long competition-autonomy sequence
- full Onshape Fundamentals completion
- required Andrew Ng CNN course
- required Edge Impulse course

These may be added later only when a project creates a real need.

---

# Current Core Sequence

1. Engineering Notebook — ongoing
2. Onshape Part Studio essentials
3. Introduction to Onshape Assemblies
4. VEX V5 Parts Library
5. TrainingBot CAD — completed
6. VEXcode V5 platform basics + Python Code Viewer
7. Drivetrain mini-task
8. Mount AI Vision Sensor on Advanced Trainingbot
9. AI Vision camera feed
10. Color Signature
11. centerX / centerY / width / height
12. Object Centering Robot
13. Object Following Robot
14. Coursera OpenCV Fundamentals
15. OpenCV HSV / mask / contour / bounding-box labs
16. AprilTag
17. Integrated Autonomous Vision Robot
18. Onshape camera-mount redesign based on test evidence

That sequence is the current curriculum backbone.