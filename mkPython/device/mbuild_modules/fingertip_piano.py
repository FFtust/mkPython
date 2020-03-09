from utils.common import num_range_scale
from engine.F0F7.neurons_engine import neurons_request, neurons_blocking_read, neurons_async_read

#macro definition
__BUTTON_1 = 0x00
__BUTTON_2 = 0x01

__TOUCH_BUTTON_1 = 0x00
__TOUCH_BUTTON_2 = 0x01
__TOUCH_BUTTON_3 = 0x02
__TOUCH_BUTTON_4 = 0x03

__JOYSTICK_X = 0x00
__JOYSTICK_Y = 0x01

__INQUIRE_REPORT_MODE = 0x00
__CHANGE_REPORT_MODE = 0x01
__PERIOD_REPORT_MODE = 0x02
__REPORT_TIME = 20

JOYSTICK_ACTIVE_THRESHOLD = 60

#global variable definition

# common functions
def set_rgb(red_value, green_value, blue_value, index = 1):
    if not isinstance(index, (int, float)):
        return

    if not isinstance(red_value, (int, float)):
        return
    if not isinstance(green_value, (int, float)):
        return
    if not isinstance(blue_value, (int, float)):
        return

    red_value = num_range_scale(red_value, 0, 255)
    green_value = num_range_scale(green_value, 0, 255)
    blue_value = num_range_scale(blue_value, 0, 255)
    neurons_request("m_fingertip_piano", "set_rgb", (red_value, green_value, blue_value), index)

def is_button_pressed(button_idx, index = 1):
    if not isinstance(index, (int, float)):
        return False

    value = neurons_async_read("m_fingertip_piano", "get_button_state", (), index)
    if value:
        if button_idx == 'button1':
            return bool(value[0])
        elif button_idx == 'button2':
            return bool(value[1])
    else:
        return False

def set_button_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_button_report_mode", (mode,timestamp), index)
    else:
        pass

def get_button_count(button_idx,index = 1):
    if not isinstance(index, (int, float)):
        return 0
        
    value = neurons_async_read("m_fingertip_piano", "get_button_count", (), index)
    if value:
        if button_idx == 'button1':
            return value[0]
        elif button_idx == 'button2':
            return value[1]
    else:
        return 0

def reset_button_count(button_idx,index = 1):
    if button_idx == 'button1':
        idx = 0
    elif button_idx == 'button2':
        idx = 1
    elif button_idx == 'all':
        idx = 2
    neurons_request("m_fingertip_piano", "reset_button_count", (idx), index)
    # neurons_blocking_read("m_fingertip_piano", "get_button_count", (), index)


def set_button_count_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_button_count_report_mode", (mode,timestamp), index)
    else:
        pass


def is_touchpad_pressed(touchpad_idx, index = 1):
    if not isinstance(index, (int, float)):
        return False

    value = neurons_async_read("m_fingertip_piano", "get_touchpad_state", (), index)
    if value:
        if touchpad_idx == 'touchpad1':
            return bool(value[0])
        elif touchpad_idx == 'touchpad2':
            return bool(value[1])
        elif touchpad_idx == 'touchpad3':
            return bool(value[2])
        elif touchpad_idx == 'touchpad4':
            return bool(value[3])
    else:
        return False

def set_touchpad_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_touchpad_report_mode", (mode,timestamp), index)
    else:
        pass


def get_touchpad_value(touchpad_idx, index = 1):
    if not isinstance(index, (int, float)):
        return False    
    
    value = neurons_async_read("m_fingertip_piano", "get_touchpad_value", (), index)
    if value:
        if touchpad_idx == 'touchpad1':
            return value[0]
        elif touchpad_idx == 'touchpad2':
            return value[1]
        elif touchpad_idx == 'touchpad3':
            return value[2]
        elif touchpad_idx == 'touchpad4':
            return value[3]
    else:
        return 0

def set_touchpad_value_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_touchpad_value_report_mode", (mode,timestamp), index)
    else:
        pass


def get_joystick(opt, index = 1):
    if not isinstance(index, (int, float)):
        return 0

    value = neurons_async_read("m_fingertip_piano", "get_joystick_value", (), index)

    if value:
        if opt == 'x':
            return value[0]
        elif opt == 'y':
            return value[1]
        elif opt == 'all':
            return value

    else:
        if opt == 'all':
            return [0, 0]
        elif opt == 'y':
            return 0

    return 0

def is_joystick_active(opt, index = 1):
    value = get_joystick("all", index)
    if opt == "up":
        return bool(value[1] > JOYSTICK_ACTIVE_THRESHOLD)
    elif opt == "down":
        return bool(value[1] < -JOYSTICK_ACTIVE_THRESHOLD)
    elif opt == "left":
        return bool(value[0] < -JOYSTICK_ACTIVE_THRESHOLD)
    elif opt == "right":
        return bool(value[0] > JOYSTICK_ACTIVE_THRESHOLD)
    else:
        return False

def set_joystick_value_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_joystick_value_report_mode", (mode,timestamp), index)
    else:
        pass

def get_gesture(index = 1):
    if not isinstance(index, (int, float)):
        return False

    value = neurons_async_read("m_fingertip_piano", "get_gesture", (), index)
    if value != None:
        return value[0]
    else:
        return False

def set_gesture_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_gesture_report_mode", (mode,timestamp), index)
    else:
        pass

def get_distance(index = 1):
    if not isinstance(index, (int, float)):
        return 0

    value = neurons_async_read("m_fingertip_piano", "get_distance", (), index)

    if value:
        return value[0]
    else:
        return 0

    return 0

def set_distance_report_mode(mode,timestamp,index = 1):
    timestamp = num_range_scale(timestamp, 10, None)
    if mode == 0x00 or mode == 0x01 or mode == 0x02:
        neurons_request("m_fingertip_piano", "set_distance_report_mode", (mode,timestamp), index)
    else:
        pass



#set_button_report_mode(__CHANGE_REPORT_MODE, __REPORT_TIME)
set_button_count_report_mode(__CHANGE_REPORT_MODE, __REPORT_TIME)
#set_touchpad_report_mode(__CHANGE_REPORT_MODE, __REPORT_TIME)
set_touchpad_value_report_mode(__PERIOD_REPORT_MODE, __REPORT_TIME)
set_joystick_value_report_mode(__PERIOD_REPORT_MODE, __REPORT_TIME)
#set_gesture_report_mode(__CHANGE_REPORT_MODE, __REPORT_TIME)
set_distance_report_mode(__PERIOD_REPORT_MODE, __REPORT_TIME)
