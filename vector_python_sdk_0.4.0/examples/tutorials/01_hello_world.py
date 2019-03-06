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

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""

import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Say 'Hello World'...")
        # robot.say_text("Joy, Good luck in your game today, you got this")
        robot.say_text("Hello World")
        # print(robot.anim.load_animation_list())
        robot.anim.play_animation('anim_greeting_imhome_01')

        # anim_request = robot.anim.load_animation_list()
        # anim_request.result()
        # anim_names = robot.anim.anim_list
        # for anim_name in anim_names:
        #         print(anim_name)

if __name__ == "__main__":
    main()
