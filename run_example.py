import halo
import time,math

a = 0
while True:
    a += 1 
    # led.show_all(0,math.fabs(math.sin(a/100)) *100 + 3,0, 100)
    if halo.touchpad1.is_touched():
        halo.led.show_all(100, 100, 0, 100)
    else:
        halo.led.show_all(0, 0, 0, 100)
        
