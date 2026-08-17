# Lesson 21 — Vision to Decision Logic

## Course position
Week 31 · AI Vision and Robot Decision Making

## Learning objectives
Students will be able to:
- convert visual output into a small set of robot states;
- separate perception, decision and action code;
- define safe behavior when no target is detected;
- test decision logic without immediately moving the robot;
- explain why uncertain perception should not produce aggressive actions.

## Core architecture
Use a clean three-layer design:

1. **Perception** — detect target and estimate position.
2. **Decision** — choose a state from perception output.
3. **Action** — command motors according to that state.

Example decision states:
- TARGET_LEFT
- TARGET_CENTER
- TARGET_RIGHT
- NO_TARGET

## Part A — Decision table
Before connecting motors, create a table mapping perception to intended behavior.

Example:
| Perception | Decision | Intended action |
|---|---|---|
| Target left | ALIGN_LEFT | rotate slowly left |
| Target center | APPROACH | move forward slowly |
| Target right | ALIGN_RIGHT | rotate slowly right |
| No target | SAFE_SEARCH / STOP | teacher-approved safe behavior |

## Part B — Software-only test
Feed saved images or mocked perception values into the decision function.

Verify that each input produces the expected state.

## Part C — Add confidence rules
Create at least one rule that prevents unstable decisions, such as:
- minimum contour area;
- center tolerance band;
- require several consistent frames;
- stop if detection disappears.

## Part D — Robot integration at low speed
Only after software-only decision tests pass, connect states to conservative drivetrain actions.

Use a bounded test area and a clear stop procedure.

## Evidence to submit
- decision table;
- perception/decision/action diagram;
- test cases for all states;
- code or pseudocode with separated functions/modules;
- explanation of the no-target safety behavior.

## AI literacy
A system is not intelligent merely because it moves toward a detected target. Students should be able to identify which parts are explicit human-designed rules and which inputs come from perception.

## AI use
AI may review code organization or suggest test cases. Students must verify every state transition and safety condition with their own tests.

## Next lesson
Build a closed-loop vision-guided alignment behavior and measure oscillation, stability and recovery when perception changes.
