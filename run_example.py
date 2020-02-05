import halo
import time,math

a = 0
while True:
    a += 1 
    # led.show_all(0,math.fabs(math.sin(a/100)) *100 + 3,0, 100)
    # if halo.touchpad0.is_touched():
    #     halo.led.ring_graph(100)
    # else:
    #     halo.led.show_all(0, 0, 0)
        
    print(halo.motion_sensor.get_acceleration('x'))
    time.sleep(0.5)
