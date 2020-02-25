# import _thread

import mkPython.halo as halo
import mkPython.mbuild as mbuild
import time,math,random

while True:
    halo.led.show_all(0,0,mbuild.dual_rgb_sensor.get_intensity("RGB1"))
    # print(mbuild.dual_rgb_sensor.get_intensity("RGB1"))
    # halo.led.show_all(100, 0, 0)
    # time.sleep(0.1)
