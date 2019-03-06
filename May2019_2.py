"""
Script to write a given word on paper
IMPORTANT: Assumes Vector is facing the user, and that is the start point
"""
import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
import time

# Constants
J_LENGTH = 100
O_LENGTH = 80
NEXT_LETTER = 50
SPEED = 50

def writeLetter(robot, letter):
    if letter == 'j':
        robot.behavior.set_lift_height(0.0) # bring down the lift
        robot.behavior.drive_straight(distance_mm(J_LENGTH), speed_mmps(SPEED))
        robot.behavior.turn_in_place(degrees(-45))
        robot.behavior.set_lift_height(1.0) # bring up the lift
        robot.behavior.turn_in_place(degrees(45))
        # go back to initial position
        robot.behavior.turn_in_place(degrees(180))
        robot.behavior.drive_straight(distance_mm(J_LENGTH - 10), speed_mmps(SPEED)) # slightly shorter than above
        robot.behavior.turn_in_place(degrees(-90))
        robot.behavior.drive_straight(distance_mm(NEXT_LETTER), speed_mmps(SPEED)) 
        robot.behavior.turn_in_place(degrees(-90))

    elif letter == 'o':
        robot.behavior.drive_straight(distance_mm(O_LENGTH), speed_mmps(SPEED))
        robot.behavior.set_lift_height(0.0) # bring down the lift
        robot.behavior.turn_in_place(degrees(360))
        robot.behavior.set_lift_height(1.0) # bring up the lift
        # go back to initial position
        robot.behavior.turn_in_place(degrees(180))
        robot.behavior.drive_straight(distance_mm(100), speed_mmps(SPEED)) # TODO: check distance to move back
        robot.behavior.turn_in_place(degrees(-90))
        robot.behavior.drive_straight(distance_mm(50), speed_mmps(SPEED)) # TODO: check time to move for next letter
        robot.behavior.turn_in_place(degrees(-90))

    elif letter == 'y':
        robot.behavior.turn_in_place(degrees(45))
        robot.behavior.set_lift_height(0.0) # bring down the lift
        robot.behavior.drive_straight(distance_mm(80), speed_mmps(SPEED))
        robot.behavior.set_lift_height(1.0) # bring up the lift
        robot.behavior.drive_straight(distance_mm(25), speed_mmps(SPEED)) # align itself TODO: highlighy depends on sharpie
        robot.behavior.turn_in_place(degrees(90))
        robot.behavior.drive_straight(distance_mm(-140), speed_mmps(SPEED)) # align itself
        robot.behavior.set_lift_height(0.0) # bring down the lift
        robot.behavior.drive_straight(distance_mm(120), speed_mmps(SPEED))
        robot.behavior.set_lift_height(1.0) # bring up the lift
        robot.behavior.turn_in_place(degrees(180)) # look to the user
        robot.behavior.drive_straight(distance_mm(160), speed_mmps(SPEED))


def writeWord():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Start moving ...")
        robot.behavior.set_lift_height(1.0) # bring up the lift
        writeLetter(robot, 'j')
        writeLetter(robot, 'o')
        writeLetter(robot, 'y')

        robot.anim.play_animation('anim_greeting_imhome_01')

if __name__ == "__main__":
    writeWord()
