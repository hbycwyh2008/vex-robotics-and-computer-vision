# Syllabus — VEX Robotics, AI Vision, and Intelligent Control

## Course Description

VEX Robotics, AI Vision, and Intelligent Control is a **full-year, project-based high school course** in which students build, program, test, debug, document, and improve real robots using the **VEX V5 Competition Starter Kit**.

Students begin with the official VEX **TrainingBot — Competition Kit**, then progress through driver control, VEXcode/Python programming, sensors, autonomous behavior, engineering design, mechanisms, and competition-style challenges. In the later part of the course, students use **Python and OpenCV** to build a transparent classical computer-vision pipeline, then study selected required material from **Andrew Ng / DeepLearning.AI's Convolutional Neural Networks** course and **Edge Impulse's Computer Vision with Embedded Machine Learning** course to connect classical vision to CNNs, transfer learning, object detection, embedded vision, and robot decision making.

The central systems idea is:

> **Perception → Decision → Action → Testing → Improvement**

The computer-vision learning progression is:

> **Pixels → Rules → Objects → CNNs → Detection → Embedded Vision → Robot Decisions**

This remains a hands-on robotics engineering course rather than a full deep-learning specialization. However, **modern CNN-based computer vision is a required conceptual component**, not optional enrichment. Students learn enough CNN, MobileNet, transfer-learning, localization, IoU, NMS, and YOLO concepts to understand how modern learned perception differs from the classical OpenCV system they build themselves.

---

## Shared Classroom Learning Flow

This course uses the same learning language as the Full-Stack Web and AI course:

> **Learn → Practice → Rebuild → Share**

In VEX Robotics, students apply that shared learning flow through the engineering cycle:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

See [classroom-learning-flow.md](classroom-learning-flow.md).

A robot working once does not prove mastery. Students are expected to explain, rebuild, debug, improve, and document important engineering patterns as the course progresses.

---

## Mastery Levels

The course uses the shared **Mastery Level 0–5** system:

- **Level 0 — Exposure**
- **Level 1 — Follow and make it work**
- **Level 2 — Explain while looking**
- **Level 3 — Rebuild with a checklist**
- **Level 4 — Rebuild independently**
- **Level 5 — Modify, debug, and transfer**

Mastery Levels describe **how independently a student can perform and transfer a skill**. They do not replace the existing 4-level project rubrics, which measure **how well a particular project meets requirements**.

See [mastery-levels.md](mastery-levels.md).

---

## Schedule

- Approximately **36 instructional weeks**
- **2–3 class meetings per week**
- Approximately **72–108 class periods** depending on the school calendar
- Significant lab time is reserved for building, testing, rebuilding, debugging, redesign, documentation, and demonstrations
- Coursera content is assigned as **selected video segments mapped to local lessons**, not as an unstructured requirement to complete entire external courses

## Prerequisites

- High school standing (Grade 9+ recommended)
- Comfort with basic problem solving and teamwork
- Prior programming exposure is helpful but not required
- No prior robotics experience required

## Standard Hardware and Software

### Robotics

- **VEX V5 Competition Starter Kit** per team
- V5 Robot Brain, Controller, Battery, Smart Motors, structural components, drivetrain parts, and available V5 sensors
- Official **TrainingBot — Competition Kit** as the first instructional build

### Programming

- **VEXcode V5**
- Python where supported/appropriate for course programming
- GitHub + Markdown for portfolio evidence

### AI Vision

- Computer with Python
- OpenCV
- Jupyter notebook or Python IDE as appropriate
- USB webcam and/or school-approved VEX vision hardware as available
- Coursera access for selected videos from:
  - IBM — **Introduction to Computer Vision and Image Processing**
  - DeepLearning.AI / Andrew Ng — **Convolutional Neural Networks**
  - Edge Impulse — **Computer Vision with Embedded Machine Learning**

See [resources.md](resources.md) for the exact video-to-lesson mapping.

---

## Learning Outcomes

By the end of the course, students will be able to:

1. Follow robotics lab safety and hardware-management procedures.
2. Identify, select, assemble, and maintain major VEX V5 components.
3. Build and troubleshoot a reliable V5 drivetrain.
4. Configure the V5 Brain, Controller, motors, and sensors.
5. Program robot motion using readable, modular code.
6. Use functions, loops, conditionals, sensor input, and feedback in robot programs.
7. Design and test autonomous robot behaviors.
8. Explain speed/torque trade-offs and apply basic mechanism design principles.
9. Apply the engineering design process to open-ended robot challenges.
10. Use repeated tests and evidence to diagnose failures and justify changes.
11. Rebuild core robotics/programming patterns with progressively less support.
12. Process camera images with OpenCV using color spaces, masks, contours, bounding boxes, and target position.
13. Build and test a complete transparent classical computer-vision detector.
14. Explain the conceptual roles of convolution, pooling, CNN feature learning, MobileNet, transfer learning, and data augmentation.
15. Distinguish image classification, localization, object detection, and segmentation at the appropriate conceptual level.
16. Explain bounding boxes, IoU, NMS, anchor boxes, and the basic idea behind YOLO.
17. Compare classical hand-designed computer vision with learned CNN-based computer vision and justify when each may be appropriate.
18. Explain why lightweight architectures and transfer learning are important for embedded/robotics vision.
19. Connect a perception result—classical or learned—to a robot decision and action through a modular perception/decision/action architecture.
20. Test vision systems under changing conditions and explain failure modes including brittle thresholds, domain shift, dataset mismatch, false positives/negatives, latency, and uncertain perception.
21. Use AI coding tools responsibly while retaining understanding and ownership of submitted work.
22. Maintain a Team Engineering Notebook with evidence of testing, debugging, iteration, and decisions.
23. Maintain an Individual Engineering Learning Log showing personal contribution and mastery.
24. Maintain a GitHub/Markdown portfolio with curated project evidence.
25. Present and defend an integrated robotics project and explain individual technical contributions.

---

## Major Units

1. **Unit 00 — Course Onboarding, Safety, Learning Flow, Mastery, and Engineering Documentation**
2. **Unit 01 — VEX V5 Foundations and TrainingBot**
3. **Unit 02 — Driver Control and Robot Motion Programming**
4. **Unit 03 — Sensors and Autonomous Control**
5. **Unit 04 — Engineering Design, Mechanisms, and Robot Challenges**
6. **Unit 05 — Classical Computer Vision Foundations with OpenCV**
7. **Unit 06 — Modern AI Vision, CNN Concepts, and Robot Decision Making**
8. **Unit 07 — Integrated Robotics + Vision Capstone**

## Major Projects

1. **TrainingBot Build & Driver Challenge**
2. **Project 01 — Basic Driving Robot**
3. **Project 02 — Sensor-Based Autonomous Robot**
4. **Project 03 — Robot Challenge Design**
5. **Project 04 — Color Object Detection with OpenCV**
6. **Project 05 — Vision-Guided Robot Decision System**
7. **Final — Integrated Robotics and Vision Capstone**

The capstone may use a classical, learned, or hybrid perception approach, but the choice must be justified by requirements, reliability evidence, deployment constraints, and testing—not by choosing the most complex method automatically.

---

## Required Computer Vision Video Path

### Stage 1 — Classical CV foundation

**IBM — Introduction to Computer Vision and Image Processing**

Use selected introductory and image-processing videos alongside Lessons 17–18.

### Stage 2 — Modern CV foundation — required

**DeepLearning.AI / Andrew Ng — Convolutional Neural Networks**

Required selected topics distributed across Lessons 19–23 include:
- computer vision and edge detection;
- convolution, padding, stride and pooling;
- CNN architecture intuition;
- MobileNet;
- transfer learning;
- data augmentation;
- object localization and detection;
- bounding-box prediction;
- IoU;
- non-max suppression;
- anchor boxes;
- YOLO.

### Stage 3 — Embedded vision bridge

**Edge Impulse — Computer Vision with Embedded Machine Learning**

Use selected videos on image classification, CNNs, MobileNet/transfer learning, object-detection metrics, model training, and deployment to connect modern CV concepts to robotics/edge constraints.

See [resources.md](resources.md) and Lessons 17–23 for exact assignments.

---

## Engineering Evidence

### Team Engineering Notebook

The team notebook records the shared engineering process:

> **Goal → Design / Change → Test → Problem → Diagnosis → Decision → Retest → Next Step**

The notebook is written during the engineering process, not reconstructed at the end.

### Individual Engineering Learning Log

Each student records:

- what they personally worked on;
- one engineering decision they understand;
- one problem and diagnosis;
- their personal contribution;
- what they can now explain or rebuild;
- current Mastery Level and evidence;
- next learning step.

### Testing Rule

When a student/team claims that a robot, perception module, or subsystem became more reliable, accurate, consistent, or effective, the claim should be supported by repeated trials or a controlled comparison.

> **Build / Program → Test → Record → Explain**

For learned vision, high model confidence alone is not proof of system reliability. Students must distinguish model output from measured deployment performance.

See:

- [Engineering Notebook Guide](student-handouts/engineering-notebook-guide.md)
- [Team Engineering Notebook Template](student-handouts/engineering-notebook-template.md)
- [Individual Engineering Learning Log](student-handouts/individual-engineering-learning-log.md)
- [Engineering Test Record Template](student-handouts/test-record-template.md)

---

## Assessment Categories

| Category | Suggested Weight | Evidence |
|---|---:|---|
| Engineering evidence & GitHub portfolio | 20% | Team notebook, individual logs, code, photos/video, test data, reflections |
| Formative checks & quizzes | 15% | Hardware, programming, sensor, engineering, classical CV, CNN/object-detection concepts, mastery checks |
| Projects & engineering challenges | 40% | Performance + design process + evidence |
| Final integrated project | 20% | System design, build, code, testing, demo + individual defense |
| Presentation & reflection | 5% | Technical explanation and defense |

> Adjust weights to match school grading policy.

The existing **4-level project rubrics** remain the project grading scale. Mastery Levels 0–5 are used as a separate framework for learning independence and skill verification.

See [assessment-plan.md](assessment-plan.md).

---

## Classroom Expectations

- Follow lab safety rules at all times.
- Use the correct tool for each VEX fastener and component.
- Power down and store equipment properly.
- Keep team parts organized and return hardware to the correct location.
- Follow the shared learning cycle: **Learn → Practice → Rebuild → Share**.
- Treat the first successful build/run as a starting point, not final proof of mastery.
- Document work while building; do not reconstruct the Team Engineering Notebook at the end.
- Debug systematically using **Symptom → Hypothesis → Test → Evidence → Decision** rather than random changes.
- Use evidence to justify redesign and retest important changes.
- Every team member must be able to explain their contribution and relevant robot structure/code.
- Complete individual learning evidence honestly; do not copy a teammate's reflection.
- Watch assigned external videos actively and connect them to the local build/program/test task rather than treating video completion as mastery.
- Respect shared hardware and clean the workstation before leaving.

---

## AI Use Expectations

AI tools may be used as learning and development assistants when allowed by the teacher. Students must:

- disclose meaningful AI assistance;
- understand and explain generated code;
- test generated suggestions on the real system;
- verify technical claims against documentation or evidence;
- modify and debug the work themselves;
- never invent measurements or test data;
- never submit AI output as evidence of understanding without being able to defend it.

See [student-handouts/ai-use-policy.md](student-handouts/ai-use-policy.md).

---

## Classroom Posters

Shared classroom posters used by this course are stored in:

[public-documents/posters/](public-documents/posters/README.md)

They reinforce:

- classroom learning flow;
- Mastery Levels;
- responsible AI use;
- optional CS / robotics competition pathways.

---

## Portfolio Expectations

Every student maintains an engineering portfolio. Each major project should include:

- design goal and constraints;
- build photos or diagrams;
- code and configuration notes;
- test procedure and results;
- failures and debugging evidence;
- design changes and reasons;
- retest/comparison evidence when appropriate;
- final demonstration evidence;
- individual contribution and mastery reflection;
- reflection on what the student would improve or test next.

Computer-vision portfolio evidence should also demonstrate that the student can distinguish:

- hand-written classical CV rules;
- learned CNN-based perception;
- perception output;
- decision logic;
- robot action/control;
- measured reliability under changing conditions.

See [portfolio-requirements.md](portfolio-requirements.md) and [pacing-guide.md](pacing-guide.md).
