# Lesson 10 — Inertial Sensor: Reliable Turning

## Course position
Week 6–7 · Sensors and Autonomous Control

## Learning objectives
Students will be able to:
- explain what robot heading/orientation represents;
- calibrate and read an Inertial Sensor correctly;
- compare open-loop turning with sensor-feedback turning;
- use a target heading to control a turn;
- measure repeatability across multiple trials.

## Core idea
A timed turn assumes the robot behaves the same way every time. A feedback-based turn measures what the robot is actually doing and uses that measurement to decide when to stop turning.

## Part A — Open-loop baseline
Program a nominal 90-degree turn using the team's current method. Run at least five trials from the same start orientation.

Record the final heading or measured turn angle for each trial.

## Part B — Inertial Sensor setup
Configure the sensor and follow the required calibration procedure before using heading data.

Students should identify:
- initial heading;
- direction of increasing/decreasing heading;
- how the value changes during a full rotation.

## Part C — Feedback turn
Create a behavior that turns toward a target orientation and stops based on measured heading rather than only elapsed time.

Use conservative speed first. The objective is stable repeatability, not maximum turning speed.

## Part D — Compare methods
Run at least five trials using the feedback method and compare results with the open-loop baseline.

Suggested metrics:
- mean absolute angle error;
- largest error;
- consistency across trials.

## Engineering discussion
Why might a robot overshoot a target angle even when it knows its current heading?

Possible factors to investigate:
- turning speed;
- momentum;
- wheel slip;
- sensor update timing;
- stopping behavior;
- chassis geometry.

## Evidence to submit
- open-loop trial table;
- feedback trial table;
- comparison of repeatability;
- code or pseudocode for the feedback turn;
- one evidence-based improvement.

## AI connection
This is a feedback-control example. The system repeatedly senses its state, compares it with a target, and acts to reduce the difference.

## AI use
AI may help students explain feedback-control concepts or calculate summary statistics from their own measurements. Students must not substitute generated data for real trials.

## Next lesson
Combine distance, orientation and drivetrain feedback into a small autonomous state sequence.
