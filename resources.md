# Resources — Current VEX Robotics + Computer Vision Path

This file follows [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md). Prefer official VEX, Onshape, OpenCV, and the selected Coursera material.

---

# 1. Engineering Notebook

- VEX — Getting Started with Engineering Notebooks: https://kb.vex.com/hc/en-us/articles/49010276056596-Getting-Started-with-Engineering-Notebooks
- VEX — Digital Engineering Notebook Templates: https://kb.vex.com/hc/en-us/articles/49020662150676-Digital-Engineering-Notebook-Templates

Use the notebook continuously across CAD, coding, AI Vision, OpenCV, testing, and redesign.

---

# 2. Essential Onshape

## Core learning

- Onshape Fundamentals: CAD: https://learn.onshape.com/learning-paths/onshape-fundamentals-cad

Only the following are core for this course:
- Part Studio essentials
- Introduction to Onshape Assemblies
- VEX V5 Parts Library

The current class has already completed the TrainingBot CAD model.

## VEX-specific Onshape resources

- Using the VEX IQ and VEX V5 Parts Libraries in Onshape: https://www.onshape.com/en/blog/vex-iq-vex-v5-parts-libraries
- Using Onshape to Design a VEX Robot in the Cloud: https://www.onshape.com/en/resource-center/videos/using-onshape-to-design-a-vex-robot-in-the-cloud

Do not require Drawings, Detailed Drawings, Inspection and Repair, advanced surfacing, sheet metal, or certification preparation.

---

# 3. Standard Robot Platform

Primary platform:
- VEX V5 TrainingBot / Advanced Trainingbot-style four-wheel drivetrain
- V5 Brain
- Controller
- Smart Motors
- VEX AI Vision Sensor

Official mounting resource:
- Mounting and Wiring the AI Vision Sensor on the V5 Advanced Trainingbot: https://kb.vex.com/hc/en-us/articles/28385212896916-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Advanced-Trainingbot

---

# 4. VEXcode V5 — Minimum Required Before Vision

## Platform

- VEXcode V5 web app: https://codev5.vex.com/

## Required introductory videos

- Lesson 1 — Coding with VEXcode V5: https://pd.vex.com/hu/node/1479
- Lesson 2a — Using the Code Viewer in VEXcode V5 (Python): https://pd.vex.com/training/v5/vex-v5-introductory-training-course/lesson-2a-using-the-code-viewer-in-vexcode-v5

## Required robot-control concepts

Students only need enough control for later CV work:
- drive
- drive_for
- turn
- turn_for
- stop
- set_drive_velocity
- variables
- if / elif / else
- while
- simple functions

Mini-task:

> **Forward → Turn → Stop → Forward**

Do not delay AI Vision by turning this into a long complete VEX programming sequence.

---

# 5. VEX AI Vision Sensor — Core Resources

## Setup

- Getting Started with the AI Vision Sensor with VEX V5: https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5

## Color Signature

- Configuring Color Signatures with the AI Vision Sensor in VEXcode V5: https://kb.vex.com/hc/en-us/articles/24067512493972-Configuring-Color-Signatures-with-the-AI-Vision-Sensor-in-VEXcode-V5

Students should test color detection under different:
- lighting
- distance
- viewing angle
- background

## Vision data

- Understanding the Data in the AI Vision Utility in VEXcode V5: https://kb.vex.com/hc/en-us/articles/24068869007636-Understanding-the-Data-in-the-AI-Vision-Utility-in-VEXcode-V5
- Coding with the AI Vision Sensor in VEXcode V5 Python: https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python

Focus on:
- exists
- centerX
- centerY
- width
- height
- take_snapshot()

The sensor image is 320 × 240, so the approximate center is (160, 120).

## AI Vision videos

- Detecting a Color with the AI Vision Sensor: https://pd.vex.com/videos/exp/detecting-a-color-with-the-ai-vision-sensor
- Adjusting a Color Signature: https://pd.vex.com/videos/exp/adjusting-a-color-signature
- Using Data from the AI Vision Utility in a Project: https://pd.vex.com/videos/exp/using-data-from-the-ai-vision-utility-in-a-project

These PD+ videos may show EXP/Blocks, but the visual-data concepts transfer directly to V5.

---

# 6. Vision-Based Robot Projects

## Project A — Object Centering

Core control idea:

> **error = centerX - 160**

Behavior:
- target left → turn left
- target right → turn right
- target near center → stop turning

Control loop:

> **See → Measure → Decide → Move → See Again**

## Project B — Object Following

Use:
- centerX for steering
- width / height as a rough distance proxy

Behavior:
- detect
- center
- approach
- stop
- repeat

---

# 7. Formal Computer Vision Course

## Core Coursera course

**Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Use this as the main structured CV course.

### Required

- Module 1 — OpenCV foundations and image basics
- Module 2 — image transformations / geometry as relevant
- Module 3 — real-time webcam/video-processing portions

### Optional / skip

- face-recognition-specific workflow unless used in an extension

---

# 8. OpenCV Official References

- OpenCV-Python Tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Changing Color Spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Image Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- Contour Features / Bounding Box: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

Required conceptual pipeline:

> **image → HSV → threshold/mask → contour → bounding box → center**

Students connect that to:

> **AI Vision snapshot → object → centerX / centerY / width / height**

---

# 9. AprilTag

- Using AprilTags with the AI Vision Sensor in VEXcode V5: https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

Teach AprilTags after color tracking and object following work reliably.

Students use:
- Tag ID
- target position
- size
- orientation/angle data
- tag-based robot decisions

---

# 10. Optional Advanced CV Extensions

The following are no longer required core curriculum:

- DeepLearning.AI / Andrew Ng — Convolutional Neural Networks: https://www.coursera.org/learn/convolutional-neural-networks
- Edge Impulse — Computer Vision with Embedded Machine Learning: https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning

Use them only after students can build and explain the classical OpenCV + VEX AI Vision system.

Possible extension topics:
- CNN concepts
- MobileNet
- transfer learning
- learned object detection
- embedded deployment

---

# 11. Resource Selection Rule

Before assigning a resource:
1. confirm it still exists;
2. confirm it matches VEX V5 or clearly label when a video demonstrates EXP;
3. assign only the portions needed for the current project;
4. do not require completion of a full external course when only selected modules are needed;
5. keep the physical robot task as the main evidence of learning.