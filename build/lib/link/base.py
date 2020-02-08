class base_link(object):
    _LINK_STA_NOT_INIT = 0
    _LINK_STA_INIT = 1
    _LINK_STA_OPEN = 2
    _LINK_STA_CLOSE = 3

    def __init__(self):
        self.status = self._LINK_STA_NOT_INIT
    
    def config(self, para):
        self.status = self._LINK_STA_INIT
        
    def open(self):
        self.status = self._LINK_STA_OPEN
        
    def close(self):
        self.status = self._LINK_STA_CLOSE

    def get_status(self):
        return self.status
    
    def bind_protocol(self, protocol_obj):
        pass

    def write(self, frame):
        pass

    def read(self, bytes_num = 1):
        pass