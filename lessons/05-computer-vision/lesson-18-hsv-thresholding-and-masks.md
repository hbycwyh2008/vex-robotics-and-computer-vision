# Lesson 18 — HSV Thresholding and Color Masks

## Course position
Weeks 26–27 · Computer Vision Foundations

## Learning objectives
Students will be able to:
- explain why HSV can be useful for color-based vision tasks;
- convert an image from BGR to HSV;
- select lower/upper color bounds from observed pixel data;
- create a binary mask;
- evaluate false positives and false negatives under changing conditions.

## Required video learning

### Coursera — IBM: Introduction to Computer Vision and Image Processing
Course: https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Use the remaining selected Module 2 videos as preparation/review:
- Pixel Transformations
- Geometric Operations
- Spatial Operations in Image Processing

The Coursera videos provide the image-processing foundation. The lesson's HSV and masking work is taught primarily through OpenCV documentation plus hands-on experimentation.

## Required technical references

- OpenCV changing color spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- OpenCV image thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

## Core idea
A color mask is a rule-based classifier. Each pixel is tested against a range and classified as target / not target.

Students should explicitly recognize that this is **classical, hand-designed computer vision**, not a trained neural network.

## Part A — Explore HSV
Use several pixels from the target object and background. Record their HSV values.

Discuss:
- Hue as color family;
- Saturation as color intensity/purity;
- Value as brightness.

## Part B — Build the mask
Convert the image to HSV and use lower/upper bounds to produce a binary mask.

Students should avoid guessing arbitrary ranges. Start from sampled data and expand only as testing requires.

## Part C — Test conditions
Test the same mask under at least three conditions such as:
- brighter/dimmer light;
- different camera distance;
- different background;
- partial occlusion;
- target near similarly colored objects.

Record where the mask succeeds and fails.

## Part D — Improve the rule
Modify one bound at a time and note the effect on:
- missed target pixels;
- unwanted background pixels.

If appropriate, introduce basic morphological cleanup only after students understand what problem it solves.

## Discussion bridge — rules vs learning

Students discuss:

- Who selected the HSV ranges: the computer or the programmer?
- What evidence caused the team to widen or narrow the range?
- What kinds of visual variation would make a hand-written threshold brittle?
- If a model later learns visual features from examples, how would that differ from this pipeline?

Do not teach CNNs in detail yet. This discussion prepares the comparison students will make after the classical detector is complete.

## Evidence to submit
- original image and mask screenshots;
- HSV sample table;
- final threshold values;
- condition-testing table;
- one false-positive and one false-negative example if observed;
- explanation of the trade-off in widening/narrowing the range.

## AI connection
This is perception through explicit rules rather than machine learning. Students should understand that an AI-like application can still use deterministic computer-vision algorithms.

## AI use
AI may explain HSV or OpenCV functions, but students must derive threshold decisions from their own images and test conditions.

## Next lesson
Turn the mask into object-level information by finding contours, bounding boxes and target centroids, then begin connecting these transparent geometric features to the concepts used in modern computer vision.
