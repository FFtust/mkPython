import link.find_device


vailable_port = []

class port_c():
    def __init__(self, port_type, channel):
        '''
        self.port_type = None/uart/ble/wifi
        self.channel = COM3/...
        '''
        self.port_type = None
        self.channel = None

        self.status = None

        self.link_obj = None

    def is_open(self):
        return self.status


def get_available_port():
    global vailable_port
    ports = link.find_device.get_port("all")

    for p in ports:
        for item in vailable_port:
            if item.channel ==  p:
                continue
        vailable_port.append(port_c("uart", p))

    return vailable_port



