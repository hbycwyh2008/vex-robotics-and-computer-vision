# Lesson 03 — TrainingBot Build II and First Power-On

## Course position
Week 2 · Build Foundations

## Learning objectives
Students will be able to:
- complete and inspect a TrainingBot-class V5 drivetrain;
- connect the Brain, motors, battery and controller safely;
- perform pre-power mechanical and electrical checks;
- distinguish mechanical faults from configuration/control faults;
- establish a baseline robot before modification.

## Build completion
Continue the official TrainingBot instructions until the baseline robot is mechanically complete enough for drivetrain testing.

## Pre-power inspection
No team powers on until another student or the teacher verifies:

### Mechanical
- fasteners are present and secure;
- wheels rotate without unexpected binding;
- shafts cannot slide out of position;
- no structural member contacts a rotating component;
- the battery and Brain are mechanically secure.

### Electrical
- Smart Cables are fully inserted;
- cables are routed away from wheels/gears;
- no cable is sharply pinched;
- motor ports are recorded;
- battery connection is secure.

## First-power procedure
1. Raise or secure the drivetrain so an unexpected wheel movement is safe.
2. Turn on the V5 Brain.
3. Confirm that expected devices appear connected.
4. Pair/check the Controller as needed.
5. Test one drivetrain direction at low speed.
6. Stop immediately if motion, sound or wiring differs from expectation.

## Diagnostic matrix
| Symptom | First category to inspect |
|---|---|
| Wheel does not turn | wiring / port / motor configuration |
| Motor turns but wheel does not | mechanical transmission |
| Wheel binds or chatters | alignment / shaft / spacer / gear mesh |
| Left and right sides oppose unexpectedly | motor direction / configuration |
| Robot veers | mechanical symmetry, wheel friction, then software |

Students should learn not to change code when the root cause is mechanical.

## Baseline driving mission
When safe operation is confirmed, drive a short marked route:
- forward;
- stop inside a target box;
- reverse;
- left/right turn;
- return to start.

Record observations. Do not optimize yet.

## Evidence to submit
- completed baseline robot photo;
- wiring/port map;
- completed pre-power checklist;
- one observed issue classified as mechanical, electrical, configuration or driver-control;
- 3–5 sentence reflection on what the team would inspect first if the robot stopped moving tomorrow.

## AI connection
Introduce the course control loop:

**Perception → Decision → Action**

At this stage, perception is mostly the human driver. Later, sensors and computer vision will provide machine perception; code will make decisions; motors will produce actions.

## Teacher notes
Do not introduce OpenCV yet. Students need a reliable physical platform and a mental model of robot subsystems before AI perception becomes meaningful.

## Next lesson
Create the first VEXcode project, configure drivetrain motors, and translate driver intent into programmed motor commands.
