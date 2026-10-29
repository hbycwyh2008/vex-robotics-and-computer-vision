# CURRENT COURSE PATH — VEX Robotics + Computer Vision

> **Status:** authoritative current course path. If older lesson files conflict with this document, follow this document.

## Current Classroom Status

The current class has already:
- built the VEX V5 TrainingBot / simple four-wheel robot;
- completed the TrainingBot in Onshape;
- learned the basic VEXcode V5 / Python workflow;
- connected and run the VEX AI Vision Sensor successfully.

The next major step is to move from **vision-guided mobile behavior** to **vision-guided manipulation**, then use robotics-focused OpenCV material to explain the CV behind the VEX sensor.

## Course Architecture

> **VEX official robotics mainline → Robotics-focused OpenCV → Modern CV theory → Integrated intelligent robot**

The VEX robot remains the main platform throughout the course. External CV courses support the robot work; they do not replace it.

---

# Phase 1 — Engineering Notebook (ongoing)

Students document:
- Goal
- Work / change
- Evidence
- Test result
- Decision
- Next step

Use the notebook throughout CAD, coding, AI Vision, claw integration, OpenCV, testing, and redesign.

Resources:
- https://kb.vex.com/hc/en-us/articles/49010276056596-Getting-Started-with-Engineering-Notebooks
- https://kb.vex.com/hc/en-us/articles/49020662150676-Digital-Engineering-Notebook-Templates

---

# Phase 2 — Essential Onshape

Required:
- Part Studio essentials;
- Introduction to Onshape Assemblies;
- VEX V5 Parts Library;
- ability to understand/rebuild the robot in CAD;
- later redesign of the AI Vision mount or manipulator only when test evidence creates a real need.

Current status: **TrainingBot CAD completed.**

Do not require the rest of Onshape Fundamentals such as Drawings, Detailed Drawings, Inspection and Repair, advanced surfacing, sheet metal, or certification preparation.

---

# Phase 3 — VEXcode V5 / Python Foundation

Students need enough VEXcode/Python to connect perception to robot action.

Core drivetrain control:
- drive()
- drive_for()
- turn()
- turn_for()
- stop()
- set_drive_velocity()

Core Python:
- variables
- if / elif / else
- while loops
- simple functions

Current status: **basic VEXcode/Python introduction completed.**

Useful official learning:
- Coding with VEXcode V5: https://pd.vex.com/hu/node/1479
- Code Viewer in VEXcode V5 (Python): https://pd.vex.com/training/v5/vex-v5-introductory-training-course/lesson-2a-using-the-code-viewer-in-vexcode-v5

---

# Phase 4 — VEX AI Vision Sensor Core

This is the main robotics-vision unit.

Students learn:
- camera feed / AI Vision Utility;
- Color Signature;
- lighting / distance / angle / background effects;
- exists;
- centerX;
- centerY;
- width;
- height;
- repeated snapshot → decision → movement.

Core projects:
1. **Reliable Color Detection**
2. **Object Centering Robot**
3. **Object Following Robot**

Core loop:

> **See → Measure → Decide → Move → See Again**

Official resources:
- Getting Started: https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5
- Color Signatures: https://kb.vex.com/hc/en-us/articles/24067512493972-Configuring-Color-Signatures-with-the-AI-Vision-Sensor-in-VEXcode-V5
- V5 Python AI Vision: https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python
- AI Vision Python API: https://api.vex.com/v5/home/python/Vision/AiVision.html

Official video sequence:
- Detecting a Color: https://pd.vex.com/videos/exp/detecting-a-color-with-the-ai-vision-sensor
- Adjusting a Color Signature: https://pd.vex.com/videos/exp/adjusting-a-color-signature
- Using Data from the AI Vision Utility: https://pd.vex.com/videos/exp/using-data-from-the-ai-vision-utility-in-a-project
- AI Classifications: https://pd.vex.com/videos/exp/ai-classifications-with-the-ai-vision-sensor
- AprilTags: https://pd.vex.com/videos/exp/apriltags-with-the-ai-vision-sensor

---

# Phase 5 — Add Arm + Claw: Vision-Guided Manipulation

Now that the basic AI Vision workflow has been run successfully, add the mechanical arm / claw.

Recommended platform:
- V5 Clawbot / Clawbot-style arm + claw
- AI Vision Sensor mounted with the official VEX method

Official resources:
- AI Vision on V5 Clawbot: https://kb.vex.com/hc/en-us/articles/28385434989716-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Clawbot
- V5 Claw reassembly / 3D instructions: https://kb.vex.com/hc/en-us/articles/15516473701524-Repairing-and-Reassembling-a-V5-Clawbot-Claw-V5-Claw-Kit-v2
- Programming the Robot Arm — Python: https://education.vex.com/stemlabs/v5/stem-labs/speedy-delivery/programming-the-robot-arm-python

Core project:

> **Detect → Center → Approach → Open Claw → Grab → Lift**

Students should keep perception, decision, drivetrain, arm, and claw code conceptually separated.

---

# Phase 6 — AprilTag Navigation

After color tracking / following and basic claw integration work, add AprilTags.

Students use:
- Tag ID
- target center
- size
- angle / orientation
- tag-based decisions

Possible behaviors:
- Tag 1 → turn left
- Tag 2 → turn right
- Tag 3 → stop
- later: navigate to a delivery location

Official resource:
- https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

---

# Phase 7 — Practical CV Video Course: Robotics-Focused OpenCV

The external CV course should reinforce the robot work, not become a separate unrelated subject.

## Recommended video course

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Do **not** require the full course.

Use selected sections that map directly to the VEX AI Vision workflow:
- Color Spaces
- Thresholding
- Contour Detection
- Morphological Operations
- Object Tracking
- ArUco Marker
- optional: Image-Based Visual Servoing

Mapping:

| VEX AI Vision | OpenCV / Robotic Vision |
|---|---|
| Color Signature | HSV + thresholding |
| centerX / centerY | contour / bounding-box center |
| width / height | bounding-box size |
| Object Following | object tracking / visual servoing |
| AprilTag | fiducial / ArUco marker concepts |
| AI Vision + Claw | vision-guided manipulation |

OpenCV official references remain the technical source of truth:
- https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

---

# Phase 8 — Modern Computer Vision Theory: Stanford CS231n (selected)

After students understand classical CV and have built a working VEX vision system, introduce modern learned vision.

Course:
- Stanford CS231n — Deep Learning for Computer Vision: https://cs231n.stanford.edu/
- Schedule: https://cs231n.stanford.edu/schedule

Use selected lectures only:
- **Lecture 1 — Computer Vision / course overview**
- **CNN lecture** — convolution, feature learning, pooling
- **CNN architectures / transfer learning** — focus on why pretrained features matter
- **Object Detection lecture** — bounding boxes, detection, YOLO-style ideas

Do not require the entire Stanford course or its full assignment sequence.

Student progression should be:

> **I can use VEX AI Vision → I understand the classical CV behind it → I understand how modern learned vision goes beyond hand-written rules.**

---

# Phase 9 — Final Integrated Intelligent Robot

Recommended capstone:

> **Search → Detect → Center → Approach → Grab → Navigate → Deliver / Place**

Required integration:
- VEX V5 drivetrain
- VEXcode Python
- AI Vision Sensor
- arm + claw
- perception data
- decision logic
- repeated feedback
- AprilTag or target-based navigation
- testing evidence
- engineering notebook
- explanation of classical vs learned CV

Possible extension:
- state machine
- multi-target sorting
- visual servoing
- learned object detection
- Edge Impulse / MobileNet / YOLO

---

# Phase 10 — Evidence-Based CAD Redesign

After students have real camera / claw test data, return to Onshape.

Possible redesign targets:
- camera height
- camera angle
- field of view
- vibration
- cable routing
- arm occlusion
- claw geometry
- AI Vision mount stiffness

Engineering loop:

> **CAD → Build → Code → Vision → Test → Redesign**

---

# No Longer the Core CV Course

The following are not the current main CV pathway:
- IBM Introduction to Computer Vision and Image Processing
- Coursera Master OpenCV Fundamentals as the main course
- required Andrew Ng CNN sequence
- required Edge Impulse sequence

They may still be used as optional references or extensions.

# Current Core Sequence

1. Engineering Notebook — ongoing
2. Onshape essentials — completed for TrainingBot
3. VEXcode V5 / Python foundation — completed
4. VEX AI Vision core
5. Object Centering
6. Object Following
7. Add arm + claw
8. Vision-Guided Grab
9. AprilTag Navigation
10. Udemy Robotics Vision selected OpenCV sections
11. Map OpenCV concepts back to VEX AI Vision
12. Stanford CS231n selected modern-CV lectures
13. Final Search → Detect → Center → Approach → Grab → Navigate → Deliver project
14. Evidence-based Onshape redesign

That is the current curriculum backbone.
