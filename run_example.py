from mkPython.halo import mbuild
import time

while True:
    print(mbuild.multi_touch.is_active(1,1))
    time.sleep(0.1)
