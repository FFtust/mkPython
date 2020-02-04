import engine.protocol.F3F4
import engine.database

import link.commu_uart

uart = link.commu_uart.uart_link(["COM0", 115200])

protocol = engine.protocol.F3F4.F3F4_frame()
protocol.register_frame_process(engine.database.database)

def set_channel(channel, bauadrate = 115200):
    global uart, protocol
    uart.config([channel, str(bauadrate)])
    uart.open()
    uart.start_listening()

    uart.rigister_protocol_parse_handle(protocol)

    run_into_online_mode()

def run_into_online_mode():
    global uart, protocol
    
    protocol.send_protocol(bytes([0x0d, 0x00, 0x01]))