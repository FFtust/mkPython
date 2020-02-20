import engine.database
import engine.protocol
import engine.protocol.F3F4
import link.commu_uart

from device.table_halocode import table_halocode_tag

class adapter_halo():
    def __init__(self, port, bauadrate = 115200):
        self.port = port
        self.bauadrate = 115200 

        self.table_tag = table_halocode_tag.copy()
        self.table_key = self.create_key(self.table_tag)

        self.data_base = engine.database.database_c()
        self.data_base.data_tag.update(self.table_tag)
        self.data_base.data_key.update(self.table_key)


    def create_key(self, table_tag):
        table_key = {}

        key_index = 0
        for item in table_tag:
            table_tag[item]['key'] = key_index 
            table_key.update({key_index: {"tag":item, "obj":table_tag[item]["obj"]}})
            key_index += 1

        return table_key

    def start(self):
        self.link_obj = link.commu_uart.uart_link(["COM0", 115200])

        self.link_obj.config([self.port, str(self.bauadrate)])
        self.link_obj.open()
        self.link_obj.start_listening()

        self.protocol_obj = engine.protocol.F3F4.F3F4_frame()
        self.protocol_obj.register_frame_process(self.data_base)

        self.link_obj.rigister_protocol_parse_handle(self.protocol_obj)

        # send online mode command
        self.__run_into_online_mode()

    def __run_into_online_mode(self):        
        self.protocol_obj.send_protocol(bytes([0x0d, 0x00, 0x01]))
