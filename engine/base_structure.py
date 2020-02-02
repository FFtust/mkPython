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
        self.data_update_callBack = None
        self.subscribe_handle = None
        
        self.auto_subscribe_control_flag = True
        self.get_value_called_count = 0

    def reset_status(self):
        self.value = None
        self.data_new_flag = None
        self.subscribe_handle = None
        self.get_value_called_count = 0
        self.data_update_callBack = None
        self.auto_subscribe_control_flag = True

