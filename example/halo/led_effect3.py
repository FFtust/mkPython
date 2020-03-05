from mkPython import halo
import time,math,random

i = 0

halo.led.show_ring('r b b b b')
while True:
    val = halo.microphone.get_loudness()
    halo.led.show_all(100, 0, 0, val)
    time.sleep(0.02)
