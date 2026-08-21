# Engineering Notebook Guide

Your **Team Engineering Notebook** is the evidence trail of how the robot or system changed over time. It is not a polished report written at the end, and it is not a diary.

The notebook should show a real engineering process:

> **Goal → Design / Change → Test → Problem → Diagnosis → Decision → Retest → Next Step**

The course also uses an **Individual Engineering Learning Log** so each student records personal learning, contribution, and mastery evidence.

- Team evidence: [engineering-notebook-template.md](engineering-notebook-template.md)
- Individual evidence: [individual-engineering-learning-log.md](individual-engineering-learning-log.md)
- Repeated testing: [test-record-template.md](test-record-template.md)

---

## Team Notebook vs Individual Learning Log

### Team Engineering Notebook

The team notebook records the shared engineering process:

- what the team is trying to make the system do;
- design and build decisions;
- code, wiring, mechanism, sensor, or vision configuration;
- test procedures;
- measurements and observations;
- failures and debugging evidence;
- changes and redesigns;
- retest results;
- next steps;
- photos, diagrams, code/commit links, or videos when useful.

### Individual Engineering Learning Log

Each student completes a short individual record showing:

- what I personally worked on;
- one engineering decision I understand;
- one problem the team encountered;
- how it was diagnosed;
- what I personally contributed;
- what I can now explain, rebuild, or repeat;
- my current Mastery Level for the main skill.

A successful team robot does **not** automatically prove individual mastery.

---

## Minimum Record Every Work Session

Before the team leaves class, the notebook should contain at least:

1. **Today's goal**
2. **One design / build / code change**
3. **One test or observation**
4. **One result, measurement, or failure**
5. **One next step**

For major engineering challenges, the notebook should include the full test–debug–retest cycle.

> **Build / Program → Test → Record → Explain**

If a result is not documented, it cannot be used as engineering evidence.

---

## What to Record Every Work Session

- date and lesson/project;
- goal for the session;
- team members and roles;
- current robot/code/vision setup;
- prediction or hypothesis before a major change;
- test procedure;
- measurements/results;
- failures and debugging evidence;
- design/code changes and why they were made;
- retest result;
- next step;
- evidence links;
- AI assistance disclosure when relevant.

Use the ready-to-copy [engineering notebook template](engineering-notebook-template.md).

---

## What Counts as Strong Evidence

Strong evidence is specific, measurable when possible, and reproducible.

**Weak:**

> The robot was bad at turning, so we fixed it.

**Strong:**

> Across five 90° turn trials, the robot averaged 101°. We reduced turn speed from 70% to 45% and repeated the same five-trial test; average final angle decreased to 93°. We kept the lower speed.

The goal is not to make every notebook entry long. The goal is to show **why the team made the next engineering decision**.

---

## Photos and Diagrams

Use images when they help someone understand:

- mechanism geometry;
- shaft/gear placement;
- wiring/port configuration;
- sensor position;
- camera setup;
- test field layout;
- before/after revisions.

Label important parts rather than uploading unexplained photos.

---

## Debugging Entries

Use:

> **Symptom → Hypothesis → Test → Evidence → Decision**

A failed hypothesis is still useful engineering if the test was valid and the result was recorded.

Example:

- **Symptom:** robot drifts left while commanded forward.
- **Hypothesis:** one drivetrain side has greater mechanical resistance.
- **Test:** inspect wheel freedom and compare left/right motion with the robot lifted safely.
- **Evidence:** right rear wheel rubs against a structural part.
- **Decision:** correct spacing and repeat the same straight-drive test.

Do not write only the final fix. Record the reasoning that led to the fix.

---

## Data Expectations

When a claim involves reliability, accuracy, consistency, or improvement, use repeated trials rather than one successful demo.

Examples:

- 8/10 successful autonomous runs;
- five measured turning errors before and after tuning;
- false-positive/false-negative counts for vision;
- mechanism cycle times;
- scored challenge results;
- repeated sensor readings under controlled conditions.

Use [test-record-template.md](test-record-template.md) when a structured comparison is useful.

---

## Connection to Mastery Levels

The course uses the shared `mastery-levels.md` system:

- **Level 0 — Exposure**
- **Level 1 — Follow and make it work**
- **Level 2 — Explain while looking**
- **Level 3 — Rebuild with a checklist**
- **Level 4 — Rebuild independently**
- **Level 5 — Modify, debug, and transfer**

The notebook should make growth visible. For example:

- Level 1 evidence may show a completed build following instructions.
- Level 2 evidence includes a clear explanation of how the system works.
- Level 3 evidence shows a repeatable checklist and successful rebuild/test.
- Level 4 evidence shows independent setup and validation.
- Level 5 evidence shows diagnosis, redesign, retesting, and transfer to a new challenge.

The notebook supports mastery evidence, but students may still be asked to rebuild a skill or explain it orally.

---

## AI Assistance

AI may support explanations, debugging ideas, code review, pseudocode, or data organization when allowed.

Record:

- what tool was used;
- what question or task it helped with;
- what suggestion or code it provided;
- how the team verified it;
- what students changed or did themselves.

Never use AI-generated measurements or invented trial data.

AI output is not evidence that the robot works. **Physical tests, measured data, explainable code, and student reasoning are the evidence.**

---

## End-of-Project Reflection

Answer:

1. What changed most from the first design?
2. Which evidence caused that change?
3. Which failure taught the team the most?
4. What limitation still remains?
5. What would you test next?
6. What part can each team member now explain or rebuild independently?
