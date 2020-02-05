import json

from utils.mylog import console

from engine.package import create_package, print_frame
from engine.base_structure import cell_item

table_tag = \
{
    "T1": {"key":1, "obj":cell_item("T1", "halo.button.is_pressed", (), False)},
    "T2": {"key":2, "obj":cell_item("T2", "led.show_all", (0,0,0), None)},
}

table_key = \
{
    1: {"tag":"T1", "obj":table_tag["T1"]['obj']},
    2: {"tag":"T2", "obj":table_tag["T2"]['obj']}
}

class subscribe_item_structure_c():
    def __init__(self, frame = None):
        self.frame = frame

    def set_frame(self, frame):
        self.frame = frame

    def get_json_str(self):
        str_len = 2
        service_len = 1

        json_string = str(self.frame[str_len + service_len :], "utf8")

        return json_string

    def get_json_obj(self):
        return eval(self.get_json_str())

class database_c():
    def __init__(self):
        self.data_key = table_key
        self.data_tag = table_tag
        self.protocol = None

        self.subscribe_item = subscribe_item_structure_c()
    
    def process(self, frame, d_info = None):
        if frame[0] == 0x29:
            self.__process_subscribe(frame[1:])
        elif frame[0] == 0x28:
            console.debug("process 0x28 frame %s" %frame)
            self.__process_realtime(frame[1:])

    def __process_subscribe(self, frame):
        '''
        process topic data(0x29)
        '''
        self.subscribe_item.set_frame(frame)
        obj = self.subscribe_item.get_json_obj()
        print("OOO", obj)
        for item in obj:
            if item in self.data_key:
                self.data_key[item]['obj'].update_value(obj[item])

        
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

    def create_subcribe_frame(self, cell_item):
        key = cell_item['key']
        func_script = cell_item['obj'].func
        para = str(cell_item['obj'].paras)
        return create_package("subscribe.add_item(%s, %s, %s)" %(key, func_script, para))

############################################################
    def data_lib_append(self, lib_dict):
        pass

    def data_lib_set(slef, lib_dict):
        pass

    def get_value(self, tag, para = None):
        if tag in self.data_tag:
            if not self.data_tag[tag]['obj'].subscribed_flag:
                self.data_tag[tag]['obj'].data_new_flag = False
                self.protocol.send_protocol(self.create_subcribe_frame(self.data_tag[tag]))
                self.data_tag[tag]['obj'].wait_data_new()
                
                self.data_tag[tag]['obj'].subscribed_flag = True

            return self.data_tag[tag]['obj'].get_value()
        else:
            return None

    def get_value_by_tag(self, tag, para = None):
        return self.get_value(tag, para)


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
