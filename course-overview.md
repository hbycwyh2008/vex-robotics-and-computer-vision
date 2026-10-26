# Course Overview — VEX Robotics + Computer Vision

## What This Course Is

A project-based high school course that uses a simple VEX V5 mobile robot as the physical platform for learning robotics, computer vision, and intelligent control.

The current course is intentionally streamlined around:

> **Essential CAD → Minimum Robot Control → AI Vision → Vision-Based Control → Formal OpenCV → Integrated Vision Robot**

The goal is not to complete every traditional VEX topic before computer vision. The goal is to make students understand and build a complete perception-to-action system.

See [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md) for the authoritative sequence.

## Current Starting Point

The current class has already:
- built the basic VEX V5 TrainingBot / four-wheel robot;
- used an existing Controller program to drive it;
- recreated the TrainingBot in Onshape.

Therefore, the next sequence begins with minimal VEXcode/Python motion control and the AI Vision Sensor.

## Standard Platform

- VEX V5 TrainingBot / Advanced Trainingbot-style four-wheel drivetrain
- V5 Brain
- Controller
- Smart Motors
- **VEX AI Vision Sensor**
- VEXcode V5
- Python
- Onshape
- OpenCV

## Course Philosophy

- **Keep the robot simple while vision is new.** Avoid unnecessary claw/arm complexity at the start of CV.
- **Use CAD only when it serves the robot.** Students learn only the Onshape skills needed to understand assemblies and design a useful mount.
- **Code only what vision needs first.** Students learn the Drivetrain API and basic Python control, then move directly to AI Vision.
- **Make perception visible.** Students inspect centerX, centerY, width, height, masks, contours, and bounding boxes.
- **Use closed-loop behavior early.** The core idea is See → Measure → Decide → Move → See Again.
- **Teach formal CV, not only sensor APIs.** Students complete a structured OpenCV course and connect its pipeline to the VEX AI Vision data model.
- **Redesign from evidence.** Camera mounting is revisited after real testing, not before students know what problem they need to solve.

## Essential Onshape Scope

Required:
- Part Studio essentials
- Introduction to Onshape Assemblies
- VEX V5 Parts Library
- ability to understand/rebuild the robot as an assembly
- later camera-mount redesign

Not required:
- Drawings
- Detailed Drawings
- Inspection and Repair
- advanced surfacing
- sheet metal
- certification preparation

The current class has already completed the TrainingBot CAD model.

## Minimum VEXcode Scope

Students learn only enough to control the robot for vision work:
- drive
- drive_for
- turn
- turn_for
- stop
- set_drive_velocity
- variables
- conditionals
- while loops
- simple functions

Checkpoint:

> **Forward → Turn → Stop → Forward**

## AI Vision Learning Sequence

1. Mount/connect the sensor.
2. Open the camera feed and AI Vision Utility.
3. Configure a Color Signature.
4. Test detection under changing light, angle, distance, and background.
5. Read exists, centerX, centerY, width, and height.
6. Build an Object Centering Robot.
7. Build an Object Following Robot.
8. Add AprilTag behavior after color tracking is reliable.

## Formal Computer Vision

Core structured course:

**Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Students learn:
- images as pixels
- RGB/BGR
- HSV
- thresholding
- masks
- contours
- bounding boxes
- center/centroid
- real-time frames

They explicitly connect:

> **OpenCV: image → HSV → mask → contour → bounding box → center**

with:

> **VEX AI Vision: snapshot → detected object → centerX / centerY / width / height**

Andrew Ng CNN and Edge Impulse are optional extensions after the core system works.

## Core Projects

1. VEXcode Motion Mini-Task
2. Reliable Color Detection
3. Object Centering Robot
4. Object Following Robot
5. OpenCV Image/HSV/Mask/Contour Labs
6. AprilTag Behavior
7. Integrated Autonomous Vision Robot
8. AI Vision Sensor Mount Redesign

## Final System

The final core robot should be able to perform:

> **Search → Detect → Center → Approach → Stop / Perform Task**

Students should be able to explain:
- what the camera detects;
- how the data is represented;
- how code converts perception into a decision;
- how the drivetrain acts;
- why the system fails under some conditions;
- what evidence justifies the next redesign.

## Engineering Evidence

Engineering Notebook work continues throughout the course.

Evidence includes:
- CAD screenshots
- code
- camera configuration
- test conditions
- detection data
- failures
- decisions
- retest results
- redesign evidence

## Topics Removed from the Core Path

These are now optional/just-in-time rather than required before CV:
- separate Distance Sensor unit
- separate Optical Sensor unit
- separate Inertial Sensor unit
- full Controller programming unit
- long autonomous-navigation sequence
- dedicated PID unit
- full Onshape Fundamentals completion
- mandatory Andrew Ng CNN sequence
- mandatory Edge Impulse sequence

## Central Systems Idea

> **Camera → Perception Data → Decision Logic → Drivetrain Action → New Camera Data**

That feedback loop is the core of the course.