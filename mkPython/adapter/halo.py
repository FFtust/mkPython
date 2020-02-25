import time

import engine.F3F4.process 
import engine.F3F4.protocol

import link.commu_uart
import link.p_link

from device.table_halocode import table_halocode_tag

class adapter_halo():
    def __init__(self, port, bauadrate = 115200):
        self.port = port
        self.bauadrate = 115200 

        self.table_tag = table_halocode_tag.copy()
        self.table_key = self.create_key(self.table_tag)

        self.process = engine.F3F4.process.F3F4_process_c()
        self.process.data_tag.update(self.table_tag)
        self.process.data_key.update(self.table_key)


    def create_key(self, table_tag):
        table_key = {}

        key_index = 0
        for item in table_tag:
            table_tag[item]['key'] = key_index 
            table_key.update({key_index: {"tag":item, "obj":table_tag[item]["obj"]}})
            key_index += 1

        return table_key
 
    def start(self):
        port_device = link.p_link.get_available_port()[0]
        if not port_device.is_open():
            self.link_obj = link.commu_uart.uart_link(["COM0", 115200])

            self.link_obj.config([self.port, str(self.bauadrate)])
            self.link_obj.open()
            self.link_obj.start_listening()

            port_device.status = 1
            port_device.link_obj = self.link_obj
        else:
            self.link_obj = port_device.link_obj

        self.protocol_obj = engine.F3F4.protocol.F3F4_frame()
        self.protocol_obj.register_frame_process(self.process)

        self.sys_process = engine.F3F4.process.system_cmd_process_c()
        self.protocol_obj.register_frame_process(self.sys_process)


        self.link_obj.rigister_protocol_parse_handle(self.protocol_obj)

        # send online mode command
        self.__run_into_online_mode()

    def __run_into_online_mode(self):  
        while True:
            if self.sys_process.get_sys_status() != None:
                break
        time.sleep(0.2)
        self.protocol_obj.send_protocol(bytes([0x0d, 0x00, 0x01]))
