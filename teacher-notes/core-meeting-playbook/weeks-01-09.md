# Core Meeting Playbook — Weeks 01–09

All meetings are designed for 90 minutes. Adjust physical setup time locally, but preserve testing, documentation and reset time.

---

## Week 1 — Course Launch, Safety and Kit Systems

### Meeting 1A — How This Course Works + Safe Engineering
**Anchor:** Lesson 01

**Objective:** Students can explain the course learning flow, identify major robot subsystems and apply baseline safety rules.

**Prep:** Display classroom-flow/mastery/AI-use posters; place one powered-off V5 kit per team; prepare lab sheets.

- **0–10 Launch:** Poster walk in teams. Each group records one behavior that matches each poster.
- **10–20 Learn:** Establish `Learn → Practice → Rebuild → Share` and the robotics cycle. Demonstrate safe power-down before mechanical/wiring work.
- **20–45 Investigation:** Teams sort representative components into structure, motion, actuation, control and sensing/intelligence.
- **45–65 Safety cases:** Give four scenarios (rewiring while powered, hair near wheels, stripped screw, battery damage). Teams decide stop/continue and justify.
- **65–78 Evidence:** Create first notebook entry with 8+ identified components and one safety decision.
- **78–85 Share:** Each team teaches one subsystem to another team.
- **85–90 Exit/reset:** Individually answer: “Why is working once not mastery?” Return parts/tools.

**Evidence:** first team notebook entry + individual exit.

### Meeting 1B — Parts Identification + Storage System
**Objective:** Students can distinguish easily confused VEX parts and create a storage system that supports debugging and rebuild.

**Prep:** Mix small sets of shafts, spacers, collars, bearings, screws, nuts, gears and structural pieces.

- **0–10 Retrieval:** Without notes, identify five displayed parts by function, not part number.
- **10–20 Demo:** Show shaft vs spacer vs shaft collar; show correct tool fit and signs of overtightening/stripping.
- **20–50 Parts challenge:** Teams identify at least 12 components and complete name/function/connects-to/handling notes.
- **50–65 Storage design:** Teams propose labels/bins; another team audits whether a new student could restore the kit.
- **65–75 Rebuild check:** Teacher mixes six items; students restore them without asking where they belong.
- **75–85 Document:** Photograph organized kit and record one confusing pair of parts.
- **85–90 Exit:** “What storage decision will save the most debugging time later, and why?”

**Evidence:** 12-part table + labeled storage photo.

---

## Week 2 — Documentation, Tools and GitHub Evidence

### Meeting 2A — Engineering Notebook as a Debugging Tool
**Objective:** Students can record engineering evidence using Goal → Change → Test → Problem → Diagnosis → Decision → Retest → Next Step.

**Prep:** Prepare one strong and one weak sample notebook entry; no names.

- **0–10 Launch:** Students compare the two entries and highlight what would help reproduce/debug the work.
- **10–20 Learn:** Model the notebook pattern and distinguish observation from interpretation.
- **20–45 Evidence reconstruction:** Give a short teacher demo with one intentional failure; teams write the event sequence from observations.
- **45–60 Peer audit:** Swap entries and ask: “Could another team continue from this?”
- **60–75 Rebuild:** Students revise entries to add missing measurements, diagnosis and next step.
- **75–85 Individual log:** First individual engineering learning log.
- **85–90 Exit:** Write one example of evidence that cannot honestly be invented after class.

**Evidence:** revised notebook entry + individual log.

### Meeting 2B — Tools, Fasteners, Shafts + GitHub Portfolio Setup
**Objective:** Students demonstrate safe fastening and create a working evidence repository structure.

**Prep:** VEX tools/hardware; GitHub access; portfolio guide.

- **0–10 Retrieval:** Match tool to fastener and explain why wrong-size tools damage hardware.
- **10–25 Demo:** Correct fastening, nut retention, shaft support, collar placement; show one bad assembly.
- **25–45 Skill stations:** Students complete fastener, shaft/collar and bearing/support micro-builds.
- **45–60 Practical check:** Each student corrects one planted assembly error.
- **60–78 GitHub:** Create portfolio folders/README and commit a Week 1 evidence artifact with a meaningful commit message.
- **78–85 Explain:** Partner checks whether the commit explains what changed.
- **85–90 Exit:** “What is the difference between GitHub evidence and the team notebook?”

**Evidence:** hardware skill check + first portfolio commit.

---

## Week 3 — Structure and TrainingBot Chassis

### Meeting 3A — Structure, Rigidity and Drivetrain Principles
**Anchor:** Lesson 02

**Objective:** Students predict how frame alignment and shaft support affect drivetrain reliability.

**Prep:** One aligned and one intentionally misaligned mini-assembly if possible; TrainingBot build instructions.

- **0–10 Launch:** Inspect two assemblies; predict which will roll straighter and why.
- **10–22 Demo:** Frame rigidity, square construction, bearing alignment, free-spinning shafts, wheel clearance.
- **22–45 Investigation:** Teams perform a “free-spin audit” on sample wheel/shaft assemblies.
- **45–65 Guided build:** Begin TrainingBot chassis using official Competition Kit instructions; stop at teacher-defined checkpoint.
- **65–75 QC:** Teams use a peer checklist: square frame, fastener security, free rotation, correct part choice.
- **75–85 Notebook:** Photo + last known-correct build step + one QC result.
- **85–90 Exit:** Name one mechanical symptom that could later look like a programming bug.

**Evidence:** chassis checkpoint photo + QC notes.

### Meeting 3B — TrainingBot Chassis Build + Explain While Looking
**Objective:** Students continue the official build and explain the function of each completed subsystem.

**Prep:** Build instructions at correct Competition Kit variant; spare fasteners/tools.

- **0–8 Retrieval:** Point to three parts from last meeting and explain their job.
- **8–18 Build-risk briefing:** Teacher shows only the next common error; avoid narrating every build step.
- **18–60 Build:** Continue chassis/drivetrain in role rotations (builder, parts/QC, documenter, verifier).
- **60–70 Stop-and-explain:** Random team member explains wheel/shaft/bearing/support path.
- **70–80 Mechanical test:** Push/roll robot unpowered; inspect friction, rubbing and frame twist.
- **80–86 Document:** Record one problem/diagnosis/change if any.
- **86–90 Reset/exit:** “What is the last known-correct checkpoint for your team?”

**Evidence:** build status + explanation check.

---

## Week 4 — Drivetrain Completion and Electronics

### Meeting 4A — Drivetrain Alignment + Motor Installation
**Anchor:** Lessons 02–03

**Objective:** Students complete reliable drivetrain mechanics and diagnose friction before applying power.

**Prep:** TrainingBot instructions; straightedge/ruler if useful; motors/cables kept separate until mechanical QC.

- **0–10 Launch:** Each team predicts one failure caused by overtightening or misalignment.
- **10–18 Demo:** Motor output, shaft connection and why forced alignment creates friction.
- **18–55 Build:** Install drivetrain/motors to checkpoint.
- **55–68 Unpowered validation:** Wheel rotation, symmetry, fastener check, cable-clearance planning.
- **68–78 Fault hunt:** Teacher/peer identifies one suspicious symptom; team uses Symptom → Hypothesis → Test → Evidence → Decision.
- **78–85 Notebook:** Record validation results.
- **85–90 Exit:** Mechanical or software? Robot pulls to one side before any code exists—justify.

**Evidence:** drivetrain QC record.

### Meeting 4B — Brain, Battery, Smart Cables and Port Map
**Anchor:** Lesson 03

**Objective:** Students wire the robot safely and create an accurate physical-to-software port map.

**Prep:** Brain, battery, Smart Cables; board with example port map.

- **0–10 Retrieval:** Why must the robot be powered down before rewiring?
- **10–22 Demo:** Brain ports, battery connection, cable strain/route, port documentation.
- **22–50 Build:** Install electronics according to official build instructions.
- **50–62 Port-map task:** Students record device → physical port → expected role.
- **62–72 Peer verification:** Another team traces every listed cable physically.
- **72–80 Cable management:** Correct rubbing, pinch points and loose routing.
- **80–86 Notebook:** Add wiring photo and verified port map.
- **86–90 Exit:** “What would happen if software configuration says Port 1 but the motor is physically in Port 2?”

**Evidence:** verified port map + wiring photo.

---

## Week 5 — TrainingBot Completion and Pre-Power Validation

### Meeting 5A — Build Completion + Quality Control
**Objective:** Students complete the TrainingBot and pass a structured pre-power inspection.

**Prep:** Printed/shared pre-power checklist; spare parts; charged battery remains disconnected initially.

- **0–10 Launch:** Teams list three checks that must happen before first power.
- **10–18 Mini-demo:** Show one loose fastener, one rubbing cable and one incorrectly retained shaft.
- **18–58 Build:** Finish required TrainingBot steps.
- **58–72 Pre-power QC:** Mechanical, electrical, cable and workspace inspection; teacher signs only after team self-check.
- **72–80 Rebuild spot check:** Remove/reinstall one low-risk component with reduced instructions.
- **80–86 Document:** Final build photo + issues found during QC.
- **86–90 Exit:** Which QC item most directly prevents hardware damage?

**Evidence:** signed pre-power checklist.

### Meeting 5B — First Power-On + Diagnostic Observation
**Objective:** Students power on safely, observe system status and separate configuration/electrical/mechanical symptoms.

**Prep:** Safe test stands/area; charged batteries; VEXcode available but no aggressive motion program.

- **0–10 Safety/setup:** Wheels off ground or robot in bounded safe state as appropriate.
- **10–20 Demo:** Brain power-on, device detection/status, emergency stop/power-off procedure.
- **20–40 Team first power:** Observe Brain/device status without driving.
- **40–55 Diagnosis:** Resolve missing-device/port/cable issues systematically.
- **55–70 Low-risk motor/device check:** One device at a time.
- **70–80 Peer explanation:** Student traces one device from physical motor → cable → port → configuration expectation.
- **80–86 Notebook:** Record first-power results and any failure chain.
- **86–90 Exit:** Classify one observed issue as mechanical, electrical or configuration and justify.

**Evidence:** first-power diagnostic record.

---

## Week 6 — First Drive and Foundation Practical

### Meeting 6A — First Controlled Drive + Baseline Diagnostics
**Objective:** Students drive the TrainingBot conservatively and collect a baseline for straightness/control.

**Prep:** Mark short straight lane; clear floor; controller pairing ready.

- **0–10 Launch:** Predict three reasons a mechanically complete robot may still drive poorly.
- **10–20 Demo:** Safe controller pairing and low-speed first drive.
- **20–45 Trials:** Three short straight runs; record drift/qualitative behavior.
- **45–62 Diagnose:** Teams choose the largest issue and test one hypothesis at a time.
- **62–72 Retest:** Repeat controlled runs after one justified change.
- **72–82 Explain/share:** Compare baseline vs revised behavior.
- **82–90 Notebook + exit:** “What evidence supports that your change helped—or did not?”

**Evidence:** baseline/retest table.

### Meeting 6B — Checkpoint C2: Build Skills Practical
**Objective:** Verify individual foundation mastery before programming sequence accelerates.

**Prep:** `assessments/practical-checkpoints.md`, small hardware stations.

- **0–8 Setup:** Explain that team success does not substitute for individual demonstration.
- **8–55 Practical rotations:** Identify parts; correct a fastening/shaft error; trace a motor port; explain safe power-down; inspect drivetrain symptom.
- **55–68 Rebuild:** Students reproduce one small assembly from a checklist, not step-by-step teacher help.
- **68–78 Short concept check:** Select Unit 00–01 quiz-bank questions.
- **78–86 Individual learning log:** Mastery level + evidence.
- **86–90 Reset:** Students who need reassessment receive specific skill target, not a generic grade.

**Evidence:** C2 practical record.

---

## Week 7 — VEXcode and Device Configuration

### Meeting 7A — Physical Robot ↔ Software Configuration
**Anchor:** Lesson 04

**Objective:** Students configure drivetrain/devices so software matches the physical robot.

**Prep:** VEXcode V5; completed port maps; one intentionally mismatched example configuration if possible.

- **0–10 Launch:** Give physical port map and wrong software config; students locate mismatch.
- **10–22 Demo:** Device configuration, left/right direction, drivetrain geometry parameters at concept level.
- **22–45 Guided config:** Teams configure their robot from verified port map.
- **45–60 Static checks:** Confirm device visibility and direction safely.
- **60–72 Debug challenge:** Teacher introduces one configuration mismatch or team tests a planned hypothesis.
- **72–82 Rebuild:** One student recreates config from the port map with teammates only checking afterward.
- **82–90 Commit/exit:** Save/commit configuration notes. Explain why “the code is correct” can still produce wrong motion.

**Evidence:** configuration screenshot/record + commit.

### Meeting 7B — Minimal Drivetrain Program + Test Loop
**Objective:** Students write and test a minimal motion program and use measured evidence to debug.

**Prep:** Safe lane; starter project with device config only, not completed solution code.

- **0–10 Predict:** Read a short motion sequence; predict robot behavior.
- **10–22 Demo:** Program structure, command sequence, wait/stop behavior, conservative velocity.
- **22–45 Guided coding:** Forward → stop → reverse/turn micro-task.
- **45–60 Physical test:** One trial at a time; observer records actual behavior.
- **60–72 Debug:** Symptom → hypothesis → test → evidence → decision.
- **72–80 Rebuild:** Students recreate the core motion sequence without copying the teacher screen.
- **80–86 Commit/notebook:** Commit meaningful change and record test.
- **86–90 Exit:** Why should motion testing begin at conservative speed?

**Evidence:** runnable minimal program + test note.

---

## Week 8 — Controller Programming and Driver Systems

### Meeting 8A — Tank Drive + Deadband
**Anchor:** Lesson 06

**Objective:** Students map controller axes to motors and explain why deadband is needed.

**Prep:** Controller axis diagram; safe driver area.

- **0–10 Launch:** Display noisy small joystick values; ask whether robot should move.
- **10–22 Demo:** Controller axis input, tank mapping, deadband concept.
- **22–48 Program:** Implement tank drive with readable variable names and deadband.
- **48–62 Test:** Slow figure-eight/straight tasks; observer watches control stability.
- **62–72 Debug/refine:** Adjust one deadband/control parameter based on evidence.
- **72–82 Rebuild:** Driver and programmer swap; second student explains mapping.
- **82–90 Evidence/exit:** Code commit + “What problem does deadband solve, and what too-large deadband causes?”

**Evidence:** tank-drive program + parameter explanation.

### Meeting 8B — Arcade Drive + Controlled Comparison
**Objective:** Students implement arcade drive and compare it with tank drive using evidence rather than preference alone.

**Prep:** Same timed course for both drive modes.

- **0–10 Retrieval:** Draw tank-drive input→motor mapping from memory.
- **10–20 Demo:** Arcade drive concept: forward + turn components.
- **20–42 Program:** Implement arcade mode or teacher-approved switch between modes.
- **42–65 Comparison trials:** Same driver runs same course under both modes; record time, errors and subjective workload separately.
- **65–75 Analyze:** Teams decide which mode better fits a specified task and cite data.
- **75–84 Share:** Different teams defend different choices.
- **84–90 Exit/reset:** Distinguish measured performance from driver preference.

**Evidence:** tank-vs-arcade comparison table.

---

## Week 9 — Python Motion, Variables and Functions

### Meeting 9A — Python Motion + Variables as Tunable Parameters
**Anchor:** Lesson 05

**Objective:** Students use variables to control reusable motion parameters and explain why hard-coded repeated values are harder to tune.

**Prep:** Starter Python/VEXcode project with device config; safe motion lane.

- **0–10 Launch:** Compare duplicated numeric literals with named speed/distance variables.
- **10–22 Demo:** Variables, assignment, readable naming, change-one-place tuning.
- **22–45 Program:** Forward/turn sequence using named parameters.
- **45–60 Trials:** Measure repeated route behavior.
- **60–72 Tune one variable:** Predict effect before changing; run retest.
- **72–82 Rebuild:** Students reconstruct parameterized version from a short checklist.
- **82–90 Commit/exit:** Why does parameterization improve engineering experimentation?

**Evidence:** parameterized program + before/after trial.

### Meeting 9B — Functions as Robot Behaviors
**Objective:** Students encapsulate repeated robot actions in functions and verify behavior independently.

**Prep:** One deliberately repetitive code sample.

- **0–10 Code inspection:** Mark repeated patterns in sample.
- **10–22 Demo:** Function definition/call, parameters at introductory level, single responsibility.
- **22–45 Refactor:** Convert repeated actions into functions such as move/turn or teacher-approved equivalents.
- **45–60 Function tests:** Test each function separately before full sequence.
- **60–72 Integration:** Build a short route from function calls.
- **72–82 Peer code review:** Another student explains function inputs/effects without running it.
- **82–90 Commit/exit:** “Why test functions separately before integrating the whole route?”

**Evidence:** modular program + peer explanation.