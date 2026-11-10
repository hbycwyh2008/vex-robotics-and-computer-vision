# Current CV Learning Guide

This guide aligns CV learning with the current VEX V5 mobile-robot course.

## Current Status

The class has completed the official VEX AI Vision Sensor project sequence. The next stage is to understand the underlying CV concepts and then design independent autonomous behavior.

---

# Layer 1 — Short OpenCV Bridge

## IBM Coursera

**Introduction to Computer Vision and Image Processing**

https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Use:
- Module 1 — selected introduction;
- Module 2 — core digital-image / OpenCV content;
- Module 5 — selected object-detection concepts.

Skip as core:
- Module 3;
- Module 4;
- Module 6.

Recommended total use: about **3–5 hours**, not full-course completion.

## Required conceptual mapping

| VEX experience | CV concept |
|---|---|
| Color Signature | color representation + thresholding |
| centerX / centerY | object / bounding-box center |
| width / height | bounding-box size |
| Object Following | repeated perception + feedback control |
| AprilTag | visual fiducial / marker-based decision |

---

# Layer 2 — Independent VEX Project

Move away from tutorials.

Recommended challenge:

> **Search → Detect → Center → Approach → Identify Marker → Choose Action → Navigate → Stop**

Students should decide:
- states;
- transitions;
- thresholds;
- stopping conditions;
- failure recovery;
- test protocol.

---

# Layer 3 — Modern CV Theory

## Stanford CS231n

Course: https://cs231n.stanford.edu/

Schedule: https://cs231n.stanford.edu/schedule

Use selected topics only:
- Computer Vision overview;
- CNN / convolution;
- feature learning / pooling;
- architectures / transfer-learning overview;
- object detection;
- bounding boxes / IoU / NMS / YOLO-style ideas.

The purpose is conceptual depth, not completion of the Stanford assignment sequence.

---

# Layer 4 — Optional Advanced Coursera

## University of Toronto — Visual Perception for Self-Driving Cars

https://www.coursera.org/learn/visual-perception-self-driving-cars

Status: **Optional Advanced / after-class enrichment**.

Good for stronger students interested in:
- camera calibration;
- feature matching;
- visual odometry;
- detection / tracking;
- semantic segmentation;
- autonomous-vehicle and mobile-robot perception.

---

# Viewing Protocol

For any video segment:
1. Predict one idea before watching.
2. Watch a focused segment.
3. Represent the concept with a diagram / code / comparison.
4. Apply it to OpenCV or VEX.
5. Test and collect evidence.
6. Explain without replaying the video.

## Student Note Format

- Input
- Processing
- Output
- VEX connection
- Failure / limitation
- Next test

---

# Not in the Current Learning Path

- Udemy Hands on Robotic Vision course;
- mechanical-arm / pick-and-place content;
- full IBM completion;
- full CS231n completion.

The physical VEX mobile robot remains the main assessed platform.