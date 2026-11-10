# Current CV Learning Guide

The class has completed the official VEX AI Vision Sensor project sequence. The next stage is:

> **Understand the underlying CV → build independently → learn modern CV core → gain frontier vision**

---

# Layer 1 — IBM OpenCV Bridge

Course:
https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Detailed guide:
[ibm-opencv-bridge-guide.md](ibm-opencv-bridge-guide.md)

Core selection:
- Module 1: Introduction / Applications / Recent Research;
- Module 2: all six videos;
- required OpenCV labs;
- local VEX/OpenCV bridge lab;
- Module 5 detection concepts.

Skip as core:
- Modules 3, 4, 6;
- duplicate Pillow labs.

Required mapping:

| VEX experience | Classical CV idea |
|---|---|
| Color Signature | HSV / threshold |
| detected object | contour / object region |
| centerX / centerY | bounding-box center |
| width / height | bounding-box dimensions |
| Object Following | repeated perception + feedback |

---

# Layer 2 — Independent VEX Vision Project

> **Search → Detect → Center → Approach → Identify Marker → Choose Action → Navigate → Stop**

Students design:
- states;
- transitions;
- thresholds;
- stopping conditions;
- failure recovery;
- test protocol.

---

# Layer 3 — CS231n Core Mastery

Official course:
https://cs231n.stanford.edu/

Public 2025 playlist:
https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16

Detailed guide:
[cs231n-selected-viewing-guide.md](cs231n-selected-viewing-guide.md)

Core:
> **L1 → L4 → L5 → L6 → L9**

Students should master:
- CV overview;
- neural-network learning intuition;
- CNN / convolution / pooling;
- feature learning;
- ResNet / transfer learning;
- object detection;
- bounding boxes;
- IoU / NMS / YOLO.

---

# Layer 4 — CS231n Frontier Vision

Frontier:
> **L8 → L12 → L16 → L17 / current World Modeling**

Themes:
- Transformer / ViT;
- Self-Supervised Learning / DINO;
- Vision-Language Models;
- World Models.

The public playlist is 2025. Use the 2026 schedule/slides to keep frontier topics current.

Teaching depth:
- identify the problem;
- explain the key idea;
- explain why it matters;
- connect to future robotics / AI;
- no full implementation required.

---

# Layer 5 — Optional Advanced Coursera

University of Toronto — Visual Perception for Self-Driving Cars:
https://www.coursera.org/learn/visual-perception-self-driving-cars

Optional after-class enrichment.

---

# Teaching Principle

> **Core content goes deep. Frontier content goes wide.**

The course should not become passive video consumption. Every core topic should be followed by explanation, diagramming, comparison, coding, or robot-system analysis.
