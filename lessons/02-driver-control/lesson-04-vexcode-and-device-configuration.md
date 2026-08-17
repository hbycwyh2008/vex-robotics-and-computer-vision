# Lesson 04 — VEXcode and Device Configuration

## Course position
Weeks 7–8 · Driver Control and Robot Motion Programming

## Learning objectives
Students will be able to:
- create and save a VEXcode V5 project;
- configure drivetrain motors using the robot's documented port map;
- explain why software configuration must match physical wiring;
- download/run a minimal program safely;
- use a systematic test to diagnose configuration errors.

## Required resources
- completed TrainingBot
- V5 Brain, Controller and charged Battery
- computer with VEXcode V5
- Smart Cable for programming if required by the classroom setup
- engineering notebook / portfolio

## Core idea
A robot has two models at the same time:
1. the **physical robot** — motors, ports, wiring and mechanisms;
2. the **software model** — the devices and directions declared in VEXcode.

Reliable robotics requires these two models to agree.

## Hands-on mission
### Part A — Port map
Before opening device configuration, teams record each drivetrain motor and its physical Brain port.

### Part B — Create the project
Create a new VEX V5 project and give it a meaningful name using the class naming convention.

Configure the drivetrain/motors so that the software matches the actual robot.

### Part C — Minimal motion test
Write or use a minimal command that makes the drivetrain move briefly at a conservative speed.

Test with the robot positioned safely. Observe:
- Did both sides move?
- Did they move in the intended direction?
- Did the robot move straight?
- Did any motor report as disconnected?

### Part D — Diagnose before editing
For each failure, classify the likely source as:
- mechanical;
- wiring/port;
- device configuration;
- program logic.

Do not randomly change multiple settings at once.

## Debugging ladder
1. Is the Brain powered?
2. Is the motor physically connected?
3. Is the Smart Cable fully seated?
4. Is the recorded port correct?
5. Does VEXcode use that same port?
6. Is motor direction/reversal configured correctly?
7. Only then inspect program logic.

## Evidence to submit
- screenshot of device configuration;
- physical port map;
- first successful motion result;
- one debugging note using the format **symptom → hypothesis → test → result**.

## AI use
Students may ask AI to explain an error message or configuration concept, but AI must not invent the robot's port numbers. Port numbers must come from direct physical inspection.

## Mastery check
Given a robot whose left motor is plugged into a different port than VEXcode expects, explain why the program fails and identify the correct layer to fix.

## Next lesson
Use Python commands to control speed, direction, duration and stopping behavior, then connect those commands to variables and functions.
