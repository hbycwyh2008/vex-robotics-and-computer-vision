# Lesson 23 — Vision Robustness and Failure Modes

## Course position
Week 33 · AI Vision and Robot Decision Making

## Learning objectives
Students will be able to:
- identify common failure modes in a vision-guided robot;
- design adversarial or stress-test conditions deliberately;
- distinguish perception failure from decision/control failure;
- add fallback behavior for uncertain or missing perception;
- communicate system limitations honestly;
- compare robustness problems in hand-designed and learned vision systems.

## Required video learning

### DeepLearning.AI / Andrew Ng — Convolutional Neural Networks
Course: https://www.coursera.org/learn/convolutional-neural-networks

Review / connect these required ideas:
- Data Augmentation
- State of Computer Vision
- Intersection Over Union
- Non-max Suppression
- YOLO Algorithm

The focus is now not merely how the algorithms work, but **what can fail when the environment differs from the conditions used to design or train the vision system**.

### Coursera — Edge Impulse: Computer Vision with Embedded Machine Learning
Course: https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning

Required selected Module 3 material:
- Object Detection Performance Metrics
- Training an Object Detection Model
- Deploy Object Detection Model to a Single Board Computer

The deployment material is used to connect model quality with practical constraints such as latency, compute, memory and camera conditions.

## Core idea
A reliable AI/vision system is not one that works in a perfect demo. It is one whose limits are measured, understood and handled safely.

Students should now distinguish two broad families of failure:

### Classical CV failure examples
- HSV range no longer matches because lighting changed;
- similarly colored distractor passes the threshold;
- contour filter removes a real target;
- centroid becomes unstable under partial occlusion.

### Learned CV failure examples
- training data does not represent the deployment environment;
- class confusion or low-confidence detection;
- duplicate detections before NMS;
- domain shift in lighting/background/viewpoint;
- small or occluded target not represented well in training;
- latency or hardware limits make the model unusable in the control loop.

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

If students have access to a learned model or instructor-provided detections, also test or analyze:
- unfamiliar background/domain shift;
- lower-confidence detections;
- multiple overlapping detections;
- target appearance variation not present in the original examples.

## Part A — Predict before testing
For each condition, predict the likely failure mode.

Possible categories:
- false positive;
- false negative;
- unstable centroid;
- wrong target selected;
- low-confidence model output;
- duplicate/overlapping detection;
- oscillatory control;
- target lost;
- decision state stuck;
- inference too slow for useful control;
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
- ignore detections below a minimum contour area;
- ignore model detections below a justified confidence threshold;
- return to a neutral/search state;
- limit maximum motor command while vision is uncertain.

## Part D — Re-test
Repeat the relevant failure condition after the change. Compare before/after results.

## Part E — Classical vs learned robustness analysis

Students create a short engineering comparison:

| Question | Classical OpenCV | Learned CV |
|---|---|---|
| What must generalize? | thresholds/rules | learned representation/model |
| What data is needed? | test images for tuning/evaluation | training/validation/test data or pretrained model + task data |
| Typical environment risk | lighting/background breaks rules | domain shift or dataset mismatch |
| Main transparency advantage | rules are easy to inspect | output can be powerful but internal reasoning is less direct |
| Deployment concern | usually light compute | compute, memory, latency and model size may matter |

Students should explain why **data augmentation can help but does not replace real deployment testing**.

## Evidence to submit
- stress-test matrix;
- at least three documented failure examples;
- one implemented fallback behavior;
- before/after test evidence;
- system limitation statement suitable for a technical presentation;
- classical-vs-learned robustness comparison;
- explanation of one case where data augmentation or broader training data could help a learned detector;
- explanation of one case where a simple classical CV solution may still be preferable.

## Responsible AI connection
Students should be able to explain that confidence in a system should come from tested evidence, not from how impressive a demo looks. They should distinguish what the system can reliably do from what it sometimes appears to do, and distinguish high model confidence from proven system reliability.

## AI use
AI may help generate test-condition ideas or organize failure categories. Students must conduct the actual tests and write limitations based on observed evidence.

## Unit 06 checkpoint
Students are ready for the capstone when they can integrate visual perception with robot action; explain the difference between classical and CNN-based vision; understand the core ideas behind localization, IoU, NMS, YOLO, MobileNet and transfer learning; and identify, measure and mitigate important failure modes.

## Next unit
Design an integrated robotics + AI vision capstone with explicit requirements, architecture, tests and demonstration criteria. Teams may justify a classical, learned or hybrid perception approach rather than choosing a model simply because it appears more advanced.
