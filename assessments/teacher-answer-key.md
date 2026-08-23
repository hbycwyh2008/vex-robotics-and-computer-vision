# Teacher Answer Key — Unit Quiz Bank

This key supports `unit-quizzes.md`. Accept equivalent technically correct wording. Require students to connect concepts to the robot/system when the prompt asks for reasoning.

---

## Unit 00–01 — VEX Foundations / TrainingBot

1. **Shaft / spacer / shaft collar:** shaft transmits/supports rotational motion; spacer maintains axial distance/position; shaft collar clamps to a shaft to prevent axial sliding.
2. **Power down before rewiring:** reduces risk of shorts, unintended motor motion, device damage and injury.
3. **Last known-correct step:** narrows the fault search; errors are more likely after that checkpoint and the build can be compared systematically.
4. **Poor drivetrain alignment signs:** wheels/shafts bind, robot does not roll freely, one side drags, frame twists, abnormal friction/noise, inconsistent straight driving.
5. **Document motor ports:** software configuration must match physical wiring; documentation makes troubleshooting/rebuild reproducible.

---

## Unit 02 — Driver Control and Programming

1. **Physical ↔ VEXcode match:** device type, port and relevant direction/configuration must represent the actual robot.
2. **Deadband:** ignores small joystick values/noise near center so the robot does not creep; too large makes control unresponsive around center.
3. **Tank vs arcade:** tank usually maps separate joystick axes to left/right drive; arcade combines forward/back and turn inputs to derive left/right motor commands.
4. **Functions:** encapsulate repeated behavior, improve readability, reduce duplication and make isolated testing/refactoring easier.
5. **Curves right:** mechanical example—right/left friction difference, wheel alignment, loose shaft; software example—different velocity/direction/config or wrong motor mapping. Accept any plausible paired hypotheses.
6. **One run insufficient:** cannot estimate consistency/reliability or separate luck/random variation from systematic performance.

---

## Unit 03 — Sensors and Autonomous Control

1. **Raw data vs threshold decision:** raw data is the measured value; thresholding converts measurement into a discrete condition/action rule.
2. **FP/FN:** FP = system claims condition/target when absent; FN = misses condition/target when present. Context-specific examples accepted.
3. **Open-loop vs feedback:** open-loop acts without measuring result during action; feedback uses measurements to adjust/stop based on current state/error.
4. **Overshoot 90°:** speed/inertia, delayed update, weak stop logic, calibration error, mechanical slip or aggressive control. Student should name mechanism, not just “sensor bad.”
5. **State transition:** defined change from one behavior/state to another when a condition/event is satisfied.
6. **Consistent start position:** controls a major variable so repeated trials are comparable and conclusions about changes are fair.

---

## Unit 04 — Engineering Design and Mechanisms

1. **Driver/driven gear:** driver receives input from motor/source; driven receives motion from driver.
2. **Gear reduction:** typically reduces output speed while increasing available torque (ignoring losses); inverse arrangement increases speed while reducing torque.
3. **Shaft support:** limits bending/wobble/misalignment, maintains gear/wheel engagement and improves consistency.
4. **Hypothesis:** must predict effect of a defined change with reasoning, e.g. “If we reduce turn speed, then heading overshoot will decrease because the robot has less momentum near the target.”
5. **One major variable:** helps attribute observed change to a cause; multiple simultaneous changes confound interpretation.
6. **Fastest not always best:** may reduce torque/control/reliability, increase overshoot or fail task constraints.

---

## Unit 05 — Computer Vision

1. **Digital image:** conceptually an array/grid of numerical pixel values, often with multiple color channels.
2. **HSV:** Hue = color family/angle; Saturation = color purity/intensity; Value = brightness.
3. **Binary mask:** classifies each pixel as meeting/not meeting the threshold rule (target-like vs not target-like).
4. **Contour:** boundary/connected-object representation derived from connected foreground regions in a binary image.
5. **Bounding box info:** x/y position, width, height, approximate size/area and center; can support relative position.
6. **False color detection causes:** lighting shift, similar-colored object/background, reflections, bad calibration, overly broad threshold, camera auto-exposure/white balance. One valid condition sufficient.

---

## Unit 06 — AI Robotics Integration

1. **Three layers:** perception → decision → action.
2. **Separate layers:** enables independent testing, safer logic, clearer interfaces and easier diagnosis of where a failure occurs.
3. **Center tolerance band:** avoids demanding exact pixel equality and reduces jitter/oscillation around center.
4. **Oscillation causes:** turn command too aggressive, tolerance too narrow, latency/noisy centroid, insufficient damping/hysteresis or delayed stop.
5. **Safe target-loss fallbacks:** stop; slow bounded search; return to neutral state; timeout; require reacquisition before movement. Any two justified safe behaviors.
6. **Stress testing:** exposes failures hidden by ideal demo conditions and provides evidence about operating limits/robustness.

---

## Unit 07 — Capstone

1. **Measurable requirement:** has observable pass/fail or quantitative criterion and test condition, not vague wording like “works well.”
2. **Requirement traceability:** mapping each requirement to design element/test/evidence so completion can be verified.
3. **Subsystem before integration:** isolates faults, confirms interfaces and prevents unknown failures from stacking.
4. **Limitation vs bug:** limitation is a known boundary/unsupported condition of the designed system; bug is unintended incorrect behavior relative to requirements/design.
5. **Reliability evidence:** repeated controlled trials across relevant conditions, including failures; one successful demo is not enough.
6. **AI disclosure:** tool/use purpose, meaningful suggestion/output incorporated, and how the student verified/tested/modified it.

---

# Scoring Suggestion

For short responses:

- **2 points:** correct concept + relevant robot/system reasoning/example.
- **1 point:** partly correct definition but missing mechanism/context or contains a minor misconception.
- **0 points:** incorrect, contradictory or no usable evidence of understanding.

For diagnostic questions, reward a **testable hypothesis + discriminating test** more than a long list of random possible causes.