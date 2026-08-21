# Student-Ready Lesson Sequence

This directory turns the 36-week course framework into classroom-ready anchor lessons.

## Shared Learning Culture

Every lesson inherits the same course learning language used across the CS program:

> **Learn → Practice → Rebuild → Share**

VEX Robotics applies that shared flow through the engineering cycle:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

See:

- [`../classroom-learning-flow.md`](../classroom-learning-flow.md)
- [`../mastery-levels.md`](../mastery-levels.md)
- [`../public-documents/posters/`](../public-documents/posters/README.md)

The existing lesson files do not need separate duplicated versions of these rules. Teachers should apply this shared framework whenever an anchor lesson is expanded across one or more class meetings.

---

## Design Principles

- Start from the physical VEX V5 Competition Starter Kit.
- Build the official TrainingBot baseline before major redesign.
- Establish mechanical reliability before advanced programming.
- Move from driver control → programmed motion → sensors/autonomy → engineering mechanisms → computer vision → integrated AI robotics.
- Keep approximately 70% of instructional time focused on robotics, engineering and control, with approximately 30% focused on computer vision / AI application.
- Require engineering evidence, debugging notes and reflection throughout the course.
- Treat following instructions as the beginning of learning, not final mastery.
- Reduce scaffolding over time so students move from following → explaining → rebuilding → independent engineering → transfer.
- Protect enough lab time for meaningful physical testing and retesting.

---

## Mastery Levels Used in Lessons

Every anchor lesson should identify or imply a target using the shared Mastery Levels 0–5:

| Level | Meaning |
|---|---|
| 0 | Exposure |
| 1 | Follow and make it work |
| 2 | Explain while looking |
| 3 | Rebuild with a checklist |
| 4 | Rebuild independently |
| 5 | Modify, debug, and transfer |

See [`../mastery-levels.md`](../mastery-levels.md) for VEX-specific examples.

For major course skills, the long-term target is typically **Level 3–4**. Capstone work should create opportunities for **Level 4–5** evidence.

Mastery Levels are not the same as the existing 4-level project rubrics.

---

## Engineering Evidence Required Across Lessons

### Team Engineering Notebook

The team documents:

> **Goal → Design / Change → Test → Problem → Diagnosis → Decision → Retest → Next Step**

Minimum evidence for a major work session:

- [ ] today's goal;
- [ ] one design/build/code/configuration change;
- [ ] one test or observation;
- [ ] one result, measurement, or failure;
- [ ] one next step.

Challenge/project sessions should also include:

- [ ] debugging evidence;
- [ ] justified engineering decision;
- [ ] retest or comparison evidence.

### Individual Engineering Learning Log

When assigned, each student records:

- what they personally worked on;
- one engineering decision they understand;
- one problem and diagnosis;
- their personal contribution;
- what they can now explain or rebuild;
- current Mastery Level and evidence.

Use:

- [`../student-handouts/engineering-notebook-guide.md`](../student-handouts/engineering-notebook-guide.md)
- [`../student-handouts/engineering-notebook-template.md`](../student-handouts/engineering-notebook-template.md)
- [`../student-handouts/individual-engineering-learning-log.md`](../student-handouts/individual-engineering-learning-log.md)
- [`../student-handouts/test-record-template.md`](../student-handouts/test-record-template.md)

> **Build / Program → Test → Record → Explain**

---

## Standard Lesson Architecture

Each lesson or expanded class meeting should contain the following functions, even if timing changes by lesson type:

1. **Course position / entry** — retrieve prior learning, inspect the system, or predict.
2. **Learning objectives + Mastery target** — what students should become able to do independently.
3. **Focused technical instruction** — concise teacher explanation or demonstration.
4. **Guided practice** — supported first attempt.
5. **Rebuild / engineering mission** — reproduce or apply the important pattern with less support.
6. **Test / debug / redesign / retest** — use evidence, not random changes.
7. **Document / explain / share** — Team Notebook + individual evidence when assigned.
8. **AI-use guidance** where relevant.
9. **Exit mastery check** — explanation, prediction, rebuild, debugging, or transfer question.
10. **Connection to the next lesson**.

Teachers expanding an anchor lesson into a 90-minute meeting should use [`../teacher-notes/90-minute-lesson-template.md`](../teacher-notes/90-minute-lesson-template.md).

---

## Current Sequence

### Unit 00 — Getting Started

- Lesson 01: Kit Safety and Parts

### Unit 01 — TrainingBot

- Lesson 02: TrainingBot Build I — Chassis and Drivetrain
- Lesson 03: TrainingBot Build II and First Power-On

### Unit 02 — Driver Control and Programming

- Lesson 04: VEXcode and Device Configuration
- Lesson 05: Python Motion, Variables and Functions
- Lesson 06: Controller Input — Tank Drive and Arcade Drive
- Lesson 07: Driver Control Engineering Challenge

### Unit 03 — Sensors and Autonomous Control

- Lesson 08: Sensor Data and Thresholds
- Lesson 09: Distance Sensor — Obstacle Response
- Lesson 10: Inertial Sensor — Reliable Turning
- Lesson 11: Autonomous State Sequence
- Lesson 12: Autonomous Navigation Challenge

### Unit 04 — Engineering Design and Mechanisms

- Lesson 13: Gear Ratio — Speed and Torque Trade-Offs
- Lesson 14: Manipulator Mechanism Prototype
- Lesson 15: Engineering Iteration and Test Data
- Lesson 16: Competition-Style Robot Challenge

### Unit 05 — Computer Vision Foundations

- Lesson 17: Images as Data — Pixels and Color
- Lesson 18: HSV Thresholding and Color Masks
- Lesson 19: Contours, Bounding Boxes and Centroids
- Lesson 20: Color Object Detection Project

### Unit 06 — AI Robotics Integration

- Lesson 21: Vision to Decision Logic
- Lesson 22: Closed-Loop Vision Alignment
- Lesson 23: Vision Robustness and Failure Modes

### Unit 07 — Integrated Capstone

- Lesson 24: Capstone Proposal and System Architecture
- Lesson 25: Capstone Build, Integrate and Test
- Lesson 26: Final Validation, Showcase and Engineering Defense

---

## 36-Week Alignment

- Weeks 1–2: onboarding, safety, parts organization, learning flow, mastery, notebook routines
- Weeks 3–6: VEX V5 foundations + TrainingBot
- Weeks 7–12: VEXcode/Python + driver control
- Weeks 13–18: sensors + autonomous control
- Weeks 19–24: mechanisms + engineering challenge
- Weeks 25–30: OpenCV / computer vision
- Weeks 31–33: AI vision decision making
- Weeks 34–36: integrated capstone

---

## Teacher Implementation Note

A week may contain 2 or 3 class meetings. Lessons are therefore not required to map one-to-one to calendar weeks. Long build, testing and capstone lessons can span multiple meetings, while short programming missions may share a week.

The 26 lesson files are **anchor lessons, not 26 total class periods**. A 36-week course meeting 2–3 times per week should use each anchor lesson across one or more meetings, with additional guided practice, rebuild, debugging, assessment, testing, documentation and project days between anchors.

Do not rush from one anchor lesson to the next simply because a robot worked once. Advance when the required evidence and mastery target are reasonably secure.
