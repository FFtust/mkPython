from mkPython import halo
import time

while True:
    if halo.motion_sensor.is_tilted_left():
        print("tilted_left")
        halo.led.show_all(100, 0, 0)
    if halo.motion_sensor.is_tilted_right():
        print("tilted_right")
        halo.led.show_all(0, 100, 0)

    if halo.motion_sensor.is_arrow_up():
        print("arrow_up")
        halo.led.show_all(0, 0, 100)

    if halo.motion_sensor.is_arrow_down():
        print("arrow_down")
        halo.led.show_all(100, 100, 0)

    if halo.motion_sensor.is_rotate_clockwise():
        print("clockwise")
        halo.led.show_all(0, 100, 100)

    if halo.motion_sensor.is_rotate_anticlockwise():
        print("anticlockwise")
        halo.led.show_all(100, 0, 1000)

    if halo.motion_sensor.is_free_fall():
        print("free falling")
        halo.led.show_all(100, 100, 100)
