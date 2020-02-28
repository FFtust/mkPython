import time

class cell_item():
    def __init__(self, tag, func, paras, default_value):
        self.tag = tag
        self.func = func
        # undifined: add nothing
        # []: no parameters
        # [xx, xx]: several parameters
        self.paras = paras
        self.default_value = default_value
        
        self.key = None
        # {para1_obj:{"val": 0, "subs_flag":False, 'd_n_flag:False'}, para2_obj:{}}
        self.subscribed_para = {}
        # key will be binded with the id in onlineManager.onlineTable (type of array)
        # {key1：{obj":para1_obj}, }
        self.subscribed_key = {}

        self.data_update_callBack = []        
        self.auto_subscribe_control_flag = True
        self.get_value_called_count = 0

    def reset_status(self):
        self.subscribed_para = {}
        self.subscribed_key = {}

        self.data_update_callBack = []        
        self.auto_subscribe_control_flag = True
        self.get_value_called_count = 0

    # PC TO DEVICES
    def update_parameters(self, paras, until_done = False):
        '''
        high computer to low computer
        '''
        self.paras = tuple(paras)

    # DEVICES TO PC
    def register_data_update_callback(self, callback, para = None):
        self.data_update_callBack.append(callback)

    def update_value(self, value, key):
        '''
        low computer to high computer
        '''
        if key in self.subscribed_key:
            self.subscribed_key[key]['obj']['val'] = value
            self.subscribed_key[key]['obj']['d_n_flag'] = True

            for item in self.data_update_callBack:
                item(value)
        else:
            print("unknown key received")
    
    def wait_data_new(self, para = None, max_time = 1):
        start_t = time.time()
        while time.time() - start_t < max_time:
            if self.subscribed_para[para]["d_n_flag"] == True:
                return True
            time.sleep(0.05)

        return False

    def get_value(self, para = None):
        self.get_value_called_count += 1

        return self.subscribed_para[para]["val"]
    
    def get_default_value(self, para = None):
        # TODO
        return 0

    def __add_subscribe_para(self, para):
        if not (para in self.subscribed_para): 
            self.subscribed_para[para] = {'key':0, "val": 0, "subs_flag":False, 'd_n_flag':False} 
            if len(self.subscribed_para) > 1:
                new_key = self.key + '_' + str(len(self.subscribed_para))
            else:
                new_key = self.key

            self.subscribed_para[para]["key"] = new_key
            self.subscribed_key[new_key] = {"obj":self.subscribed_para[para]}
            print("pppp", self.subscribed_key)
    def get_subscribe_flag(self, para = None):
        if para in self.subscribed_para:
            return self.subscribed_para[para]["subs_flag"]
        else:
            self.__add_subscribe_para(para)
            return False

    def set_subscribe_flag(self, sta, para = None):
        self.subscribed_para[para]["subs_flag"] = sta

    def get_data_new_flag(self, para = None):
        if para in self.subscribed_para:
            return self.subscribed_para[para]["d_n_flag"]
        else:
            return False

    def set_data_new_flag(self, sta, para = None):
        if para in self.subscribed_para:
            self.subscribed_para[para]["d_n_flag"] = sta

    def get_key_by_para(self, para = None):
        if para in self.subscribed_para:
            return self.subscribed_para[para]["key"]