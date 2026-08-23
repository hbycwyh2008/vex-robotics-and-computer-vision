# Core Meeting Playbook — Weeks 10–18

---

## Week 10 — Sequences, Loops and Refactoring

### Meeting 10A — Loops for Repeated Robot Actions
**Objective:** Students identify when repetition should become a loop and predict loop behavior before running.

**Prep:** Repetitive square/route code sample; safe test area.

- **0–10 Launch:** Students circle repeated code and predict how many executions occur.
- **10–22 Demo:** `for`/repeat concept, loop variable only as needed, safety against unintended repetition.
- **22–45 Guided refactor:** Replace repeated route segments with a loop.
- **45–60 Test:** Compare original and looped behavior; functionality should remain equivalent.
- **60–72 Debug:** Diagnose one off-by-one or wrong-turn failure.
- **72–82 Rebuild:** Students write looped version without copying teacher code.
- **82–90 Commit/exit:** When is a loop clearer, and when would a function be the better abstraction?

**Evidence:** loop refactor + explanation.

### Meeting 10B — Programmed Route + Code Review
**Objective:** Students combine variables, functions and loops into a readable route program and defend structure choices.

**Prep:** Simple taped route; code-review checklist.

- **0–10 Predict:** Teams sketch intended route and list reusable behaviors.
- **10–18 Planning:** No coding yet; choose functions/parameters/loops.
- **18–48 Build:** Implement route.
- **48–65 Test/debug:** Repeated controlled starts; record errors.
- **65–75 Refactor:** Improve naming, duplication or function boundaries without changing target behavior.
- **75–84 Peer review:** Reviewer identifies one strength and one maintainability risk.
- **84–90 Exit:** Cite one refactor that made debugging easier.

**Evidence:** route program + code-review note.

---

## Week 11 — Encoders, Precision and Repeatability

### Meeting 11A — Motor Position/Encoder as Measurement
**Objective:** Students use motor position/rotation feedback to reason about movement instead of relying only on time.

**Prep:** Marked straight lane; ruler/tape; encoder-capable V5 motors.

- **0–10 Launch:** Compare “drive for 1 second” with “rotate a measured amount.” What changes if battery/load changes?
- **10–22 Demo:** Motor rotation/position as measured feedback; distinguish commanded value from physical distance.
- **22–45 Calibration lab:** Run several commanded rotations and measure physical displacement.
- **45–60 Analyze:** Compute/compare variability; do not overclaim precision.
- **60–72 Build:** Use measured movement in a short task.
- **72–82 Retest:** Same start point, multiple trials.
- **82–90 Exit:** Why is repeatability different from accuracy?

**Evidence:** rotation-vs-distance data table.

### Meeting 11B — Precision Movement Investigation
**Objective:** Students quantify route error and test one hypothesis for improving repeatability.

**Prep:** Defined target line/box; 5-trial test sheet.

- **0–10 Predict:** Identify likely mechanical and software sources of positional error.
- **10–18 Test-plan review:** Keep start position and major variables controlled.
- **18–45 Baseline:** Five repeated movement trials.
- **45–58 Analyze:** Range/mean or simple summary appropriate to class level.
- **58–72 Change one variable:** e.g., speed, stopping behavior or mechanical correction.
- **72–82 Retest:** Five trials again.
- **82–90 Exit:** Was the change better? Answer only from data.

**Evidence:** baseline/retest table + evidence-based conclusion.

---

## Week 12 — Project 01: Basic Driving Robot

### Meeting 12A — Project 01 Performance Test
**Objective:** Students demonstrate reliable driver/programmed motion and provide test evidence.

**Prep:** `student-handouts/project-delivery-pack.md`; defined course; rubric/checklist.

- **0–10 Requirements:** Teams translate project criteria into a test checklist.
- **10–25 Final readiness:** No feature additions; inspect configuration, battery, mechanical state and code version.
- **25–60 Performance trials:** Required repeated runs; record failures, not just best run.
- **60–72 Corrective window:** One justified fix and retest if needed.
- **72–82 Evidence packaging:** Commit final code, test table, short demo evidence.
- **82–90 Exit:** Individual: identify one system failure and the evidence used to diagnose it.

**Evidence:** Project 01 submission package.

### Meeting 12B — C3 Practical + Individual Explanation
**Objective:** Verify each student can independently explain/configure/program core motion skills.

**Prep:** C3 practical stations; selected Unit 02 quiz questions.

- **0–8 Setup:** Explain individual standard.
- **8–50 Practical:** Configure/check device; explain tank/arcade mapping; interpret a motion function; diagnose a curved-drive symptom.
- **50–65 Short written check:** 3–5 concept questions.
- **65–78 Rebuild task:** Recreate a small movement behavior from requirements only.
- **78–86 Learning log:** Mastery level and next target.
- **86–90 Reset/reassessment assignment.**

**Evidence:** C3 record.

---

## Week 13 — Sensors as Measurement

### Meeting 13A — Raw Sensor Data Before Decisions
**Anchor:** Lesson 08

**Objective:** Students distinguish raw measurement, threshold and decision.

**Prep:** Distance/bumper/available sensor stations; sensor test sheet.

- **0–10 Launch:** Give a raw distance value; ask what can and cannot be concluded without context.
- **10–22 Demo:** `sensor → raw value → processing/threshold → decision → action`.
- **22–48 Investigation:** Collect raw data under at least five controlled conditions.
- **48–60 Plot/table inspection:** Identify noise/range/edge cases.
- **60–72 Propose threshold:** Students justify from their own data.
- **72–82 Peer challenge:** Another team gives a borderline case.
- **82–90 Exit:** Why should thresholds come after data collection rather than guessing?

**Evidence:** raw-data table + proposed threshold.

### Meeting 13B — Bumper/Distance Investigation + False Decisions
**Objective:** Students test sensor-based decisions and identify false positives/false negatives.

**Prep:** Obstacle/target objects; safe stationary tests first.

- **0–10 Retrieval:** Define raw value vs threshold decision with an example.
- **10–20 Demo:** Simple boolean decision; introduce FP/FN in robotics terms.
- **20–45 Offline/static tests:** Evaluate target present/absent or obstacle/no obstacle across conditions.
- **45–60 Confusion-style tally:** correct positive, correct negative, false positive, false negative.
- **60–72 Adjust threshold:** One change only; predict trade-off.
- **72–82 Retest:** Same test set.
- **82–90 Exit:** Which error is more dangerous for the chosen robot behavior, and why?

**Evidence:** before/after decision table.

---

## Week 14 — Inertial Sensor, Calibration and Conditionals

### Meeting 14A — Inertial Sensor + Calibration
**Anchor:** Lesson 10

**Objective:** Students calibrate/read heading and explain why valid sensing requires correct initialization.

**Prep:** Robots with inertial sensor; open turning area.

- **0–10 Launch:** Why might a heading reading be wrong immediately after startup?
- **10–22 Demo:** Calibration procedure, heading/rotation concept, wait-until-ready pattern.
- **22–42 Static investigation:** Read values at known orientations.
- **42–60 Turning trials:** Command/drive turns and compare target vs measured heading.
- **60–72 Diagnose:** overshoot, calibration, mechanical slip or logic issue.
- **72–82 Rebuild:** Students reproduce initialization/read pattern with reduced support.
- **82–90 Exit:** What evidence distinguishes calibration error from overshoot?

**Evidence:** target-vs-measured heading table.

### Meeting 14B — Conditionals and Threshold Decisions
**Objective:** Students program `if/else` decisions based on sensor input and test boundary cases.

**Prep:** Safe stationary examples first; threshold values from collected data.

- **0–10 Predict:** Trace three sensor values through a threshold rule.
- **10–22 Demo:** conditional structure, comparison operators, clear safe default.
- **22–45 Guided coding:** Sensor value controls visible/state output before motor action.
- **45–58 Boundary tests:** just below, at and above threshold.
- **58–72 Add conservative motor action:** only after logic tests pass.
- **72–82 Debug:** Fix one wrong comparison or unsafe default.
- **82–90 Exit:** Why must boundary values be tested deliberately?

**Evidence:** tested conditional + boundary table.

---

## Week 15 — Obstacle Response and Feedback Turning

### Meeting 15A — Distance Sensor Obstacle Response
**Anchor:** Lesson 09

**Objective:** Students build a safe obstacle-response behavior and validate it across distances/surfaces.

**Prep:** obstacles with consistent placement; low-speed limit.

- **0–10 Launch:** Write desired behavior as input → condition → action.
- **10–18 Safety:** stop condition and maximum test speed.
- **18–42 Program:** approach/stop or teacher-approved response.
- **42–60 Baseline trials:** at least five consistent-start tests.
- **60–72 Failure search:** different obstacle material/angle/distance.
- **72–82 Improve:** one justified threshold or state change.
- **82–90 Exit:** Report one false decision and likely cause.

**Evidence:** 5+ trial table + failure example.

### Meeting 15B — Feedback Turning
**Objective:** Students compare open-loop turn commands with sensor-informed stopping.

**Prep:** marked angles; inertial sensor.

- **0–10 Predict:** Which will be more repeatable: timed turn or heading-based stop? State assumptions.
- **10–20 Demo:** feedback concept without overcomplicating control theory.
- **20–40 Open-loop baseline:** repeated turn trials.
- **40–58 Feedback implementation:** stop/adjust based on heading.
- **58–72 Repeated comparison:** same start conditions.
- **72–82 Analyze:** overshoot and variability.
- **82–90 Exit:** Explain open-loop vs feedback using this robot, not a memorized definition.

**Evidence:** open-loop vs feedback comparison.

---

## Week 16 — Autonomous States and Route Construction

### Meeting 16A — State-Based Autonomous Behavior
**Anchor:** Lesson 11

**Objective:** Students represent autonomous behavior as explicit states/transitions rather than one long unstructured sequence.

**Prep:** state diagram example; whiteboards/cards.

- **0–10 Launch:** Give a robot mission; teams name likely states before coding.
- **10–22 Demo:** state, transition condition, safe terminal/fallback state.
- **22–40 Paper design:** teams create state diagram and transition table.
- **40–60 Code skeleton:** implement state variables/functions without full motion first.
- **60–72 Offline trace:** manually feed conditions; verify transitions.
- **72–82 Add limited robot actions:** test one transition at a time.
- **82–90 Exit:** What makes a transition testable?

**Evidence:** state diagram + transition table.

### Meeting 16B — Autonomous Route Build + Debugging Clinic
**Objective:** Students integrate sensor/motion states into a short autonomous mission and isolate failures by subsystem.

**Prep:** bounded course; debugging checklist.

- **0–10 Plan:** mark route states and expected transitions.
- **10–45 Integration:** add one state/transition at a time.
- **45–62 Controlled trials:** record first failing state, not just final outcome.
- **62–75 Debug clinic:** each team presents Symptom → Hypothesis → Test; peers may challenge the test, not provide full code.
- **75–84 Retest:** after one evidence-based change.
- **84–90 Exit:** “Where exactly did your last failed run first diverge from expectation?”

**Evidence:** route trace + debugging record.

---

## Week 17 — Project 02 Baseline and Iteration

### Meeting 17A — Sensor-Based Autonomous Project Baseline
**Anchor:** Lesson 12

**Objective:** Teams establish a measurable baseline before optimizing Project 02.

**Prep:** project requirements, fixed start position, scoring/mission criteria.

- **0–10 Requirements:** identify measurable success criteria and safety boundaries.
- **10–20 Test plan:** define start state, trial count and data to record.
- **20–55 Baseline runs:** minimum five; no hiding failed trials.
- **55–65 Analyze:** locate dominant failure category.
- **65–76 Hypothesis:** choose one variable/system to change.
- **76–84 Implement but do not over-tune.
- **84–90 Exit:** Predict the effect of the chosen change before next meeting.

**Evidence:** baseline dataset + hypothesis.

### Meeting 17B — Controlled Iteration + Reliability Retest
**Objective:** Students evaluate whether one engineering change improves Project 02 reliability.

**Prep:** preserve baseline configuration/data.

- **0–10 Retrieval:** Restate hypothesis and success metric.
- **10–25 Complete change:** only the planned variable if practical.
- **25–60 Retest:** same trial protocol as baseline.
- **60–72 Compare:** success rate/error/failure categories.
- **72–80 Decision:** keep, revert or revise; justify.
- **80–86 Commit/notebook:** tag/version final tested code.
- **86–90 Exit:** What would make your comparison unfair?

**Evidence:** baseline-vs-retest evidence.

---

## Week 18 — Project 02 Practical and Technical Defense

### Meeting 18A — Project 02 Validation
**Objective:** Demonstrate final autonomous behavior under defined conditions and document reliability honestly.

**Prep:** final test protocol; rubric; charged batteries; no new feature work during validation.

- **0–10 Readiness:** configuration/build/code version check.
- **10–55 Validation runs:** required repeated trials; teacher observes process and safety.
- **55–65 One repair window:** only for clear defect; record it.
- **65–75 Revalidation if changed:** never claim old data after a material change.
- **75–84 Submission packaging:** code, state diagram, test data, failure/limitation statement.
- **84–90 Individual exit:** Identify the strongest evidence of reliability and the largest limitation.

**Evidence:** Project 02 final package.

### Meeting 18B — C4 Individual Technical Defense + Reassessment
**Objective:** Verify each student understands sensors, thresholds, feedback, states and debugging.

**Prep:** C4 practical prompts; selected Unit 03 questions.

- **0–10 Setup:** students review their own project evidence only.
- **10–55 Individual rotations:** explain raw data→threshold→decision; interpret FP/FN; trace state transition; diagnose a hypothetical failure; demonstrate one sensor read/conditional pattern.
- **55–68 Written check:** short-response concepts.
- **68–78 Rebuild/transfer:** modify a threshold or state requirement and explain expected effect.
- **78–86 Learning log:** current mastery + evidence.
- **86–90 Reset/reassessment targets.**

**Evidence:** C4 practical record.