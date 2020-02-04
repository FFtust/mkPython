import engine.protocol.F3F4
import engine.database

import link.commu_uart

def set_channel(channel, bauadrate = 115200):
	uart = link.commu_uart.uart_link([channel, str(bauadrate)])
	uart.config([channel, str(bauadrate)])
	uart.open()

	protocol = engine.protocol.F3F4.F3F4_frame()
	protocol.register_frame_process(engine.database.database)

	uart.rigister_protocol_parse_handle(protocol)
