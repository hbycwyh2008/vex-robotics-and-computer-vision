# Lesson 15 — Engineering Iteration and Test Data

## Course position
Weeks 21–22 · Engineering Design and Mechanisms

## Learning objectives
Students will be able to:
- identify a mechanism's highest-priority failure mode;
- define a measurable performance metric;
- make one targeted design change at a time;
- compare baseline and revised performance;
- defend a design decision using evidence.

## Core idea
Iteration is not random modification. A strong engineering cycle is:

**Observe → define the problem → form a hypothesis → change one variable → test → compare → keep/revert**

## Part A — Establish a baseline
Using the prototype from the previous lesson, define at least one measurable metric such as:
- success rate;
- cycle time;
- maximum safe lift height;
- object retention rate;
- repeatable endpoint;
- number of jams in a fixed number of trials.

Run enough baseline trials to establish a credible starting point.

## Part B — Failure analysis
Choose the single most important limitation.

Classify it as primarily:
- geometry;
- rigidity;
- friction;
- gear ratio / motor loading;
- object contact;
- alignment;
- control/code;
- inconsistent procedure.

Write a hypothesis in this format:

> If we change ___, then ___ should improve because ___.

## Part C — One-variable revision
Make one major design change while keeping the rest of the test as constant as practical.

Examples:
- change gear ratio;
- change contact surface or roller position;
- add shaft support;
- reinforce a flexible arm;
- alter mechanism angle;
- lower or raise motor speed;
- reposition a pivot.

## Part D — Re-test
Repeat the same test procedure and compare with baseline.

Do not call a change successful because it "looks better." Use the chosen metric.

## Decision
Choose one:
- **Keep** — measurable improvement with no unacceptable new problem.
- **Revert** — performance worsened or reliability declined.
- **Investigate further** — results are mixed or insufficient.

## Evidence to submit
- baseline data;
- identified failure mode;
- hypothesis;
- photo/sketch of the revision;
- revised data;
- keep/revert decision;
- short explanation of any new trade-off introduced.

## AI use
AI may help students organize test results, calculate summary statistics, or generate possible hypotheses. It may not replace direct observation or decide that a mechanism works without data.

## Teacher note
Reward careful failed experiments when the hypothesis and test are sound. Students should learn that a reverted change can still be good engineering evidence.

## Next lesson
Integrate drivetrain, driver control, mechanism and autonomous thinking into a competition-style engineering challenge.
