# Lesson 22 — Closed-Loop Vision Alignment

## Course position
Week 32 · AI Vision and Robot Decision Making

## Learning objectives
Students will be able to:
- use target position relative to image center as feedback;
- implement a simple alignment loop;
- identify oscillation, overshoot and unstable perception;
- tune speed/tolerance using measured tests;
- explain why feedback must balance responsiveness and stability;
- connect classical centroid alignment to modern object-localization and detection outputs.

## Required video learning

### DeepLearning.AI / Andrew Ng — Convolutional Neural Networks
Course: https://www.coursera.org/learn/convolutional-neural-networks

Required Week 3 selections:
- Object Localization
- Object Detection
- Bounding Box Predictions
- Intersection Over Union
- Non-max Suppression
- Anchor Boxes
- YOLO Algorithm

These videos are required because students already have concrete experience with bounding boxes and centroids from OpenCV. Andrew Ng's object-detection sequence now gives them the modern learned-model version of localization and detection.

Optional extension:
- Region Proposals
- Semantic Segmentation with U-Net
- U-Net Architecture Intuition
- U-Net Architecture

### Coursera — Edge Impulse: Computer Vision with Embedded Machine Learning
Course: https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning

Recommended reinforcement:
- Introduction to Object Detection
- Object Detection Performance Metrics
- Object Detection Models

## Core idea
A vision-guided robot repeatedly does this:

**See target → measure horizontal error → choose turn direction/speed → move → see again**

This is a feedback loop, not a one-time command.

The perception source may be classical or learned. For example:

**Classical:** contour centroid x-coordinate

**Learned:** detected bounding-box center x-coordinate

The control problem can remain similar even when the perception method changes.

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

## Part E — Modern detection reasoning

Using the Andrew Ng videos, students explain how a learned object detector would add information beyond the current classical pipeline:

- predicted bounding box;
- class label;
- confidence/objectness-related score;
- multiple candidate boxes;
- IoU for measuring overlap;
- NMS for removing duplicate detections.

Students should be able to explain why **NMS is a perception-stage operation** and why the final selected target can still feed the same alignment controller.

## Engineering discussion
A robot that reacts too strongly may oscillate. A robot that reacts too weakly may align slowly. This is a control trade-off.

A second trade-off now appears in perception: a more sophisticated detector may handle more varied targets, but may also introduce computational cost, latency, confidence thresholds and new failure modes.

## Evidence to submit
- alignment logic diagram;
- baseline and revised trial tables;
- chosen tolerance;
- explanation of one oscillation/overshoot case;
- final low-speed alignment demonstration;
- labeled explanation of bounding box, IoU, NMS and YOLO at the conceptual level;
- one diagram showing either contour-centroid input or learned bounding-box input feeding the same control loop.

## AI connection
Visual perception is now part of a real closed-loop control system. The camera does not merely label an object; its output continuously changes robot behavior. Students also connect transparent classical localization to modern learned object detection without confusing perception with control.

## AI use
AI may help students reason about tuning hypotheses or summarize measured data. All tuning decisions must be validated on the physical system.

## Next lesson
Stress-test both the vision-guided control behavior and the assumptions behind perception under lighting, clutter, occlusion, target loss and domain shift.
