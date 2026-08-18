# Project 04 — Color Object Detection

## Goal
Build/test an OpenCV pipeline that detects a target under more than one condition.

`camera/image → color conversion → threshold/mask → cleanup → contours → filtering → box/centroid → target result`

## Evidence
Source frames; thresholds; mask; filtering logic; box/centroid; tests under at least **3 changed conditions** (lighting, distance, background, angle or occlusion); false-positive/false-negative observations.

A detector working on one chosen image is not robust. State where it works and fails. AI may explain APIs or suggest hypotheses; thresholds and robustness claims require your own evidence.