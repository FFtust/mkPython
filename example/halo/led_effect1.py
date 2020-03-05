from mkPython import halo
import time,math,random


while True:
    i = 0
    j = 0
    k = 0
    import random

    H_J = 1
    while True:
        data = [0] * 36
        for t in range(12):
            red  = 32 * (1 + math.sin((t / 2.0 + j / 4.0) * H_J) )
            green = 32 * (1 + math.sin((t / 1.0 + j / 9.0 + 2.1)) * H_J )
            blue = 32 * (1 + math.sin((t / 3.0 + k / 14.0 + 4.2)) * H_J )
            data[t * 3] = int(red)
            data[t * 3 + 1] = int(green)
            data[t * 3 + 2] = int(blue)
        data = bytearray(data)
        halo.led.show_full_color(data)
        j += random.randint(1, 6) / 6.0
        j += random.randint(1, 6) / 6.0
        k += random.randint(1, 6) / 6.0