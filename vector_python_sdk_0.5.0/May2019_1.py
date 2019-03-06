"""
Script to sing Happy Birthday song
Notes:
    F C7 Bb
"""
import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
import time

def sing():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Start singing ...")
        time.sleep(3)
        robot.say_text("Are you ready Ma tea") # phonetics

        time.sleep(3)
        robot.say_text("Are you ready Ma tea") # phonetics
        robot.say_text("one")
        robot.say_text("two")
        robot.say_text("three")
        
        for _ in range(2):
            robot.behavior.turn_in_place(degrees(30))
            robot.say_text("Happy")
            robot.behavior.turn_in_place(degrees(-30))
            robot.say_text("birthday") # F, C7
            robot.behavior.turn_in_place(degrees(30))
            robot.say_text("to")
            robot.behavior.turn_in_place(degrees(-30))
            robot.say_text("you") # C7, F
            robot.behavior.turn_in_place(degrees(30))
        
        robot.say_text("Happy")
        robot.behavior.turn_in_place(degrees(-30))
        robot.say_text("birthday") # F
        robot.behavior.turn_in_place(degrees(30))
        robot.say_text("dear")
        robot.behavior.turn_in_place(degrees(-30))
        robot.say_text("Joy") # Bb
        robot.behavior.turn_in_place(degrees(30))
        robot.say_text("Happy")
        robot.behavior.turn_in_place(degrees(-30))
        robot.say_text("birthday") # F
        robot.behavior.turn_in_place(degrees(30))
        robot.say_text("to") # C7
        robot.behavior.turn_in_place(degrees(-30))
        robot.say_text("you") # F
        robot.anim.play_animation('anim_greeting_imhome_01')

if __name__ == "__main__":
    sing()
