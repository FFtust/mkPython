# coding:utf-8
from mkPython.application.game.game import set_screen_update_func, game_base, sprite_create, RIGHT_MEET, LEFT_MEET,UP_MEET,DOWN_MEET
from mkPython.application.game.game_simulator import play_music, set_dir, simulator_quit, get_events, initialize, update_screen

from pygame.locals import *

import time
import random
import sys

# screen set as simulator
set_dir("UPRIGHT")
set_screen_update_func(update_screen)

# game control
game = game_base()

score = 0
a_s = '10101010000000000000000000000000'
b_s = '10380000000000000000000000000000'
c_s = '30300000000000000000000000000000'
d_s = '10180800000000000000000000000000'
e_s = '30101000000000000000000000000000'
f_s = '08181000000000000000000000000000'

sprite_num = 6
sprites = [a_s, b_s, c_s, d_s, e_s, f_s]
current_script = None
move_lock_flag = False

move_flag = 0
down_speed = 10

def line_remove_process():
    global score
    screen = game.get_screen()
    background = game.get_background()
    removed_flag = False
    i = 0
    while i < 16:
        if screen[i] & 0xff == 0xff:
            score += 1
            removed_flag = True
            del background[i]
            background.insert(0, 0x00)
            play_music("score.wav")
        i += 1
    if removed_flag:
        pass
    game.set_background(background)

def move_control():
    global down_speed, current_script, move_lock_flag
    global quit
    if current_script == None :
        time.sleep(0.2)
        return

    for event in get_events():
        if event.type==QUIT:
            quit = True
            simulator_quit()

        elif event.type == 2:
            if event.key == K_LEFT and move_lock_flag == False:
                current_script.up()
                if game.background_collision_check(current_script):
                    current_script.down()

            elif event.key == K_RIGHT and move_lock_flag == False:
                current_script.down()
                if game.background_collision_check(current_script):
                    current_script.up()

            elif event.key == K_UP and move_lock_flag == False:
                current_script.rotate()

            elif event.key == K_DOWN and move_lock_flag == False:
                down_speed = 2

    temp = current_script.meet_border_check()
    if temp == UP_MEET:
        current_script.down()
        while current_script.meet_border_check() == UP_MEET:
            current_script.down()
    elif temp == DOWN_MEET:
        current_script.up()
        while current_script.meet_border_check() == DOWN_MEET:
            current_script.up()

def work():
    global current_script, down_speed, score, move_lock_flag
    game.game_start()
    game.set_background([0] * 16)
    while True:
        index = random.randint(0, sprite_num - 1)
        current_script = sprite_create(sprites[index])
        game.add_sprite(current_script)
        current_script.left(2)
        if game.background_collision_check(current_script):
            game.del_sprite(current_script)
            current_script = None
            game.game_over()
            print("your score is:", score)
            score = 0
            break
        count = 1
        down_speed = 10
        while True:
            if count % down_speed == 0:
                current_script.right()
            
            if current_script.meet_border_check() == RIGHT_MEET:
                move_lock_flag = True
                current_script.left()
                break

            if game.background_collision_check(current_script):
                move_lock_flag = True
                current_script.left()
                break

            move_control()

            time.sleep(0.05)
            count += 1

        time.sleep(0.1)
        game.set_background(game.get_screen())
        current_script.hide()
        time.sleep(0.1)
        line_remove_process()
        game.del_sprite(current_script)
        move_lock_flag = False


work()