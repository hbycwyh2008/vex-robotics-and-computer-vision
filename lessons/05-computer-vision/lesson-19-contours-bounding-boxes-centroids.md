# Lesson 19 — Contours, Bounding Boxes and Centroids

## Course position
Weeks 28–29 · Computer Vision Foundations

## Learning objectives
Students will be able to:
- find contours from a binary mask;
- filter detections using simple geometric criteria;
- draw bounding boxes around candidate objects;
- calculate/estimate a target centroid;
- convert visual position into useful numerical features;
- begin connecting hand-designed visual features to modern learned visual features.

## Required video learning

### DeepLearning.AI / Andrew Ng — Convolutional Neural Networks
Course: https://www.coursera.org/learn/convolutional-neural-networks

Start the modern-CV bridge with these Week 1 videos:
- Computer Vision
- Edge Detection Example
- More Edge Detection

The purpose here is **not yet to build a CNN**. Students use Andrew Ng's edge-detection discussion to notice a key transition:

> Classical CV explicitly designs operations and geometric rules; CNNs can learn useful feature detectors from data.

## Required technical reference

- OpenCV contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html

## Core idea
A mask labels target-like pixels. Contours group connected target pixels into candidate objects. From each candidate, the program can derive measurements such as:
- area;
- width/height;
- center position;
- relative location in the camera frame.

These measurements are transparent, human-designed features. Later, CNNs will learn internal feature representations rather than relying only on manually specified color and geometry rules.

## Part A — Find contours
Use the mask from the previous lesson and find connected contours.

Print or record the number of detected contours for several test images.

## Part B — Filter noise
Create a simple minimum-area rule or another justified geometric filter so tiny artifacts are ignored.

Students must explain why the filter is needed and what genuine targets it could accidentally remove.

## Part C — Bounding boxes
Draw a rectangle around each remaining candidate.

Record:
- x/y location;
- width/height;
- area.

## Part D — Centroid / target center
Calculate or obtain the object's center point.

Compare the target center with the image center and classify the target as:
- left;
- center;
- right.

Use a tolerance band rather than demanding a perfectly centered pixel coordinate.

## Part E — Multiple targets
If multiple candidates appear, define a selection rule such as:
- largest area;
- nearest image center;
- highest confidence according to a simple rule;
- target in a specific region.

Test whether the rule behaves as intended.

## Discussion bridge — feature engineering vs feature learning

Use the completed contour pipeline plus the Andrew Ng videos to compare:

- Which features did we explicitly create ourselves?
- Why do edges often contain useful information?
- How is a fixed edge filter different from a learned convolutional filter?
- Why might a learned detector handle some variations better than a fixed HSV rule?
- Why might the simple OpenCV pipeline still be the better engineering choice in some situations?

## Evidence to submit
- annotated detection screenshot;
- contour filtering rule;
- sample bounding-box measurements;
- centroid calculation/logic;
- left/center/right classification result;
- one example where multiple candidates make the decision ambiguous;
- short comparison: **one hand-designed feature in our OpenCV pipeline vs one feature-learning idea from the Andrew Ng videos**.

## AI connection
The output is now no longer merely an image. It is structured perception data that a robot can use for decisions. This lesson also creates the conceptual bridge from explicit feature engineering to learned visual features.

## AI use
AI may help explain contour syntax or review geometric calculations. Students must verify every detection on actual images and explain the chosen filtering/selection rules.

## Next lesson
Build a complete color-object detection project, measure reliability across realistic conditions, and then use the finished transparent pipeline as the baseline for learning CNN foundations.
