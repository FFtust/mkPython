from utils.common import num_range_scale
from engine.F0F7.neurons_engine import neurons_request, neurons_blocking_read, neurons_async_read

def is_pressed(index = 1):
    if not isinstance(index, (int, float)):
        return False

    value = neurons_async_read("m_button", "get_value", (), index)
    if value != None:
        return bool(value[0])
    else:
        return False

def get_count(index = 1):
    if not isinstance(index, (int, float)):
        return 0
        
    value = neurons_async_read("m_button", "get_pressed_count", (), index)
    if value != None:
        return value[0]
    else:
        return 0

def reset_count(index = 1):
    neurons_request("m_button", "reset_count", (), index)
    neurons_blocking_read("m_button", "get_pressed_count", (), index)

def set_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_button", "set_report_mode", (mode,timestamp), index)
    else:
        pass
