from engine.package import create_package
from engine.base_structure import cell_item
table_halocode_tag = \
{
    "T1": {"key":1, "obj":cell_item("T1", "halo.button.is_pressed", (), False)},
    "T2": {"key":2, "obj":cell_item("T2", "led.show_all", (0,0,0), None)},
}

table_halocode_key = \
{
    "1": {"tag":"T1", "obj":table_halocode_tag["T1"]},
    "2": {"tag":"T2", "obj":table_halocode_tag["T2"]}
}


class database_c():
    def __init__(self):
        self.data_key = table_halocode_key
        self.data_tag = table_halocode_tag
        self.protocol = None
    
    def process(self, frame, d_info = None):
        if frame[0] == 0x29:
            self.__process_subscribe(frame)
        elif frame[0] == 0x28:
            self.__process_realtime(frame)

    def __process_subscribe(self, frame):
        '''
        process topic data(0x29)
        '''
        pass

    def __process_realtime(self, frame):
        '''
        process client-server data(0x28)
        '''
        pass

############################################################
    def create_frame(sllf, cell_item):
        func_script = cell_item['obj'].func
        para = str(cell_item['obj'].paras)
        return create_package(func_script + para)

############################################################
    def data_lib_append(self, lib_dict):
        pass

    def data_lib_set(slef, lib_dict):
        pass

    def get_value(self, tag, para = None):
        if tag in self.data_tag:
            return self.data_tag["tag"].get_value()
        else:
            return None

    def get_value_by_tag(self, tag, para = None):
        return self.get_value(key, para)


    def get_value_by_key(self, key, para = None):
        if key in self.data_key:
            return self.data_key["tag"].get_value()
        else:
            return None

    def update_value_by_key(self, key, value):
        if key in self.data_key:
            self.data_key["key"].update_value(value)

    def update_value_by_tag(self, tag, value):
        if tag in self.data_tag:
            self.data_tag[tag]['obj'].update_value(value)

    def update_para_by_tag(self, tag, para = None):
        if tag in self.data_tag:
            self.data_tag[tag]['obj'].update_parameters(para)

        if self.protocol:
            # print(self.create_frame(self.data_tag[tag]))
            self.protocol.send_protocol(self.create_frame(self.data_tag[tag]))

    def update_para_by_key(self, key, para = None):
        pass


database = database_c()
