from utils.common import num_range_scale
from engine.F0F7.neurons_engine import neurons_request, neurons_blocking_read, neurons_async_read

#channel dictionary
channel_dict = {
    "M1": 0x01,
    "M2": 0x02,
    "S1": 0x01,
    "S2": 0x02,
    "ALL":0x00
}

button_id_dict = {
    "A"       :  0x45,
    "B"       :  0x46,
    "C"       :  0x47,
    "D"       :  0x44,
    "E"       :  0x43,
    "F"       :  0x0D,
    "UP"      :  0x40,
    "DOWN"    :  0x19,
    "LEFT"    :  0x07,
    'RIGHT'   :  0x09,
    'SET'     :  0x15,
    "0"       :  0x16,
    "1"       :  0x0C,
    '2'       :  0x18,
    "3"       :  0x5E,
    "4"       :  0x08,
    "5"       :  0x1C,
    "6"       :  0x5A,
    "7"       :  0x42,
    "8"       :  0x52,
    "9"       :  0x4A
}

#private function
def __set_power(channel, power, index = 1):
    neurons_request("m_halobot", "dc_motor_set_power", (channel,power), index)

#class
class ir(object):
    def __init__(self):
        self.flag = None

    def send(data, index = 1):
        if index != 0x01:
            return
        data = str(data) + '\n'
        length = len(data)
        if length == 0 or length > 127:
            return
        #list_data = list(map(ord, list(data)))
        neurons_request("m_halobot", "ir_send", data, index)

    def send_remote_code(addr, data, index = 1):
        if index != 0x01:
            return
        if not isinstance(addr, (int)) or not isinstance(data, (int)):
            return
        addr = num_range_scale(addr, 0, 255)
        data = num_range_scale(data, -128, 127)    
        neurons_request("m_halobot", "ir_send_remote_code", (addr,data), index)

    def receive(index = 1):
        if index != 0x01:
            return 0
        value = neurons_async_read("m_halobot", "ir_receive", (), index, False)
        if value != None:
            data_str = value[0]
            if type(data_str) == str:
                data_str = data_str[0: len(data_str)-1]
                return data_str
        return 0

    def receive_remote_code(index = 1):
        if index != 0x01:
            return 0
        value = neurons_async_read("m_halobot", "ir_receive_remote_code", (), index, False)
        if value != None:
            return value[1]
        else:
            return 0

    def is_pressed(button, index = 1):
        if index != 0x01:
            return False
        if not isinstance(button, (str,)):
            return False
        if button not in button_id_dict.keys():
            return False
        value = neurons_async_read("m_halobot", "ir_receive_remote_code", (), index, False)
        if value != None:
            if value[1] == button_id_dict[button]:
                return True
            else:
                return False
        else:
            return False

class servo(object):
    def __init__(self):
        self.flag = None

    def change_angle(channel = None, angle = 0, index = 1):
        if index != 0x01:
            return
        if channel != "ALL" and channel != "S1" and channel != "S2":
            return
        if not isinstance(angle, (int)):
            return
        angle = num_range_scale(angle, -180, 180)
        neurons_request("m_halobot", "servo_change_angle", (channel_dict[channel],angle), index)

    def get_angle(channel = None, index = 1):
        if index != 0x01:
            return 0
        if channel != "ALL" and channel != "S1" and channel != "S2":
            return 0
        value = neurons_blocking_read("m_halobot", "servo_get_angle", (channel_dict["ALL"]), index)
        #print(value)
        if value != None:
            if channel == "S1":
                return value[1]
            elif channel == "S2":
                return value[2]
            else:
                return value[1:]
        else:
            return 0

    def get_current(channel = None, index = 1):
        if index != 0x01:
            return 0
        if channel != "ALL" and channel != "S1" and channel != "S2":
            return 0
        value = neurons_blocking_read("m_halobot", "servo_get_current", (channel_dict["ALL"]), index)
        #print(value)
        if value != None:
            if channel == "S1":
                return value[1]
            elif channel == "S2":
                return value[2]
            else:
                return value[1:]
        else:
            return 0

    def set_angle(channel = None, angle = 0, index = 1):
        if index != 0x01:
            return
        if channel != "ALL" and channel != "S1" and channel != "S2":
            return
        if not isinstance(angle, (int)):
            return
        angle = num_range_scale(angle, 0, 180)
        neurons_request("m_halobot", "servo_set_angle", (channel_dict[channel],angle), index)

class dc_motor(object):
    def __init__(self):
        self.flag = None

    def set_power(channel = None, power =0, index = 1):
        if index != 0x01:
            return
        if channel != "ALL" and channel != "M1" and channel != "M2":
            return
        if not isinstance(power, (int,float)):
            return
        power = int(power)
        power = num_range_scale(power, -100, 100)
        if channel == "M1":
            __set_power(channel_dict[channel], power, index)
        elif channel == "M2":
            __set_power(channel_dict[channel], -power, index)
        else:
            __set_power(channel_dict["M1"], power, index)
            __set_power(channel_dict["M2"], -power, index)

'''
class button(object):
    def __init__(self):
        self.flag = None

    def get_value(index =1):
        value = neurons_async_read("m_halobot", "button_get_value", (), index False)
        if value != None:
            return value[0]
        else:
            return 0

    def set_report_mode(mode, timestamp, index = 1):
        timestamp = num_range_scale(timestamp, 10, None)
        if mode == 0x00 or mode == 0x01 or mode == 0x02:
            neurons_request("m_halobot", "button_set_report_mode", (mode, timestamp), index)
        else:
            pass
'''