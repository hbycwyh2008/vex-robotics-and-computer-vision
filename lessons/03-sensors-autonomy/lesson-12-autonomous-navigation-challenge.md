# Lesson 12 — Autonomous Navigation Challenge

## Course position
Week 18 · Sensors and Autonomous Control

## Learning objectives
Students will be able to:
- integrate sensor readings, thresholds, heading feedback and state logic;
- design a repeatable autonomous test procedure;
- measure reliability rather than judging success from a single run;
- diagnose failure by subsystem and state;
- communicate why an autonomous system succeeds or fails.

## Challenge brief
Program the robot to complete a short autonomous route without driver input. The route must include:
- at least one forward travel segment;
- at least one controlled turn;
- at least one sensor-triggered decision or stop condition;
- a clearly defined finish condition.

The teacher may adapt field dimensions to the available room and hardware.

## Constraints
- The robot begins from a marked start position and orientation.
- Teams may not touch the robot after the run begins except for safety.
- The final program must include a safe stop/end state.
- Students must be able to explain every state and transition.

## Engineering workflow
### 1. Plan
Draw the route and state diagram before coding.

### 2. Baseline
Run the initial complete routine three times without changing the code.

### 3. Diagnose
For each failure, classify the first observable cause as:
- sensing;
- threshold/condition;
- state transition;
- drivetrain/control;
- mechanical;
- inconsistent test setup.

### 4. Improve
Change one major factor at a time. Record the hypothesis before the next run.

### 5. Validate
Run the final version at least 10 times under the same conditions.

## Required data
Track:
- trial number;
- success/failure;
- completion time if relevant;
- state where any failure occurred;
- observed cause;
- change made;
- result of that change.

## Performance target
A team should define a reliability target before final testing, such as 8/10 or 9/10 successful runs. The specific target may be adjusted for challenge difficulty.

## Evidence to submit
- route diagram;
- state diagram;
- final code or pseudocode;
- baseline and final reliability data;
- debugging log;
- short engineering defense explaining the most important design decision.

## Reflection
Answer:
1. Which sensor or feedback mechanism contributed most to reliability?
2. Which failure was hardest to diagnose?
3. What would you improve if the robot had to run in a different environment?

## AI connection
Students now have a complete non-vision autonomous system:

**Perceive → Decide → Act → Re-measure → Continue**

This control loop becomes the foundation for later AI/computer-vision integration.

## AI use
AI may help students summarize their own data, generate test cases, or review state logic. It may not invent measurements, replace physical testing, or serve as evidence that the robot works.

## Unit 03 checkpoint
Students are ready for engineering design when they can build and defend a repeatable autonomous behavior using measured sensor feedback.

## Next unit
Shift from sensing/control to mechanism engineering: gear ratio, torque, speed, manipulators, constraints and iterative design.
