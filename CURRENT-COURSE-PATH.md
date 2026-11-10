# CURRENT COURSE PATH — VEX Robotics + Computer Vision

> **Status:** authoritative current course path. If older lesson files conflict with this document, follow this document.

## Current Classroom Status

The current class has already:
- built the VEX V5 TrainingBot / simple four-wheel robot;
- completed the TrainingBot in Onshape;
- learned the basic VEXcode V5 / Python workflow;
- completed the official VEX AI Vision Sensor project sequence used in this course.

There is **no mechanical arm / manipulator unit in the current course**.

## Current Course Architecture

> **VEX AI Vision completed → IBM OpenCV Bridge → Independent VEX Vision Challenge → CS231n Core + Frontier → Final Autonomous Vision Robot**

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

---

# Phase 2 — Foundations Already Completed

Current class status:
- TrainingBot build completed;
- TrainingBot CAD completed;
- VEXcode / Python foundation completed;
- official AI Vision project sequence completed.

Do not restart these units unless troubleshooting requires it.

---

# Phase 3 — IBM OpenCV Bridge (Core, Short)

Course:

**IBM — Introduction to Computer Vision and Image Processing**

https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Detailed teacher guide:
[teacher-notes/ibm-opencv-bridge-guide.md](teacher-notes/ibm-opencv-bridge-guide.md)

## Required IBM scope

### Module 1
Watch:
- Introduction to Computer Vision
- Applications of Computer Vision
- Recent Research in Computer Vision

### Module 2
Watch all six short image-processing videos.

Required OpenCV labs:
- Image processing with OpenCV
- Basic Image Manipulation with OpenCV
- Spatial Filtering OpenCV

Optional:
- Geometric Transformations with OpenCV

Skip as core:
- Pillow duplicates
- histogram work if time is tight

### Module 5
Use:
- Object Detection video
- Object Detection with Deep Learning reading

Haar Cascade: awareness only.
Faster R-CNN / Haar labs: optional.

### Skip as core
- Module 3 — classical ML image classification
- Module 4 — neural networks / CNN
- Module 6 — transfer-learning project

Those topics are handled better later through CS231n.

## Required local bridge project

> **Camera / image → HSV → threshold → mask → contour / object region → bounding box → centerX / centerY / width / height**

Students explicitly connect this pipeline to the VEX AI Vision abstraction.

Suggested time: **3–5 focused hours plus the local bridge lab.**

---

# Phase 4 — Independent VEX Vision Challenge

Students stop following official step-by-step tutorials.

Recommended behavior:

> **Search → Detect → Center → Approach → Identify Marker → Choose Action → Navigate → Stop**

Requirements should emphasize:
- repeated visual feedback;
- state / decision logic;
- reliability;
- failure analysis;
- testing under changed conditions;
- engineering evidence.

---

# Phase 5 — Stanford CS231n: Core + Frontier

Official course:
https://cs231n.stanford.edu/

2026 schedule:
https://cs231n.stanford.edu/schedule

Public 2025 Stanford Online video playlist:
https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16

Detailed guide:
[teacher-notes/cs231n-selected-viewing-guide.md](teacher-notes/cs231n-selected-viewing-guide.md)

## Core mastery

> **L1 → L4 → L5 → L6 → L9**

Core topics:
- CV overview
- neural networks / backprop intuition
- CNNs / convolution / pooling
- ResNet / transfer learning
- object detection
- bounding boxes
- IoU / NMS
- YOLO
- segmentation overview

## Frontier vision

> **L8 → L12 → L16 → L17 / 2026 World Modeling**

Frontier topics:
- Attention / Transformers / ViT
- Self-Supervised Learning / DINO
- Vision-Language Models
- World Models

Teaching principle:

> **Core content goes deep; frontier content goes wide.**

Students should master core ideas but only need conceptual literacy for frontier topics.

Note:
- the public playlist is Spring 2025;
- the current Stanford schedule is Spring 2026;
- 2025 L17 is Robot Learning;
- 2026 L17 is World Modeling.

Use 2026 slides / teacher synthesis to keep the frontier component current.

---

# Phase 6 — Optional Advanced Coursera Study

**University of Toronto — Visual Perception for Self-Driving Cars**

https://www.coursera.org/learn/visual-perception-self-driving-cars

Status: **Optional Advanced / after-class enrichment.**

Recommended for stronger students interested in:
- camera calibration;
- feature detection / matching;
- visual odometry;
- object detection / tracking;
- semantic segmentation;
- mobile-platform perception.

Do not make this a whole-class requirement.

---

# Phase 7 — Final Autonomous Vision Robot

Recommended capstone:

> **Search → Detect → Center → Approach → Identify → Decide → Navigate → Stop**

Required integration:
- VEX V5 drivetrain
- VEXcode Python
- AI Vision Sensor
- perception data
- decision logic
- repeated feedback
- robustness testing
- engineering notebook
- explanation of classical CV vs learned CV
- ability to place the project within the modern CV landscape

---

# What Is Not Core

- mechanical arm / claw / pick-and-place;
- Udemy Hands on Robotic Vision course;
- full IBM course completion;
- full CS231n course completion;
- full Toronto advanced course;
- mandatory Andrew Ng CNN;
- mandatory Edge Impulse.

# Current Core Sequence

1. Engineering Notebook — ongoing
2. Onshape / VEXcode foundations — completed
3. Official VEX AI Vision projects — completed
4. IBM OpenCV Bridge — selected Modules 1, 2, 5 + local bridge lab
5. Independent VEX Vision Challenge
6. CS231n Core — L1, L4, L5, L6, L9
7. CS231n Frontier — L8, L12, L16, latest World Modeling discussion
8. Final Autonomous Vision Robot
9. Toronto Visual Perception — optional advanced enrichment

That is the current curriculum backbone.
