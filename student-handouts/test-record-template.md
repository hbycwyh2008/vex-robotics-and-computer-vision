# Engineering Test Record Template

Use this sheet when a claim depends on **performance, reliability, accuracy, or improvement**. One successful run is not enough evidence.

## Test Identity

- **Date:**
- **Lesson / project:**
- **Team:**
- **System / subsystem:**
- **Question being tested:**

## Baseline

What is the current system configuration before the change?


## Variable

What one factor are you changing?


## Controlled Conditions

What will stay the same between trials?


## Prediction

> If we change ___, then ___ should happen because ___.

## Trial Data

| Trial | Condition / Setting | Measured Result | Success? | Notes |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Add more trials when reliability matters.

## Failure Pattern

What repeated error, inconsistency, or failure mode do you see?


## Engineering Decision

Based on the evidence, choose one:

- [ ] Keep the current design / setting
- [ ] Modify the design / setting
- [ ] Revert the change
- [ ] Run more trials
- [ ] Redesign the test

Explain why:


## Retest Comparison

After the change, repeat the relevant test.

| Metric | Before | After | Better / Worse / No Clear Change |
|---|---:|---:|---|
| | | | |
| | | | |

## Conclusion

What can you claim from the evidence?


What can you **not** claim yet?


## Evidence Links

- Engineering notebook entry:
- Photo / video:
- GitHub commit / code:
- Other evidence:

---

> **Engineering rule:** use data to justify the next change. Do not invent measurements, and do not treat one lucky run as proof of reliability.
