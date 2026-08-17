# Lesson 23 — Vision Robustness and Failure Modes

## Course position
Week 33 · AI Vision and Robot Decision Making

## Learning objectives
Students will be able to:
- identify common failure modes in a vision-guided robot;
- design adversarial or stress-test conditions deliberately;
- distinguish perception failure from decision/control failure;
- add fallback behavior for uncertain or missing perception;
- communicate system limitations honestly.

## Core idea
A reliable AI/vision system is not one that works in a perfect demo. It is one whose limits are measured, understood and handled safely.

## Stress-test matrix
Test the integrated vision system under several conditions:
- brighter light;
- dimmer light;
- cluttered background;
- similar-colored distractor;
- target at different distances;
- partial occlusion;
- target briefly leaving the frame;
- camera vibration or small viewpoint change.

## Part A — Predict before testing
For each condition, predict the likely failure mode.

Possible categories:
- false positive;
- false negative;
- unstable centroid;
- wrong target selected;
- oscillatory control;
- target lost;
- decision state stuck;
- mechanical/control issue unrelated to vision.

## Part B — Run controlled tests
Keep one condition changed at a time when possible. Record:
- condition;
- expected behavior;
- actual behavior;
- failure category;
- severity;
- recovery behavior.

## Part C — Add fallback behavior
Implement at least one robust response, such as:
- stop after target loss;
- require multiple consistent frames;
- use a timeout;
- ignore detections below a minimum area;
- return to a neutral/search state;
- limit maximum motor command while vision is uncertain.

## Part D — Re-test
Repeat the relevant failure condition after the change. Compare before/after results.

## Evidence to submit
- stress-test matrix;
- at least three documented failure examples;
- one implemented fallback behavior;
- before/after test evidence;
- system limitation statement suitable for a technical presentation.

## Responsible AI connection
Students should be able to explain that confidence in a system should come from tested evidence, not from how impressive a demo looks. They should distinguish what the system can reliably do from what it sometimes appears to do.

## AI use
AI may help generate test-condition ideas or organize failure categories. Students must conduct the actual tests and write limitations based on observed evidence.

## Unit 06 checkpoint
Students are ready for the capstone when they can integrate visual perception with robot action and can identify, measure and mitigate important failure modes.

## Next unit
Design an integrated robotics + AI vision capstone with explicit requirements, architecture, tests and demonstration criteria.
