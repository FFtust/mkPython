import engine.F0F7
import engine.F0F7.protocol
import engine.F0F7.process
import link.commu_uart

from device.table_halocode import table_halocode_tag

class adapter_mbuild():
    def __init__(self, port, bauadrate = 115200):
        self.port = port
        self.bauadrate = 115200 


    # not used
    def create_key(self, table_tag):
    	pass

    def start(self):
        self.link_obj = link.commu_uart.uart_link(["COM0", 115200])

        self.link_obj.config([self.port, str(self.bauadrate)])
        self.link_obj.open()
        self.link_obj.start_listening()

        self.protocol_obj = engine.F0F7.protocol.F0F7_frame()

        self.process = engine.F0F7.process.neurons_process_c()
        self.protocol_obj.register_frame_process(self.process)

        self.link_obj.rigister_protocol_parse_handle(self.protocol_obj)
