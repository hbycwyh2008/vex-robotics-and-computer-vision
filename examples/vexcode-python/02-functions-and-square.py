# Classroom pattern: reusable robot behaviors
# Assumption: configured drivetrain object is named `drivetrain`.

from vex import *

DRIVE_SPEED = 30
TURN_SPEED = 25
SIDE_MM = 300
TURN_DEG = 90

def drive_forward(distance_mm):
    drivetrain.set_drive_velocity(DRIVE_SPEED, PERCENT)
    drivetrain.drive_for(FORWARD, distance_mm, MM)


def turn_right(angle_deg):
    drivetrain.set_turn_velocity(TURN_SPEED, PERCENT)
    drivetrain.turn_for(RIGHT, angle_deg, DEGREES)


def drive_square(side_mm):
    for _ in range(4):
        drive_forward(side_mm)
        turn_right(TURN_DEG)


drive_square(SIDE_MM)

# Investigation:
# Does the robot finish at exactly the starting pose?
# Record translation error and orientation error.
# Do not immediately "fix the code"; identify possible mechanical and physical causes.