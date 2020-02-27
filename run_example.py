from mkPython import mbuild
import time

mbuild.colorful_handle.set_rgb(100, 0, 0)

while True:
    print(mbuild.colorful_handle.is_button_pressed("button1"))
    time.sleep(0.1)


# from mkPython import multi_devices
# halo1 = multi_devices.create_new("halo", "COM3")

# halo1.led.show_all(100, 0, 0)