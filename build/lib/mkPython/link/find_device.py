import serial.tools.list_ports
import time
import re

BOARD_IDS = set([
    (0x1A86, 0x7523),  # halocode usb-uart VID, PID
])

#####list serial ports####
def get_port(ipt = "first"):
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) == 0:
        print('no port found')
    else:
        for i in range(0,len(port_list)):
            v_pid = (port_list[i].vid, port_list[i].pid)
            if v_pid in BOARD_IDS:
                return port_list[i][0]
