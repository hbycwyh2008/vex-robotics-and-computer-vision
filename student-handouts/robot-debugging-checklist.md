# Robot Debugging Checklist

Use this checklist before asking for help. Change **one major variable at a time** and record what you tested.

## Layer 1 — Power and Connection
- Is the V5 Battery charged and connected securely?
- Is the Brain powered on?
- Is the Controller paired/connected?
- Is the programming cable/connection working?
- Does VEXcode detect the Brain?

## Layer 2 — Device Configuration
- Does the physical motor/sensor port match VEXcode configuration?
- Is motor reversal/direction configured correctly?
- Does VEXcode show the device as connected?
- Did someone move a cable to a different port since the last working version?

## Layer 3 — Mechanical System
- Can wheels/shafts rotate freely by hand when appropriate?
- Is anything rubbing against a wheel, gear or shaft?
- Are shaft collars/spacers positioned correctly?
- Are gears aligned and meshing correctly?
- Is a shaft bent or poorly supported?
- Are fasteners loose?
- Is the mechanism overloaded or flexing excessively?

## Layer 4 — Program Logic
- What exact behavior did you expect?
- What exact behavior happened instead?
- Which line/function/state should cause the behavior?
- Are conditions using the intended comparison and units?
- Are loops running too quickly or never ending?
- Is the program entering the state/function you think it is?

## Layer 5 — Sensor Data
- What raw value is the sensor actually reporting?
- Is the value plausible?
- Was the sensor calibrated if required?
- Is the threshold based on measured data?
- Does lighting/distance/background affect the reading?
- Is the sensor mounted securely and aimed correctly?

## Layer 6 — Test Procedure
- Is the robot starting from the same position/orientation?
- Is battery level similar between tests?
- Did you change more than one variable?
- Are you measuring the result consistently?
- Did you repeat the trial enough times to know whether the change helped?

## Debugging Log Format
Write one entry before making another major change:

> **Symptom:**
>
> **Most likely layer:** Mechanical / Electrical / Configuration / Code / Sensor / Test procedure
>
> **Hypothesis:**
>
> **Test:**
>
> **Evidence:**
>
> **Decision:** Keep / Revert / Test again / Escalate

## When to Ask the Teacher
Ask after you can show:
1. the exact symptom;
2. the last known working state;
3. at least one test you already performed;
4. the evidence from that test;
5. what you think the next hypothesis is.

"It doesn't work" is not a debugging report.
