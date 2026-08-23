# Teacher Start Here — Ready-to-Teach Delivery Guide

Use this file if you need to teach the course without first redesigning the curriculum.

The repository has two layers:

1. **Anchor lessons** in `lessons/` explain the curriculum milestones and technical intent.
2. **Core meeting playbooks** in `teacher-notes/core-meeting-playbook/` turn the year into 72 directly teachable 90-minute meetings.

For normal delivery, teach from the **core meeting playbook** and open the matching anchor lesson only when you need the deeper technical explanation, project context, or resource links.

---

## Before the First Class

Complete these checks before students arrive:

- [ ] Confirm each team has a VEX V5 Competition Starter Kit or a documented equivalent parts set.
- [ ] Charge and label V5 batteries; verify chargers and safe charging/storage location.
- [ ] Confirm V5 Brain, Controller, Smart Motors, Smart Cables, tools, shafts, collars, spacers, gears and structural parts are available.
- [ ] Open VEXcode V5 on student devices and confirm a Brain can connect/download.
- [ ] Decide team size and assign the first role rotation.
- [ ] Prepare one Team Engineering Notebook per team.
- [ ] Prepare the Individual Engineering Learning Log for each student.
- [ ] Create or confirm the GitHub/Markdown portfolio workflow.
- [ ] Print or share `student-handouts/daily-engineering-lab-sheet.md`.
- [ ] Review `teacher-notes/hardware-preparation-checklist.md`.
- [ ] Review the Week 1 plans in `teacher-notes/core-meeting-playbook/weeks-01-09.md`.

Do **not** begin the year with a long syllabus lecture. The first meetings use poster inspection, kit investigation, sorting, safety decisions and evidence creation.

---

## What to Open Each Day

For each meeting, open these in this order:

1. `teacher-notes/core-meeting-playbook/` — minute-by-minute plan.
2. Matching file in `lessons/` — technical anchor and deeper notes.
3. Matching student handout/project brief.
4. `assessments/practical-checkpoints.md` when a checkpoint is scheduled.
5. `assessments/teacher-answer-key.md` when using quiz-bank questions.

For computer vision weeks also open:

- `teacher-notes/cv-coursera-viewing-guide.md`
- `resources.md`
- OpenCV documentation linked there.

---

## Standard 90-Minute Flow

Unless a meeting plan says otherwise, use:

| Time | Function |
|---:|---|
| 0–10 | Retrieval, prediction, failure case, safety/setup |
| 10–25 | Short focused learning/demo/video segment |
| 25–55 | Guided practice → reduced-support rebuild/application |
| 55–75 | Test → debug → modify → retest |
| 75–85 | Evidence, notebook, explanation/share |
| 85–90 | Exit mastery check + physical reset |

Direct instruction should normally be **15 minutes or less at a time**. The course is learned through building, programming, testing, discussion, comparison and explanation.

---

## Required Learning Flow

Across the whole course:

> **Learn → Practice → Rebuild → Share**

Robotics execution uses:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

A robot working once is not mastery. A team result is not automatic evidence of individual mastery.

---

## Two Meetings vs Three Meetings per Week

The core course is **72 meetings: Meeting A + Meeting B for 36 weeks**.

If you have a third meeting, use it for one of these purposes before adding new content:

1. rebuild without instructions;
2. repeated trials and reliability measurement;
3. debugging clinic;
4. practical/reassessment;
5. engineering notebook conference;
6. driver practice;
7. hardware repair;
8. advanced competition extension;
9. capstone iteration.

Do not consume every third meeting with extra curriculum. Robotics needs buffer capacity.

---

## Student Evidence Minimum

Every substantial work session should leave evidence of:

- goal;
- what was built/programmed/changed;
- test or observation;
- result or failure;
- diagnosis or explanation;
- next step.

Project sessions also require controlled retesting and an individual technical explanation.

Use:

- `student-handouts/daily-engineering-lab-sheet.md`
- `student-handouts/engineering-notebook-template.md`
- `student-handouts/individual-engineering-learning-log.md`
- `student-handouts/project-delivery-pack.md`

---

## Assessment Baseline

Use performance evidence first and quizzes second.

Suggested categories:

- Engineering evidence / portfolio: 20%
- Formative checks / quizzes: 15%
- Projects / engineering challenges: 40%
- Final integrated project: 20%
- Presentation / reflection: 5%

Practical checkpoints are in `assessments/practical-checkpoints.md`.

Quiz-bank answers and acceptable reasoning are in `assessments/teacher-answer-key.md`.

---

## Computer Vision / AI Sequence

The required conceptual order is:

> **pixels → classical OpenCV rules → contours/geometry → CNNs → learned object detection → embedded vision → robot decisions**

Required Coursera pathway:

1. **IBM — Introduction to Computer Vision and Image Processing** for digital-image/OpenCV foundations.
2. **DeepLearning.AI / Andrew Ng — Convolutional Neural Networks** as the required modern-CV bridge.
3. **Edge Impulse — Computer Vision with Embedded Machine Learning** for edge/robotics deployment thinking.

Students do not need to complete every Coursera programming assignment. The local robotics labs remain the main assessed work. Exact assigned videos and discussion prompts are in `teacher-notes/cv-coursera-viewing-guide.md`.

---

## If Hardware Fails

Do not lose the entire period. Move the affected team to one of these evidence-producing tasks:

- configuration/code review;
- fault diagnosis using the robot debugging checklist;
- saved sensor-data analysis;
- OpenCV work on laptop images/video;
- test-plan design;
- notebook reconstruction from same-day evidence only;
- subsystem explanation/rebuild planning.

See `teacher-notes/hardware-failure-continuity-plan.md`.

---

## Teacher Readiness Standard

A meeting is ready to teach when you can answer, before class:

1. What will students be able to do by the end?
2. What do I need physically/digitally prepared?
3. What will students do during the first 10 minutes?
4. What is the one focused concept/demo?
5. What will students build/program/test themselves?
6. What evidence will they submit?
7. What is the exit mastery check?
8. What will I do if hardware/software fails?

The core meeting playbook supplies those answers for the 72 guaranteed meetings.