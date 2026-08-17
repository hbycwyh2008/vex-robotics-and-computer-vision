# Lesson 08 — Sensor Data and Thresholds

## Course position
Week 5–6 · Sensors and Autonomous Control

## Learning objectives
Students will be able to:
- explain the difference between a sensor reading and a decision;
- collect repeated sensor measurements under controlled conditions;
- choose and justify a threshold from observed data;
- write conditional logic that responds to sensor input;
- identify noise, variability and calibration as engineering problems.

## Core idea
A sensor does not tell the robot what to do. It produces data. Code interprets that data and decides what action to take.

**Sensor → Data → Decision rule → Motor action**

This is the same architecture students will later use for computer vision.

## Hands-on mission
Use one available classroom sensor suitable for distance/contact/environment measurements.

### Part A — Observe raw data
Collect readings in at least three clearly different physical conditions. Record multiple measurements for each condition rather than a single value.

### Part B — Find overlap
Compare the distributions of readings. Ask:
- Are readings perfectly stable?
- Do nearby conditions overlap?
- What environmental factors change the values?

### Part C — Choose a threshold
Create a rule such as:

```text
IF sensor value meets condition:
    take action A
ELSE:
    take action B
```

Students must justify the threshold from measured data.

### Part D — Test reliability
Run at least 10 trials. Record correct/incorrect decisions and note borderline cases.

## Data table
Include:
- physical condition;
- sensor reading;
- predicted class/state;
- actual result;
- correct/incorrect.

## Engineering discussion
A good threshold is not simply "the middle number." It should be chosen from evidence and tested under realistic variation.

Discuss:
- noise;
- calibration;
- false positive;
- false negative;
- robustness.

## Evidence to submit
- raw measurement table;
- chosen threshold and justification;
- conditional code or pseudocode;
- 10-trial reliability result;
- one limitation of the rule.

## AI connection
This is deliberately simple AI-style decision making: perception data is converted into a discrete decision. Students should understand that later computer-vision systems do the same thing with more complex inputs.

## AI use
AI may help explain threshold logic or suggest ways to organize data. It may not invent sensor readings or choose a threshold without the team's measurements.

## Next lesson
Apply the same measurement-and-threshold process to a Distance Sensor so the robot can react to obstacles autonomously.
