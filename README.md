# VEX Robotics + Computer Vision

A project-based high school course that uses **VEX V5 + VEX AI Vision Sensor + Python + OpenCV** to teach robotics, computer vision, engineering iteration, and intelligent control.

> **Current curriculum backbone:** CAD → Robot Control → AI Vision → Vision-Based Control → Formal CV Course → Integrated Vision Robot

Start with the authoritative current sequence:

- [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md)
- [syllabus.md](syllabus.md)
- [resources.md](resources.md)
- [pacing-guide.md](pacing-guide.md)

## Current Classroom Status

The present class has already:
- built the basic VEX V5 TrainingBot / four-wheel drive robot;
- created the TrainingBot in Onshape;
- used a working Controller program to drive the robot.

Therefore the course no longer spends a long block on rebuilding the drivetrain, full controller programming, or separate Distance/Optical/Inertial sensor units before computer vision.

## Standard Platform

- VEX V5 Competition Starter Kit / compatible V5 hardware
- V5 TrainingBot / Advanced Trainingbot-style four-wheel drivetrain
- V5 Brain + Controller + Smart Motors
- **VEX AI Vision Sensor** as the primary perception sensor
- VEXcode V5
- Python
- Onshape
- OpenCV

## Essential Onshape Only

Onshape is an enabling skill, not a separate full CAD course.

Students need:
1. Part Studio essentials;
2. **Introduction to Onshape Assemblies**;
3. VEX V5 Parts Library;
4. ability to rebuild the real robot in CAD;
5. ability to redesign the AI Vision Sensor mount after real testing.

The current class has already completed the TrainingBot CAD model.

Do not require the rest of Onshape Fundamentals such as Drawings, Detailed Drawings, Inspection and Repair, advanced surfacing, sheet metal, or certification preparation.

## Minimum VEXcode Before Vision

Students only need enough VEXcode/Python to connect code to motion:
- drive;
- drive_for;
- turn;
- turn_for;
- stop;
- set_drive_velocity;
- variables;
- if / elif / else;
- while loops;
- simple functions.

Mini-task:

> **Forward → Turn → Stop → Forward**

Once this works, move directly to AI Vision.

## AI Vision Sequence

1. Mount and connect the AI Vision Sensor.
2. Open the camera feed / AI Vision Utility.
3. Configure a Color Signature.
4. Test under different lighting, distance, angle, and background conditions.
5. Read **centerX, centerY, width, height, exists**.
6. Build an Object Centering Robot.
7. Build an Object Following Robot.
8. Add AprilTag behavior after color tracking works reliably.

Core control idea:

> **See → Measure → Decide → Move → See Again**

## Formal Computer Vision Course

Students should not only call VEX AI Vision APIs. The current structured CV course is:

**Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Use the OpenCV foundations, image-processing, geometry, and real-time video portions. Face-recognition-specific content is optional.

Students must understand:
- images and pixels;
- RGB/BGR and HSV;
- thresholding;
- masks;
- contours;
- bounding boxes;
- center/centroid;
- real-time frames.

They then connect:

> **OpenCV: image → HSV → mask → contour → bounding box → center**

to:

> **VEX AI Vision: snapshot → detected object → centerX / centerY / width / height**

Andrew Ng CNN and Edge Impulse material are now **optional advanced extensions**, not required core content.

## Final Integrated Project

The core final system should perform:

> **Search → Detect → Center → Approach → Stop / Perform Task**

After real testing exposes a camera-placement or visibility problem, students return to Onshape and redesign the AI Vision mount using evidence from the physical robot.

> **CAD → Build → Code → Vision → Test → Redesign**

## Engineering Evidence

Students maintain a Team Engineering Notebook and individual learning evidence throughout the course.

Use:
- [Engineering Notebook Guide](student-handouts/engineering-notebook-guide.md)
- [Team Engineering Notebook Template](student-handouts/engineering-notebook-template.md)
- [Individual Engineering Learning Log](student-handouts/individual-engineering-learning-log.md)
- [Engineering Test Record Template](student-handouts/test-record-template.md)

## Repository Structure

- CURRENT-COURSE-PATH.md — authoritative current sequence
- syllabus.md — course requirements and units
- pacing-guide.md — suggested pacing
- resources.md — official resources and video/course links
- lessons/ — anchor lessons and reference material
- student-handouts/ — student-facing templates and project documents
- teacher-notes/ — teacher implementation notes
- assessments/ — practical and written assessment resources

## Important Note About Older Materials

Some older lesson/playbook files in this repository reflect the previous broader sequence with separate sensor/autonomy units and required CNN/Edge Impulse study. Treat those files as **reference/extension material** unless they match [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md).

The current path intentionally prioritizes **AI Vision + real robot behavior + formal OpenCV learning** over completing every traditional VEX topic first.