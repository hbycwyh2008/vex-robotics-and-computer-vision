# Core Meeting Playbook — Weeks 28–36

---

## Week 28 — Contours, Bounding Boxes and Centroids

### Meeting 28A — From Pixels to Candidate Objects
**Anchor:** Lesson 19

**Objective:** Students convert a binary mask into contours and filter noise using an explainable rule.

**Prep:** working masks; OpenCV contour tutorial.

- **0–10 Launch:** A mask has 500 white pixels—how many objects does that mean? Students identify ambiguity.
- **10–22 Demo:** contours/connectivity, area, minimum-area filter.
- **22–48 Lab:** find contours and print count/area.
- **48–60 Filter:** derive a justified minimum-area rule from observed data.
- **60–72 Failure search:** small true target or large distractor; discuss trade-off.
- **72–82 Rebuild:** recreate contour stage from a checklist.
- **82–90 Exit:** what genuine target could your filter accidentally remove?

**Evidence:** contour list + filter rationale.

### Meeting 28B — Bounding Box, Centroid and Left/Center/Right
**Objective:** Students turn a detection into numerical position data usable by a robot.

**Prep:** image center overlay; several target positions.

- **0–10 Retrieval:** what information survives after thresholding/contours?
- **10–22 Demo:** bounding box, center point, image center, tolerance band.
- **22–48 Lab:** draw boxes/centroids; output x/y/w/h/center.
- **48–62 Classify:** target left/center/right with tolerance, not exact pixel equality.
- **62–72 Multiple candidates:** define selection rule (largest/nearest center/etc.).
- **72–82 Adversarial image:** test ambiguous candidate case.
- **82–90 Exit:** justify tolerance band and target-selection rule.

**Evidence:** annotated detection screenshot + position output.

---

## Week 29 — Complete Classical Detection Pipeline + Andrew Ng Bridge

### Meeting 29A — Project 04 Pipeline Build
**Anchor:** Lesson 20

**Objective:** Students integrate capture → HSV → mask → cleanup → contours → filter → selection → annotation → structured output.

**Prep:** `project-delivery-pack.md`; teacher test images; webcam optional.

- **0–10 Pipeline cards:** students arrange stages and explain data type at each stage.
- **10–18 Teacher demo:** only interfaces between stages; do not provide full final code.
- **18–55 Build/integrate:** students combine their prior components.
- **55–68 Test:** known easy, hard and target-absent cases.
- **68–78 Debug:** identify first pipeline stage where failure appears.
- **78–85 Commit/evidence.
- **85–90 Exit:** which stage is currently your bottleneck and what evidence proves it?

**Evidence:** working classical pipeline version.

### Meeting 29B — CNN Bridge: Convolution and Learned Features
**Required video:** Andrew Ng, *Computer Vision*, *Edge Detection Example*, selected *More Edge Detection*.

**Objective:** Students compare hand-written visual rules with convolution-based feature extraction.

**Prep:** Coursera access; simple edge kernel image if demonstrating.

- **0–8 Launch:** “Our detector uses human-chosen HSV ranges. What would it mean for a model to learn useful features?”
- **8–32 Video:** assigned Andrew Ng segments with pause prompts from CV guide.
- **32–45 Unplugged convolution:** apply a tiny kernel to a small grid conceptually; focus on local pattern detection.
- **45–60 Compare:** HSV rule, contour geometry and learned filters—who chooses features?
- **60–72 Lab connection:** inspect edges/gradients on one image using OpenCV if time.
- **72–82 Discussion:** when is classical CV the better engineering choice?
- **82–90 Exit:** explain convolution as local feature detection without saying “AI recognizes it.”

**Evidence:** classical-vs-learned comparison note.

---

## Week 30 — Project 04 Robustness + CNN Foundations

### Meeting 30A — Project 04 Validation and C6
**Objective:** Students validate classical detector across varied conditions and report limitations honestly.

**Prep:** fixed test matrix: target present/absent, lighting, distance, clutter, occlusion.

- **0–10 Freeze version:** commit/tag tested code; define success criteria.
- **10–55 Validation:** minimum 20 labeled trials/frames across conditions.
- **55–68 Metrics:** success rate + FP/FN counts; optional position accuracy.
- **68–76 Failure analysis:** choose one representative failure and identify pipeline stage.
- **76–84 Final artifact:** screenshots/data/limitation.
- **84–90 Individual exit:** what claim can your data support and what claim can it not support?

**Evidence:** Project 04 + C6 record.

### Meeting 30B — Andrew Ng CNN Foundations
**Required video:** *Padding*, *Strided Convolutions*, *Convolutions Over Volume*, *One Layer of a Convolutional Network*, *Pooling Layers*, *Why Convolutions?* (teacher may split before/after class according to viewing guide).

**Objective:** Students explain the functional purpose of convolution, channels, stride/padding and pooling at conceptual level.

**Prep:** Coursera clips assigned; board sketches of feature-map dimensions.

- **0–10 Retrieval:** local filter/edge concept from Week 29.
- **10–35 Curated video:** pause for prediction; avoid playing 50+ minutes continuously.
- **35–50 Whiteboard model:** input → filters → feature maps → activation/pooling.
- **50–65 Dimension/pattern questions:** qualitative, not heavy derivation.
- **65–76 Compare to OpenCV:** what was hand-selected vs learned?
- **76–84 Pair explanation:** one student teaches stride/padding, other pooling.
- **84–90 Exit:** why can learned features outperform fixed color thresholds under some conditions?

**Evidence:** CNN concept map.

---

## Week 31 — Perception to Decision + MobileNet/Transfer Learning

### Meeting 31A — Clean Perception → Decision → Action Interface
**Anchor:** Lesson 21

**Objective:** Students separate perception output from robot decision/action and test logic without motors first.

**Prep:** saved detections/images; decision-table worksheet.

- **0–10 Launch:** Why is it risky if camera code directly commands motors everywhere?
- **10–20 Architecture:** perception returns structured state/data; decision chooses state; action executes bounded command.
- **20–38 Design:** TARGET_LEFT/CENTER/RIGHT/NO_TARGET table and safe behavior.
- **38–58 Offline tests:** mock perception values; verify every state.
- **58–70 Confidence rule:** tolerance/min-area/multi-frame consistency.
- **70–80 Negative tests:** no target/ambiguous target.
- **80–90 Exit:** explain why offline decision testing precedes robot motion.

**Evidence:** decision table + tested function/pseudocode.

### Meeting 31B — Andrew Ng: MobileNet, Transfer Learning and Data Augmentation
**Required video:** selected *MobileNet*, *MobileNet Architecture*, *Transfer Learning*, *Data Augmentation*, *State of Computer Vision*.

**Objective:** Students explain why pretrained lightweight networks and augmentation matter for robotics/edge vision.

**Prep:** viewing guide; examples of limited robotics dataset.

- **0–8 Launch:** “We have 200 labeled robot-camera images, not 2 million. What can we reuse?”
- **8–35 Curated videos with pauses.
- **35–50 Concept map:** pretrained backbone → adapt/fine-tune → local task.
- **50–62 MobileNet discussion:** constrained compute/latency/size.
- **62–74 Augmentation design:** propose realistic transformations; reject unrealistic ones.
- **74–84 Engineering choice:** classical HSV vs transfer learning for three scenarios.
- **84–90 Exit:** when can transfer learning reduce data/training burden?

**Evidence:** approach-selection table.

---

## Week 32 — Learned Object Detection + Closed-Loop Alignment

### Meeting 32A — Andrew Ng Object Detection: Localization to YOLO
**Required video:** *Object Localization*, *Object Detection*, *Bounding Box Predictions*, *Intersection Over Union*, *Non-max Suppression*, *Anchor Boxes*, *YOLO Algorithm* (split into assigned pre-view + in-class synthesis).

**Objective:** Students explain the outputs and post-processing of modern object detectors and connect them to their OpenCV box/centroid work.

**Prep:** viewing guide; two overlapping-box examples.

- **0–10 Retrieval:** classical bounding box/centroid from Week 28.
- **10–30 Synthesis clips:** localization vs detection; bounding-box output.
- **30–45 IoU activity:** compare candidate boxes qualitatively/numerically with simple examples.
- **45–58 NMS simulation:** groups remove duplicate boxes by score/overlap.
- **58–70 Anchor/YOLO concept:** multiple boxes/classes in one model; no implementation required.
- **70–82 Compare:** classical contour box vs learned detector box.
- **82–90 Exit:** explain why NMS exists.

**Evidence:** detector pipeline sketch.

### Meeting 32B — Closed-Loop Vision Alignment
**Anchor:** Lesson 22

**Objective:** Students use target-center error as feedback and tune a conservative alignment behavior.

**Prep:** safe bounded test area; low-speed cap; camera/vision output available.

- **0–10 Predict:** robot sees target 120 px right of center—what should happen next?
- **10–20 Demo:** `error = target_x - image_center_x`; tolerance; target-loss stop.
- **20–38 Offline simulation:** feed error values to decision logic.
- **38–58 Low-speed robot trials:** align from several start offsets.
- **58–70 Record:** time, overshoot, oscillation, target loss.
- **70–80 Tune one variable:** turn speed/tolerance/frame consistency.
- **80–90 Exit:** explain responsiveness vs stability trade-off.

**Evidence:** baseline/revised alignment table.

---

## Week 33 — Embedded Vision, Failure Modes and Project 05

### Meeting 33A — Edge Impulse: From Model to Embedded System + Failure Analysis
**Required video:** selected Edge Impulse *What is Computer Vision?*, *Transfer Learning and MobileNet*, *Introduction to Object Detection*, *Object Detection Performance Metrics*, *Deploy Object Detection Model to a Single Board Computer*.

**Objective:** Students understand the deployment pipeline and compare model errors with control/system errors.

**Prep:** Coursera guide; architecture cards.

- **0–10 Launch:** model works on laptop—what new problems appear on a robot/edge device?
- **10–32 Curated video/synthesis.
- **32–45 Architecture:** camera → preprocessing → model → detections → decision → control.
- **45–58 Failure sorting:** data/model/latency/integration/control/mechanical.
- **58–70 Metrics:** precision/recall concept linked to FP/FN; avoid metric overload.
- **70–82 Design fallback:** no detection, low confidence, latency spike.
- **82–90 Exit:** name one failure a better model would not fix.

**Evidence:** deployment architecture + failure taxonomy.

### Meeting 33B — Project 05 Validation: Vision-Guided Decision System
**Anchor:** Lesson 23

**Objective:** Students validate integrated perception→decision→action and demonstrate safe fallback behavior.

**Prep:** project pack; stress-test matrix; rubric.

- **0–10 Freeze version/safety check.
- **10–45 Validation:** normal + at least three stress conditions.
- **45–58 Required target-loss/fallback test.
- **58–68 Diagnose failures by layer.
- **68–76 One bounded fix/retest if appropriate.
- **76–84 Package evidence:** decision table, trials, limitation, demo.
- **84–90 Individual C7 exit:** “Which failure mode is most serious and how does the system fail safely?”

**Evidence:** Project 05 + C7 record.

---

## Week 34 — Capstone Requirements and Architecture

### Meeting 34A — Capstone Problem, Requirements and Scope
**Anchor:** Lesson 24

**Objective:** Teams define a feasible integrated robotics/vision problem with measurable requirements and test criteria.

**Prep:** capstone brief; examples of over-scoped projects.

- **0–10 Launch:** critique one vague capstone goal.
- **10–20 Requirements review:** measurable, testable, bounded.
- **20–42 Teams:** define problem, user/context, 4–7 requirements, constraints.
- **42–55 Approach choice:** classical CV, learned CV or hybrid; justify based on task/data/compute.
- **55–68 Risk list:** hardware, perception, control, integration, time.
- **68–80 Scope cut:** identify minimum viable demo and one optional feature.
- **80–90 Exit:** each member names one requirement and how it will be tested.

**Evidence:** capstone requirements draft.

### Meeting 34B — System Architecture + Test Plan + Proposal Conference
**Objective:** Teams create subsystem interfaces, integration order and validation plan before building.

**Prep:** architecture template; teacher conference schedule.

- **0–10 Retrieval:** subsystem vs feature.
- **10–22 Demo:** interface contracts and test-before-integration principle.
- **22–45 Architecture:** hardware, perception, decision, action/control, logging/evidence.
- **45–60 Test plan:** unit/subsystem/integration/final tests mapped to requirements.
- **60–78 Teacher conference:** approve, conditionally approve or require scope reduction.
- **78–86 GitHub:** proposal/diagram commit.
- **86–90 Exit:** identify first subsystem to validate and why.

**Evidence:** approved proposal + traceability table.

---

## Week 35 — Capstone Integration Sprint

### Meeting 35A — Subsystem Build and Interface Validation
**Anchor:** Lesson 25

**Objective:** Teams validate subsystems independently and integrate only known-working interfaces.

**Prep:** team-specific hardware/data; test plans visible.

- **0–10 Stand-up:** yesterday/next blocker/risk.
- **10–20 Readiness:** each team states measurable target for meeting.
- **20–55 Build/test:** subsystem work; teacher conferences focus on evidence and interface clarity.
- **55–68 Integration gate:** only connect subsystems that passed their local test.
- **68–78 First integration trial:** log first divergence.
- **78–86 Commit/notebook.
- **86–90 Exit:** what is currently known to work independently?

**Evidence:** subsystem test + integration log.

### Meeting 35B — Debugging, Robustness and Validation Dataset
**Objective:** Teams run planned stress tests and prioritize the highest-impact failure.

**Prep:** capstone test matrix; spare battery/hardware.

- **0–10 Failure review:** select top risk, not easiest bug.
- **10–45 Controlled tests:** collect enough repeated data for claim.
- **45–58 Diagnose by layer.
- **58–70 Implement one evidence-backed fix.
- **70–80 Retest same condition.
- **80–86 Freeze candidate version if requirements met.
- **86–90 Exit:** what evidence still blocks a reliability claim?

**Evidence:** before/after robustness test.

---

## Week 36 — Final Validation, Showcase and Defense

### Meeting 36A — Final Validation + Evidence Freeze
**Anchor:** Lesson 26

**Objective:** Teams complete final requirement-based validation and freeze the version used for presentation.

**Prep:** final rubric; requirement traceability; recording setup.

- **0–10 Version check:** code/config/build state documented.
- **10–50 Final validation:** execute pre-written tests; no cherry-picking only best trials.
- **50–62 Failure/limitation statement:** distinguish known limitation from unresolved bug.
- **62–74 Traceability:** each requirement → evidence link.
- **74–84 Portfolio cleanup:** final code, diagrams, trials, AI disclosure.
- **84–90 Individual rehearsal:** each member answers one technical defense question.

**Evidence:** frozen final validation package.

### Meeting 36B — Showcase + Individual Engineering Defense
**Objective:** Students demonstrate the system and independently defend technical decisions, failures and evidence.

**Prep:** demo order; defense prompts; backup video allowed only as backup, not substitute for explanation.

- **0–10 Setup/safety.
- **10–55 Team demonstrations:** problem → architecture → live behavior → evidence → limitation.
- **55–78 Individual defense:** random questions on subsystem, code/control, vision approach, testing, debugging and AI use.
- **78–85 Peer technical reflection:** one design insight learned from another team.
- **85–90 Final reflection/reset:** what can you now rebuild, debug or transfer independently that you could not at Week 1?

**Evidence:** final project + individual C8 defense.