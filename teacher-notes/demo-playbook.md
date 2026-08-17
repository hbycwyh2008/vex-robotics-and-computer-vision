# Teacher Demonstration Playbook

Use short demonstrations to expose one idea, then move students quickly into physical testing. Avoid turning robotics class into long lectures.

## Recommended demo structure (8–15 minutes)

1. **Predict** — ask students what they expect.
2. **Show** — run one controlled demonstration.
3. **Observe** — students state what actually happened.
4. **Explain** — introduce the technical concept.
5. **Change one variable** — run a comparison.
6. **Release to teams** — students reproduce and extend it.

## Demo 1 — Mechanical fault vs software fault

Purpose: establish layered debugging.

Prepare a robot with one visible/reversible configuration or connection problem. Ask students not to touch code first. Work through:

physical structure → cable → port map → device configuration → program logic.

Key message: changing code cannot repair a mechanical transmission problem.

## Demo 2 — Same code, imperfect physical motion

Run the same straight/turn routine several times from a marked start pose. Mark endpoints.

Discuss friction, battery condition, wheel slip, mechanical alignment and accumulated error.

Key message: a physical robot is not a perfect mathematical simulator.

## Demo 3 — Controller deadband

Display or observe joystick values near center. Compare control with and without a small deadband.

Key message: real input data can contain small unwanted variation.

## Demo 4 — Open loop vs feedback

First execute a turn using a fixed command/timing approach. Then use orientation feedback.

Collect several final-angle measurements for each method.

Key message: feedback uses the current measured state rather than assuming the robot behaved as predicted.

## Demo 5 — Sensor threshold

Show several readings for two physical conditions. Ask students to propose a threshold before revealing a teacher choice.

Then deliberately test a borderline case.

Key message: perception and decision are different stages; thresholds have failure cases.

## Demo 6 — Gear ratio trade-off

Use two gear configurations or a teacher-prepared mechanism. Compare speed and load-handling using the same test procedure.

Key message: engineering design is constrained optimization, not maximizing one number.

## Demo 7 — Computer vision under changing light

Show the same colored object under two lighting conditions. Compare raw image and mask.

Key message: a detector that works once is not yet a reliable perception system.

## Demo 8 — Perception → Decision → Action

Move a detected target left, center and right in the camera image. Show the resulting symbolic decision before connecting it to robot motion.

Key message: keep perception, decision and action separable so each layer can be tested.

## Demo discipline

- Never introduce several new hardware/software variables simultaneously.
- Record at least one measurement when making a reliability claim.
- Preserve a known-working baseline project before demonstrations.
- If a demo fails, use the failure as a debugging demonstration rather than hiding it.
- Require students to predict before they copy the teacher's solution.