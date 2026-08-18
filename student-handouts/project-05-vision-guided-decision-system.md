# Project 05 — Vision-Guided Decision System

## Goal
Connect vision output to explicit robot decisions while keeping perception, decision and action separately testable.

Classify at least three states (for example left/center/right; optional not-found) and map each to an action.

## Evidence
Perception-output definition; decision table; action mapping; offline decision tests; integrated trials; failure cases; latency/oscillation observations when relevant; safe not-found behavior.

Architecture: `Camera → Perception → Symbolic state → Decision → Robot action`.

## Defense
Explain one perception failure and one control/decision failure and how you distinguished them.