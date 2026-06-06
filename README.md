# VEX Robotics and Computer Vision

A project-based high school course where students build, program, and debug real robots — then teach those robots to *see* using introductory computer vision. The course connects hands-on robotics engineering with AI application thinking, without turning into a deep machine learning course.

> Students don't just learn about robots and AI. They **build robots, program behavior, and make a robot act on what a camera sees.**

---

## Course Purpose

Give students a practical, portfolio-ready pathway through:

- Robot building, wiring, and the build–test–debug cycle
- Programming robot motion, functions, and driver control
- Sensors and autonomous decision making
- The engineering design process and robot challenges
- Computer vision foundations with OpenCV
- Vision-based robot decision making
- Documentation, GitHub/Markdown portfolios, and final presentations

## Target Students

High school students in a CS / AI pathway. No robotics experience required. Some prior programming exposure is helpful but not required — programming concepts are taught with Python-style pseudocode and VEXcode.

## Course Outcomes

By the end of the course, students can:

1. Build and wire a working VEX robot and keep an engineering notebook.
2. Program robot motion using functions and modular code.
3. Use sensors to make a robot act autonomously.
4. Apply the engineering design cycle to a robot challenge.
5. Process images with OpenCV (color, thresholding, contours).
6. Connect a vision result to a robot decision.
7. Document work in a GitHub/Markdown portfolio and present a final project.

---

## Course Map

### Unit Map

| Unit | Title | Focus |
|---|---|---|
| [00](units/Unit%2000%20-%20Course%20Onboarding%20and%20Safety/unit-overview.md) | Course Onboarding and Safety | Safety, teams, notebook, GitHub |
| [01](units/Unit%2001%20-%20VEX%20Robotics%20Foundations/unit-overview.md) | VEX Robotics Foundations | Components, drivetrain, build cycle |
| [02](units/Unit%2002%20-%20Programming%20Robot%20Motion/unit-overview.md) | Programming Robot Motion | Movement, functions, driver control |
| [03](units/Unit%2003%20-%20Sensors%20and%20Autonomous%20Control/unit-overview.md) | Sensors and Autonomous Control | Sensors, autonomy, calibration |
| [04](units/Unit%2004%20-%20Engineering%20Design%20and%20Robot%20Challenges/unit-overview.md) | Engineering Design and Robot Challenges | Design cycle, strategy, iteration |
| [05](units/Unit%2005%20-%20Computer%20Vision%20Foundations/unit-overview.md) | Computer Vision Foundations | Pixels, HSV, contours |
| [06](units/Unit%2006%20-%20Vision-Based%20Robot%20Decision%20Making/unit-overview.md) | Vision-Based Robot Decision Making | Vision → action, tracking, limits |
| [07](units/Unit%2007%20-%20Integrated%20Robotics%20and%20Vision%20Project/unit-overview.md) | Integrated Robotics and Vision Project | Final integrated project |

### Project Map

| Project | Title | Unit Link |
|---|---|---|
| [01](projects/project-01-basic-driving-robot.md) | Basic Driving Robot | Unit 02 |
| [02](projects/project-02-sensor-based-autonomous-robot.md) | Sensor-Based Autonomous Robot | Unit 03 |
| [03](projects/project-03-robot-challenge-design.md) | Robot Challenge Design | Unit 04 |
| [04](projects/project-04-color-object-detection-with-opencv.md) | Color Object Detection with OpenCV | Unit 05 |
| [05](projects/project-05-vision-guided-robot-decision-system.md) | Vision-Guided Robot Decision System | Unit 06 |
| [Final](projects/final-project-integrated-robotics-and-vision.md) | Integrated Robotics and Vision | Unit 07 |

### Assessment Overview

- **Formative checks** — quick in-class checks (see [assessments/formative-checks.md](assessments/formative-checks.md)).
- **Unit quizzes** — short concept checks (see [assessments/unit-quizzes.md](assessments/unit-quizzes.md)).
- **Project assessments** — graded with [rubrics/](rubrics/).
- **Final assessment** — final integrated project + presentation.
- Full plan: [assessment-plan.md](assessment-plan.md).

---

## Folder Structure

```text
vex-robotics-and-computer-vision/
├── README.md
├── syllabus.md
├── course-overview.md
├── pacing-guide.md
├── assessment-plan.md
├── portfolio-requirements.md
├── resources.md
├── lesson-template.md
├── project-template.md
├── units/                # 8 unit folders, each with 6 planning files
├── lessons/              # 24 ready-to-teach lessons
├── projects/             # 6 project briefs
├── assessments/          # formative, quizzes, project, final
├── rubrics/              # 6 four-level rubrics
├── student-handouts/     # safety, notebook, portfolio, debugging guides
├── teacher-notes/        # hardware, management, errors, differentiation
├── media/                # images, diagrams, screenshots
└── examples/             # exemplar student work
```

---

## How Students Use This Course

1. Start with [syllabus.md](syllabus.md) and the safety handout in [student-handouts/](student-handouts/).
2. Set up your engineering notebook and GitHub/Markdown portfolio (Unit 00).
3. Follow lessons in [lessons/](lessons/) in order.
4. Build the projects in [projects/](projects/) and save evidence to your portfolio.
5. Use the debugging checklists when robots or vision code misbehave.
6. Present your final integrated project.

## How Teachers Use This Course

1. Read [course-overview.md](course-overview.md) and [pacing-guide.md](pacing-guide.md).
2. Prepare hardware using [teacher-notes/hardware-preparation-checklist.md](teacher-notes/hardware-preparation-checklist.md).
3. Teach unit by unit using the unit folders and [lessons/](lessons/).
4. Grade with [rubrics/](rubrics/) and track progress with [assessments/](assessments/).
5. Adapt placeholders to your school's equipment and policies.

> Edit any document to match your VEX hardware (V5 or IQ), schedule, and school policies. Placeholders are marked where school-specific info is needed.

## AI Application Connection

This course treats computer vision as an **AI application**: a robot uses a camera to perceive, then decides and acts. Students discuss responsible AI use, the limits of perception systems, and where AI helps vs. where it fails — without needing to train machine learning models. See [resources.md](resources.md#ai-literacy-connections).
