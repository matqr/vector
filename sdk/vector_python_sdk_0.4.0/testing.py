#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Testing script for random playful things with Vector
Installation:
https://forums.anki.com/t/vector-sdk-pre-alpha-notes-and-tips/21038

References:
https://forums.anki.com/t/interact-with-vector-without-stopping-built-in-behaviors/21475/10
https://forums.anki.com/t/vector-and-having-him-wait-to-finish-saying-something/22039
https://www.kinvert.com/anki-vector-examples-tutorials-projects-python-sdk/
https://forums.anki.com/t/vectorcloud-a-web-interface-for-anki-vector/22129
https://pastebin.com/NEZbGG88

Ideas to test:
-Sing happy birthday
-Pick up it's birthday hat
-Change eye Colors
"""

import anki_vector

def speak():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Say 'Hello World'...")
        # robot.say_text("Joy, Good luck in your game today, you got this")
        robot.say_text("TESTING")
        # wait to finish saying the sentence? use time.sleep
        # print(robot.anim.load_animation_list())
        robot.anim.play_animation('anim_greeting_imhome_01')

if __name__ == "__main__":
    speak()
