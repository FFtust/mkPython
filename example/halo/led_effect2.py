from mkPython import halo
import time,math,random

i = 0
while True:
    val = math.fabs(math.sin(i / 40)) * 50
    halo.led.show_all(val, 0, val)
    i = i + 1