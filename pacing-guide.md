# Pacing Guide — 36-Week Full-Year Course

This is a **regular academic course**, not an after-school club. It is designed for approximately **36 instructional weeks**, meeting **2–3 times per week**, with **90 minutes per class**.

That provides approximately:

- **72–108 class meetings** per year;
- **108–162 instructional hours**;
- enough time for sustained building, programming, rebuilding, failure analysis, redesign, driver practice, assessment, documentation, classical computer vision, required modern-CV video study, AI/robotics integration, and a substantial capstone.

The course uses the **VEX V5 Competition Starter Kit** as the standard hardware platform. Students begin with the official **TrainingBot — Competition Kit** pathway before progressing to custom mechanisms, autonomous control, and computer vision.

## Shared Learning Framework

Across the year, students use:

> **Learn → Practice → Rebuild → Share**

and the VEX engineering cycle:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

Teachers should not advance simply because a robot or program worked once. Pacing should protect time for students to explain, rebuild, test, debug, and document important skills.

See:

- [classroom-learning-flow.md](classroom-learning-flow.md)
- [mastery-levels.md](mastery-levels.md)

---

## Computer Vision Resource Rule

The CV portion uses **selected external videos mapped directly to local lessons**, not an expectation that students complete entire Coursera courses independently.

Required progression:

1. **IBM — Introduction to Computer Vision and Image Processing** for digital-image/OpenCV foundations.
2. **OpenCV official documentation** for HSV, thresholding, masks and contours.
3. **DeepLearning.AI / Andrew Ng — Convolutional Neural Networks** as the required modern-CV bridge: convolution, pooling, MobileNet, transfer learning, localization, IoU, NMS and YOLO.
4. **Edge Impulse — Computer Vision with Embedded Machine Learning** for embedded deployment and object-detection context.

See [resources.md](resources.md) for the exact video-to-lesson mapping.

---

## Full-Year Sequence

| Weeks | Unit | Focus | Major Evidence / Deliverable |
|---|---|---|---|
| 1–2 | Unit 00 | Course orientation, shared posters/flow, Mastery Levels, lab safety, parts organization, Team Engineering Notebook, Individual Learning Log, GitHub | Lab-ready team + first team notebook + first individual mastery evidence + portfolio setup |
| 3–4 | Unit 01 | V5 Competition Starter Kit orientation; structure, fasteners, shafts, bearings, motors, Brain, battery, controller | Hardware identification + build skills check |
| 5–6 | Unit 01 | Official TrainingBot build; guided build → explain → rebuild/check → test/debug cycle | Working TrainingBot + build log + mastery evidence |
| 7–8 | Unit 02 | Controller setup, drivetrain configuration, tank/arcade driving, driver practice | Driver-control challenge + measured trials |
| 9–10 | Unit 02 | VEXcode / Python foundations: sequence, variables, functions, loops | Programmed movement challenges + rebuild checks |
| 11–12 | Unit 02 | Precise movement, motor encoders, reusable movement functions | **Project 01: Basic Driving Robot** |
| 13–14 | Unit 03 | Sensors: bumper, distance, motor position/encoder, Inertial Sensor | Sensor investigation notebook + individual explanation |
| 15–16 | Unit 03 | Conditionals, feedback, calibration, autonomous routines | Autonomous navigation challenge |
| 17–18 | Unit 03 | Testing reliability and systematic debugging | **Project 02: Sensor-Based Autonomous Robot** + repeated validation |
| 19–20 | Unit 04 | Engineering design process; mechanisms, gear ratio, torque/speed trade-offs | Mechanism prototype + design review |
| 21–22 | Unit 04 | Intake/lift/manipulator concepts; iteration and constraints | Mechanism challenge + redesign/retest evidence |
| 23–24 | Unit 04 | Competition-style strategy, driver skills, autonomous strategy | **Project 03: Robot Challenge Design** |
| 25–26 | Unit 05 | Images, pixels, RGB/BGR, camera input + selected IBM Coursera image-processing videos | First OpenCV camera/image program + pixel/channel explanation |
| 27–28 | Unit 05 | HSV, thresholding, masks, morphology, lighting/calibration + OpenCV docs; begin Andrew Ng edge-detection bridge | Color segmentation investigation + controlled comparison |
| 29–30 | Unit 05 | Contours, bounding boxes, centroids, target position; complete classical detector; Andrew Ng CNN foundations | **Project 04: Color Object Detection** + classical-vs-CNN comparison |
| 31 | Unit 06 | Andrew Ng MobileNet, transfer learning, data augmentation; Edge Impulse embedded-vision bridge; perception → decision → action | Vision decision prototype + classical/learned perception architecture diagram |
| 32 | Unit 06 | Andrew Ng object localization/detection, bounding boxes, IoU, NMS, anchor boxes, YOLO; closed-loop alignment | Closed-loop vision alignment + modern object-detection concept check |
| 33 | Unit 06 | Classical vs learned vision robustness, domain shift, false detections, deployment constraints, responsible AI | **Project 05: Vision-Guided Decision System** + robustness evidence |
| 34 | Unit 07 | Capstone proposal, requirements, system architecture | Approved capstone plan + test plan |
| 35 | Unit 07 | Build, integrate, test, debug, collect evidence | Working capstone prototype + documented iteration |
| 36 | Unit 07 | Final validation, demo, individual engineering defense, portfolio cleanup, reflection | **Final Integrated Robotics + Vision Project** |

---

## Standard 90-Minute Lesson Architecture

A normal technical lesson should reserve most of the period for active engineering.

| Time | Phase | Typical activity |
|---:|---|---|
| 0–10 min | Entry / retrieval / predict | Safety check, prior-learning retrieval, prediction, quick hardware/code inspection |
| 10–25 min | Learn / focused demo | One concept, selected video segment, worked example, physical demonstration, or debugging model |
| 25–55 min | Practice → rebuild | Guided work followed by reduced scaffolding or an independent engineering task |
| 55–75 min | Test / debug / redesign / retest | Controlled tests, diagnosis, evidence-based change, comparison |
| 75–85 min | Document / explain / share | Team Engineering Notebook, Individual Learning Log when assigned, technical explanation |
| 85–90 min | Reset / exit | Parts reset, battery/cable check, mastery-focused exit ticket |

This is a **default architecture**, not a rigid script. Lab, testing, or rebuild blocks should expand when the task requires it.

Use [teacher-notes/90-minute-lesson-template.md](teacher-notes/90-minute-lesson-template.md) to expand anchor lessons into actual class meetings.

---

## 90-Minute Lesson Variants

### Build Day

- 0–10: setup + retrieval + build target
- 10–20: focused teacher demonstration / common assembly risk
- 20–55: guided build and practice
- 55–72: reduced-support rebuild/check, alignment test, or subsystem validation
- 72–85: quality-control inspection + Team Engineering Notebook + individual explanation if assigned
- 85–90: parts/tool reset + exit

### Programming / Control Day

- 0–10: retrieval / predict program behavior
- 10–25: code demonstration
- 25–55: guided implementation → reduced-support rebuild
- 55–75: controlled tests / debugging / measurement / comparison
- 75–85: commit/save + notebook + individual learning evidence
- 85–90: reset + mastery check

### Engineering Challenge Day

- 0–10: requirements + scoring + safety
- 10–20: team plan / baseline prediction
- 20–68: repeated **test → debug → modify → retest** cycles
- 68–78: final measured trials / comparison
- 78–85: engineering decision + notebook + individual contribution evidence
- 85–90: reset + exit

### Computer Vision / AI Day

- 0–10: retrieval + failure-case image/video
- 10–25: selected Coursera segment / OpenCV concept / focused discussion; avoid passive long-form viewing
- 25–55: coding, image experiment, concept reconstruction, or robot integration task
- 55–75: robustness testing under changed conditions or classical-vs-learned comparison
- 75–85: evidence + AI-use disclosure + technical explanation
- 85–90: exit mastery check

For Andrew Ng material, students should repeatedly connect the video idea to something already visible in their own system: edge/filter, bounding box, target center, false detection, latency, or robot response.

### Assessment / Engineering Defense Day

- 0–10: setup and criteria review
- 10–60: performance test / practical assessment
- 60–80: individual technical explanation, rebuild/debugging/transfer check, or engineering defense
- 80–90: evidence submission and reset

---

## Recommended Weekly Rhythm

### Three 90-minute meetings

1. **Learn + investigation** — establish the engineering/computing idea through a short demo, selected video segment and controlled experiment.
2. **Practice + rebuild + test** — sustained production, reduced scaffolding, debugging and validation.
3. **Challenge + iteration + evidence** — measured performance, redesign, retest, notebook evidence, individual mastery check, or technical explanation.

### Two 90-minute meetings

1. **Learn + guided practice + substantial lab** — keep direct instruction/video short enough to preserve a meaningful engineering block.
2. **Rebuild + challenge + debugging + evidence** — apply the concept with less support, test reliability, and document decisions.

Do not eliminate the testing/iteration or rebuild opportunities merely to cover more content.

---

## Anchor Lessons vs Actual Class Meetings

The repository's **26 anchor lessons are curriculum milestones**, not a claim that the year contains only 26 lessons. A 90-minute full-year course should use anchor lessons to organize approximately 72–108 actual meetings.

Additional meetings are intentionally used for:

- course orientation and poster/mastery routines;
- TrainingBot build continuation;
- mechanical skill practice;
- rebuild checks;
- VEXcode practice;
- driver training;
- autonomous reliability testing;
- mechanism prototyping;
- redesign after failure;
- quizzes/practicals;
- Team Engineering Notebook conferences;
- Individual Engineering Learning Log / mastery conferences;
- competition-style challenge rounds;
- OpenCV coding labs;
- selected IBM / Andrew Ng / Edge Impulse video discussions;
- CNN/object-detection concept reconstruction;
- computer-vision robustness experiments;
- capstone integration;
- catch-up / hardware repair;
- final portfolio and technical defense.

A useful planning target is **80–90 explicitly planned 90-minute meetings**, while retaining the remaining calendar capacity as controlled buffers, reteaching, reassessment, extended challenges, and capstone iteration.

---

## Year-at-a-Glance

- **Weeks 1–2:** Learning culture + safety + VEX kit + engineering evidence routines
- **Weeks 3–6:** VEX V5 foundations + official TrainingBot
- **Weeks 7–12:** Driver control + VEXcode/Python motion programming
- **Weeks 13–18:** Sensors + autonomous robotics
- **Weeks 19–24:** Engineering design + mechanisms + competition-style challenges
- **Weeks 25–30:** Classical OpenCV foundations + transition into Andrew Ng CNN foundations
- **Weeks 31–33:** Modern CV concepts + embedded-vision context + vision-based decision making and intelligent control
- **Weeks 34–36:** Integrated capstone + showcase

---

## Checkpoints

| Checkpoint | By end of | Requirement |
|---|---|---|
| C1: Course/lab ready | Week 2 | Safety + posters/flow + mastery language + Team Notebook + Individual Log + GitHub ready |
| C2: TrainingBot works | Week 6 | Correct build, wiring, controller operation + explanation/rebuild evidence |
| C3: Programmed driving | Week 12 | Project 01 complete + core programming mastery evidence |
| C4: Autonomous behavior | Week 18 | Project 02 complete + reliability/debugging evidence |
| C5: Engineering challenge | Week 24 | Project 03 complete + redesign/retest evidence |
| C6: Classical vision + CNN bridge | Week 30 | Project 04 complete + varied-condition testing + explain hand-designed pipeline vs learned CNN features |
| C7: Vision drives decisions | Week 33 | Project 05 complete + explain MobileNet/transfer learning/localization/IoU/NMS/YOLO + robustness evidence |
| C8: Final showcase | Week 36 | Capstone + validation + individual defense + portfolio |

---

## Teacher Pacing Notes

- Treat each 90-minute meeting as a substantial lab period; avoid filling it with lecture or passive video watching.
- Use the local course posters in [`public-documents/posters/`](public-documents/posters/README.md) as recurring visual references, not as one-time decorations.
- Do **not** rush the TrainingBot build. Students should learn correct fastening, alignment, wiring, maintenance, explanation, and systematic diagnosis rather than merely copy assembly steps.
- Preserve rebuild time. A guided success should be followed later by an opportunity to reproduce the important pattern with less support.
- Preserve iteration time. A robot that fails and is debugged carefully is often more valuable than a build that works immediately.
- Keep the course primarily robotics engineering. A useful target is roughly **70% robotics / control / engineering** and **30% computer vision / AI application**.
- The Andrew Ng component is required, but it should be integrated through selected videos and discussion/application tasks rather than displacing the physical robotics work.
- Computer vision work can run on laptops while robot hardware is shared.
- Use buffer meetings after major builds and before showcases for hardware failures, absent students, redesign, reassessment, and mastery checks.
- Advanced teams can use the competition extension track rather than accelerating the entire class prematurely.
