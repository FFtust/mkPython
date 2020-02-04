class cell_item():
    def __init__(self, tag, func, paras, default_value):
        self.tag = tag
        self.func = func
        # undifined: add nothing
        # []: no parameters
        # [xx, xx]: several parameters
        self.paras = paras
        self.default_value = default_value
        
        # key will be binded with the id in onlineManager.onlineTable (type of array)
        self.key = None

        self.value = None
        self.data_new_flag = None
        self.data_update_callBack = []
        self.subscribe_handle = None
        
        self.auto_subscribe_control_flag = True
        self.get_value_called_count = 0

    def reset_status(self):
        self.value = None
        self.data_new_flag = None
        self.subscribe_handle = []
        self.get_value_called_count = 0
        self.data_update_callBack = None
        self.auto_subscribe_control_flag = True

    def register_data_update_callback(self, callback):
        self.data_update_callBack.append(callback)

    def update_value(self, value):
        '''
        low computer to high computer
        '''

        self.value = value
        self.data_new_flag = True

        for item in self.data_update_callBack:
            item(value)

    def update_parameters(self, paras, until_done = False):
        '''
        high computer to low computer
        '''
        self.paras = paras

    def get_value(self):
        self.get_value_called_count += 1

        return self.value



