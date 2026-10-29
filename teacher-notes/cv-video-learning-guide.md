# Current CV Video Learning Guide

This guide aligns video learning with the current VEX V5 + AI Vision course.

The goal is not to complete entire external courses. Every video segment should explain or extend a behavior students already build on the robot.

---

# Layer 1 — VEX Official AI Vision

Use VEX official resources first because the robot is the main platform.

## Color Detection
- Detecting a Color: https://pd.vex.com/videos/exp/detecting-a-color-with-the-ai-vision-sensor
- Adjusting a Color Signature: https://pd.vex.com/videos/exp/adjusting-a-color-signature

Apply immediately:
- configure one Color Signature;
- test lighting, angle, distance, background;
- record failure cases.

## Vision Data
- Using Data from the AI Vision Utility: https://pd.vex.com/videos/exp/using-data-from-the-ai-vision-utility-in-a-project

Apply immediately:
- centerX / centerY;
- width / height;
- Object Centering;
- Object Following.

## AI Classification / AprilTag
- AI Classifications: https://pd.vex.com/videos/exp/ai-classifications-with-the-ai-vision-sensor
- AprilTags: https://pd.vex.com/videos/exp/apriltags-with-the-ai-vision-sensor

Pair with V5 Python docs:
- https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python
- https://api.vex.com/v5/home/python/Vision/AiVision.html

---

# Layer 2 — Vision-Guided Manipulation

After Object Following works, add arm + claw.

Official resources:
- AI Vision on V5 Clawbot: https://kb.vex.com/hc/en-us/articles/28385434989716-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Clawbot
- V5 Claw 3D instructions: https://kb.vex.com/hc/en-us/articles/15516473701524-Repairing-and-Reassembling-a-V5-Clawbot-Claw-V5-Claw-Kit-v2
- Programming Robot Arm — Python: https://education.vex.com/stemlabs/v5/stem-labs/speedy-delivery/programming-the-robot-arm-python

Project:

> **Detect → Center → Approach → Open → Grab → Lift**

---

# Layer 3 — Practical Robotics CV Video Course

## Udemy

**Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Do not assign the full course.

## Selected Learning Path

1. **Color Spaces** — connect to VEX Color Signature; focus on HSV.
2. **Thresholding** — connect to how a color target is isolated.
3. **Contour Detection** — connect to object position and shape.
4. **Morphological Operations** — connect to cleaning noisy masks.
5. **Object Tracking** — connect to VEX Object Following.
6. **ArUco Marker** — connect conceptually to AprilTag / fiducial-marker navigation.
7. **Image-Based Visual Servoing — optional** — connect camera error directly to robot motion.

## Required Mapping Discussion

| VEX experience | CV concept |
|---|---|
| Color Signature | HSV + thresholding |
| centerX / centerY | contour / bounding-box center |
| width / height | bounding-box size |
| Object Following | tracking / visual servoing |
| AprilTag | fiducial markers |
| AI Vision + Claw | vision-guided manipulation |

---

# Layer 4 — Modern CV Theory

## Stanford CS231n

Course: https://cs231n.stanford.edu/

Schedule: https://cs231n.stanford.edu/schedule

Use selected lectures only.

### Recommended topics
- Computer Vision overview
- CNNs: convolution, feature learning, pooling
- CNN architectures / transfer learning
- object detection / bounding boxes / YOLO-style ideas

Do not require the complete Stanford assignments.

## Learning Goal

Students should be able to explain:

> **Classical CV:** humans choose thresholds / geometry.

> **Learned CV:** models learn useful visual features from data.

The goal is not to teach that deep learning always wins. Students should choose the simplest perception method that meets tested requirements.

---

# Viewing Protocol

For any video resource:

1. **Predict** — ask one question before watching.
2. **Watch** — use a focused segment, usually no more than 10–15 minutes without interruption.
3. **Represent** — diagram, tiny code sample, or comparison.
4. **Apply** — immediately use the idea on VEX or OpenCV.
5. **Test** — collect evidence.
6. **Explain** — students reconstruct the idea without replaying the video.

## Student Note Format

For each segment:
- Input
- Processing
- Output
- Robot connection
- Failure / limitation
- Next test

Avoid transcript-style notes.

---

# Final Integration

The video pathway should support the final capstone:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

The robot project remains the main assessed work.