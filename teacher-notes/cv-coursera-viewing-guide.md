# Computer Vision Coursera Viewing Guide

**Verified against current Coursera course pages: 2026-08-23.** Course modules/titles may change; re-check before a new school year.

This guide prevents Coursera from turning the robotics class into passive video watching. Videos are used as **short conceptual inputs** that feed local OpenCV/robotics investigations.

## Required Course Stack

### 1. IBM — Introduction to Computer Vision and Image Processing
https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Use for **digital images + OpenCV foundations**.

Current high-value videos:

**Module 1 — Introduction to Computer Vision**
- Introduction to Computer Vision
- Applications of Computer Vision

**Module 2 — Image Processing with OpenCV and Pillow**
- What Is A Digital Image
- Manipulating Images
- Manipulating Images One Pixel At a Time
- Pixel Transformations
- Geometric Operations
- Spatial Operations in Image Processing

The local course does **not** need to complete every IBM lab/assignment. Local OpenCV labs are the primary assessed work.

### 2. DeepLearning.AI / Andrew Ng — Convolutional Neural Networks
https://www.coursera.org/learn/convolutional-neural-networks

This is **required conceptual curriculum**, not optional enrichment.

**Week 1 — Foundations of Convolutional Neural Networks**
- Computer Vision
- Edge Detection Example
- More Edge Detection
- Padding
- Strided Convolutions
- Convolutions Over Volume
- One Layer of a Convolutional Network
- Simple Convolutional Network Example
- Pooling Layers
- CNN Example
- Why Convolutions?

**Week 2 — Deep Convolutional Models**
Prioritize:
- MobileNet
- MobileNet Architecture
- Transfer Learning
- Data Augmentation
- State of Computer Vision

Classic Networks / ResNets may be taught at overview level if time allows.

**Week 3 — Object Detection**
Required:
- Object Localization
- Object Detection
- Bounding Box Predictions
- Intersection Over Union
- Non-max Suppression
- Anchor Boxes
- YOLO Algorithm

Students are not required to reproduce every Coursera programming assignment in this robotics course. The expected outcome is conceptual understanding strong enough to compare classical and learned vision and reason about robotics deployment.

### 3. Edge Impulse — Computer Vision with Embedded Machine Learning
https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning

Use for **edge deployment / robotics constraints**.

High-value selections:

**Module 1**
- What is Computer Vision?
- Overview of Digital Images
- Data Collection
- Overview of Image Classification
- Review of Neural Networks

**Module 2**
- Image Convolution
- Pooling Layer
- Convolutional Neural Network
- Training a Convolutional Neural Network
- Data Augmentation
- Transfer Learning and MobileNet

**Module 3**
- Introduction to Object Detection
- Object Detection Performance Metrics
- Object Detection Models
- Training an Object Detection Model
- Deploy Object Detection Model to a Single Board Computer

---

# Local Meeting Map

| Meeting | Video role | Local task after viewing |
|---|---|---|
| 25A | IBM Intro to CV | inspect image shape/pixels |
| 25B | IBM Digital Image + pixel manipulation | channels, ROI, BGR/RGB |
| 26A–27B | IBM concepts as review only | HSV/masks/morphology/calibration use OpenCV docs |
| 29B | Andrew Ng Computer Vision + Edge Detection | compare fixed rules vs convolutional features |
| 30B | Andrew Ng CNN Week 1 core | convolution/padding/stride/pooling concept map |
| 31B | Andrew Ng MobileNet + Transfer Learning + Data Augmentation | choose classical vs learned approach |
| 32A | Andrew Ng Object Detection through YOLO | IoU/NMS simulation + detector pipeline |
| 33A | Edge Impulse deployment/object detection selections | embedded architecture + failure taxonomy |

---

# Viewing Protocol

Do not normally play more than **10–15 uninterrupted minutes** of video in class.

Use this protocol:

1. **Predict before play** — one question students answer before the clip.
2. **Watch a focused segment** — not an entire module by default.
3. **Pause for a representation** — diagram, tiny calculation, comparison table or code inspection.
4. **Apply immediately** — OpenCV lab, robot-system decision or failure analysis.
5. **Rebuild/explain** — students reconstruct the concept without replaying the video.

## Student Note Format

For every assigned video segment, students record only:

- **Input:** what data enters this operation/model?
- **Processing:** what transformation/model operation happens?
- **Output:** what comes out?
- **Why useful:** what problem does it solve?
- **Failure/limit:** one way this can fail or become expensive.
- **Connection:** where does this appear in our robot/vision pipeline?

Avoid long transcript-style notes.

---

# Teacher Pause Prompts

## IBM / Digital Images
- If the image is 640×480×3, what do those dimensions mean?
- Why does OpenCV BGR matter when displaying with an RGB-based library?
- Does a pixel value contain the label “red ball”? Why not?

## Andrew Ng / Convolution
- What part is fixed in our HSV pipeline that can become learned in a CNN?
- Why can a small filter detect a local visual pattern?
- What information can stride reduce?
- Why might padding be useful near image boundaries?
- What does pooling trade away in exchange for compactness/invariance?

## Andrew Ng / Transfer Learning
- Why is training a vision network from scratch unrealistic for our small classroom dataset?
- What does a pretrained model already know that can be reused?
- Which augmentations simulate realistic robot-camera variation?

## Andrew Ng / Object Detection
- Classification says “what”; localization adds what?
- If two boxes describe the same object, how can IoU help identify overlap?
- Why is NMS needed?
- Why can a detection model still be confidently wrong?

## Edge Impulse / Embedded Deployment
- What changes when inference must run on a constrained device?
- Which matters more for robot control: accuracy alone or accuracy + latency + reliability?
- What should the robot do when perception is late or uncertain?

---

# Required End-of-Unit Comparison

Every student must be able to explain this comparison from memory:

| Classical OpenCV | Learned CV / CNN |
|---|---|
| human selects color/geometry rules | model learns useful features from data |
| transparent thresholds/filters | internal features are less directly interpretable |
| often low compute and little/no training data | typically needs data/pretraining and more compute |
| excellent when environment/target is constrained | stronger when variation makes hand-written rules brittle |
| fails through thresholds, calibration, geometry assumptions | fails through data gaps, domain shift, model limits and deployment constraints |

The engineering goal is **not** “deep learning always wins.” Students should choose the simplest perception method that meets tested requirements.