# Lesson 22 — Closed-Loop Vision Alignment

## Course position
Week 32 · AI Vision and Robot Decision Making

## Learning objectives
Students will be able to:
- use target position relative to image center as feedback;
- implement a simple alignment loop;
- identify oscillation, overshoot and unstable perception;
- tune speed/tolerance using measured tests;
- explain why feedback must balance responsiveness and stability.

## Core idea
A vision-guided robot repeatedly does this:

**See target → measure horizontal error → choose turn direction/speed → move → see again**

This is a feedback loop, not a one-time command.

## Part A — Define visual error
Let the image center be the desired target position. Define horizontal error conceptually as:

```text
error = target_center_x - image_center_x
```

Classify error using a tolerance band:
- negative beyond tolerance → target is left;
- within tolerance → aligned;
- positive beyond tolerance → target is right.

## Part B — Conservative alignment
At low speed, rotate toward the target until it enters the center tolerance band.

The robot should stop if:
- target is lost;
- timeout is reached;
- teacher-defined safety condition occurs.

## Part C — Observe stability
Run repeated alignment trials from different starting angles.

Record:
- starting offset;
- time to align;
- final error/category;
- overshoot/oscillation;
- lost-target events.

## Part D — Tune one variable
Change one of:
- turn speed;
- center tolerance;
- number of consistent frames required;
- update frequency.

Compare baseline and revised behavior.

## Engineering discussion
A robot that reacts too strongly may oscillate. A robot that reacts too weakly may align slowly. This is a control trade-off.

## Evidence to submit
- alignment logic diagram;
- baseline and revised trial tables;
- chosen tolerance;
- explanation of one oscillation/overshoot case;
- final low-speed alignment demonstration.

## AI connection
Visual perception is now part of a real closed-loop control system. The camera does not merely label an object; its output continuously changes robot behavior.

## AI use
AI may help students reason about tuning hypotheses or summarize measured data. All tuning decisions must be validated on the physical system.

## Next lesson
Stress-test the vision-guided system under lighting, clutter, occlusion and target-loss conditions, then define robust fallback behavior.
