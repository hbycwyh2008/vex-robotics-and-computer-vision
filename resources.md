# Resources

Curated classroom resources for the **VEX V5 Competition Starter Kit**, VEXcode, engineering design, and introductory computer vision. Prefer official documentation for student-facing technical instructions.

---

## Start Here — VEX V5 Competition Kit

### Official first robot: TrainingBot

- **Team Freeze Tag STEM Lab:** https://education.vex.com/stemlabs/v5/team-freeze-tag
- **Lesson 1 — Build TrainingBot:** https://education.vex.com/stemlabs/v5/team-freeze-tag/lesson-1-introduction/build
  - Select **3D Build Instructions — Competition Kits**.
- **V5 Build Instructions:** https://www.vexrobotics.com/v5/downloads/build-instructions

TrainingBot is the standard starting platform for this course. Students should first learn correct construction, wiring, controller use, testing, and maintenance before moving to custom mechanisms.

## VEX V5 Official Documentation

- VEX Robotics: https://www.vexrobotics.com/
- VEX V5 Knowledge Base: https://kb.vex.com/hc/en-us/categories/360002333191-V5
- Understanding and Using V5 Tools: https://kb.vex.com/hc/en-us/articles/13078845924884-Understanding-and-Using-V5-Tools
- V5 Fasteners: https://kb.vex.com/hc/en-us/articles/360035952791-Using-V5-Fasteners
- V5 Build Instructions: https://www.vexrobotics.com/v5/downloads/build-instructions

## VEXcode V5

- VEXcode V5 web app: https://codev5.vex.com/
- VEXcode downloads: https://www.vexrobotics.com/vexcode/install/v5
- VEXcode V5 Knowledge Base: https://kb.vex.com/hc/en-us/categories/360002333191-V5
- VEX Education STEM Labs: https://education.vex.com/stemlabs/v5

### Programming pathway used in this course

1. Configure drivetrain and devices correctly.
2. Test controller driving.
3. Program basic forward/reverse/turn movement.
4. Use functions and loops to reduce repeated code.
5. Read sensor values.
6. Use conditionals to create autonomous behavior.
7. Connect perception results to decisions and robot actions.

## Engineering Design and Competition Context

- VEX Robotics Competition: https://www.vexrobotics.com/v5/competition/vrc-current-game
- VEX Competition resources: https://www.vexrobotics.com/competition
- VEX Education: https://education.vex.com/

Competition-style challenges are used as engineering contexts. The course does not require students to enter an official competition.

---

# Computer Vision Learning Pathway

The computer-vision sequence intentionally uses **three layers** rather than treating all vision as one topic:

1. **Classical computer vision with OpenCV** — students directly manipulate pixels, masks, contours and geometry.
2. **Modern deep-learning computer vision** — students learn how CNNs learn visual features and how modern object detection differs from hand-written rules.
3. **Embedded / robotics vision** — students connect learned perception to constrained hardware and robot decisions.

The order matters:

> **Pixels → Rules → Objects → CNNs → Detection → Embedded Vision → Robot Decisions**

Students should first be able to explain a transparent OpenCV pipeline before moving to learned models.

## Coursera Video Course 1 — IBM: Introduction to Computer Vision and Image Processing

**Role in this course:** required foundation for Lessons 17–20.

Course:
https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Use selected videos rather than assigning the entire Coursera course indiscriminately.

### Required selections

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

### Why this course is first

It matches the local Python/OpenCV work and gives students a concrete model of an image as numerical data before they study CNNs.

## OpenCV Official Documentation — Required Technical Reference

- OpenCV official documentation: https://docs.opencv.org/
- OpenCV-Python tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Changing color spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Image thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html

The OpenCV documentation remains the primary technical reference for HSV thresholding, masks, morphology, contours, bounding boxes and centroid calculations because those operations map directly to Lessons 17–20.

## Coursera Video Course 2 — DeepLearning.AI / Andrew Ng: Convolutional Neural Networks

**Role in this course:** required modern-computer-vision bridge after students have built the classical OpenCV detector.

Course:
https://www.coursera.org/learn/convolutional-neural-networks

This is **not optional enrichment**. Students do not need to complete every programming assignment in the Coursera course, but the selected video sequence is part of the required conceptual curriculum.

### Required selections — Week 1: Foundations of Convolutional Neural Networks

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

### Required selections — Week 2: Deep Convolutional Models

Prioritize the videos that connect most directly to practical robotics vision:

- Classic Networks — overview level
- ResNets — concept level
- MobileNet
- MobileNet Architecture
- Transfer Learning
- Data Augmentation
- State of Computer Vision

In this robotics course, students are expected to understand **why MobileNet and transfer learning are useful** on constrained systems; reproducing every architecture from scratch is not required.

### Required selections — Week 3: Object Detection

- Object Localization
- Object Detection
- Bounding Box Predictions
- Intersection Over Union
- Non-max Suppression
- Anchor Boxes
- YOLO Algorithm

Optional extension:
- Region Proposals
- Semantic Segmentation with U-Net
- U-Net Architecture Intuition
- U-Net Architecture

### Required comparison after Andrew Ng

Students should be able to compare:

| Classical OpenCV pipeline | CNN / learned vision |
|---|---|
| Human chooses HSV ranges | Model learns useful visual features from data |
| Human defines contour filters | Learned model produces classifications/detections |
| Rules are directly inspectable | Internal representations are less directly interpretable |
| Can work with little training data | Usually depends on training data or pretrained models |
| Often lightweight and fast | May require more compute, optimization or edge deployment |
| Failure may come from brittle thresholds | Failure may come from dataset bias, domain shift or model limits |

The goal is not to teach that deep learning always replaces classical vision. Students should learn to choose the simplest approach that satisfies the engineering requirements.

## Coursera Video Course 3 — Edge Impulse: Computer Vision with Embedded Machine Learning

**Role in this course:** required selected material for the transition from CNN/object-detection concepts to embedded/robotics deployment.

Course:
https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning

### Recommended / required selections

**Module 1 — Image Classification**
- What is Computer Vision?
- Overview of Digital Images
- Data Collection
- Overview of Image Classification
- Review of Neural Networks

**Module 2 — Convolutional Neural Networks**
- Image Convolution
- Pooling Layer
- Convolutional Neural Network
- Training a Convolutional Neural Network
- Data Augmentation
- Transfer Learning and MobileNet

**Module 3 — Object Detection**
- Introduction to Object Detection
- Object Detection Performance Metrics
- Object Detection Models
- Training an Object Detection Model
- Deploy Object Detection Model to a Single Board Computer

Students do not need the exact same embedded target hardware used by the Coursera projects in order to learn from the deployment architecture. The classroom goal is to understand:

> **camera → preprocessing → model → detection output → decision logic → robot action**

## Video-to-Lesson Map

| Local lesson | Primary video learning | Technical / practical work |
|---|---|---|
| Lesson 17 — Images, Pixels and Color | IBM Module 1 + Module 2 digital-image videos | OpenCV image loading, pixels, coordinates, channels |
| Lesson 18 — HSV Thresholding and Masks | IBM image-manipulation videos | OpenCV HSV, thresholding, masks, morphology |
| Lesson 19 — Contours, Bounding Boxes and Centroids | Andrew Ng: Computer Vision + edge-detection bridge | OpenCV contours, geometry, center position |
| Lesson 20 — Color Object Detection Project | Complete classical pipeline first; then begin Andrew Ng Week 1 | Build and test a transparent rule-based detector |
| Lesson 21 — Vision to Decision Logic | Andrew Ng Week 1 completion + Week 2 MobileNet / Transfer Learning | Compare rule-based and learned perception; keep decision/action layers separate |
| Lesson 22 — Closed-Loop Vision Alignment | Andrew Ng Week 3 localization, bounding boxes, IoU, NMS, YOLO | Convert visual error into closed-loop robot behavior |
| Lesson 23 — Vision Robustness and Failure Modes | Andrew Ng data augmentation + Edge Impulse object-detection metrics/deployment | Stress tests, domain shift, false positives/negatives, fallback behavior |
| Capstone | Edge Impulse selected modules as needed | Choose classical CV, learned CV, or a justified hybrid approach |

## Computer Vision Learning Sequence

1. Images as arrays of pixels
2. BGR/RGB and HSV color spaces
3. Thresholding and masks
4. Morphological cleanup
5. Contours and bounding boxes
6. Centroid / target position
7. Build and test a complete classical color-object detector
8. Convolution and pooling
9. CNN feature learning
10. MobileNet and transfer learning
11. Object localization and modern object detection
12. Bounding boxes, IoU, NMS and YOLO concepts
13. Embedded vision constraints and deployment
14. Perception → decision → action
15. Testing under changing lighting, distance, background, occlusion and domain shift

## Minimum Computer Vision Mastery

By the end of the sequence, students should be able to explain all of the following without treating them as interchangeable:

- what a pixel is;
- what HSV thresholding does;
- what a contour and centroid represent;
- why a hand-written color detector is not the same thing as a trained neural network;
- what convolution and pooling do conceptually;
- why CNNs can learn visual features;
- classification vs localization vs object detection;
- bounding box and IoU;
- the purpose of NMS;
- the basic idea behind YOLO;
- why transfer learning and MobileNet matter for practical/embedded vision;
- how perception output becomes a robot decision;
- why both classical and learned vision systems must be tested under changing conditions.

---

## GitHub / Markdown

- GitHub Docs: https://docs.github.com/
- GitHub Skills: https://skills.github.com/
- Markdown basic syntax: https://www.markdownguide.org/basic-syntax/

## AI Literacy Connections

This course treats computer vision and sensor fusion as practical **AI application thinking**:

> **Perceive → Decide → Act → Test → Improve**

Students should be able to explain:

- what information the robot actually receives from sensors or a camera;
- how code or a learned model converts observations into usable perception outputs;
- how decision logic converts perception into robot behavior;
- why a vision system can fail because of lighting, occlusion, calibration, background, domain shift, biased/insufficient data, or ambiguous inputs;
- why testing across conditions matters;
- when classical computer vision is sufficient and when learned computer vision may be justified;
- when AI/coding assistants are useful and when their output must be checked;
- how to disclose and explain AI-assisted work.

AI tools may assist learning and debugging, but students remain responsible for understanding, testing, and defending the code and engineering decisions they submit.

## Teacher Verification Rule

Before assigning any external resource:

1. verify that the page still exists;
2. confirm that it matches the intended platform/topic and current course sequence;
3. confirm that VEX build instructions match **VEX V5** and the **Competition Kit** when a kit-specific version is offered;
4. preview third-party/Coursera content before sharing it with students;
5. assign selected videos by title rather than assuming students should complete an entire external course;
6. if Coursera changes module names or video ordering, preserve the local learning objective and update this mapping.
