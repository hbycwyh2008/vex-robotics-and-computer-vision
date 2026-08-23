# Project Delivery Pack — Student Version

Use this document for the major course projects. Your teacher may add local constraints, but the evidence rules below are the default minimum.

## Common Rules for Every Project

A project is **not complete** because it worked once.

Every project submission must include:

1. **Goal / requirements** — what the system must do.
2. **Design / architecture** — mechanism, code structure, state diagram or vision pipeline as appropriate.
3. **Final code/configuration** — committed version used for validation.
4. **Test plan** — conditions, start state, measurements and minimum trials.
5. **Raw results** — include failures; do not submit only the best run.
6. **Debugging/iteration evidence** — at least one meaningful diagnosis or justified change.
7. **Final validation** — repeated trials after the final material change.
8. **Limitation** — one thing the system cannot yet do reliably.
9. **Individual contribution** — what each member personally did and understands.
10. **AI disclosure** — what AI assisted with and how suggestions were verified.

If you materially change hardware/code after validation, the affected validation must be repeated.

---

# Project 01 — Basic Driving Robot

## Goal
Build/configure/program a VEX robot that can be driven reliably and execute a teacher-defined programmed movement task.

## Required Capabilities
- verified device/port configuration;
- safe controller operation;
- tank or arcade drive (teacher specifies required mode); 
- deadband or another justified method for preventing unintended joystick drift;
- reusable movement code/functions;
- readable variables/functions and meaningful commit history;
- consistent physical start procedure.

## Validation Minimum
- at least **5 repeated driver/control trials** on the same course or task;
- at least **5 repeated programmed-motion trials** if programmed movement is assessed;
- record failures and drift/error, not only success.

## Definition of Done
You can explain one mechanical, one configuration/software and one driver-related cause of poor motion and show how your team tested at least one real issue.

## Individual Defense
Be ready to:
- trace a motor from physical port to software config;
- explain tank vs arcade mapping;
- explain deadband;
- explain one movement function;
- diagnose a curved-drive symptom.

---

# Project 02 — Sensor-Based Autonomous Robot

## Goal
Use sensor input and explicit decision/state logic to complete a teacher-defined autonomous task safely.

## Required Capabilities
- raw sensor values collected before threshold choice;
- justified threshold/calibration;
- clear conditionals or state transitions;
- safe default/fallback behavior;
- at least one feedback-based behavior where appropriate;
- state diagram/transition table;
- controlled start position and test procedure.

## Validation Minimum
- at least **10 final autonomous trials** across the required conditions;
- report success count/rate;
- document at least one failure category;
- if using a threshold classifier, discuss false positive/false negative risk.

## Definition of Done
The robot's autonomous decisions can be explained as:

> sensor input → processing/threshold → state/decision → action → new measurement

## Individual Defense
Be ready to explain raw data vs threshold, open-loop vs feedback, calibration, one state transition and one debugging chain.

---

# Project 03 — Engineering Robot Challenge

## Goal
Design or improve a mechanism/robot strategy to solve a measurable physical challenge under constraints.

## Required Capabilities
- measurable requirements;
- at least two design concepts considered;
- justified mechanism/gear/support choices;
- baseline performance;
- one evidence-based redesign;
- final repeated trials;
- trade-off statement (speed, torque, reliability, weight, complexity, driver workload, etc.).

## Validation Minimum
- at least **5 baseline trials** before the main redesign when feasible;
- at least **5 comparable retest trials** after the change;
- same major test conditions for fair comparison.

## Definition of Done
Your team can show a chain:

> requirement → baseline → failure/bottleneck → hypothesis → design change → retest → decision

## Individual Defense
Be ready to identify force/motion path, explain gear-ratio trade-off, diagnose structural weakness and defend the fairness of your test.

---

# Project 04 — Color Object Detection with OpenCV

## Goal
Build a transparent rule-based vision pipeline that detects a teacher-approved target and outputs information a robot could use.

## Required Pipeline
1. image/camera input;
2. BGR → HSV;
3. threshold mask;
4. justified cleanup if needed;
5. contour detection;
6. noise filtering;
7. target-selection rule;
8. bounding box/centroid;
9. structured output such as found/not-found and left/center/right;
10. visual annotation for debugging.

## Validation Minimum
At least **20 labeled test cases/trials/frames** distributed across:
- normal condition;
- changed lighting;
- changed distance;
- clutter/background challenge;
- target absent;
- one additional stress condition such as partial occlusion or similar color.

Track at minimum:
- expected target present/absent;
- program result;
- correct/incorrect;
- false positive count;
- false negative count.

## Definition of Done
You can identify the first pipeline stage responsible for one real failure and explain why widening/narrowing a threshold creates a trade-off.

## Required Modern-CV Comparison
After the classical detector, explain how a CNN/learned detector differs: who chooses features, data needs, compute, interpretability and failure modes.

---

# Project 05 — Vision-Guided Robot Decision System

## Goal
Connect perception to safe robot decisions/actions using a clean interface and validate the integrated system under stress.

## Required Architecture

> perception → structured output → decision state → bounded robot action → new perception

Required states should include a safe **NO_TARGET / uncertain** behavior.

## Required Capabilities
- target left/center/right or equivalent structured perception;
- decision table;
- offline/mock decision tests before motor integration;
- safe speed/stop behavior;
- target-loss fallback;
- repeated alignment/decision trials;
- stress testing.

## Validation Minimum
At least **12 integrated trials**, including:
- normal condition;
- target initially left;
- target initially right;
- target centered;
- target absent/lost;
- at least two stress conditions.

Record overshoot/oscillation/target-loss or other relevant error.

## Definition of Done
The robot fails safely when perception is missing/uncertain and your team can classify a failure as perception, decision, control/integration or mechanical.

---

# Final Capstone — Integrated Robotics + Vision

## Goal
Design, build and defend a complete system that integrates meaningful robotics engineering with visual perception or another teacher-approved intelligent sensing approach.

## Proposal Must Include
- problem/context;
- measurable requirements;
- constraints;
- system architecture;
- classical CV vs learned CV vs hybrid choice and justification;
- subsystem interfaces;
- test plan mapped to requirements;
- top risks;
- minimum viable demo;
- optional stretch feature.

## Validation Minimum
- every requirement has an explicit test/evidence link;
- every performance/reliability claim uses repeated trials;
- at least one non-ideal/stress condition is included;
- final validation is run on the frozen final version;
- limitations are stated honestly.

## Final Presentation
Explain:
1. problem and requirements;
2. architecture;
3. key engineering decisions;
4. live behavior/demonstration;
5. validation evidence;
6. important failure/debugging example;
7. limitation and next improvement;
8. AI-use disclosure.

Every team member completes an individual technical defense.