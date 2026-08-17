# VEX Robotics, AI Vision, and Intelligent Control

A **36-week, project-based high school robotics course** built around the **VEX V5 Competition Starter Kit**. Students build and maintain real robots, program driver-controlled and autonomous behavior, solve engineering challenges, and then extend their systems with **OpenCV / AI vision**.

> Students do not just learn *about* robotics and AI. They **build, program, test, debug, redesign, and defend intelligent robotic systems.**

## Course Format

- **Length:** approximately 36 instructional weeks
- **Meetings:** 2–3 classes per week (approximately 72–108 periods)
- **Hardware:** VEX V5 Competition Starter Kit
- **First official build:** TrainingBot — Competition Kit
- **Programming:** VEXcode V5 + Python where appropriate
- **AI / Vision:** Python + OpenCV
- **Method:** project-based engineering, build–test–debug–iterate
- **Evidence:** engineering notebook + GitHub/Markdown portfolio

## Core Learning Path

```text
V5 hardware & safety
        ↓
TrainingBot — Competition Kit
        ↓
Controller driving + VEXcode
        ↓
Robot motion + modular programming
        ↓
Sensors + autonomous control
        ↓
Mechanisms + engineering challenges
        ↓
OpenCV / computer vision
        ↓
Perception → Decision → Action
        ↓
Integrated robotics + AI vision capstone
```

## What Students Learn

### Robotics Engineering

- VEX V5 structural components, fasteners, shafts, bearings, motors, Brain, battery, controller, and sensors
- Reliable drivetrain construction, wiring, maintenance, and troubleshooting
- Mechanisms, gear ratios, speed/torque trade-offs, iteration, and engineering constraints

### Programming and Control

- VEXcode V5
- Python-style computational thinking and modular programming
- Sequences, variables, functions, loops, conditionals
- Driver control and autonomous routines
- Sensor input, motor encoders, calibration, and feedback

### AI Vision

- Images and pixels
- RGB/BGR and HSV color spaces
- Thresholding and masks
- Contours, bounding boxes, and target position
- Vision-system testing and failure analysis
- Connecting perception to robot decisions and actions

### Engineering Practice

- Build → test → debug → redesign
- Engineering notebook evidence
- Team roles and technical communication
- Competition-style challenges
- Responsible use of AI coding tools
- Portfolio and final technical presentation

## 36-Week Course Map

| Weeks | Phase | Focus |
|---|---|---|
| 1–6 | Foundations | Safety, V5 hardware, parts management, official TrainingBot build |
| 7–12 | Programming | Driver control, VEXcode/Python, programmed movement |
| 13–18 | Autonomy | Sensors, conditionals, calibration, autonomous behavior |
| 19–24 | Engineering | Mechanisms, design process, competition-style robot challenges |
| 25–30 | AI Vision | OpenCV, HSV, masks, contours, object position |
| 31–33 | Intelligent Control | Vision → decision → robot action, robustness and limitations |
| 34–36 | Capstone | Integrated build, testing, demo, engineering defense |

Full detail: [pacing-guide.md](pacing-guide.md)

## Unit Map

| Unit | Title | Focus |
|---|---|---|
| [00](units/Unit%2000%20-%20Course%20Onboarding%20and%20Safety/unit-overview.md) | Course Onboarding and Safety | Safety, teams, notebook, GitHub |
| [01](units/Unit%2001%20-%20VEX%20Robotics%20Foundations/unit-overview.md) | VEX V5 Foundations and TrainingBot | Competition Kit components, drivetrain, build cycle |
| [02](units/Unit%2002%20-%20Programming%20Robot%20Motion/unit-overview.md) | Driver Control and Robot Motion | Movement, functions, controller programming |
| [03](units/Unit%2003%20-%20Sensors%20and%20Autonomous%20Control/unit-overview.md) | Sensors and Autonomous Control | Sensors, feedback, autonomy, calibration |
| [04](units/Unit%2004%20-%20Engineering%20Design%20and%20Robot%20Challenges/unit-overview.md) | Engineering Design and Robot Challenges | Mechanisms, strategy, iteration |
| [05](units/Unit%2005%20-%20Computer%20Vision%20Foundations/unit-overview.md) | Computer Vision Foundations | Pixels, HSV, masks, contours |
| [06](units/Unit%2006%20-%20Vision-Based%20Robot%20Decision%20Making/unit-overview.md) | AI Vision and Robot Decision Making | Perception → decision → action |
| [07](units/Unit%2007%20-%20Integrated%20Robotics%20and%20Vision%20Project/unit-overview.md) | Integrated Robotics + Vision Capstone | Final intelligent robotics project |

## Major Projects

1. **TrainingBot Build & Driver Challenge**
2. [Project 01 — Basic Driving Robot](projects/project-01-basic-driving-robot.md)
3. [Project 02 — Sensor-Based Autonomous Robot](projects/project-02-sensor-based-autonomous-robot.md)
4. [Project 03 — Robot Challenge Design](projects/project-03-robot-challenge-design.md)
5. [Project 04 — Color Object Detection with OpenCV](projects/project-04-color-object-detection-with-opencv.md)
6. [Project 05 — Vision-Guided Robot Decision System](projects/project-05-vision-guided-robot-decision-system.md)
7. [Final — Integrated Robotics and Vision](projects/final-project-integrated-robotics-and-vision.md)

## Official Starting Resources

- VEX Team Freeze Tag STEM Lab: https://education.vex.com/stemlabs/v5/team-freeze-tag
- TrainingBot build lesson: https://education.vex.com/stemlabs/v5/team-freeze-tag/lesson-1-introduction/build
  - Choose **3D Build Instructions — Competition Kits**.
- VEX V5 build instructions: https://www.vexrobotics.com/v5/downloads/build-instructions
- VEXcode V5: https://codev5.vex.com/
- Full curated resource list: [resources.md](resources.md)

## Assessment

- **Engineering notebook & portfolio:** ongoing evidence of design and debugging
- **Formative checks / quizzes:** hardware, programming, sensors, engineering, vision
- **Projects:** robot performance + engineering process + technical explanation
- **Final capstone:** integrated system + testing + demonstration + defense

See [assessment-plan.md](assessment-plan.md).

## Repository Structure

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
├── units/
├── lessons/
├── projects/
├── assessments/
├── rubrics/
├── student-handouts/
├── teacher-notes/
├── media/
└── examples/
```

## AI Application Philosophy

The course treats AI as a **system capability that must be tested**, not as magic. Students repeatedly ask:

1. **What can the robot sense or see?**
2. **How is that information represented?**
3. **What rule or algorithm makes the decision?**
4. **What action does the robot take?**
5. **Under what conditions does the system fail?**
6. **How can evidence guide the next design iteration?**

AI coding tools may support development, but students must understand, test, explain, and take responsibility for the work they submit.