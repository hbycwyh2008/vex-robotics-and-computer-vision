# Engineering Notebook Guide

Your engineering notebook is the evidence trail of how the robot/system changed over time. It is not a polished report written at the end.

## What to Record Every Work Session
- date and lesson/project;
- goal for the session;
- team role(s);
- current robot/code/vision setup;
- prediction or hypothesis before a major change;
- test procedure;
- measurements/results;
- failures and debugging evidence;
- design/code changes and why they were made;
- next step;
- AI assistance disclosure when relevant.

Use the ready-to-copy [engineering notebook template](engineering-notebook-template.md).

## What Counts as Strong Evidence
Strong evidence is specific and reproducible.

**Weak:** "The robot was bad at turning, so we fixed it."

**Strong:** "Across five 90° turn trials, the robot averaged 101°. We reduced turn speed from 70% to 45% and repeated the same five-trial test; average final angle decreased to 93°. We kept the lower speed."

## Photos and Diagrams
Use images when they help someone understand:
- mechanism geometry;
- shaft/gear placement;
- wiring/port configuration;
- camera setup;
- test field layout;
- before/after revisions.

Label important parts rather than uploading unexplained photos.

## Debugging Entries
Use:

**Symptom → Hypothesis → Test → Evidence → Decision**

A failed hypothesis is still useful engineering if the test was valid and the result was recorded.

## Data Expectations
When a claim involves reliability, accuracy or improvement, use repeated trials rather than one successful demo.

Examples:
- 8/10 successful autonomous runs;
- five measured turning errors before and after tuning;
- false-positive/false-negative counts for vision;
- mechanism cycle times;
- scored challenge results.

## AI Assistance
AI may support explanations, debugging ideas, code review or data organization when allowed. Record what it contributed and how you verified it.

Never use AI-generated measurements or invented trial data.

## End-of-Project Reflection
Answer:
1. What changed most from the first design?
2. Which evidence caused that change?
3. Which failure taught the team the most?
4. What limitation still remains?
5. What would you test next?
