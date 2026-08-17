# Lesson 17 — Images as Data: Pixels and Color

## Course position
Weeks 25–26 · Computer Vision Foundations

## Learning objectives
Students will be able to:
- explain that a digital image is an array of pixel values;
- distinguish image width, height and color channels;
- load and display an image with Python/OpenCV;
- inspect pixel values and simple image properties;
- connect camera perception to the same perceive–decide–act architecture used with robot sensors.

## Required resources
- computer with Python and OpenCV
- sample images and/or USB webcam
- Jupyter notebook or Python IDE
- engineering notebook / GitHub portfolio

## Core idea
A camera does not give a robot "objects." It gives the computer a grid of numerical values. Computer vision turns those values into useful measurements and decisions.

## Part A — Load an image
Students load a teacher-provided image with OpenCV and inspect:
- image dimensions;
- number of channels;
- data type;
- several individual pixel values.

## Part B — Coordinate system
Identify:
- top-left origin;
- row/column or y/x relationship;
- one selected pixel coordinate;
- a rectangular region of interest.

## Part C — Color channels
Compare OpenCV BGR channel order with the familiar RGB representation.

Create or display:
- original image;
- one isolated channel;
- grayscale version.

Students should describe what information is preserved or lost.

## Part D — Camera connection
If a webcam is available, capture one frame and compare it with a saved image. Discuss how repeated frames form a live perception stream.

## Evidence to submit
- Python script/notebook;
- screenshot showing image dimensions and pixel inspection;
- annotated explanation of image coordinates;
- short response: **What does a camera actually provide to an AI/robot system?**

## AI connection
This lesson intentionally demystifies computer vision. The input is data, not understanding. Meaning comes from algorithms, thresholds, models or other processing steps.

## AI use
AI may explain OpenCV syntax, but students must run the code, inspect actual pixel values and explain what each operation changes.

## Next lesson
Move from raw color channels to HSV color space and build a robust color mask for target detection.
