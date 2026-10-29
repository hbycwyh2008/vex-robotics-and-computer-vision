# Pacing Guide — Current VEX Robotics + Computer Vision Path

This pacing guide follows [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md).

## Current Class Entry Point

Already completed:
- TrainingBot / four-wheel build;
- TrainingBot CAD in Onshape;
- basic VEXcode V5 / Python;
- initial AI Vision Sensor setup and successful operation.

Begin from the AI Vision control / claw integration stages below.

## Phase 1 — Engineering Notebook (ongoing)
Use 10–15 minutes within major work sessions.

> **Goal → Work → Evidence → Decision → Next Step**

## Phase 2 — AI Vision Reliability
Suggested time: 2–3 meetings.

- Color Signature
- lighting / distance / angle / background tests
- centerX / centerY / width / height
- repeated snapshots

Checkpoint:
> **Stable detection under several classroom conditions**

## Phase 3 — Object Centering
Suggested time: 2–4 meetings.

> **error = centerX - 160**

Build:
> **See → Measure → Decide → Turn → See Again**

## Phase 4 — Object Following
Suggested time: 3–5 meetings.

Use:
- centerX for steering;
- width / height as rough near/far evidence.

Checkpoint:
> **Find → Center → Approach → Stop**

## Phase 5 — Add Arm + Claw
Suggested time: 3–6 meetings.

Tasks:
1. build / integrate arm and claw;
2. learn arm/claw motor control;
3. mount AI Vision in a useful viewing position;
4. test occlusion and camera angle;
5. integrate vision and manipulation.

Core project:
> **Detect → Center → Approach → Open → Grab → Lift**

## Phase 6 — AprilTag Navigation
Suggested time: 2–4 meetings.

Students use:
- Tag ID;
- center;
- size;
- orientation / angle;
- tag-based decisions.

Possible challenge:
> **Grab target → find target AprilTag → navigate → deliver**

## Phase 7 — Robotics-Focused OpenCV Video Study
Suggested time: 4–8 meetings plus selected homework/video time.

Use selected sections from:

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Selected topics:
1. Color Spaces
2. Thresholding
3. Contour Detection
4. Morphological Operations
5. Object Tracking
6. ArUco Marker
7. optional Visual Servoing

Local labs should map each idea back to the VEX robot.

## Phase 8 — OpenCV Concept Mapping
Suggested time: 2–4 meetings.

Students explicitly connect:

> **VEX Color Signature ↔ HSV + thresholding**

> **centerX / centerY ↔ contour / bounding-box center**

> **width / height ↔ bounding-box size**

> **Object Following ↔ tracking / visual servoing**

> **AprilTag ↔ fiducial marker concepts**

## Phase 9 — Stanford CS231n Selected Theory
Suggested time: 3–6 meetings.

Use selected lectures only:
- Computer Vision overview;
- CNNs;
- architectures / transfer learning;
- object detection.

Goal:
> **Understand how learned vision goes beyond hand-written thresholds and contours.**

Do not require the full Stanford assignments.

## Phase 10 — Final Integrated Intelligent Robot
Suggested time: 5–10 meetings.

Recommended behavior:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

Required:
- drivetrain;
- Python;
- AI Vision Sensor;
- arm + claw;
- repeated feedback;
- AprilTag or target navigation;
- test evidence;
- engineering notebook;
- explanation of classical vs learned CV.

## Phase 11 — Evidence-Based Onshape Redesign
Suggested time: 1–3 meetings.

Redesign only when data shows a need:
- camera angle / height;
- field of view;
- arm occlusion;
- vibration;
- cable routing;
- claw geometry;
- mount stiffness.

> **CAD → Build → Code → Vision → Test → Redesign**

## Optional Extensions
Only after the core project works:
- state machine;
- multi-target sorting;
- learned object detection;
- YOLO;
- Edge Impulse;
- MobileNet;
- advanced visual servoing.

## Recommended 90-Minute Rhythm
- 0–10: retrieval / prediction / setup
- 10–25: focused video/demo
- 25–60: build/code/practice
- 60–78: test/debug/retest
- 78–87: engineering notebook
- 87–90: exit check / reset

The robot task remains the main learning evidence; videos support the project rather than replacing it.
