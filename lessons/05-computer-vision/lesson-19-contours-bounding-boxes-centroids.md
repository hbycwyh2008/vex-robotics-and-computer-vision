# Lesson 19 — Contours, Bounding Boxes and Centroids

## Course position
Weeks 28–29 · Computer Vision Foundations

## Learning objectives
Students will be able to:
- find contours from a binary mask;
- filter detections using simple geometric criteria;
- draw bounding boxes around candidate objects;
- calculate/estimate a target centroid;
- convert visual position into useful numerical features.

## Core idea
A mask labels target-like pixels. Contours group connected target pixels into candidate objects. From each candidate, the program can derive measurements such as:
- area;
- width/height;
- center position;
- relative location in the camera frame.

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

## Evidence to submit
- annotated detection screenshot;
- contour filtering rule;
- sample bounding-box measurements;
- centroid calculation/logic;
- left/center/right classification result;
- one example where multiple candidates make the decision ambiguous.

## AI connection
The output is now no longer merely an image. It is structured perception data that a robot can use for decisions.

## AI use
AI may help explain contour syntax or review geometric calculations. Students must verify every detection on actual images and explain the chosen filtering/selection rules.

## Next lesson
Build a complete color-object detection project and measure detection reliability across realistic conditions.
