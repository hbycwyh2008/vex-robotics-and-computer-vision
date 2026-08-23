# VEX Robotics, AI Vision, and Intelligent Control

A **36-week, project-based high school robotics course** built around the **VEX V5 Competition Starter Kit**. Students build and maintain real robots, program driver-controlled and autonomous behavior, solve engineering challenges, and then extend their systems with **Python + OpenCV + modern computer vision concepts**.

> Students do not just learn *about* robotics and AI. They **build, program, test, debug, redesign, measure, document, and defend intelligent robotic systems.**

## Shared Course Learning Culture

This course uses the same core learning language as the Full-Stack Web and AI course:

> **Learn → Practice → Rebuild → Share**

VEX Robotics then applies that shared learning flow through an engineering-specific cycle:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

Students also use the shared **Mastery Level 0–5** system:

- **Level 0 — Exposure**
- **Level 1 — Follow and make it work**
- **Level 2 — Explain while looking**
- **Level 3 — Rebuild with a checklist**
- **Level 4 — Rebuild independently**
- **Level 5 — Modify, debug, and transfer**

See:

- [Classroom Learning Flow](classroom-learning-flow.md)
- [Mastery Levels — Robotics and Engineering](mastery-levels.md)
- [Course Posters](public-documents/posters/README.md)

**Important:** Mastery Level and project rubric level are different measures. Mastery describes **how independently a student can perform and transfer a skill**. Project rubrics describe **how well a particular project meets its engineering requirements**.

## Engineering Evidence System

Robotics is team-based, but team success does not automatically prove individual mastery. The course therefore uses two complementary records.

### Team Engineering Notebook

The team records the shared engineering process:

> **Goal → Design / Change → Test → Problem → Diagnosis → Decision → Retest → Next Step**

### Individual Engineering Learning Log

Each student records:

- what they personally worked on;
- one engineering decision they understand;
- one problem and how it was diagnosed;
- their specific contribution;
- what they can now explain or rebuild;
- their current Mastery Level and supporting evidence.

Use:

- [Engineering Notebook Guide](student-handouts/engineering-notebook-guide.md)
- [Team Engineering Notebook Template](student-handouts/engineering-notebook-template.md)
- [Individual Engineering Learning Log](student-handouts/individual-engineering-learning-log.md)
- [Engineering Test Record Template](student-handouts/test-record-template.md)

> **Build / Program → Test → Record → Explain**

A working robot is not sufficient evidence by itself. Claims about reliability, accuracy, or improvement should be supported by repeated tests and documented evidence.

## Course Format

- **Length:** approximately 36 instructional weeks
- **Meetings:** 2–3 classes per week (approximately 72–108 periods)
- **Hardware:** VEX V5 Competition Starter Kit
- **First official build:** TrainingBot — Competition Kit
- **Programming:** VEXcode V5 + Python where appropriate
- **AI / Vision:** Python + OpenCV + required selected Coursera material
- **CV video pathway:** IBM → Andrew Ng / DeepLearning.AI → Edge Impulse
- **Method:** project-based engineering, build–test–debug–iterate
- **Evidence:** Team Engineering Notebook + Individual Engineering Learning Log + GitHub/Markdown portfolio

## Core Learning Path

```text
V5 hardware & safety
        ↓
TrainingBot — Competition Kit
        ↓
Controller driving + VEXcode
        ↓
Python robot motion + modular programming
        ↓
Sensors + autonomous control
        ↓
Mechanisms + engineering challenges
        ↓
OpenCV classical computer vision
        ↓
Andrew Ng CNN foundations + object detection
        ↓
Embedded vision / Edge Impulse concepts
        ↓
Perception → Decision → Action
        ↓
Integrated robotics + AI vision capstone
```

## Computer Vision Learning Strategy

The CV sequence deliberately separates three layers:

1. **Classical CV** — students build a transparent OpenCV pipeline themselves.
2. **Modern learned CV** — students study required selected material from Andrew Ng / DeepLearning.AI to understand convolution, CNNs, MobileNet, transfer learning, localization, IoU, NMS and YOLO.
3. **Embedded / robotics CV** — students use selected Edge Impulse material to understand deployment constraints and how perception feeds robot decisions.

The progression is:

> **Pixels → Rules → Objects → CNNs → Detection → Embedded Vision → Robot Decisions**

Andrew Ng's CNN course is **required conceptual curriculum**, not optional enrichment. The robotics course does not require students to complete every Deep Learning Specialization programming assignment; selected videos are mapped directly to Lessons 19–23.

See [resources.md](resources.md) for the exact mapping.

## What Students Learn

### Robotics Engineering

- VEX V5 structure, fasteners, shafts, bearings, motors, Brain, battery, controller and sensors
- Reliable drivetrain construction, wiring, maintenance and troubleshooting
- Mechanisms, gear ratios, speed/torque trade-offs, rigidity, alignment and engineering constraints

### Programming and Control

- VEXcode V5
- Python-style computational thinking and modular programming
- Sequences, variables, functions, loops and conditionals
- Driver control and autonomous routines
- Sensor input, motor feedback, calibration and state-based control

### AI Vision

- Images and pixels
- BGR/RGB and HSV color spaces
- Thresholding and masks
- Contours, bounding boxes and target position
- Classical feature engineering vs learned feature representations
- Convolution and pooling
- CNN architecture intuition
- MobileNet and transfer learning
- Classification vs localization vs object detection
- Bounding boxes, IoU, NMS, anchor boxes and YOLO concepts
- Embedded-vision constraints
- Vision-system testing, domain shift and failure analysis
- Connecting perception to robot decisions and actions

### Engineering Practice

- Predict → build → test → debug → redesign → retest
- Team Engineering Notebook evidence
- Individual mastery and contribution evidence
- Repeated trials and evidence-based decisions
- Team roles and technical communication
- Competition-style challenges
- Responsible use of AI coding tools
- Portfolio and final technical presentation/defense

## 36-Week Course Map

| Weeks | Phase | Focus |
|---|---|---|
| 1–2 | Onboarding | Safety, parts organization, classroom flow, mastery, engineering notebook |
| 3–6 | Foundations | V5 hardware + official TrainingBot build |
| 7–12 | Programming | Driver control, VEXcode/Python, programmed movement |
| 13–18 | Autonomy | Sensors, conditionals, feedback, autonomous behavior |
| 19–24 | Engineering | Mechanisms, gear ratios, iteration, competition-style challenge |
| 25–30 | Classical + CNN Bridge | OpenCV, HSV, masks, contours, object position + Andrew Ng CNN foundations |
| 31–33 | Modern CV + Intelligent Control | MobileNet, transfer learning, localization/detection, IoU/NMS/YOLO, embedded vision, vision → decision → robot action |
| 34–36 | Capstone | Integrated build, testing, demo and engineering defense |

Full detail: [pacing-guide.md](pacing-guide.md)

## Ready-to-Teach Lesson Anchors

The repository contains **26 anchor lessons** spanning the full 36-week course. These are not 26 total class periods; long build/project lessons intentionally span multiple meetings, with practice, rebuilding, debugging, assessment and iteration days between anchors.

Start here: **[lessons/README.md](lessons/README.md)**

### Unit 00 — Getting Started

- [Lesson 01 — Kit Safety and Parts](lessons/00-getting-started/lesson-01-kit-safety-and-parts.md)

### Unit 01 — TrainingBot

- [Lesson 02 — TrainingBot Build I: Chassis and Drivetrain](lessons/01-trainingbot/lesson-02-trainingbot-build-1.md)
- [Lesson 03 — TrainingBot Build II and First Power-On](lessons/01-trainingbot/lesson-03-trainingbot-build-2-and-first-power.md)

### Unit 02 — Driver Control and Programming

- [Lesson 04 — VEXcode and Device Configuration](lessons/02-driver-control/lesson-04-vexcode-and-device-configuration.md)
- [Lesson 05 — Python Motion, Variables and Functions](lessons/02-driver-control/lesson-05-python-motion-and-functions.md)
- [Lesson 06 — Controller Input: Tank Drive and Arcade Drive](lessons/02-driver-control/lesson-06-controller-tank-and-arcade-drive.md)
- [Lesson 07 — Driver Control Engineering Challenge](lessons/02-driver-control/lesson-07-driver-control-challenge.md)

### Unit 03 — Sensors and Autonomous Control

- [Lesson 08 — Sensor Data and Thresholds](lessons/03-sensors-autonomy/lesson-08-sensor-data-and-thresholds.md)
- [Lesson 09 — Distance Sensor: Obstacle Response](lessons/03-sensors-autonomy/lesson-09-distance-sensor-obstacle-response.md)
- [Lesson 10 — Inertial Sensor: Reliable Turning](lessons/03-sensors-autonomy/lesson-10-inertial-sensor-turning.md)
- [Lesson 11 — Autonomous State Sequence](lessons/03-sensors-autonomy/lesson-11-autonomous-state-sequence.md)
- [Lesson 12 — Autonomous Navigation Challenge](lessons/03-sensors-autonomy/lesson-12-autonomous-navigation-challenge.md)

### Unit 04 — Engineering Design and Mechanisms

- [Lesson 13 — Gear Ratio: Speed and Torque Trade-Offs](lessons/04-engineering-design/lesson-13-gear-ratio-speed-and-torque.md)
- [Lesson 14 — Manipulator Mechanism Prototype](lessons/04-engineering-design/lesson-14-manipulator-mechanism-prototype.md)
- [Lesson 15 — Engineering Iteration and Test Data](lessons/04-engineering-design/lesson-15-iteration-and-test-data.md)
- [Lesson 16 — Competition-Style Robot Challenge](lessons/04-engineering-design/lesson-16-competition-style-robot-challenge.md)

### Unit 05 — Computer Vision Foundations

- [Lesson 17 — Images as Data: Pixels and Color](lessons/05-computer-vision/lesson-17-images-pixels-and-color.md)
- [Lesson 18 — HSV Thresholding and Color Masks](lessons/05-computer-vision/lesson-18-hsv-thresholding-and-masks.md)
- [Lesson 19 — Contours, Bounding Boxes and Centroids](lessons/05-computer-vision/lesson-19-contours-bounding-boxes-centroids.md)
- [Lesson 20 — Color Object Detection Project](lessons/05-computer-vision/lesson-20-color-object-detection-project.md)

### Unit 06 — Modern AI Vision + Robotics Integration

- [Lesson 21 — Vision to Decision Logic](lessons/06-ai-robotics-integration/lesson-21-vision-to-decision-logic.md)
- [Lesson 22 — Closed-Loop Vision Alignment](lessons/06-ai-robotics-integration/lesson-22-closed-loop-vision-alignment.md)
- [Lesson 23 — Vision Robustness and Failure Modes](lessons/06-ai-robotics-integration/lesson-23-vision-robustness-and-failure-modes.md)

### Unit 07 — Capstone

- [Lesson 24 — Capstone Proposal and System Architecture](lessons/07-capstone/lesson-24-capstone-proposal-and-architecture.md)
- [Lesson 25 — Capstone Build, Integrate and Test](lessons/07-capstone/lesson-25-capstone-build-integrate-test.md)
- [Lesson 26 — Final Validation, Showcase and Engineering Defense](lessons/07-capstone/lesson-26-final-validation-showcase-and-defense.md)

## Classroom Execution Resources

The lesson sequence is supported by materials that can be used directly during class:

- [Classroom Learning Flow](classroom-learning-flow.md) — shared learning cycle plus the VEX engineering cycle
- [Mastery Levels](mastery-levels.md) — Levels 0–5 with robotics examples
- [Course Posters](public-documents/posters/README.md) — visible classroom references shared across the CS program
- [VEXcode V5 Python classroom examples](examples/vexcode-python/README.md) — small device-configuration-aware programming patterns rather than unexplained full solutions
- [Driver Control Test Sheet](student-handouts/driver-control-test-sheet.md) — baseline trials, diagnosis and controlled iteration
- [Sensor & Autonomous Test Sheet](student-handouts/sensor-autonomy-test-sheet.md) — raw measurements, threshold justification and 10-trial reliability testing
- [Engineering Notebook Guide](student-handouts/engineering-notebook-guide.md)
- [Team Engineering Notebook Template](student-handouts/engineering-notebook-template.md)
- [Individual Engineering Learning Log](student-handouts/individual-engineering-learning-log.md)
- [Engineering Test Record Template](student-handouts/test-record-template.md)
- [Robot Debugging Checklist](student-handouts/robot-debugging-checklist.md)
- [AI Use Policy](student-handouts/ai-use-policy.md)
- [Teacher Demonstration Playbook](teacher-notes/demo-playbook.md) — short predict/show/observe/explain demos for major concepts
- [90-Minute Lesson Template](teacher-notes/90-minute-lesson-template.md)
- [Hardware Preparation Checklist](teacher-notes/hardware-preparation-checklist.md)
- [Advanced Competition Extension Track](extensions/competition-track.md) — optional work for teams that master the core sequence early

## Major Performance Milestones

1. **TrainingBot Build & First Drive** — reliable hardware baseline
2. **Driver Control Challenge** — controller mapping + measured iteration
3. **Autonomous Navigation Challenge** — sensors + feedback + state logic
4. **Competition-Style Robot Challenge** — mechanisms + strategy + testing
5. **Color Object Detection Project** — complete OpenCV perception pipeline + classical-vs-CNN explanation
6. **Vision-Guided Robot Decision System** — perception → decision → action + modern object-detection concepts + robustness
7. **Final Integrated Capstone** — build + vision + control + evidence + defense

## Official Starting Resources

- VEX Team Freeze Tag STEM Lab: https://education.vex.com/stemlabs/v5/team-freeze-tag
- TrainingBot build lesson: https://education.vex.com/stemlabs/v5/team-freeze-tag/lesson-1-introduction/build
  - Choose **3D Build Instructions — Competition Kits**.
- VEX V5 build instructions: https://www.vexrobotics.com/v5/downloads/build-instructions
- VEXcode V5: https://codev5.vex.com/
- IBM Coursera — Introduction to Computer Vision and Image Processing: https://www.coursera.org/learn/introduction-computer-vision-watson-opencv
- DeepLearning.AI / Andrew Ng — Convolutional Neural Networks: https://www.coursera.org/learn/convolutional-neural-networks
- Edge Impulse — Computer Vision with Embedded Machine Learning: https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning
- Full curated resource list: [resources.md](resources.md)

## Assessment

- **Team Engineering Notebook + portfolio:** ongoing evidence of design, testing, debugging and iteration
- **Individual Engineering Learning Log + mastery checks:** evidence of each student's contribution and independence
- **Formative checks / quizzes:** hardware, programming, sensors, engineering, classical CV and modern CV concepts
- **Performance challenges:** robot performance + engineering process + technical explanation
- **Final capstone:** integrated system + testing + demonstration + defense

The **4-level project rubrics remain in place**. Mastery Levels 0–5 are an additional learning-independence framework, not a replacement grading scale.

See [assessment-plan.md](assessment-plan.md).

## Core Repository Files

```text
vex-robotics-and-computer-vision/
├── README.md
├── syllabus.md
├── course-overview.md
├── classroom-learning-flow.md
├── mastery-levels.md
├── pacing-guide.md
├── assessment-plan.md
├── portfolio-requirements.md
├── resources.md
├── lessons/
├── examples/
├── student-handouts/
│   ├── engineering-notebook-guide.md
│   ├── engineering-notebook-template.md
│   ├── individual-engineering-learning-log.md
│   └── test-record-template.md
├── teacher-notes/
├── assessments/
├── rubrics/
├── extensions/
└── public-documents/
    └── posters/
```

## AI Application Philosophy

The course treats AI as a **system capability that must be tested**, not as magic. Students repeatedly ask:

1. **What can the robot sense or see?**
2. **How is that information represented?**
3. **Is perception based on hand-written rules, learned features, or both?**
4. **What algorithm/model produces the perception output?**
5. **What decision logic converts perception into action?**
6. **Under what conditions does the system fail?**
7. **How can evidence guide the next design iteration?**

AI coding tools may support development, but students must understand, test, explain, document, and take responsibility for the work they submit.
