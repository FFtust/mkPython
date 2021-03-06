import json
import time 

from utils.mylog import console

from engine.F3F4.package import create_package, print_frame
from engine.F3F4.base_structure import cell_item

GET_VALUE_DELAY_TIME = 0.001
REQUEST_DELAY_TIME = 0.05

def delay_sync(t = 0):
    if t > 0:
        time.sleep(t)

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

class F3F4_process_c():
    def __init__(self):
        self.data_key = {}
        self.data_tag = {}
        self.protocol = None

        self.subscribe_item = subscribe_item_structure_c()

############################################################
    '''
    subscribe - publish communication 
    '''
    def get_value(self, tag, para = None):
        if not isinstance(para, tuple):
            para = (para, )

        delay_sync(GET_VALUE_DELAY_TIME)
        return self.get_value_by_tag(tag, para)


    '''
    Real-time communication
    '''
    def request(self, tag, para = None, wait_time = None):
        if not isinstance(para, tuple):
            para = (para, )

        if wait_time == None:
            self.update_para_by_tag(tag, para)
        else:
            pass

        delay_sync(REQUEST_DELAY_TIME)
        

    '''
    special usage
    '''
    def request_with_origin_script(self, script, wait_time = None):

        delay_sync()



############################################################

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
        for item in obj:

            if '_' in item:
                obj_key = item.split('_')[0]
            else:
                obj_key = item

            if obj_key in self.data_key:
                self.data_key[obj_key]['obj'].update_value(obj[item], item)

        
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

    def create_subcribe_frame(self, cell_item, para):
        key = cell_item['obj'].get_key_by_para(para)
        func_script = cell_item['obj'].func
        # para = str(cell_item['obj'].paras)
        return create_package("subscribe.add_item('%s', %s, %s)" %(key, func_script, para))

############################################################
    def data_lib_append(self, lib_dict):
        pass

    def data_lib_set(slef, lib_dict):
        pass

    def get_value(self, tag, para = None):
        para = tuple(para)
        if tag in self.data_tag:
            if not self.data_tag[tag]['obj'].get_subscribe_flag(para):
                self.data_tag[tag]['obj'].set_data_new_flag(False, para)
                
                console.debug(self.create_subcribe_frame(self.data_tag[tag], para))

                self.protocol.send_protocol(self.create_subcribe_frame(self.data_tag[tag], para))
                
                if self.data_tag[tag]['obj'].wait_data_new(para):
                    self.data_tag[tag]['obj'].set_subscribe_flag(True, para)
                    return self.data_tag[tag]['obj'].get_value(para)
                else:
                    return self.data_tag[tag]['obj'].get_default_value(para)

            return self.data_tag[tag]['obj'].get_value(para)
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



class system_cmd_process_c():
    def __init__(self):
        self.protocol = None

        self.sys_status = None
        self.sys_mode = None

    def process(self, frame, d_info = None):
        if frame[0] == 0x0d:
            self.sys_status = frame[2]

    def get_sys_status(self):
        if self.protocol:
            self.protocol.send_protocol(bytes([0x0d, 0x80]))
        time.sleep(0.2)
        return self.sys_status

    def send_sys_cmd(self, script):
        if self.protocol:
            print(create_package(script, 0x00, 0x03))   
            self.protocol.send_protocol(create_package(script, 0x00, 0x03))