import _thread

import mkPython.halo as halo
import time,math,random

# a = 0
# while True:
#     a += 1 
#     # led.show_all(0,math.fabs(math.sin(a/100)) *100 + 3,0, 100)
#     # if halo.touchpad0.is_touched():
#     #     halo.led.ring_graph(100)
#     # else:
#     #     halo.led.show_all(0, 0, 0)
        
#     print(halo.motion_sensor.get_acceleration('x'))
#     time.sleep(0.5)

def test():
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
        # print(data)
        data = bytearray(data)
            # halo.led.show_single(t+1, red, green, blue)
        halo.led.show_full_color(data)
        # halo.led.show_ring("red green", int(halo.motion_sensor.get_rotation('z')))
        # halo.led.show_all(100, 0, 0, halo.microphone.get_loudness())
        j += random.randint(1, 6) / 6.0
        j += random.randint(1, 6) / 6.0
        k += random.randint(1, 6) / 6.0

# test()
# halo.wifi.start("iPhone fftust", "12345678")
# while True:
#     if halo.pin0.is_touched():
#         halo.led.show_all(100, 0, 0)
#         print(halo.wifi.get_mac())
#     else:
#         halo.led.show_all(0, 0, 0)


while True:
    print(halo.mbuild.dual_rgb_sensor.get_reflected_light("RGB1", 1))
    time.sleep(0.2)
