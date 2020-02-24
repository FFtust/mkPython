import json
import time 

from utils.mylog import console

from engine.package import create_package, print_frame
from engine.base_structure import cell_item

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

class process_c():
    def __init__(self):
    	pass

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
            if item in self.data_key:
                self.data_key[item]['obj'].update_value(obj[item])

        
    def __process_realtime(self, frame):
        '''
        process client-server data(0x28)
        '''
        pass

############################################################
    def create_frame(self, cell_item):
        func_script = cell_item['obj'].func
        para = str(cell_item['obj'].paras)
        return create_package(func_script + para)

    def create_subcribe_frame(self, cell_item):
        key = cell_item['key']
        func_script = cell_item['obj'].func
        para = str(cell_item['obj'].paras)
        return create_package("subscribe.add_item(%s, %s, %s)" %(key, func_script, para))
