# Stanford CS231n — Selected Viewing Guide for VEX Robotics + Computer Vision

> **Teaching principle:** core content goes deep; frontier content goes wide.

Official course:
https://cs231n.stanford.edu/

2026 schedule / slides:
https://cs231n.stanford.edu/schedule

Public Stanford Online 2025 video playlist:
https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16

Lecture 1:
https://www.youtube.com/watch?v=2fq9wYslV0A

## Important version note

The public full video playlist is the **Spring 2025** offering. The current Stanford course site is **Spring 2026**.

The core sequence is very similar, but frontier topics can change. In particular:
- 2025 Lecture 17 = **Robot Learning**
- 2026 Lecture 17 = **World Modeling**

Use the public 2025 videos for viewing and the 2026 schedule/slides to keep the frontier discussion current.

---

# Part A — Core Required Content

These topics should be learned for **mastery**, not just exposure.

## L1 — Introduction

### Required
- computer vision overview;
- major CV tasks;
- why visual recognition matters;
- historical / field-level perspective.

### Learning depth
Students should be able to explain where classification, localization, detection and robotics perception fit in the broader CV field.

---

## L4 — Neural Networks and Backpropagation

### Required / selected
- multilayer perceptron concept;
- forward pass;
- loss;
- backpropagation intuition;
- how parameters learn from error.

### Do not over-focus on
- long derivative algebra;
- implementation details unrelated to the course.

### Learning depth
Students should be able to explain **how a neural network learns**, not reproduce every derivation.

---

## L5 — Image Classification with CNNs

### Highest-priority core lecture

Required:
- image features;
- convolution;
- filters / kernels;
- feature maps;
- receptive-field intuition;
- pooling;
- hierarchical visual features.

### Learning depth
Students should be able to draw and explain a simple CNN pipeline and explain why convolution is useful for images.

---

## L6 — CNN Architectures

Required:
- why architectures became deeper;
- AlexNet / VGG at overview level;
- **ResNet / residual connections**;
- Batch Normalization at concept level;
- **Transfer Learning**.

### Learning depth
Transfer learning is more important than memorizing architecture details.

Students should be able to explain:
- why pretrained features can be reused;
- why training from scratch is often unnecessary;
- why residual connections help deep networks.

---

## L9 — Object Detection, Segmentation, Visualizing and Understanding

### Highest-priority robotics connection

Required:
- classification vs localization vs detection;
- bounding boxes;
- single-stage vs two-stage detectors;
- R-CNN family at overview level;
- **YOLO**;
- **IoU**;
- **NMS**;
- DETR at awareness level;
- segmentation categories at overview level.

### VEX connection

Connect:
- VEX object center / size
- bounding boxes
- target selection
- robot decisions based on visual location

### Learning depth
Students should understand the detection pipeline conceptually. They do not need to implement R-CNN or DETR from scratch.

---

# Part B — Frontier Vision

These topics are for **frontier literacy**. Students should know what problem the method solves, why it matters, and how it differs from older approaches. Full implementation is not required.

## L8 — Attention and Transformers

### Required frontier topic
- self-attention;
- transformer idea;
- **Vision Transformer (ViT)**;
- image patches as tokens;
- global relationships vs local convolution.

Students should be able to answer:
> Why can a vision model use Transformer-style attention instead of relying only on CNNs?

---

## L12 — Self-Supervised Learning

### Required frontier topic
- learning useful representations without manually labeling every image;
- pretext tasks;
- contrastive learning;
- **DINO** awareness;
- why unlabeled visual data is valuable.

Students should be able to answer:
> Why is self-supervised learning important when labeled robotics data is expensive?

---

## L16 — Vision and Language

### Required frontier topic
Focus on:
- vision-language models;
- shared visual / language representations;
- image-text reasoning;
- how visual recognition is expanding toward multimodal understanding.

Students should understand the shift from:
> **recognize an object**

to:
> **understand and reason about a visual scene using language**

---

## L17 — Latest Frontier Topic

### 2025 public video: Robot Learning

Useful concepts:
- perception connected to action;
- model learning;
- deep reinforcement learning;
- robotics applications.

### 2026 current course: World Modeling

Use the 2026 slides / teacher summary for:
- models that represent environment dynamics;
- predicting future states;
- moving from static perception toward models of how the world changes.

For the current course, **World Modeling is the preferred latest-frontier discussion**, while the 2025 Robot Learning video remains a useful robotics extension.

---

# Part C — Optional Frontier / Enrichment

## L14 — Diffusion Models
Optional if students need broader generative-AI vision literacy.

## L15 — 3D Vision
Optional for students interested in spatial perception, reconstruction, autonomous systems, or future robotics work.

## L18 — Human-Centered AI
Optional but useful for ethics, human impact, and design discussion.

---

# Usually Skip for This Course

Unless a student wants extra depth:

- **L2 — Linear Classifiers**
- **L3 — Regularization and Optimization**
- **L7 — RNNs**
- **L10 — Video Understanding**
- **L11 — Large-Scale Distributed Training**
- **L13 — VAE / GAN / autoregressive generative models**

These are legitimate CS231n topics, but they are lower priority for this high-school VEX + CV pathway.

---

# Recommended Student Sequence

## Core mastery

> **L1 → L4 → L5 → L6 → L9**

## Frontier vision

> **L8 → L12 → L16 → L17 / 2026 World Modeling**

This creates the conceptual progression:

> **Computer Vision**
> → **Neural Networks**
> → **CNN feature learning**
> → **Transfer Learning**
> → **Object Detection**
> → **Transformers / ViT**
> → **Self-Supervised Learning**
> → **Vision-Language Models**
> → **World Models**

---

# Assessment Depth

| Category | Expected student performance |
|---|---|
| Core CNN / detection | explain, diagram, compare, apply to examples |
| Transfer learning | explain when and why to use it |
| IoU / NMS / YOLO | explain detection decisions and outputs |
| ViT / Transformers | explain the main idea and difference from CNNs |
| Self-supervised learning | explain why unlabeled data can be useful |
| Vision-language | explain multimodal visual understanding |
| World models | explain why predicting environment dynamics matters |

## Rule

> **Core content: deep enough to use and explain.**
>
> **Frontier content: broad enough to understand where the field is going.**

Do not require students to reproduce graduate-level derivations or full Stanford assignments.
