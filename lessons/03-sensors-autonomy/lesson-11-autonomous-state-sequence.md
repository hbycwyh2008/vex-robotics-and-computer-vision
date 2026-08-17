# Lesson 11 — Autonomous State Sequence

## Course position
Weeks 16–17 · Sensors and Autonomous Control

## Learning objectives
Students will be able to:
- break an autonomous task into discrete states;
- use sensor input and conditions to transition between states;
- combine drivetrain motion with distance/orientation feedback;
- distinguish sequence bugs from sensor and mechanical faults;
- test autonomous behavior with repeatable start conditions.

## Core idea
Long autonomous scripts become difficult to debug when every command is chained together. A better approach is to think in states.

Example:

```text
STATE 1: move forward
IF target condition is reached → STATE 2

STATE 2: turn
IF target heading is reached → STATE 3

STATE 3: move to finish zone
IF finish condition is reached → STOP
```

## Challenge setup
Create a short autonomous route with at least three states. The route should require at least two of the following:
- measured drivetrain movement;
- distance sensing;
- orientation/heading feedback;
- a timed fallback or safety stop.

## Part A — Draw the state diagram
Before coding, teams draw:
- state names;
- action performed in each state;
- transition condition;
- what happens if the condition is never reached.

## Part B — Implement incrementally
Do not write the full routine at once.

1. Test State 1 alone.
2. Add the first transition.
3. Test State 2.
4. Continue until the route is complete.
5. Add a safe terminal state.

## Part C — Controlled trials
Use the same starting position and orientation for at least 10 trials.

Record:
- completed/not completed;
- state where failure occurred;
- observed cause;
- change made before the next test.

## Debugging framework
When the routine fails, ask:
1. Did the sensor produce a plausible value?
2. Did the condition evaluate as expected?
3. Did the program enter the intended state?
4. Did the drivetrain execute the intended action?
5. Did the physical robot behave consistently?

## Evidence to submit
- state diagram;
- autonomous program or pseudocode;
- 10-trial reliability table;
- failure classification by state;
- one revision supported by evidence.

## Mastery checkpoint — Unit 03
Students should now be able to:
- collect and interpret sensor data;
- choose thresholds from measurements;
- implement conditional autonomous behavior;
- use feedback to improve repeatability;
- design and debug a multi-state autonomous routine.

## AI connection
This lesson makes the course architecture explicit:

**Perception → Decision → Action → New perception**

Computer vision later changes the type of perception, but the control architecture remains similar.

## AI use
AI may help review a state diagram for missing transitions or suggest test cases. Students must still create, run and interpret the physical trials themselves.

## Next lesson
Apply the full sensor-and-autonomy workflow in a measured autonomous navigation challenge.
