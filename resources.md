# Resources — Current VEX Robotics + Computer Vision Path

This resource list follows [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md).

# 1. VEX / Engineering Foundations

- Engineering Notebooks: https://kb.vex.com/hc/en-us/articles/49010276056596-Getting-Started-with-Engineering-Notebooks
- Digital Notebook Templates: https://kb.vex.com/hc/en-us/articles/49020662150676-Digital-Engineering-Notebook-Templates
- VEXcode V5: https://codev5.vex.com/
- AI Vision Getting Started: https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5
- AI Vision Python: https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python
- AI Vision Python API: https://api.vex.com/v5/home/python/Vision/AiVision.html
- AprilTags: https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

Current status: the class has completed the official AI Vision project sequence.

# 2. Core OpenCV Bridge — Coursera / IBM

**IBM — Introduction to Computer Vision and Image Processing**

https://www.coursera.org/learn/introduction-computer-vision-watson-opencv

Use only selected material:
- Module 1 — selected introduction;
- Module 2 — core digital-image / OpenCV content;
- Module 5 — selected object-detection concepts.

Skip Modules 3, 4, and 6 as core requirements.

Recommended total use: about **3–5 hours** of focused video/lab work, not full-course completion.

# 3. OpenCV Official References

- Python tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Color spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- Contour features / bounding box: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

Core bridge pipeline:

> **image → HSV / threshold → mask → contour / object region → bounding box → center**

Connect to:

> **VEX Color Signature → centerX / centerY / width / height**

# 4. Modern CV Theory — Stanford CS231n

- Course: https://cs231n.stanford.edu/
- Schedule: https://cs231n.stanford.edu/schedule

Use selected topics only:
- CV overview;
- CNNs;
- feature learning / pooling;
- architectures / transfer learning overview;
- object detection;
- IoU / NMS / YOLO-style ideas.

Do not require the full course or all assignments.

# 5. Optional Advanced Coursera Study

**University of Toronto — Visual Perception for Self-Driving Cars**

https://www.coursera.org/learn/visual-perception-self-driving-cars

Status: **Optional Advanced / after-class enrichment**.

High-value topics for stronger students:
- camera model / calibration;
- feature detection / matching;
- visual odometry;
- object detection / tracking;
- semantic segmentation;
- mobile-platform perception.

# 6. Onshape

- Onshape Fundamentals: https://learn.onshape.com/learning-paths/onshape-fundamentals-cad
- VEX V5 Parts Libraries: https://www.onshape.com/en/blog/vex-iq-vex-v5-parts-libraries

Return to Onshape only for evidence-based redesign.

# 7. No Longer Planned as Core

- Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation
- Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision
- full IBM course
- mandatory Andrew Ng CNN
- mandatory Edge Impulse
- robot-arm / pick-and-place pathways

These may be used only if a specific future need justifies them.

# 8. Teacher Verification Rule

Before assigning an external resource:
1. verify the page still exists;
2. preview the exact section;
3. assign only material that supports the current project;
4. keep the physical robot task as the main evidence of learning.