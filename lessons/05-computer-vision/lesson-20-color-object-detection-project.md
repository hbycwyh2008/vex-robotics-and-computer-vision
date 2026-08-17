# Lesson 20 — Color Object Detection Project

## Course position
Weeks 29–30 · Computer Vision Foundations

## Learning objectives
Students will be able to:
- integrate image capture, HSV masking, contour filtering and target selection;
- define measurable detection success criteria;
- test a vision pipeline across changing conditions;
- calculate simple reliability/error rates from collected trials;
- document limitations before connecting vision to robot motion.

## Project brief
Build a Python/OpenCV program that detects a teacher-approved colored target and outputs useful information such as:
- target found / not found;
- bounding box;
- target center;
- left / center / right position;
- optional target size estimate.

## Required pipeline
The program should include:
1. image or camera input;
2. BGR → HSV conversion;
3. threshold mask;
4. optional mask cleanup when justified;
5. contour detection;
6. noise filtering;
7. target-selection rule;
8. visual annotation;
9. structured output for later robot decisions.

## Test plan
Before final testing, define at least four conditions to test, such as:
- normal lighting;
- dimmer/brighter lighting;
- target at different distances;
- cluttered background;
- partial occlusion;
- second similarly colored object.

For each condition, run repeated trials or evaluate a repeated set of frames/images.

## Metrics
Track at minimum:
- target present / absent;
- program prediction;
- correct / incorrect;
- false positive count;
- false negative count.

Optional metrics:
- position classification accuracy;
- detection latency;
- centroid error relative to a manually marked point.

## Engineering rule
Students may not improve the system by testing only easy cases. A valid project deliberately searches for failure conditions.

## Evidence to submit
- complete Python/OpenCV program;
- annotated screenshots from multiple conditions;
- test matrix;
- calculated success rate;
- one documented false positive or false negative if encountered;
- explanation of the largest limitation;
- proposed next improvement.

## AI literacy checkpoint
Students should be able to explain:
- what the system literally measures;
- what rules produce the detection;
- why visual perception can be confidently wrong;
- why lighting/background/calibration matter;
- why test-set diversity matters.

## AI use
AI may help debug Python syntax, propose test conditions, or calculate statistics from student-collected results. Students must understand the full perception pipeline and independently explain all thresholds and filters used.

## Unit 05 checkpoint
Students are ready for robot integration when their vision program produces stable, interpretable output that can be consumed by decision logic.

## Next unit
Connect vision output to robot decisions: target left → turn left, target centered → approach, target missing → search or stop.
