import time

from engine.F3F4.package import create_package, print_frame
from engine.F3F4.protocol import create_frame

import engine.F0F7
import engine.F0F7.protocol
import engine.F0F7.process
import link.commu_uart
import link.p_link

from device.table_halocode import table_halocode_tag

class adapter_mbuild():
    def __init__(self, port, bauadrate = 115200):
        self.port = port
        self.bauadrate = 115200 


    # not used
    def create_key(self, table_tag):
    	pass

    def start(self):
        start_heart_package = True
        port_device = link.p_link.get_available_port()[0]
        if not port_device.is_open():
            self.link_obj = link.commu_uart.uart_link(["COM0", 115200])

            self.link_obj.config([self.port, str(self.bauadrate)])
            self.link_obj.open()
            self.link_obj.start_listening()
            port_device.status = 1

            port_device.link_obj = self.link_obj
            start_heart_package = True
        else:
            start_heart_package = False
            self.link_obj = port_device.link_obj


        self.protocol_obj = engine.F0F7.protocol.F0F7_frame()

        self.process = engine.F0F7.process.neurons_process_c()
        self.protocol_obj.register_frame_process(self.process)

        self.link_obj.rigister_protocol_parse_handle(self.protocol_obj)

        engine.F0F7.neurons_engine.neuron_request_bind_phy(self.protocol_obj.send_protocol)
        self.process.start_engine(start_heart_package)
        
        print(create_frame(create_package("import communication", 0x00, 0x04)))
        self.link_obj.write(create_frame(create_package("import communication", 0x00, 0x04)))
        time.sleep(0.9)
        self.link_obj.write(create_frame(create_package("halo.led.show_all(10,10,0)", 0x00, 0x04)))
        time.sleep(0.1)
        self.link_obj.write(create_frame(create_package("communication.bind_passthrough_channels(\"uart0\", \"uart1\")", 0x00, 0x04)))

        # time.sleep(1)
        # self.link_obj.write(bytes("halo.led.show_all(10, 0, 0)\r\n", "utf8"))
        # time.sleep(1)
        # self.link_obj.write(bytes("communication.bind_passthrough_channels(\"uart0\", \"uart1\")\r\n","utf8"))