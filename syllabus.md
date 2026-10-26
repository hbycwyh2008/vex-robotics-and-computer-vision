# Syllabus — VEX Robotics + Computer Vision

## Course Description

This project-based high school course uses **VEX V5 robotics, the VEX AI Vision Sensor, Python, Onshape, and OpenCV** to teach engineering design, robot control, computer vision, and intelligent behavior.

The current course is intentionally streamlined. Students do not complete every traditional VEX sensor/autonomy topic before computer vision. Instead, they use a simple four-wheel V5 robot as the physical platform for learning:

> **Perception → Decision → Action → Testing → Improvement**

The current sequence is:

> **Essential CAD → Minimum Robot Control → AI Vision → Vision-Based Robot Control → Formal OpenCV Course → Integrated Vision Robot**

See [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md) for the authoritative implementation path.

---

## Current Classroom Starting Point

The current class has already:
- built a working VEX V5 TrainingBot / four-wheel robot;
- driven it using an existing Controller program;
- completed the TrainingBot in Onshape.

Therefore, the next work begins with minimal VEXcode/Python control and AI Vision rather than another long drivetrain or sensor unit.

---

## Standard Hardware and Software

### Robotics
- VEX V5 Competition Starter Kit or equivalent V5 parts
- V5 Brain
- V5 Controller
- V5 Smart Motors
- simple four-wheel TrainingBot / Advanced Trainingbot-style drivetrain
- **VEX AI Vision Sensor**

### Software
- VEXcode V5
- Python
- Onshape
- OpenCV
- GitHub + Markdown

### Structured CV Course

Core Coursera course:

**Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Andrew Ng CNN and Edge Impulse content are optional advanced extensions rather than required core material.

---

## Learning Outcomes

By the end of the course, students will be able to:

1. Maintain an engineering notebook with goals, evidence, tests, decisions, and next steps.
2. Use essential Onshape Part Studio tools for simple robot-related part design.
3. Use Onshape Assemblies and mates to understand and represent a VEX robot.
4. Use the VEX V5 Parts Library rather than redrawing standard VEX parts.
5. Explain the major components of the existing four-wheel V5 robot.
6. Use VEXcode V5 and Python to make a drivetrain move, turn, stop, and change speed.
7. Use variables, conditionals, loops, and simple functions in robot-control code.
8. Mount, connect, and configure the VEX AI Vision Sensor.
9. Configure and test Color Signatures under changing conditions.
10. Interpret AI Vision properties including exists, centerX, centerY, width, and height.
11. Build a closed-loop Object Centering Robot.
12. Build an Object Following Robot using target position and apparent size.
13. Use AprilTags for tag-based robot decisions after color tracking is reliable.
14. Explain images as pixel data.
15. Explain RGB/BGR and HSV color representations.
16. Use OpenCV thresholding, masks, contours, bounding boxes, and center/centroid calculations.
17. Connect a classical OpenCV pipeline to the data returned by the VEX AI Vision Sensor.
18. Build and test an integrated autonomous vision robot.
19. Use evidence from physical testing to justify a redesign, including a camera-mount redesign in Onshape when appropriate.
20. Explain the complete system as perception → decision → action.

---

## Core Units

### Unit 1 — Engineering Notebook and Engineering Process

Ongoing throughout the course.

Students document:
- Goal
- Design/change
- Evidence
- Test result
- Decision
- Next step

### Unit 2 — Essential Onshape

Required only:
- Part Studio essentials
- Introduction to Onshape Assemblies
- VEX V5 Parts Library
- robot CAD understanding

The current class has already completed the TrainingBot CAD model.

Not required:
- Drawings
- Detailed Drawings
- Inspection and Repair
- advanced surfacing
- sheet metal
- certification preparation

Later in the course, students return to Onshape only when real AI Vision testing creates a mounting/design need.

### Unit 3 — Minimum VEXcode V5 for Vision

Required:
- project/device setup
- drivetrain control
- drive / drive_for
- turn / turn_for
- stop
- set_drive_velocity
- variables
- if / elif / else
- while loops
- simple functions

Performance checkpoint:

> **Forward → Turn → Stop → Forward**

### Unit 4 — AI Vision Sensor Fundamentals

Students learn:
- sensor mounting and connection
- AI Vision Utility / camera feed
- Color Signature
- Hue Range
- Saturation Range
- lighting/background effects
- detection testing

### Unit 5 — Vision Data and Closed-Loop Control

Students use:
- exists
- centerX
- centerY
- width
- height

Major Project 1:

**Object Centering Robot**

Core idea:

> error = centerX - 160

Major Project 2:

**Object Following Robot**

Use centerX for steering and width/height as a rough near/far proxy.

### Unit 6 — Formal Computer Vision with OpenCV

Students complete selected parts of:

**Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision**

Required concepts:
- image/pixel basics
- RGB/BGR
- HSV
- thresholding
- masks
- contours
- bounding boxes
- center/centroid
- real-time video frames

Face-recognition-specific material is optional.

Students explicitly compare:

> **OpenCV: image → HSV → mask → contour → bounding box → center**

with:

> **VEX AI Vision: snapshot → detected object → centerX / centerY / width / height**

### Unit 7 — AprilTag and Vision-Based Navigation

After color tracking works reliably, students add:
- Tag ID
- orientation/angle data
- tag-based decisions
- simple station/navigation behavior

### Unit 8 — Integrated Vision Robot

Core final behavior:

> **Search → Detect → Center → Approach → Stop / Perform Task**

Students integrate:
- drivetrain
- VEXcode Python
- AI Vision Sensor
- perception data
- decision logic
- closed-loop movement
- formal CV understanding
- engineering evidence

### Unit 9 — Evidence-Based Redesign

After real testing, students identify a genuine camera-placement or visibility problem and redesign the AI Vision Sensor mount in Onshape.

> **CAD → Build → Code → Vision → Test → Redesign**

---

## Major Projects

1. **VEXcode Motion Mini-Task** — Forward → Turn → Stop → Forward
2. **Reliable Color Detection** — configure and stress-test a Color Signature
3. **Object Centering Robot** — turn until the target is centered
4. **Object Following Robot** — center, approach, and stop
5. **OpenCV Vision Labs** — HSV, masks, contours, bounding boxes
6. **AprilTag Behavior** — tag-based robot decisions
7. **Final Integrated Vision Robot** — autonomous perception-to-action system
8. **AI Vision Mount Redesign** — evidence-based CAD iteration

---

## What Is Not Core

The following topics may be used later as extensions but are no longer required before CV:
- separate Distance Sensor unit
- separate Optical Sensor unit
- separate Inertial Sensor unit
- full controller-programming unit
- long competition-autonomy sequence
- dedicated PID unit
- full Onshape Fundamentals completion
- required CNN/YOLO theory sequence
- required Edge Impulse course

---

## Engineering Evidence

### Team Engineering Notebook

Use the ongoing pattern:

> **Goal → Work → Evidence → Decision → Next Step**

Students should include:
- CAD screenshots
- code
- camera configuration
- test conditions
- detection results
- failures
- changes
- retest evidence

### Individual Learning Evidence

Each student should be able to explain:
- what they changed;
- what data they observed;
- why the robot behaved as it did;
- what they would test next.

---

## Assessment Emphasis

Suggested weighting:
- Engineering evidence / portfolio: 20%
- Formative checks / quizzes: 15%
- Projects and robotics/CV challenges: 40%
- Final integrated project: 20%
- Presentation / reflection: 5%

Performance evidence is more important than simply completing videos or tutorials.

---

## Core Learning Principle

The course should not become a checklist of software features.

The desired student progression is:

> **I can model it → I can move it → I can make it see → I can use what it sees → I can explain how the vision works → I can redesign the system from evidence.**