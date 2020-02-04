import engine.protocol.F3F4
import engine.database

import link.commu_uart

uart = link.commu_uart.uart_link(["COM3", "115200"])
uart.config(["COM3", "115200"])
uart.open()

protocol = engine.protocol.F3F4.F3F4_frame()
protocol.register_frame_process(engine.database.database)

uart.rigister_protocol_parse_handle(protocol)

# # uart.write(b"hello")
# uart.start_listening()

# import example.main
from device.halocode import halo 

halo = halo()

halo.led_show_all(126,100,33)
# f3 11 1e 00  28 00 00 00  18 00 6c 65  64 2e 73 68 6f 77 5f 61  6c 6c 28 31  32 36 2c 32  31 31 2c 33 33 29 38 f4  