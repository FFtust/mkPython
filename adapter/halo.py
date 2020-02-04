import communication.protocol.F3F4
import communication.channel.commu_uart

uart = communication.channel.commu_uart.uart_link(["COM3", "115200"])
uart.config(["COM3", "115200"])
uart.open()

protocol = communication.protocol.F3F4.F3F4_frame()

uart.rigister_protocol_parse_handle(protocol)

# uart.write(b"hello")
uart.start_listening()