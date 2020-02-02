import time
import threading

from utils.mylog import console
import firefly_online.communication.common_link as common_link
import firefly_online.adapter.frame_package as frame_package
from firefly_online.adapter.data_sync import hardware_data

COM_PORT = "COM28"
COM_BAUDRATE = 115200

WRITE_BUFFER_ENABLE = True
WRITE_UPDATE_INTERVAL = 0.025


SERIAL_NUM_WRITE_WITHOUT_RESPONSE = 0x05

def sync_delay(t = 0.01):
    import time
    if t == None:
        pass
    else:
        time.sleep(t)

class script_hash(object):
    def __init__(self):
        self.script_hash = {}
        self.danymic_number = 1

    def register(self, script):
        if not (script in self.script_hash):
            self.script_hash[script] = self.danymic_number
            self.danymic_number += 1
        return self.danymic_number - 1
    
    def unregister(self, script):
        if script in self.script_hash:
            self.script_hash.pop(script)

    def get_hash(self, script):
        if script in self.script_hash:
            return self.script_hash[script]
        else:
            return None
    
    def restart(self):
        self.script_hash = {}


class exec_script_hash(object):
    def __init__(self, common_link):
        self.script_hash = {}
        self.danymic_number = 1
        self.interval = WRITE_UPDATE_INTERVAL
        self.common_link = common_link

    def register(self, script, para):
        if not (script in self.script_hash):
            self.script_hash[script] = [self.danymic_number, para, True]
            self.danymic_number += 1
        return self.danymic_number - 1

    def unregister(self, script):
        if script in self.script_hash:
            self.script_hash.pop(script)

    def get_hash(self, script):
        if script in self.script_hash:
            return self.script_hash[script]
        else:
            return None

    def update_para(self, script, para, update_flag = False):
        if script in self.script_hash:
            if update_flag or self.script_hash[script][1] != para:
                self.script_hash[script][1] = para
                self.script_hash[script][2] = True

    def work(self):
        while True:
            para_dict = {}
            console.debug('******', self.script_hash)
            if self.script_hash:
                for value in self.script_hash.values():
                    if value[2] == True:
                        para_dict[value[0]] = value[1]
                        value[2] = False

                if para_dict != {}:
                    self.common_link.phy.write(frame_package.create_frame(0x01, ('subscribe.up_para(%s)' %(str(para_dict), )).replace(' ','')))
            time.sleep(self.interval)

    def start(self):
        self.th = threading.Thread(target = self.work, args = ())
        self.th.start()


class adapter(object):
    def __init__(self, phy_para = [COM_PORT], phy_type = 'serial'):
        self.script_hash = script_hash()

        self.phy_type = phy_type
        self.phy_para = phy_para

        if phy_type == 'serial':
            self.phy = common_link.phy_uart(phy_para[0], COM_BAUDRATE)
            self.common_link = common_link.common_link(self.phy)
            self.hd_data = hardware_data()
            self.common_link.register_process_function(frame_package.PROTOCOL_SUBSCRIBE_ID, self.hd_data.data_parse)
            self.common_link.start()
            time.sleep(1)

        # clear the buffer in lower computer
        # self.common_link.phy.write(frame_package.create_frame(0x00, "subscribe.restart()"))
        
        if WRITE_BUFFER_ENABLE:
            self.exec_script_hash = exec_script_hash(self.common_link)
            self.exec_script_hash.start()

    def __del__(self):
        console.debug("adapter del")
        if self.phy_type == 'serial':
            self.common_link.__del__()

    def write_str_directly(self, script, service_id = 0x00):
        self.common_link.phy.write(frame_package.create_frame(service_id, script))
        sync_delay()

    def write_sync(self, script):
        sync_delay()

        return

    def write_async(self, script, para = None, update_flag = False):
        sync_delay()

        if para != None:
            para = para.replace(' ','')

        t_script = script
        if script[-3: -1] == '__': 
            script = script[:-3]

        if not WRITE_BUFFER_ENABLE:
            if para == None:
                self.common_link.phy.write(frame_package.create_frame(0x00, script + '()', SERIAL_NUM_WRITE_WITHOUT_RESPONSE))
            else:
                self.common_link.phy.write(frame_package.create_frame(0x00, script + para, SERIAL_NUM_WRITE_WITHOUT_RESPONSE))
        else:
            hash_id = self.exec_script_hash.get_hash(t_script)
            if not hash_id:
                hash_id  = self.exec_script_hash.register(t_script, eval(para))
                if para == None:
                    frame = frame_package.create_frame(0x01, "subscribe.add_exec_item(%d, %s, ())" %(hash_id, script))
                else:
                    console.debug("subscribe.add_exec_item(%d, %s, %s)" %(hash_id, script, para))
                    frame = frame_package.create_frame(0x01, "subscribe.add_exec_item(%d, %s, %s)" %(hash_id, script, para))

                self.common_link.phy.write(frame)
                time.sleep(0.2)
            else:
                self.exec_script_hash.update_para(t_script, eval(para), update_flag)

    def write_imidiate_script(self, script, para = None, temp = None):
        sync_delay()
        if para != None:
            para = para.replace(' ','')

        t_script = script
        if script[-3: -1] == '__': 
            script = script[:-3]

        if para == None:
            self.common_link.phy.write(frame_package.create_frame(0x00, script + '()', SERIAL_NUM_WRITE_WITHOUT_RESPONSE))
        else:
            console.debug("write_imidiate_script: %s" %(script + para))
            self.common_link.phy.write(frame_package.create_frame(0x00, script + para, SERIAL_NUM_WRITE_WITHOUT_RESPONSE))

    def read_sync(self, script):
        sync_delay()
        return

    def read_async(self, script, para = None):
        sync_delay()

        if para != None:
            para = para.replace(' ','')

        t_script = script
        if script[-3: -1] == '__': 
            script = script[:-3]

        hash_id = self.script_hash.get_hash(t_script)
        if not hash_id:
            hash_id  = self.script_hash.register(t_script)
            if para == None:
                console.debug("subscribe.add_item(%d, codey.%s, ())" %(hash_id, script))
                frame = frame_package.create_frame(0x01, "subscribe.add_item(%d, %s, ())" %(hash_id, script))
            else:
                console.debug("subscribe.add_item(%d, %s, %s)" %(hash_id, script, para))
                frame = frame_package.create_frame(0x01, "subscribe.add_item(%d, %s, %s)" %(hash_id, script, para))

            self.common_link.phy.write(frame)
            # wait the first value update
            self.hd_data.wait_value_first_update(hash_id)
        
        if hash_id in self.hd_data.sensor_data:
            return self.hd_data.sensor_data[hash_id].value
        else:
            return None

    # special application
    def write_bytes_directly(self, frame):
        sync_delay()

        self.common_link.phy.write(frame)
