# GitHub / Markdown Engineering Portfolio Guide

Every student maintains a portfolio that shows **what was built, what failed, what was changed, and what evidence supports the final result**.

## Recommended Project Entry Structure

Use one folder or Markdown page per major project.

### 1. Project Title and Goal
State the problem in one or two sentences.

### 2. Requirements and Constraints
List what the robot/system must do and any limits on hardware, time, field size, sensors, or safety.

### 3. Design
Include:
- photos or sketches;
- mechanism explanation;
- motor/sensor port map;
- software/state diagram when relevant;
- computer-vision pipeline when relevant.

### 4. Code
Link to or include the relevant code.

Explain the most important functions, states, thresholds or decision rules. Do not paste code without explanation.

### 5. Testing
Show real evidence:
- repeated trial table;
- success rate;
- measurements;
- annotated screenshots;
- photos/video links if allowed by school policy.

### 6. Debugging and Iteration
Include at least one meaningful example using:

**Symptom → Hypothesis → Test → Evidence → Decision**

### 7. Final Result
State what the system can reliably do. Avoid claims that are not supported by tests.

### 8. Limitations
Identify at least one important weakness or failure condition.

### 9. Reflection
What would you improve with more time?

### 10. AI Assistance Disclosure
If AI tools were used, record:
- tool;
- task/question;
- useful suggestion;
- how it was checked;
- what the student changed or debugged independently.

## Minimum Evidence by Project Type

### Robot Build / Mechanism
- build photo(s)
- labeled subsystem explanation
- at least one test result
- iteration evidence

### Robot Programming / Autonomous
- code or repository link
- state/logic explanation
- repeated run data
- failure analysis

### Computer Vision
- input and annotated output screenshots
- threshold/filter values
- test conditions
- false-positive / false-negative discussion

### Final Capstone
- system architecture
- requirements traceability
- integrated code/build evidence
- repeated final validation
- limitations
- final demo evidence

## Commit Expectations
Use meaningful commit messages such as:
- `fix drivetrain motor direction`
- `add distance sensor stop threshold`
- `test HSV mask under dim lighting`
- `reinforce lift shaft support`

Avoid a history made only of messages like `update`, `stuff`, or `final final`.

## Quality Standard
A strong portfolio should let a reader understand **how the engineering changed over time**, not only what the final robot looked like.
