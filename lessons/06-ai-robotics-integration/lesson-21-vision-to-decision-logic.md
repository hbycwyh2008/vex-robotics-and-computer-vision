# Lesson 21 — Vision to Decision Logic

## Course position
Week 31 · AI Vision and Robot Decision Making

## Learning objectives
Students will be able to:
- convert visual output into a small set of robot states;
- separate perception, decision and action code;
- define safe behavior when no target is detected;
- test decision logic without immediately moving the robot;
- explain why uncertain perception should not produce aggressive actions;
- explain why MobileNet and transfer learning are useful for practical/embedded vision.

## Required video learning

### DeepLearning.AI / Andrew Ng — Convolutional Neural Networks
Course: https://www.coursera.org/learn/convolutional-neural-networks

Required Week 2 selections:
- Classic Networks — overview level
- ResNets — concept level
- MobileNet
- MobileNet Architecture
- Transfer Learning
- Data Augmentation
- State of Computer Vision

Students do not need to reproduce every architecture from scratch. The required goal is to understand why modern systems often reuse pretrained visual representations and why lightweight architectures matter when compute is constrained.

### Coursera — Edge Impulse: Computer Vision with Embedded Machine Learning
Course: https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning

Required bridge selections:
- What is Computer Vision?
- Overview of Image Classification
- Review of Neural Networks
- Transfer Learning and MobileNet

Use Edge Impulse to connect Andrew Ng's CNN concepts to the practical idea of deploying learned perception near a robot or embedded system.

## Core architecture
Use a clean three-layer design:

1. **Perception** — detect target and estimate position.
2. **Decision** — choose a state from perception output.
3. **Action** — command motors according to that state.

Example decision states:
- TARGET_LEFT
- TARGET_CENTER
- TARGET_RIGHT
- NO_TARGET

This software architecture should remain clean whether the perception layer is:
- an HSV/contour OpenCV detector;
- a pretrained/transfer-learned CNN;
- an object-detection model;
- another sensor or perception method.

## Part A — Decision table
Before connecting motors, create a table mapping perception to intended behavior.

Example:
| Perception | Decision | Intended action |
|---|---|---|
| Target left | ALIGN_LEFT | rotate slowly left |
| Target center | APPROACH | move forward slowly |
| Target right | ALIGN_RIGHT | rotate slowly right |
| No target | SAFE_SEARCH / STOP | teacher-approved safe behavior |

## Part B — Software-only test
Feed saved images or mocked perception values into the decision function.

Verify that each input produces the expected state.

## Part C — Add confidence rules
Create at least one rule that prevents unstable decisions, such as:
- minimum contour area;
- center tolerance band;
- require several consistent frames;
- minimum model confidence when using learned perception;
- stop if detection disappears.

## Part D — Robot integration at low speed
Only after software-only decision tests pass, connect states to conservative drivetrain actions.

Use a bounded test area and a clear stop procedure.

## Discussion — perception can change without rewriting decision logic

Compare two hypothetical perception modules:

**Classical CV:**
`HSV mask -> contour -> centroid`

**Learned CV:**
`camera -> CNN/object detector -> bounding box/confidence`

Students identify what can stay the same in the downstream decision/action layer. This reinforces modular system design and prevents students from treating "AI" as the entire robot program.

## Evidence to submit
- decision table;
- perception/decision/action diagram;
- test cases for all states;
- code or pseudocode with separated functions/modules;
- explanation of the no-target safety behavior;
- short explanation of why MobileNet/transfer learning can matter for robotics or embedded vision;
- diagram showing how either classical or learned perception could feed the same decision layer.

## AI literacy
A system is not intelligent merely because it moves toward a detected target. Students should be able to identify which parts are explicit human-designed rules, which outputs come from perception, and which parts may have been learned from training data.

## AI use
AI may review code organization or suggest test cases. Students must verify every state transition and safety condition with their own tests.

## Next lesson
Build a closed-loop vision-guided alignment behavior while learning the modern object-detection concepts that formalize localization, bounding boxes, IoU, NMS and YOLO.
