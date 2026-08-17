# Lesson 09 — Distance Sensor: Obstacle Response

## Course position
Weeks 14–15 · Sensors and Autonomous Control

## Learning objectives
Students will be able to configure and read a VEX Distance Sensor, collect repeated measurements, implement a simple stop response, diagnose sensing versus control issues, and evaluate reliability through trials.

## Required resources
- TrainingBot or equivalent drivetrain
- VEX Distance Sensor if available
- VEXcode V5
- ruler or tape measure
- classroom test objects
- engineering notebook

## Launch question
If a robot should stop before reaching an object, why is one sensor reading not enough to prove that the system is reliable?

## Part A — Characterize the sensor
Place a target at several known distances and collect repeated readings.

Suggested distances: 10 cm, 20 cm, 30 cm and 50 cm.

Record the actual distance, sensor reading, error and any unusual values.

## Part B — Stop response
Program the robot to move forward at a conservative speed and stop when an object is detected within a chosen distance threshold.

Keep the logic separated into three steps:
1. read the sensor;
2. compare the reading with the threshold;
3. command the drivetrain.

## Part C — Reliability testing
Run at least 10 trials from a consistent start location. Record whether the robot stopped successfully and note any unusual result.

Then change one factor, such as speed or starting distance, and compare the results.

## Debugging questions
If the robot does not stop where expected, inspect:
- sensor reading quality;
- threshold choice;
- robot speed;
- program update rate;
- target position and surface;
- drivetrain stopping behavior.

## Evidence to submit
- measurement table;
- selected threshold and justification;
- code or pseudocode;
- reliability result from repeated trials;
- explanation of one observed limitation.

## AI connection
The robot now has machine perception of a simple physical property: distance. It converts perception into a decision and then an action.

## AI use
AI may suggest hypotheses for unexpected behavior, but students must verify each hypothesis with physical measurements and tests.

## Next lesson
Use orientation feedback from the Inertial Sensor to improve turning consistency.
