# Resources — Current VEX Robotics + Computer Vision Path

This resource list follows [CURRENT-COURSE-PATH.md](CURRENT-COURSE-PATH.md).

---

# 1. Engineering Notebook

- Getting Started with Engineering Notebooks: https://kb.vex.com/hc/en-us/articles/49010276056596-Getting-Started-with-Engineering-Notebooks
- Digital Engineering Notebook Templates: https://kb.vex.com/hc/en-us/articles/49020662150676-Digital-Engineering-Notebook-Templates

---

# 2. Onshape

- Onshape Fundamentals: CAD: https://learn.onshape.com/learning-paths/onshape-fundamentals-cad
- VEX V5 Parts Libraries: https://www.onshape.com/en/blog/vex-iq-vex-v5-parts-libraries
- Using Onshape to Design a VEX Robot in the Cloud: https://www.onshape.com/en/resource-center/videos/using-onshape-to-design-a-vex-robot-in-the-cloud

Core scope only:
- Part Studio essentials
- Introduction to Onshape Assemblies
- VEX V5 Parts Library
- later evidence-based AI Vision / claw redesign

---

# 3. VEXcode V5 / Python

- VEXcode V5: https://codev5.vex.com/
- Coding with VEXcode V5: https://pd.vex.com/hu/node/1479
- Code Viewer in VEXcode V5 (Python): https://pd.vex.com/training/v5/vex-v5-introductory-training-course/lesson-2a-using-the-code-viewer-in-vexcode-v5

Python practice:
- Medbot: https://education.vex.com/stemlabs/v5/stem-labs/labs/medbot
- Loops — Python: https://education.vex.com/stemlabs/v5/stem-labs/loop-there-it-is/programming-loops-python
- Conditionals — Python: https://education.vex.com/stemlabs/v5/stem-labs/to-do-or-not-to-do/programming-with-conditionals-python

---

# 4. VEX AI Vision Sensor

## Core documentation
- Getting Started: https://kb.vex.com/hc/en-us/articles/24062385752212-Getting-Started-with-the-AI-Vision-Sensor-with-VEX-V5
- Configuring Color Signatures: https://kb.vex.com/hc/en-us/articles/24067512493972-Configuring-Color-Signatures-with-the-AI-Vision-Sensor-in-VEXcode-V5
- Coding with AI Vision Sensor in VEXcode V5 Python: https://kb.vex.com/hc/en-us/articles/24616732648468-Coding-with-the-AI-Vision-Sensor-in-VEXcode-V5-Python
- V5 Python AI Vision API: https://api.vex.com/v5/home/python/Vision/AiVision.html
- AprilTags: https://kb.vex.com/hc/en-us/articles/30488063603988-Using-AprilTags-with-the-AI-Vision-Sensor

## Official video sequence
- Introducing AI Vision Sensor: https://pd.vex.com/videos/exp/introducing-the-ai-vision-sensor
- Detecting a Color: https://pd.vex.com/videos/exp/detecting-a-color-with-the-ai-vision-sensor
- Adjusting a Color Signature: https://pd.vex.com/videos/exp/adjusting-a-color-signature
- Using Data from the AI Vision Utility: https://pd.vex.com/videos/exp/using-data-from-the-ai-vision-utility-in-a-project
- AI Classifications: https://pd.vex.com/videos/exp/ai-classifications-with-the-ai-vision-sensor
- AprilTags: https://pd.vex.com/videos/exp/apriltags-with-the-ai-vision-sensor

Note: PD+ examples may use EXP / Blocks. Use them for concepts and pair them with the V5 Python documentation.

---

# 5. Arm + Claw + AI Vision

- AI Vision Sensor on V5 Clawbot: https://kb.vex.com/hc/en-us/articles/28385434989716-Mounting-and-Wiring-the-AI-Vision-Sensor-on-the-V5-Clawbot
- V5 Claw Kit v2 3D reassembly: https://kb.vex.com/hc/en-us/articles/15516473701524-Repairing-and-Reassembling-a-V5-Clawbot-Claw-V5-Claw-Kit-v2
- Programming the Robot Arm — Python: https://education.vex.com/stemlabs/v5/stem-labs/speedy-delivery/programming-the-robot-arm-python

Core integration task:

> **Detect → Center → Approach → Open Claw → Grab → Lift**

---

# 6. Practical CV Video Course — Robotics Focus

## Recommended

**Udemy — Hands on Robotic Vision: OpenCV, PyTorch, YOLO, Simulation**

https://www.udemy.com/course/hands-on-computer-vision-for-robotics-opencv-pytorch-yolo/

Do not assign the full course.

Recommended selected topics:
- Color Spaces
- Thresholding
- Contour Detection
- Morphological Operations
- Object Tracking
- ArUco Marker
- optional Image-Based Visual Servoing

Use it to map robot behavior to CV concepts:

| VEX AI Vision | Robotics CV |
|---|---|
| Color Signature | HSV + thresholding |
| centerX / centerY | contour / bounding-box center |
| width / height | bounding-box size |
| Object Following | object tracking / visual servoing |
| AprilTag | fiducial / ArUco marker concepts |
| AI Vision + Claw | vision-guided manipulation |

---

# 7. OpenCV Official Technical References

- OpenCV-Python Tutorials: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- Color Spaces / HSV: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
- Contours: https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
- Contour Features / Bounding Box: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

Core classical pipeline:

> **image → HSV → threshold/mask → contour → bounding box → center**

---

# 8. Modern CV Theory — Stanford CS231n

- Course: https://cs231n.stanford.edu/
- Schedule: https://cs231n.stanford.edu/schedule

Use selected lectures only:
- Computer Vision overview
- CNNs
- CNN architectures / transfer learning
- object detection

Do not require the complete Stanford course or all assignments.

Goal:

> **VEX AI Vision use → classical CV understanding → modern learned CV understanding**

---

# 9. Optional Extensions

Optional only after the core system works:
- DeepLearning.AI / Andrew Ng CNN
- Edge Impulse
- MobileNet
- YOLO implementation
- learned object detection
- visual servoing
- state machines
- sorting / delivery challenges

---

# 10. No Longer the Main CV Course

The following are not the current main pathway:
- IBM — Introduction to Computer Vision and Image Processing
- Coursera — Master OpenCV Fundamentals for Real-Time Computer Vision

They may remain useful as optional references.

---

# 11. Teacher Verification Rule

Before assigning any external resource:
1. verify the page still exists;
2. confirm the platform and language shown;
3. preview the exact section;
4. assign only material that supports the current robot project;
5. keep the physical robot task as the primary evidence of learning.
