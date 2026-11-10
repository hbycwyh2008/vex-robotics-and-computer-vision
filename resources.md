# Resources — Current VEX Robotics + Computer Vision Path

This resource list follows [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md).

# 1. VEX / Engineering Foundations

- Engineering Notebooks: https://kb.vex.com/hc/en-us/articles/49010276056596-Getting-Started-with-Engineering-Notebooks
- Digital Notebook Templates: https://kb.vex.com/hc/en-us/articles/49020662150676-Digital-Engineering-Notebook-Templates
- VEXcode V5: https://codev5.vex.com/
- AI Vision Getting Started: https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5
- AI Vision Python: https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python
- AI Vision Python API: https://api.vex.com/v5/home/python/Vision/AiVision.html
- AprilTags: https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

Current status: official AI Vision project sequence completed.

# 2. IBM OpenCV Bridge — Core

**IBM — Introduction to Computer Vision and Image Processing**

https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Detailed selection:
[teacher-notes/ibm-opencv-bridge-guide.md](teacher-notes/ibm-opencv-bridge-guide.md)

Required:
- Module 1: Introduction to CV / Applications / Recent Research
- Module 2: all six videos
- Module 2 OpenCV labs: Image Processing, Basic Image Manipulation, Spatial Filtering
- local VEX/OpenCV Bridge Lab
- Module 5: Object Detection + Deep Learning Object Detection reading

Optional:
- Geometric Transformations with OpenCV
- Haar / Faster R-CNN labs

Skip as core:
- Modules 3, 4, 6
- Pillow duplicate labs

# 3. OpenCV Official References

- Python tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Color spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- Contour features / bounding box: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

Core bridge:

> **image → HSV → threshold → mask → contour / region → bounding box → center**

# 4. Stanford CS231n — Core + Frontier

Official course:
https://cs231n.stanford.edu/

2026 schedule:
https://cs231n.stanford.edu/schedule

Public Stanford Online 2025 playlist:
https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16

Lecture 1:
https://www.youtube.com/watch?v=2fq9wYslV0A

Detailed selection:
[teacher-notes/cs231n-selected-viewing-guide.md](teacher-notes/cs231n-selected-viewing-guide.md)

## Core mastery
- L1 Introduction
- L4 Neural Networks & Backpropagation
- L5 Image Classification with CNNs
- L6 CNN Architectures / Transfer Learning
- L9 Object Detection / Segmentation

## Frontier vision
- L8 Attention / Transformers / ViT
- L12 Self-Supervised Learning / DINO
- L16 Vision and Language
- L17: use current 2026 **World Modeling** as latest frontier discussion; 2025 public video L17 is Robot Learning

Teaching rule:
> **Core deep, frontier broad.**

# 5. Optional Advanced Coursera

**University of Toronto — Visual Perception for Self-Driving Cars**

https://www.coursera.org/learn/visual-perception-self-driving-cars

Status: optional after-class study.

High-value topics:
- camera model / calibration
- feature matching
- visual odometry
- object detection / tracking
- semantic segmentation
- mobile-platform perception

# 6. Onshape

- Onshape Fundamentals: https://learn.onshape.com/learning-paths/onshape-fundamentals-cad
- VEX V5 Parts Libraries: https://www.onshape.com/en/blog/vex-iq-vex-v5-parts-libraries

# 7. Not Planned as Core

- Udemy Hands on Robotic Vision
- Coursera Master OpenCV Fundamentals
- full IBM completion
- full CS231n completion
- mechanical-arm / pick-and-place pathways
- mandatory Andrew Ng CNN
- mandatory Edge Impulse

# 8. Teacher Verification Rule

Before assigning an external resource:
1. verify the current page / lecture topic;
2. preview the exact segment;
3. assign only the depth needed;
4. distinguish **core mastery** from **frontier literacy**;
5. keep the physical VEX project as the primary evidence of learning.
