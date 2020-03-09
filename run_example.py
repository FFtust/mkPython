from mkPython import mbuild
import time

rgb_color_index = 0
gesture_flag = True


def button_test():
    print("button1_state:" , mbuild.fingertip_piano.is_button_pressed("button1"))
    print("button2_state:" , mbuild.fingertip_piano.is_button_pressed("button2"))
    button1_count = mbuild.fingertip_piano.get_button_count("button1")
    button2_count = mbuild.fingertip_piano.get_button_count("button2")
    print("button1_count:" , button1_count)
    print("button2_count:" , button2_count)
    if(button1_count > 20):
        mbuild.fingertip_piano.reset_button_count("button1")
    if(button2_count > 20):
        mbuild.fingertip_piano.reset_button_count("button2")
    time.sleep(0.1)


def touchpad_test():
    print("touchpad1_state:" , mbuild.fingertip_piano.is_touchpad_pressed("touchpad1"))
    print("touchpad2_state:" , mbuild.fingertip_piano.is_touchpad_pressed("touchpad2"))
    print("touchpad3_state:" , mbuild.fingertip_piano.is_touchpad_pressed("touchpad3"))
    print("touchpad4_state:" , mbuild.fingertip_piano.is_touchpad_pressed("touchpad4"))
    touchpad1_value = mbuild.fingertip_piano.get_touchpad_value("touchpad1")
    touchpad2_value = mbuild.fingertip_piano.get_touchpad_value("touchpad2")
    touchpad3_value = mbuild.fingertip_piano.get_touchpad_value("touchpad3")
    touchpad4_value = mbuild.fingertip_piano.get_touchpad_value("touchpad4")
    print("touchpad1_value:" , touchpad1_value)
    print("touchpad2_value:" , touchpad2_value)
    print("touchpad3_value:" , touchpad3_value)
    print("touchpad4_value:" , touchpad4_value)
    time.sleep(0.1)


def joystick_test():
    print("joystick_up_state:" , mbuild.fingertip_piano.is_joystick_active("up"))
    print("joystick_down_state:" , mbuild.fingertip_piano.is_joystick_active("down"))
    print("joystick_left_state:" , mbuild.fingertip_piano.is_joystick_active("left"))
    print("joystick_right_state:" , mbuild.fingertip_piano.is_joystick_active("right"))
    print("joystick_x_value:" , mbuild.fingertip_piano.get_joystick("x"))
    print("joystick_y_value:" , mbuild.fingertip_piano.get_joystick("y"))
    time.sleep(0.1)



def gestrue_test():
    global rgb_color_index
    global gesture_flag
    gesture = mbuild.fingertip_piano.get_gesture()
    if gesture == 1 and gesture_flag == True:
        gesture_flag = False
        rgb_color_index += 1
    elif gesture == 0:
        gesture_flag = True

    index = rgb_color_index % 4
    if index == 0:
        mbuild.fingertip_piano.set_rgb(100, 0, 0)
    elif index == 1:
        mbuild.fingertip_piano.set_rgb(0, 100, 0)
    elif index == 2:
        mbuild.fingertip_piano.set_rgb(0, 0, 100)
    elif index == 3:
        mbuild.fingertip_piano.set_rgb(100, 100, 0)

    # if gesture == 2:
    #     mbuild.fingertip_piano.set_rgb(0, 100, 0)
    # elif gesture == 3:
    # 	mbuild.fingertip_piano.set_rgb(0, 0, 0)
    print("gesture_is:" , mbuild.fingertip_piano.get_gesture())
    print("distance_is:" , mbuild.fingertip_piano.get_distance())
    time.sleep(0.01)



while True:
    # button_test()
    touchpad_test()
    # joystick_test()
    # gestrue_test()

