# Lesson 25 — Capstone Build, Integrate and Test

## Course position
Week 35 · Integrated Robotics + AI Vision Capstone

## Learning objectives
Students will be able to:
- integrate mechanical, control and vision subsystems incrementally;
- use subsystem tests to isolate faults;
- maintain a structured engineering/debugging log;
- compare prototype performance with project requirements;
- prioritize fixes based on impact and available time.

## Integration rule
Do not debug the entire system at once. Validate layers in order:

1. **Mechanical system** — mechanism moves reliably by itself.
2. **Robot control** — drivetrain/motors respond correctly without vision.
3. **Vision pipeline** — perception works off-robot or with motors disabled.
4. **Decision logic** — known test inputs produce correct states.
5. **Low-speed integration** — vision state commands safe robot actions.
6. **Full task test** — complete system attempts the capstone mission.

## Part A — Subsystem readiness check
For each subsystem, record:
- test performed;
- expected result;
- actual result;
- pass/fail;
- next action.

Students should not move to full integration while a critical subsystem is known to be unreliable.

## Part B — Integration milestones
Complete at least three staged milestones. Example:
- target detection displayed correctly;
- target position changes decision state correctly;
- robot aligns to target at low speed;
- mechanism activates only under the intended condition;
- full mission completes once;
- full mission completes repeatedly.

## Part C — Requirement traceability
Review each requirement from the proposal. Mark it as:
- not tested;
- partially met;
- met;
- failed.

For each failed requirement, decide whether to:
- fix it;
- reduce scope with teacher approval;
- document it as a limitation.

## Part D — Reliability testing
Run repeated complete or partial trials. Use consistent start conditions when measuring reliability.

Track:
- success/failure;
- perception error;
- decision error;
- control/mechanical error;
- completion time if relevant;
- recovery/fallback behavior.

## Debugging log format
Use:

**Symptom → suspected layer → hypothesis → test → evidence → decision**

Avoid entries such as "fixed code" without explaining what changed and why.

## Evidence to submit
- subsystem readiness table;
- architecture updated to match the real implementation;
- photos/video of integration milestones;
- requirement status table;
- repeated-trial data;
- debugging log with at least three meaningful entries.

## AI use
AI may help analyze logs, explain errors or propose tests. Students must validate changes physically and retain ownership of the final architecture and code.

## Teacher note
Scope control matters. A smaller system that works repeatedly and is well documented is stronger than an ambitious system that only works once.

## Next lesson
Run final validation, present the engineering argument, demonstrate the system and defend its AI/vision limitations.
