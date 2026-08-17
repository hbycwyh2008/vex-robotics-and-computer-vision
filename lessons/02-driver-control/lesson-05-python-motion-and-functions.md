# Lesson 05 — Python Motion, Variables and Functions

## Course position
Weeks 9–10 · Driver Control and Robot Motion Programming

## Learning objectives
Students will be able to:
- connect Python statements to physical robot actions;
- control speed, direction and stopping behavior;
- use variables to make motion parameters easier to change;
- create reusable functions for repeated robot behaviors;
- test motion empirically rather than assuming commands produce perfect geometry.

## Concept bridge
Students may already know Python as text on a screen. Robotics changes the feedback loop:

**code → electrical command → motor rotation → mechanical motion → observed result**

Physical systems introduce friction, battery state, wheel slip and mechanical variation.

## Hands-on mission
### Mission 1 — Controlled straight motion
Program the robot to:
1. start at a marked line;
2. drive forward at a chosen speed;
3. stop after a defined motion condition supported by the current VEXcode setup;
4. repeat three trials.

Record whether the endpoint is consistent.

### Mission 2 — Parameter experiment
Create variables for at least:
- drive speed;
- turn speed;
- one distance/time/rotation parameter used by the program.

Change only one variable between trials and record the effect.

### Mission 3 — Functions
Create reusable functions such as conceptual behaviors:
- `drive_forward(...)`
- `drive_backward(...)`
- `turn_left(...)`
- `turn_right(...)`
- `stop_robot()`

Exact implementation should match the devices configured in the team's project.

### Mission 4 — Shape challenge
Use the functions to attempt a simple route such as a square or rectangular path.

The goal is not geometric perfection. The goal is to observe accumulated error and identify possible causes.

## Programming concepts
Connect each robotics example to general CS ideas:
- variable → adjustable parameter;
- function → reusable behavior;
- argument → value supplied to a behavior;
- sequence → order of robot actions;
- debugging → evidence-based correction.

## Engineering investigation
If the robot does not return exactly to its starting orientation, list possible causes under:
- code;
- motor configuration;
- drivetrain geometry;
- friction / wheel slip;
- measurement method.

## Evidence to submit
- program file or repository link;
- table of three repeated trials;
- one function written by the team;
- short explanation of why a physical robot may produce different results from identical code.

## AI use
AI can suggest refactoring or explain Python syntax after students first state what behavior they want. Students must be able to explain every line used to control physical motion. Copying unexplained robot-control code does not count as mastery.

## Extension
Compare two speeds on the same route. Does higher speed improve or reduce repeatability? Design a fair test.

## Next lesson
Replace fixed autonomous commands with human input from the V5 Controller and compare tank drive with arcade-style control.
