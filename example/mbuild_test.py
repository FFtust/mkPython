import time

import halo
import mbuild

halo.led.show_all(100, 0, 0)

while True:
    halo.led.show_all(0, 0, mbuild.dual_rgb_sensor.get_intensity("RGB1"))