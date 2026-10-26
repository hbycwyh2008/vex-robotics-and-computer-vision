# Pacing Guide — Current VEX Robotics + Computer Vision Path

This pacing guide follows [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md). It replaces the older assumption that students must complete long sensor/autonomy and mechanism units before computer vision.

## Current Class Entry Point

The current class has already completed:
- physical TrainingBot / four-wheel build;
- working Controller operation;
- TrainingBot CAD in Onshape.

Therefore begin from Phase 3 below.

---

## Phase 1 — Engineering Notebook Setup (ongoing)

Suggested time: 1 class to launch, then 10–15 minutes integrated into major work sessions.

Students learn the notebook pattern:

> **Goal → Work → Evidence → Decision → Next Step**

Do not isolate notebook work into a separate long unit. Use it continuously.

---

## Phase 2 — Essential Onshape

Suggested time for a new cohort: 3–6 class meetings depending on prior CAD experience.

Required sequence:
1. Part Studio essentials
2. Introduction to Onshape Assemblies
3. VEX V5 Parts Library
4. rebuild/inspect the TrainingBot CAD

Current class status: **completed**.

Do not continue into Drawings, Detailed Drawings, Inspection and Repair, advanced surfacing, sheet metal, or certification preparation.

Return to Onshape later only for evidence-based AI Vision mount redesign.

---

## Phase 3 — Minimum VEXcode V5 for Vision

Suggested time: 1–2 class meetings.

### Meeting A — VEXcode platform
- Lesson 1: Coding with VEXcode V5
- connect Brain
- run/stop
- drivetrain configuration
- drive and turn

### Meeting B — Python bridge
- Lesson 2a: Code Viewer in VEXcode V5 (Python)
- drive / drive_for
- turn / turn_for
- stop
- set_drive_velocity
- variables
- if / elif / else
- while
- simple functions

Checkpoint:

> **Forward → Turn → Stop → Forward**

Stop here. Do not expand into a long general VEX programming unit.

---

## Phase 4 — AI Vision Setup and Reliable Color Detection

Suggested time: 2–3 class meetings.

### Meeting A — Mount and connect
- mount AI Vision Sensor on the Advanced Trainingbot/simple four-wheel robot
- connect to V5 Brain
- open AI Vision Utility
- verify camera feed

### Meeting B — Color Signature
- set one Color Signature
- Hue Range
- Saturation Range
- test detection

### Meeting C — Reliability test
Change:
- lighting
- distance
- angle
- background

Students record failure cases and adjust the signature.

Performance checkpoint:

> **The robot can reliably detect the chosen colored target under several classroom conditions.**

---

## Phase 5 — Vision Data

Suggested time: 1–2 class meetings.

Students learn:
- exists
- centerX
- centerY
- width
- height
- take_snapshot()

Key reference:

> Image size ≈ 320 × 240; center ≈ (160, 120).

Students should be able to explain what changes in centerX and width mean physically.

---

## Phase 6 — Project 1: Object Centering Robot

Suggested time: 2–4 class meetings.

Core idea:

> **error = centerX - 160**

Students build a repeated visual feedback loop:

> **See → Measure → Decide → Turn → See Again**

Requirements:
- target left → robot corrects left
- target right → robot corrects right
- target centered → robot stops turning
- repeated snapshots update the decision

Assessment emphasis:
- reliable behavior
- readable logic
- notebook evidence
- explanation of error and feedback

---

## Phase 7 — Project 2: Object Following Robot

Suggested time: 3–5 class meetings.

Extend the centering system:
- centerX → steering
- width/height → rough near/far estimate

Behavior:
1. find target
2. center target
3. approach
4. stop when target appears sufficiently large
5. keep updating visual data

Checkpoint:

> **Find → Center → Approach → Stop**

---

## Phase 8 — Formal CV Course: OpenCV

Suggested time: 4–8 class meetings plus selected homework/video time.

Core course:

**Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision**

https://www.coursera.org/learn/master-opencv-fundamentals-for-real-time-computer-vision

Recommended scope:
- Module 1 — required
- Module 2 — required/selected
- Module 3 — real-time webcam/video portions required
- face-recognition-specific workflow optional

Local labs should cover:
1. image / pixel / shape
2. RGB/BGR → HSV
3. threshold / inRange
4. mask
5. contours
6. bounding box
7. center/centroid
8. real-time frame processing

Students connect the OpenCV pipeline to the VEX AI Vision output.

---

## Phase 9 — AprilTag

Suggested time: 2–3 class meetings.

Teach only after color tracking and following work.

Students use:
- Tag ID
- center/size
- angle/orientation
- simple tag-based decisions

Possible challenge:
- Tag 1 → turn left
- Tag 2 → turn right
- Tag 3 → stop

Extension:
- station-to-station navigation

---

## Phase 10 — Final Integrated Vision Robot

Suggested time: 4–8 class meetings.

Core behavior:

> **Search → Detect → Center → Approach → Stop / Perform Task**

Required system elements:
- drivetrain
- Python control
- AI Vision Sensor
- perception data
- decision logic
- closed-loop movement
- formal CV explanation
- test evidence

Students should run repeated trials and report failure modes.

---

## Phase 11 — Onshape Redesign from Evidence

Suggested time: 1–3 class meetings.

Only after students have real camera-performance evidence, return to CAD.

Possible problems:
- camera too low
- poor angle
- robot structure blocks field of view
- vibration
- unstable mounting
- cable routing problem

Students redesign the AI Vision mount and retest.

> **CAD → Build → Code → Vision → Test → Redesign**

---

## Optional Extensions

Use only after the core vision robot works:
- state machine
- multiple targets
- vision-guided claw/intake
- sorting/delivery challenge
- CNN concepts
- MobileNet / transfer learning
- Edge Impulse
- learned object detection

---

## Topics That Should Not Delay CV

Do not require these before Phase 4:
- Distance Sensor unit
- Optical Sensor unit
- Inertial Sensor unit
- PID unit
- long competition autonomy sequence
- advanced mechanism unit
- full Onshape Fundamentals

Use them later only if the project creates a real need.

---

## Recommended Learning Rhythm

For a 90-minute class:
- 0–10 min: retrieval / prediction / setup
- 10–25 min: focused video/demo
- 25–60 min: build/code/practice
- 60–78 min: test/debug/retest
- 78–87 min: engineering notebook evidence
- 87–90 min: exit check / reset

The course should spend more time making systems work reliably than consuming tutorials.