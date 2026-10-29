# Lessons — Current Use

Use [../CURRENT-COURSE-PATH.md](../CURRENT-COURSE-PATH.md) as the authoritative sequence.

## Current Path

The current class has already:
- built the TrainingBot;
- completed the TrainingBot CAD model in Onshape;
- learned basic VEXcode V5 / Python;
- run the AI Vision Sensor successfully.

The current lesson sequence is:

> **AI Vision → Object Centering → Object Following → Arm + Claw → Vision-Guided Grab → AprilTag → Robotics-Focused OpenCV → CS231n selected theory → Final Intelligent Robot**

## How to Use the Existing Lesson Folders

### 01-trainingbot
Reference only for build/hardware troubleshooting.

### 02-driver-control
Use selectively for VEXcode/Python review.

### 03-sensors-autonomy
Extension/reference only. Separate Distance/Optical/Inertial units are not required before CV.

### 04-engineering-design
Reuse iteration/testing ideas. Mechanism content becomes useful now when adding arm + claw.

### 05-computer-vision
Reuse the OpenCV labs and classical-CV concepts, but replace older required IBM/Coursera viewing assignments with the current robotics-focused CV video path.

Current practical CV resource:

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Use selected topics only:
- Color Spaces
- Thresholding
- Contour Detection
- Morphological Operations
- Object Tracking
- ArUco Marker
- optional Visual Servoing

### 06-ai-robotics-integration
Use closed-loop alignment, robustness, perception → decision → action, and failure analysis.

Current implementation should emphasize:
- Color Signature
- centerX / centerY
- width / height
- Object Centering
- Object Following
- arm + claw
- AprilTag

### 07-capstone
Use after students can combine vision, motion, and manipulation.

Recommended final behavior:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

## Modern CV Theory

Use selected Stanford CS231n material only after students understand the VEX + classical OpenCV system:

https://cs231n.stanford.edu/

Focus on:
- CV overview
- CNNs
- architectures / transfer learning
- object detection

Older lesson references that call IBM, Andrew Ng, or Edge Impulse **required** should now be treated as legacy. They may be used as optional enrichment, but they are not the current core path.

## Current Required CV Core

> **VEX AI Vision + robotics-focused OpenCV + selected CS231n theory**