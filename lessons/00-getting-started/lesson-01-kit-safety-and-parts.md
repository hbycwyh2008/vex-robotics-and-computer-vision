# Lesson 01 — From Parts to Intelligent Systems

## Course Position

Week 1 · Unit 00 — Getting Started  
**Recommended duration:** 90 minutes

This is the first meeting of **VEX Robotics and Computer Vision**. The goal is not to spend Day 1 listening to a syllabus or memorizing a parts list. Students should immediately experience the course as an engineering class built around **observation, evidence, discussion, building, testing, and explanation**.

The first lesson introduces the course's central idea:

> **A robot is a system that can sense or receive information, make a decision, and produce an action.**

Students begin with a box of apparently unrelated hardware and finish by explaining how those components can eventually become a system that follows the course arc:

> **Perception → Decision → Action**

---

## Driving Question

> **How does a box of metal, motors, electronics, sensors, and code become a robot that can perceive, decide, and act?**

Keep this question visible throughout the lesson. Students should return to it at the end rather than receiving a complete answer at the beginning.

---

## Learning Objectives

Students will be able to:

- explain why a robot should be understood as a **system**, not a collection of independent parts;
- classify major VEX V5 components by the job they perform in the system;
- trace a simple **power / information / action** pathway through VEX hardware;
- identify and justify essential laboratory safety practices;
- explain the course learning flow **Learn → Practice → Rebuild → Share**;
- explain why a working team robot is not, by itself, proof of individual mastery;
- create the first Team Engineering Notebook entry using direct evidence;
- identify how today's hardware foundations will later connect to sensors, autonomous behavior, and computer vision.

---

## Student Success Criteria

By the end of class, a student should be able to look at the kit and say, in their own words:

1. **What are the major subsystems of this robot?**
2. **Where does power come from?**
3. **Where can information enter the system?**
4. **What part can make a physical action happen?**
5. **What could become unsafe if we handle the system badly?**
6. **What evidence would prove that I actually understand the system?**

Students do **not** need to memorize every VEX part name on Day 1.

---

## Mastery Target

**Target for Lesson 01: Level 2 — Explain While Looking**

Students may use the physical kit, their system map, and course posters while explaining.

Level 3 rebuilding is introduced as a future expectation but is not required today.

See [`../../mastery-levels.md`](../../mastery-levels.md).

---

## Required Resources

### Per team

- VEX V5 Competition Starter Kit
- V5 Brain
- V5 Controller
- V5 Battery
- at least one V5 Smart Motor
- Smart Cable
- representative structural and motion hardware
- hex keys / nut drivers appropriate for VEX hardware
- labeled storage tray or bins
- Team Engineering Notebook or approved digital equivalent
- [Individual Engineering Learning Log](../../student-handouts/individual-engineering-learning-log.md)

### Classroom resources

- sticky notes or index cards
- chart paper / mini-whiteboard for each team
- classroom posters in [`../../public-documents/posters/`](../../public-documents/posters/README.md)

Recommended posters:

- [Our Classroom Flow](../../public-documents/posters/classroom-flow.svg)
- [Mastery Level](../../public-documents/posters/mastery-level.svg)
- [AI Use Policy](../../public-documents/posters/ai-use-policy.svg)
- [CS Competition Pathways](../../public-documents/posters/cs-competition-pathways.svg)

---

# Before Class — Teacher Setup

Do not begin with all parts already labeled for students.

For each team, place a small representative set of components on the table, for example:

- V5 Brain;
- Controller;
- Battery;
- Smart Motor;
- Smart Cable;
- wheel;
- gear;
- shaft;
- bearing;
- spacer or shaft collar;
- C-channel or structural member;
- fastener.

Students should first infer **function** before being given complete terminology.

Also prepare six short safety-scenario cards using the scenarios later in this lesson.

If possible, keep one completed or partially completed VEX robot visible in the room. Do not explain it yet. It serves as a preview of where the loose parts are going.

---

# 0–8 min — Launch: “Is This a Robot Yet?”

Place the Brain, Battery, Motor, Controller, structural hardware, and several mechanical parts where students can inspect them.

Do **not** begin by naming the components.

### Team task

Students examine the objects and create two quick lists:

**We notice...**  
Record only observations that can be supported by visible evidence.

**We think...**  
Record hypotheses about what the components might do.

Then teams respond to the claim:

> **“These parts are already a robot.”**

Each team must choose **agree, disagree, or partly agree** and give one reason.

### Purpose

The discussion should surface the idea that a robot requires relationships among components: structure, power, control, sensing/information, and action.

Do not resolve every disagreement yet.

---

# 8–18 min — Discover the Course Destination

Give teams these three cards:

- **Perception**
- **Decision**
- **Action**

Ask teams to arrange the cards into the sequence they think an autonomous robot would need.

Then give one concrete scenario:

> A camera sees a red object. The robot decides the object is a target. The robot drives toward it.

Students match each part of the scenario to the three cards.

Reveal the course-level system model:

> **Perception → Decision → Action**

Explain only what students need now:

- **Perception:** sensors or cameras turn something in the physical world into usable information.
- **Decision:** software uses that information to choose what should happen.
- **Action:** motors and mechanisms change something in the physical world.

### Course connection

Tell students that much later in the course they will use **computer vision** as part of perception. Today they are investigating the physical system that makes the final action possible.

> We are not starting with computer vision because an intelligent robot still needs reliable hardware, control, testing, and engineering evidence.

---

# 18–35 min — Investigation: What Job Does Each Part Perform?

## Challenge

> **Organize the kit by function, not by appearance.**

Teams sort the representative components into categories they invent themselves.

Do not provide the official subsystem labels immediately.

For each category, teams must write:

- what the parts in this group appear to have in common;
- what job the group might perform;
- one piece of physical evidence supporting the idea.

### After teams commit to a first model

Introduce the course's subsystem language:

1. **Structure** — holds the robot together and establishes geometry.
2. **Motion / transmission** — transfers rotation or movement through wheels, gears, shafts, bearings, spacers, collars, or related parts.
3. **Actuation** — motors convert electrical energy into mechanical motion.
4. **Power** — battery and electrical connections provide usable electrical energy.
5. **Control / computation** — the Brain and software coordinate the system.
6. **Human input / communication** — the Controller provides driver commands.
7. **Sensing / perception** — sensors and later cameras provide information about the physical world.

Teams now **revise**, rather than erase, their original categories.

### Required evidence

Each team selects at least **8 representative components** and records:

| Component | System role | Evidence / reasoning | Connects or interacts with |
|---|---|---|---|
| Example: Smart Motor | Actuation | Has an output shaft and electrical/data connection | Brain, mechanism |

The emphasis is on **role and relationship**, not memorizing inventory numbers.

---

# 35–48 min — Safety Investigation: Find the Failure Before It Happens

Do not read a safety list aloud.

Give each group one or two safety scenarios. Students identify:

1. **What could go wrong?**
2. **What part of the system is creating the risk?**
3. **What safer engineering behavior prevents the problem?**

## Suggested scenario cards

### Scenario A — Unexpected motion
A student adjusts a gear while the robot is powered and another student touches the Controller.

### Scenario B — Battery misuse
A battery is dropped, crushed under equipment, modified, or connected in an unsafe way.

### Scenario C — Protruding shaft
A long metal shaft extends beyond the frame into a walking or working area.

### Scenario D — Tool misuse
A student uses the wrong hex key size and continues applying force after the screw begins to strip.

### Scenario E — Moving mechanism
Loose hair, clothing, fingers, or cables are close to a wheel, gear, or moving mechanism during testing.

### Scenario F — Test path
A team tests a moving robot while another student is standing directly in its expected path.

### Student output

For each scenario, write:

> **Hazard → Possible consequence → Safer action**

### Teacher safety validation

After students present, establish the non-negotiable baseline:

- Power the robot down before changing wiring or mechanisms unless a specific supervised test requires power.
- Never short, puncture, crush, modify, or misuse a battery.
- Keep fingers, hair, clothing, jewelry, and cables away from moving mechanisms.
- Treat protruding shafts and sharp/cut metal edges as hazards.
- Use the correct tool size and stop before damaging hardware.
- Do not force screws or overtighten fasteners.
- Keep the work area clear enough to find dropped hardware and tools.
- Never place a person in the expected path of robot motion.
- Stop a test immediately if the system behaves in a way the team did not predict.

The goal is not compliance through memorization. Students should understand the **mechanism of the hazard**.

---

# 48–63 min — System Challenge: Trace Power, Information, and Action

Teams now receive the Brain, Battery, Smart Motor, Smart Cable, and Controller.

## Challenge

Create a diagram showing how these components could participate in a functioning robot.

Students use three arrow labels:

- **POWER**
- **INFORMATION / COMMAND**
- **PHYSICAL ACTION**

Teams should reason about questions such as:

- Which component stores energy?
- Which component can perform computation?
- Which component can create motion?
- Where can a human command enter the system?
- Which connections carry electrical power, information, or both?

### Optional physical connection

Students may connect approved cables and components **only after the team's safety check**. Do not require motor motion or programming in Lesson 01.

The purpose is to build a correct mental model before students begin the TrainingBot.

### Transfer prompt

Add a future camera or sensor to the diagram.

Ask:

> **Where would perception enter the system?**

Teams revise their diagram to show:

> **Physical world → Perception → Decision → Action → Changed physical world**

This is the first systems model that will reappear throughout the entire course.

---

# 63–72 min — Course Learning Culture: Discover the Pattern

Only now introduce the shared course posters.

Rather than giving a syllabus lecture, teams complete a short **Notice → Connect → Predict** gallery walk.

For each assigned poster:

1. **Notice:** What is one important idea you see?
2. **Connect:** Where did that idea already appear in today's investigation?
3. **Predict:** How will this affect the way we work when we start building the robot?

Introduce the shared learning flow:

> **Learn → Practice → Rebuild → Share**

Connect it to what students have already done today:

- **Learn:** inspect and make sense of unfamiliar hardware;
- **Practice:** classify parts and model the system;
- **Rebuild:** reproduce the system model with less support in future lessons;
- **Share:** explain and defend the model with evidence.

Then introduce the VEX engineering cycle:

> **Predict → Build / Program → Test → Debug → Redesign → Retest → Document → Explain / Transfer**

Two course rules should be explicit:

> **Working once is not mastery.**

> **A team result does not automatically prove individual mastery.**

Avoid a long discussion of every mastery level. Students only need to understand that the course measures increasing independence over time.

---

# 72–82 min — Engineering Notebook: Record Evidence, Not a Story

Students create the first Team Engineering Notebook entry.

## Required entry

**Date / lesson / team members**

### 1. Driving question
How does a collection of components become a robotic system?

### 2. Initial thinking
One claim or assumption our team made near the beginning of class.

### 3. Evidence
Include:

- one photo of the team kit or subsystem organization;
- the 8-component subsystem table;
- the **Power / Information / Action** system diagram;
- one safety scenario and the team's reasoning.

### 4. Revision
One idea our team changed after examining evidence.

### 5. Next step
What do we need to learn before these components can become a functioning TrainingBot?

Introduce the recurring notebook pattern:

> **Goal → Design / Change → Test → Problem → Diagnosis → Decision → Retest → Next Step**

Explain that today's investigation does not use every stage yet. Future build sessions will.

See:

- [Engineering Notebook Guide](../../student-handouts/engineering-notebook-guide.md)
- [Team Engineering Notebook Template](../../student-handouts/engineering-notebook-template.md)

---

# 82–87 min — Individual Rebuild: Can You Explain the System Without Your Team?

Team materials are temporarily covered or moved aside except for the physical VEX components.

Each student independently sketches a simplified system using at least:

- Battery
- Brain
- Controller or future sensor/camera input
- Motor
- physical action

They label where **power**, **information**, and **action** occur.

Then students complete three lines in the [Individual Engineering Learning Log](../../student-handouts/individual-engineering-learning-log.md):

1. **One part of the robot system I can now explain:**
2. **One idea my team changed because of evidence:**
3. **One thing I still cannot explain without help:**

This is the first clear separation between **team success** and **individual mastery**.

---

# 87–90 min — Reset + Exit Claim

## Physical reset

Teams:

- return tools and loose parts;
- organize components by the agreed storage system;
- confirm batteries and electronics are stored safely;
- save notebook evidence;
- leave the workspace ready for the next class.

## Exit claim

Students answer individually in one or two sentences:

> **A robot is more than a collection of parts because...**

A strong answer should refer to **relationships among subsystems**, not simply list components.

---

# Evidence to Submit

## Team evidence

1. Photo of organized representative kit components.
2. 8-component subsystem table.
3. Power / Information / Action system diagram.
4. First Team Engineering Notebook entry.

## Individual evidence

5. Individual simplified system sketch.
6. Three-line Individual Engineering Learning Log entry.
7. Exit claim.

---

# AI Use

AI is **not needed** to identify the physical components in this lesson.

If students use AI for terminology or explanation, every claim must be checked against:

- the actual hardware;
- VEX documentation;
- observed evidence.

AI may not invent:

- component observations;
- measurements;
- test results;
- notebook evidence;
- work the student or team did not actually perform.

The first lesson should establish an important course principle:

> **AI can assist engineering reasoning, but it cannot replace contact with the physical system or responsibility for verifying evidence.**

Refer to the [AI Use Policy poster](../../public-documents/posters/ai-use-policy.svg).

---

# Teacher Look-Fors

During the lesson, look for evidence that students are moving beyond surface identification.

### Strong evidence

A student says:

- “The motor belongs in actuation because it turns electrical energy into motion.”
- “The Brain does not make the robot move by itself; it coordinates devices and executes control logic.”
- “A camera would provide perception, but the system still needs decision logic and motors to act.”
- “We changed our categories because two parts looked similar but had different functions.”
- “The danger is not just that the gear is sharp; it can begin moving unexpectedly while the robot is powered.”

### Weak evidence

A student only says:

- “This is a motor.”
- “This is the battery.”
- “The teacher said not to touch it.”
- “It goes in this bin because it looks like the other one.”

Use follow-up prompts that ask for **function, evidence, relationship, or mechanism**.

---

# Common Misconceptions to Surface Early

### “A robot is basically a machine with motors.”
A motorized mechanism may move, but later autonomous robotics requires sensing/perception, computation, decision logic, and controlled action.

### “The Controller is the brain.”
The Controller is primarily a human-input device. The V5 Brain runs robot programs and communicates with connected devices.

### “Computer vision is separate from robotics.”
In this course, computer vision becomes one way the robot or software system can obtain information about the environment.

### “If the robot works, everyone understands it.”
A successful team product is evidence about the **system**, not automatic evidence of every student's individual mastery.

### “Documentation happens after the project.”
Engineering documentation is strongest when observations, failures, tests, and decisions are recorded while they occur.

---

# Differentiation

## If students are completely new to robotics

- provide a small word bank after the first sorting attempt;
- reduce the required component table from 8 to 6 parts;
- let students label the system diagram with cards before writing explanations.

## If students already have VEX experience

Do not let them turn the lesson into a vocabulary race.

Ask them to:

- distinguish **power flow** from **information flow**;
- identify where closed-loop sensor feedback would enter the system;
- explain why a correct component can still fail because of poor integration;
- propose one failure mode that would require evidence rather than guessing.

---

# Teacher Notes

- **Do not open the course with a syllabus lecture.** Students should experience the course's learning culture before you name it.
- **Do not turn Day 1 into inventory memorization.** Students need a functional mental model of the robot more than a long parts vocabulary list.
- Let teams make an imperfect first classification. The revision is part of the learning.
- Keep direct instruction short. Most explanations should come **after students have something concrete to explain**.
- Photograph the original kit organization before students handle large quantities of hardware.
- Safety should be taught through causal reasoning: **hazard → mechanism → consequence → prevention**.
- Protect the final individual rebuild. It provides much better evidence of understanding than asking the whole class, “Does everyone understand?”
- The computer-vision connection should be brief but explicit. Students should understand on Day 1 why robotics and computer vision belong in the same course.

---

# Next Lesson

Students begin the official **TrainingBot — Competition Kit** build.

The next lesson should move students from today's system model into real assembly questions:

- Why is structure built in a particular sequence?
- How do mechanical connections constrain motion?
- How do we distinguish **following a build guide** from **understanding the mechanism**?

Students will begin at **Level 1 — Follow and make it work**, explain their assembly decisions at **Level 2**, and later use rebuild opportunities to progress toward Levels 3–5.
