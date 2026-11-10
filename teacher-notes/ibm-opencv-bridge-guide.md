# IBM OpenCV Bridge — Selected Course Guide

> **Purpose:** a short bridge from the completed VEX AI Vision Sensor projects to the underlying classical computer-vision ideas. This is **not** a full-course completion requirement.

Course:
**IBM — Introduction to Computer Vision and Image Processing**
https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Current Coursera structure: 6 modules. For this VEX course, use selected material from Modules 1, 2, and 5 only.

---

## Learning Goal

Students should be able to connect:

> **VEX AI Vision: Color Signature → centerX / centerY / width / height**

to:

> **Classical CV: image → color representation / threshold → mask → object region → bounding box → center**

The goal is understanding and debugging, not completing every IBM assignment.

---

# Module 1 — Introduction to Computer Vision

## Watch

- **Introduction to Computer Vision**
- **Applications of Computer Vision**
- **Recent Research in Computer Vision**

## Optional / skim

- Course Introduction
- Brainstorming Your Own Applications

## Expected outcome

Students can explain:
- what computer vision is;
- how perception differs from ordinary programming;
- examples in robotics, autonomous systems, medicine, and AR;
- why modern CV includes both classical image processing and learned models.

---

# Module 2 — Image Processing with OpenCV and Pillow

This is the **core IBM module** for this course.

## Watch all six short videos

1. **What Is A Digital Image**
2. **Manipulating Images**
3. **Manipulating Images One Pixel At a Time**
4. **Pixel Transformations**
5. **Geometric Operations**
6. **Spatial Operations in Image Processing**

## Required OpenCV labs

- **Lab: Image processing with OpenCV**
- **Lab: Basic Image Manipulation with OpenCV**
- **Lab: Spatial Filtering OpenCV**

## Optional lab

- **Lab: Geometric Transformations with OpenCV**

## Skip as core

- Pillow versions of the labs
- Histograms and Intensity Transformations unless time permits
- completing every graded item only for the sake of a certificate

## Expected outcome

Students can explain:
- image as an array;
- pixels and channels;
- coordinates;
- basic OpenCV image operations;
- how filtering / transformation changes image data.

---

# Local VEX/OpenCV Bridge Lab — Required

IBM does not map tightly enough to VEX by itself, so add one local lab.

## Rebuild a Simple VEX AI Vision Pipeline

Students use Python + OpenCV to create:

> **Camera / image**
> → **BGR to HSV**
> → **color threshold**
> → **mask**
> → **contour / object region**
> → **bounding box**
> → **centerX / centerY / width / height**

Minimum output:
- visible mask;
- bounding box around the selected object;
- displayed centerX / centerY;
- displayed width / height;
- LEFT / CENTER / RIGHT decision based on image center.

Core formulas:

```python
center_x = x + w // 2
center_y = y + h // 2
```

## Required conceptual comparison

| VEX AI Vision | OpenCV bridge |
|---|---|
| Color Signature | HSV range / threshold |
| detected object | contour / selected region |
| centerX / centerY | bounding-box center |
| width / height | bounding-box dimensions |
| Object Following | repeated frame → error → motion decision |

---

# Module 3 — Machine Learning Image Classification

**Skip as core.**

Reason:
- KNN, logistic regression, Softmax, SVM and classical ML classification are not the current robotics-CV bottleneck;
- the class already has ML exposure;
- modern vision theory is handled later through CS231n.

Use only as optional review.

---

# Module 4 — Neural Networks and Deep Learning for Image Classification

**Skip as core.**

Reason:
- CNNs, architectures and deep-learning concepts are taught later with Stanford CS231n;
- avoid teaching the same idea twice at different levels.

---

# Module 5 — Object Detection

## Watch / read

- **Object Detection**
- **Object Detection with Deep Learning** — reading

## Know at overview level

- Haar Cascade Classifier

## Optional, not required

- Car Detection with Haar Classifiers lab
- Faster R-CNN lab

Reason:
CS231n later gives a better conceptual treatment of modern detection, including single-stage/two-stage detectors, YOLO, IoU and NMS.

---

# Module 6 — Transfer Learning Project

**Skip as core.**

Reason:
- transfer learning will be taught later in the selected CS231n sequence;
- the IBM final project would add substantial time without enough VEX-specific benefit.

---

# Required Deliverables

Students complete:

1. selected Module 1 videos;
2. all Module 2 videos;
3. three required OpenCV labs;
4. local VEX/OpenCV Bridge Lab;
5. selected Module 5 concepts;
6. short comparison: **classical CV vs VEX AI Vision abstraction**.

## Suggested total time

Approximately **3–5 focused hours**, plus the local bridge lab.

Stop after the bridge. Do not turn IBM into a second full semester course.
