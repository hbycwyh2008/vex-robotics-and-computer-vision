# Classroom pattern: basic drivetrain motion
# Assumption: VEXcode Devices contains a drivetrain named `drivetrain`.
# Replace names only when your own Devices configuration uses different names.

from vex import *

# VEXcode normally generates device configuration above/beside student code.
# Do not invent motor ports here; configure the physical robot in Devices first.

DRIVE_SPEED = 30
TURN_SPEED = 25

drivetrain.set_drive_velocity(DRIVE_SPEED, PERCENT)
drivetrain.set_turn_velocity(TURN_SPEED, PERCENT)

# Move a measured distance.
drivetrain.drive_for(FORWARD, 300, MM)

# Turn a measured angle.
drivetrain.turn_for(RIGHT, 90, DEGREES)

# Return toward the starting area.
drivetrain.drive_for(REVERSE, 300, MM)

# Investigation:
# 1. Repeat three times from the same start line.
# 2. Measure endpoint error.
# 3. Change DRIVE_SPEED only.
# 4. Does repeatability change?