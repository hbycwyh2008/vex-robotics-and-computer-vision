# Lesson 06 — Controller Input: Tank Drive and Arcade Drive

## Course position
Weeks 10–11 · Driver Control and Robot Motion Programming

## Learning objectives
Students will be able to:
- read joystick/controller input as numerical data;
- map controller axes to drivetrain motor commands;
- implement and compare tank and arcade drive concepts;
- explain deadband and why noisy near-zero input matters;
- evaluate a control scheme using repeatable driving tasks.

## Core idea
The Controller is a sensor operated by a human. Joystick positions become input data. Code transforms that input into motor commands.

This is the first explicit classroom example of:

**Input → Decision / mapping → Action**

Later, camera and sensor data will replace or supplement human joystick input.

## Part A — Observe controller data
Before driving, inspect joystick axis values at:
- center;
- small displacement;
- half displacement;
- maximum displacement;
- positive and negative directions.

Discuss why centered sticks may not always behave like a mathematically perfect zero in real systems.

## Part B — Tank drive
Implement a tank-drive mapping in which the left and right joystick channels independently control the corresponding drivetrain sides.

Test:
- straight forward/backward;
- gradual turn;
- point turn;
- slow precision movement.

## Part C — Arcade drive
Implement or explore an arcade-style mapping based conceptually on:
- forward/backward command;
- turning command;
- combining those values into left/right drivetrain output.

Students should understand the mapping rather than merely selecting a preset.

## Part D — Deadband
Add a small deadband so tiny joystick values around center do not command unintended motor movement.

Students must justify the chosen threshold through observation.

## Driving test course
Compare tank and arcade control using the same course:
1. leave a start box;
2. pass between two markers;
3. make a controlled turn;
4. stop with the robot inside a target zone;
5. return.

Record completion time and control errors, but do not treat speed as the only measure of quality.

## Evaluation criteria
Rate each control scheme for:
- precision;
- ease of learning;
- turning control;
- low-speed maneuvering;
- driver preference.

## Evidence to submit
- controller mapping diagram;
- code/project evidence for both drive styles;
- deadband explanation;
- comparison table;
- recommendation: which control style should the team use now, and why?

## AI use
AI may explain joystick mapping mathematics or help students compare control strategies. Students must test all suggested mappings on the physical robot before accepting them.

## Extension
Investigate nonlinear joystick scaling. For example, how could a mapping provide finer low-speed control while still allowing maximum speed?

## Next lesson
Use the drivetrain in a scored driver-control challenge, collect performance data, and improve both code and driving technique.
