# Course Overview — VEX Robotics and Computer Vision

## What This Course Is

A **full-year, 90-minute regular academic course** in hands-on robotics and AI vision for high school using the **VEX V5 Competition Starter Kit** as the standard hardware platform. Students build and maintain real robots, program them with VEXcode/Python, add sensors and autonomous behavior, solve engineering challenges, and then use OpenCV to give robotic systems a basic sense of sight.

The course culminates in an integrated system where students connect:

> **Perception → Decision → Robot Action**

## Course Length

- **36 academic weeks**
- **2–3 class meetings per week**
- **90 minutes per meeting**
- Approximately **72–108 class meetings**
- Approximately **108–162 instructional hours**
- Rough target: **70% robotics/engineering/control + 30% computer vision/AI application**

This is not paced as a club or short enrichment course. The schedule deliberately protects sustained laboratory time for building, programming, testing, failure analysis, redesign, documentation, and technical defense.

See [pacing-guide.md](pacing-guide.md) for the full-year sequence and 90-minute lesson architecture.

## Standard Hardware

Primary platform:

- **VEX V5 Competition Starter Kit**
- V5 Brain, Controller, Battery, Smart Motors, drivetrain hardware, structural components, fasteners, shafts and gears
- Course begins with the official **TrainingBot — Competition Kit** build

Computer vision may initially run from a laptop/webcam before integration with the robot. Camera/sensor choices can be adapted to available school hardware, but the robotics platform remains VEX V5.

## Shared Learning Culture

This course uses the same core learning language as the Full-Stack Web and AI course:

> **Learn → Practice → Rebuild → Share**

The goal is consistency across CS and engineering courses: following instructions or making something work once is the beginning of learning, not the end.

VEX Robotics applies the shared flow through an engineering-specific cycle:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

See [classroom-learning-flow.md](classroom-learning-flow.md).

## Mastery Levels 0–5

Students use the shared mastery language throughout the course:

- **Level 0 — Exposure**
- **Level 1 — Follow and make it work**
- **Level 2 — Explain while looking**
- **Level 3 — Rebuild with a checklist**
- **Level 4 — Rebuild independently**
- **Level 5 — Modify, debug, and transfer**

Mastery Levels describe **student independence with a skill**. They do not replace the existing 4-level project rubrics, which assess **quality of a particular project**.

See [mastery-levels.md](mastery-levels.md).

## Course Philosophy

- **Build first, theory as needed.** Concepts appear when students need them to make a system work.
- **Engineering, not assembly.** Following instructions is only the starting point; students must diagnose, test, redesign, and justify decisions.
- **Iteration is the point.** Failure, debugging, calibration, and re-testing are assessed engineering skills.
- **Program for understanding.** Students should be able to explain their control logic, not merely make the robot move.
- **Rebuild to prove learning.** Students increasingly reproduce important patterns with less support rather than relying on permanent step-by-step instructions.
- **Document while engineering.** Evidence is recorded during the process, not reconstructed at the end.
- **Separate team success from individual mastery.** A working team robot does not automatically prove that every student can explain or rebuild the relevant skill.
- **AI application thinking.** Students study perception, decision logic, limitations, and responsible AI-assisted development without requiring advanced ML mathematics.
- **Protect lab time.** In a 90-minute course, direct instruction is intentionally concise so students have enough uninterrupted time to build and test real systems.

## Engineering Evidence System

The course uses three connected evidence layers.

### 1. Team Engineering Notebook

The team documents the shared engineering process:

> **Goal → Design / Change → Test → Problem → Diagnosis → Decision → Retest → Next Step**

The notebook includes design sketches, configuration, code/commit references, test procedures, measurements, failures, debugging evidence, redesign decisions and next steps.

### 2. Individual Engineering Learning Log

Each student records:

- what they personally worked on;
- one engineering decision they understand;
- one problem and diagnosis;
- their specific contribution;
- what they can now explain or rebuild;
- their current Mastery Level and evidence.

### 3. Portfolio Evidence

Students curate major project evidence in GitHub/Markdown: code, photos/video, notebook evidence, test data, debugging stories, iteration and reflection.

See:

- [Engineering Notebook Guide](student-handouts/engineering-notebook-guide.md)
- [Team Engineering Notebook Template](student-handouts/engineering-notebook-template.md)
- [Individual Engineering Learning Log](student-handouts/individual-engineering-learning-log.md)
- [Engineering Test Record Template](student-handouts/test-record-template.md)
- [Portfolio Requirements](portfolio-requirements.md)

> **Build / Program → Test → Record → Explain**

If a claim involves reliability, accuracy or improvement, one successful run is not enough. Students should use repeated trials or controlled comparisons when appropriate.

## Standard 90-Minute Teaching Pattern

A typical technical meeting uses this rhythm:

1. **0–10 min — Retrieve / predict** — prior learning, safety, system inspection, or prediction.
2. **10–25 min — Focused demo / learn** — one new concept or debugging model.
3. **25–55 min — Guided practice → rebuild** — build/program with support, then reduce scaffolding.
4. **55–75 min — Test / debug / redesign / retest** — use evidence to make an engineering decision.
5. **75–85 min — Document / explain / share** — Team Engineering Notebook, Individual Learning Log when assigned, and technical explanation.
6. **85–90 min — Reset / exit** — restore the lab and answer one mastery-focused exit question.

Build days, challenge days, AI-vision labs, and practical assessments may adapt the timing while preserving the same learning logic.

Teachers can expand individual anchor lessons into specific meetings with [teacher-notes/90-minute-lesson-template.md](teacher-notes/90-minute-lesson-template.md).

## Engineering Teaching Cycle

Across individual meetings and multi-day projects, students repeatedly use:

1. **Phenomenon / Challenge** — observe a robot behavior or engineering problem.
2. **Prediction** — predict what will happen or propose a solution.
3. **Build / Program** — create or modify the system.
4. **Test** — use a defined procedure to create evidence.
5. **Debug** — use **Symptom → Hypothesis → Test → Evidence → Decision**.
6. **Redesign** — change hardware, logic, parameters, geometry, configuration, or test conditions for a reason.
7. **Retest** — repeat the relevant test and compare evidence.
8. **Document** — record evidence and decisions while the work is happening.
9. **Explain** — connect evidence to the engineering or programming concept.
10. **Transfer** — apply the pattern to a new constraint or challenge.

## Big Ideas Across the Course

- A robot is a system: structure, power, motors, sensors, code, and human decisions working together.
- Mechanical design involves trade-offs among strength, weight, speed, torque, friction, and reliability.
- Good robot code is modular, readable, testable, and designed around physical behavior.
- Sensors convert the physical world into data that software can use.
- Autonomous behavior requires sensing, decisions, actions, testing, and calibration.
- Engineering design turns constraints and evidence into improved solutions.
- Images are numerical data; computer vision extracts useful information from those numbers.
- AI perception can fail. Lighting, background, occlusion, calibration, and ambiguous inputs matter.
- AI-assisted coding is useful only when students understand, test, and can defend the resulting work.
- Team performance and individual mastery are related but not identical.

## Learning Path

```text
Safety + Parts + Learning Culture + Engineering Notebook
  → VEX V5 Foundations + TrainingBot
    → Driver Control + VEXcode/Python
      → Sensors + Measurement
        → Autonomous Robotics
          → Mechanical Design + Engineering Challenges
            → Competition-Style Robotics
              → OpenCV / AI Vision
                → Perception → Decision → Action
                  → Integrated Capstone
```

## What Students Will Build

Across the year, students progress through increasingly independent systems:

1. **TrainingBot** — correct construction, wiring, maintenance, and driver control
2. **Programmed Driving Robot** — precise movement and reusable code
3. **Sensor-Based Autonomous Robot** — feedback and conditional behavior
4. **Engineering Challenge Robot** — custom mechanism and iterative design
5. **Competition-Style Robot Challenge** — strategy, reliability, driver/autonomous performance
6. **Computer Vision System** — color/object detection with OpenCV
7. **Vision-Guided Robot System** — perception influences decisions and actions
8. **Capstone** — integrated robotics + AI/vision project with presentation and engineering defense

## Classroom Posters

The VEX course uses shared classroom visuals for:

- classroom flow;
- Mastery Levels;
- responsible AI use;
- CS/robotics competition pathways.

See [public-documents/posters/](public-documents/posters/README.md).

These shared posters establish common learning language; VEX-specific engineering evidence and testing expectations are defined in this repository.

## AI in This Course

AI is intentionally visible throughout the course rather than isolated into one final unit.

Students learn to:

- use AI coding tools responsibly for explanation, debugging, and iteration;
- verify generated code rather than copy it blindly;
- distinguish raw sensor/camera input from software interpretation;
- analyze why an intelligent system succeeds or fails;
- test systems across different physical conditions;
- explain the chain from perception to decision to action;
- consider privacy, reliability, bias/error, and human responsibility in AI-enabled systems.

The goal is to move students from **technology users** toward **technology creators who can explain, test, document, rebuild, and improve what they build**.
