#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

class led_c():
    ''' led matrix '''
    def __init__(self):
        pass
    # __fun_type__: write
    def show_all(self, r, g, b, percentage = 100):
        """控制所有led灯的状态.

        所有灯亮同样的状态，使用r,g,b分量控制

        Args:
            r (int): 0 ~ 255; 红色分量
            g (int): 0 ~ 255; 绿色分量
            b (int): 0 ~ 255; 蓝色分量
            percentage (int): 0 ~ 100; 亮度百分比
        Returns:
               None
        """
        pass
    # __fun_type__: write
    def show_single(self, index, r, g, b):
        """控制单颗led灯的状态.

        使用r,g,b分量控制灯的状态

        Args:
            index (int): 1 ~ 12; led 编号
            r (int): 0 ~ 255; 红色分量
            g (int): 0 ~ 255; 绿色分量
            b (int): 0 ~ 255; 蓝色分量

        Returns:
            None        
        """
        pass
    # __fun_type__: write
    def move(self, offset = 1):
        """ LED 矩阵整体偏移.

        整个LED矩阵旋转顺时针旋转offset个位置，offset为负值时，逆时针旋转.

        Args:
            offset (int): no limit; 偏移值

        Returns:
            None
        
        """
        pass
    # __fun_type__: write
    def off_single(self, led_id):
        """ 熄灭单颗LED灯.

        设置12颗灯中的某一颗灯为熄灭状态.

        Args:
            led_id (int): 1 ~ 12; led 编号

        Returns:
            None
        
        """
        pass 
    # __fun_type__: write
    def off_all(self):
        """ 熄灭所有LED灯.

        设置12颗灯全部为为熄灭状态.

        Args:
            无

        Returns:
            None
        
        """
        pass 
    # __fun_type__: write
    def clear(self):
        """ 熄灭所有LED灯.

        功能同 off_all.

        Args:
            无
    
        Returns:
            None
        
        """
        pass 
    # __fun_type__: write    
    def show_ring(self, color, offset = 0):
        """ 设置led灯环状态.

        设置所有或者部分灯珠的颜色，颜色共有7中.

        Args:
            color (str): 灯珠颜色，以空格划分
            offset (int): 无限制; 旋转偏移
        Returns:
            None
        
        """
        pass 
    # __fun_type__: write
    def ring_graph(self, pct):
        """ 设置led灯环状态.

        设置所有或者部分灯珠的颜色，颜色共有7中.

        Args:
            color (str): 灯珠颜色，以空格划分
            offset (int): 无限制; 旋转偏移
        Returns:
            None
        
        """
        pass 

    # __fun_type__: write
    def show_animation(self, name, wait = True):
        """ 显示LED动画.

        阻塞显示LED动画效果. 目前共内置 几种效果

        Args:
            name (str): LED动画名称；
            wait (bool): 是否阻塞显示
        Returns:
            None
        
        """
        pass   
    # __fun_type__: write    
    def show_full_color(self, data, offset = 0):
        """ 设置led灯环状态.

        设置所有或者部分灯珠的RGB值，共36字节.
        从1~12颗灯依次计算

        Args:
            data (list，tuple): 36字节数据
            offset (int): 无限制; 旋转偏移
        Returns:
            None
        
        """
        pass 

class button_c():
    def __init__(self):
        pass

    # __fun_type__: read
    def is_pressed(self):
        """按键是否被按下.

        检测按键的状态是否被按下. 只有一个按键时，默认不填

        Args:
            index (int): 0~ ; 按键编号
        Returns:
            bool        
        """

        pass

class touchpad0_c(object):
    def __init__(self):
        pass

    # __fun_type__: read
    def is_touched(self):
        """检测触摸状态.

        检测触摸按键0是否被触发

        Args:
            无
        Returns:
            bool        
        """
        pass

    # __fun_type__: write
    def set_touch_threshold(self, value):
        """设置触摸灵敏度阈值.

        设置触摸按键0的灵敏度阈值

        Args:
            value (float): 0 ~ 1; 触摸灵敏度，值越大，越不灵敏
        Returns:
            None       
        """
        pass

    # __fun_type__: write
    def set_touch_sensitivity(self, level):
        """设置触摸灵敏度等级.

        设置触摸按键0的灵敏度等级

        Args:
            level (str): "high"/"middle"/"low"
        Returns:
            None
        """
        pass

    # __fun_type__: read
    def get_value(self):
        """获取触摸值.

        获取触摸按键0的模拟值，随外界状态变化而变化。
        正常情况下，触摸值在 0~100 范围内，但由于器件差异，个别
        板子的值会超出这个范围。

        Args:
            无
        Returns:
            int (0 ~ 100): 不同板子情况不同    
        """
        pass

class touchpad1_c(object):
    def __init__(self):
        pass

    # __fun_type__: read
    def is_touched(self):
        """检测触摸状态.

        检测触摸按键1是否被触发

        Args:
            无
        Returns:
            bool        
        """
        pass

    # __fun_type__: write
    def set_touch_threshold(self, value):
        """设置触摸灵敏度阈值.

        设置触摸按键1的灵敏度阈值

        Args:
            value (float): 0 ~ 1; 触摸灵敏度，值越大，越不灵敏
        Returns:
            None       
        """
        pass

    # __fun_type__: write
    def set_touch_sensitivity(self, level):
        """设置触摸灵敏度等级.

        设置触摸按键1的灵敏度等级

        Args:
            level (str): "high"/"middle"/"low"
        Returns:
            None
        """
        pass

    # __fun_type__: read
    def get_value(self):
        """获取触摸值.

        获取触摸按键1的模拟值，随外界状态变化而变化。
        正常情况下，触摸值在 0~100 范围内，但由于器件差异，个别
        板子的值会超出这个范围。

        Args:
            无
        Returns:
            int (0 ~ 100): 不同板子情况不同    
        """
        pass

class touchpad2_c(object):
    def __init__(self):
        pass

    # __fun_type__: read
    def is_touched(self):
        """检测触摸状态.

        检测触摸按键2是否被触发

        Args:
            无
        Returns:
            bool        
        """
        pass

    # __fun_type__: write
    def set_touch_threshold(self, value):
        """设置触摸灵敏度阈值.

        设置触摸按键2的灵敏度阈值

        Args:
            value (float): 0 ~ 1; 触摸灵敏度，值越大，越不灵敏
        Returns:
            None       
        """
        pass

    # __fun_type__: write
    def set_touch_sensitivity(self, level):
        """设置触摸灵敏度等级.

        设置触摸按键2的灵敏度等级

        Args:
            level (str): "high"/"middle"/"low"
        Returns:
            None
        """
        pass

    # __fun_type__: read
    def get_value(self):
        """获取触摸值.

        获取触摸按键2的模拟值，随外界状态变化而变化。
        正常情况下，触摸值在 0~100 范围内，但由于器件差异，个别
        板子的值会超出这个范围。

        Args:
            无
        Returns:
            int (0 ~ 100): 不同板子情况不同    
        """
        pass

class touchpad3_c(object):
    def __init__(self):
        pass

    # __fun_type__: read
    def is_touched(self):
        """检测触摸状态.

        检测触摸按键3是否被触发

        Args:
            无
        Returns:
            bool        
        """
        pass

    # __fun_type__: write
    def set_touch_threshold(self, value):
        """设置触摸灵敏度阈值.

        设置触摸按键3的灵敏度阈值

        Args:
            value (float): 0 ~ 1; 触摸灵敏度，值越大，越不灵敏
        Returns:
            None       
        """
        pass

    # __fun_type__: write
    def set_touch_sensitivity(self, level):
        """设置触摸灵敏度等级.

        设置触摸按键3的灵敏度等级

        Args:
            level (str): "high"/"middle"/"low"
        Returns:
            None
        """
        pass

    # __fun_type__: read
    def get_value(self):
        """获取触摸值.

        获取触摸按键3的模拟值，随外界状态变化而变化。
        正常情况下，触摸值在 0~100 范围内，但由于器件差异，个别
        板子的值会超出这个范围。

        Args:
            无
        Returns:
            int: 0 ~ 100; 不同板子情况不同    
        """
        pass

class microphone_c():
    def __init__(self):
        pass

    # __fun_type__: read
    def get_loudness(self):
        """获取音量值.

        获取通过麦克风计算得到的音量值。

        Args:
            无
        Returns:
            int : 0 ~ 100    
        """
        pass       

class motion_sensor_c(object):
    def __init__(self):
        pass
    # __fun_type__: read
    def get_acceleration(self, axis):
        """获取音量值.

        获取三轴加速度分量

        Args:
            axis (str): 'x'/'y'/'z'
        Returns:
            float : -2~2; 单位： g   
        """
        pass       

    # __fun_type__: read
    def get_gyroscope(self, axis):
        """获取角速度.

        获取三轴角速度分量

        Args:
            axis (str): 'x'/'y'/'z'
        Returns:
            float : 无限制; 单位： °/s
        """
        pass
    # __fun_type__: read
    def get_rotation(self, axis):
        """获取旋转的角度.

        获取三轴旋转的角度，逆时针角度为正。该值存在积累误差，请使用“reset_rotation” 函数校准。

        Args:
            axis (str): 'x'/'y'/'z'
        Returns:
            float : 无限制; 单位： °/s
        """
        pass

    # __fun_type__: read
    def reset_rotation(self, axis = "all"):
        pass
    # __fun_type__: read
    def is_shaked(self):
        pass
    # __fun_type__: read
    def is_shaken(self):
        pass
    # __fun_type__: read
    def get_shake_strength(self):
        pass
    # __fun_type__: read
    def is_tilted_left(self):
        pass
    # __fun_type__: read
    def is_tilted_right(self):
        pass
    # __fun_type__: read
    def is_arrow_up(self):
        pass
    # __fun_type__: read
    def is_arrow_down(self):
        pass
    # __fun_type__: read
    def is_led_ring_up(self):
        pass
    # __fun_type__: read
    def is_led_ring_down(self):
        pass
    # __fun_type__: read
    def is_rotate_clockwise(self):
        pass
    # __fun_type__: read
    def is_rotate_anticlockwise(self):
        pass
    # __fun_type__: read
    def is_free_fall(self):
        pass
    # __fun_type__: read
    def get_pitch(self):
        pass
    # __fun_type__: read
    def get_roll(self):
        pass
    # __fun_type__: read
    def get_yaw(self):
        pass  

class speaker_c(object):
    def __init__(self):
        pass

    def change_volume(self, value):
        pass

    def set_volume(self, value):
        pass
    # __fun_type__: read
    def get_volume(self):
        pass

    def stop_sounds(self):
        pass

    def play_melody_until_done(self, file_name):
        pass


    def play_melody(self, file_name):
        pass

    def play_tone(self, frequency, time_s = None):
        pass

    def play_note(self, note, beat = None):
        pass

    def rest(self, beat):
        pass


class pin0_c(object):
    def __init__(self, pin_id = 0):
        pass
    # __fun_type__: read
    def read_digital(self):
        pass

    def write_digital(self, value):
        pass

    def servo_write(self, value):
        pass
    # __fun_type__: read
    def read_analog(self):
        pass

    def write_analog(self, value):
        pass
    # __fun_type__: read
    def is_touched(self):
        pass

    def set_touchpad_threshold(self, value):
        pass

    def set_touchpad_sensitivity(self, level):
        pass
    # __fun_type__: read
    def get_touchpad_value(self):
        pass
    
    def set_pwm_frequency(self, frequency):
        pass

    def set_pwm_duty(self, duty):
        pass

    def play_note(self, note, beat = None):
        pass

    def play_tone(self, frequency, time_s = None):
        pass

class pin1_c(object):
    def __init__(self, pin_id = 0):
        pass
    # __fun_type__: read
    def read_digital(self):
        pass

    def write_digital(self, value):
        pass

    def servo_write(self, value):
        pass
    # __fun_type__: read
    def read_analog(self):
        pass

    def write_analog(self, value):
        pass
    # __fun_type__: read
    def is_touched(self):
        pass

    def set_touchpad_threshold(self, value):
        pass

    def set_touchpad_sensitivity(self, level):
        pass
    # __fun_type__: read
    def get_touchpad_value(self):
        pass
    
    def set_pwm_frequency(self, frequency):
        pass

    def set_pwm_duty(self, duty):
        pass

    def play_note(self, note, beat = None):
        pass

    def play_tone(self, frequency, time_s = None):
        pass

class pin2_c(object):
    def __init__(self, pin_id = 0):
        pass
    # __fun_type__: read
    def read_digital(self):
        pass

    def write_digital(self, value):
        pass

    def servo_write(self, value):
        pass
    # __fun_type__: read
    def read_analog(self):
        pass

    def write_analog(self, value):
        pass
    # __fun_type__: read
    def is_touched(self):
        pass

    def set_touchpad_threshold(self, value):
        pass

    def set_touchpad_sensitivity(self, level):
        pass
    # __fun_type__: read
    def get_touchpad_value(self):
        pass
    
    def set_pwm_frequency(self, frequency):
        pass

    def set_pwm_duty(self, duty):
        pass

    def play_note(self, note, beat = None):
        pass

    def play_tone(self, frequency, time_s = None):
        pass

class pin3_c(object):
    def __init__(self, pin_id = 0):
        pass
    # __fun_type__: read
    def read_digital(self):
        pass

    def write_digital(self, value):
        pass

    def servo_write(self, value):
        pass
    # __fun_type__: read
    def read_analog(self):
        pass

    def write_analog(self, value):
        pass

    # __fun_type__: read
    def is_touched(self):
        pass

    def set_touchpad_threshold(self, value):
        pass

    def set_touchpad_sensitivity(self, level):
        pass
    # __fun_type__: read
    def get_touchpad_value(self):
        pass
    
    def set_pwm_frequency(self, frequency):
        pass

    def set_pwm_duty(self, duty):
        pass

    def play_note(self, note, beat = None):
        pass

    def play_tone(self, frequency, time_s = None):
        pass

class mesh_c():
    def __init__(self):
        pass

    def start_group(self, group_name):
        pass


    def join_group(self, group_name):
        pass

    # __fun_type__: read
    def get_info(self, message):
        pass

    def broadcast(self, message, value = ""):
        pass

class wifi_c():
    def __init__(self):
        pass

    # __fun_type__: read
    def is_connected(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    # __fun_type__: read
    def get_mac(self):
        pass

    # only the two function below face to users
    def start(self, ssid, password):
        pass

class gamepad_c():
    def __init__(self):
        pass

    # __fun_type__: read
    def is_key_pressed(button):
        """获取蓝牙手柄按键状态.

        获取各个按键状态。

        Args:
            button (str): "R1"、 "R2"、 "L1"、, "L2"、
                        "N1"、 "N2"、 "N3"、 "N4"、
                        "Up"、 "Down"、 "Left"、 "Right"、
                        "Start"、"Select"、
                        "L_Thumb"、 "R_Thumb"
        Returns:
            bool : 
        """
        pass

    # __fun_type__: read
    def get_joystick(joystick_pos):
        """获取遥杆值分量.

        获取两个遥杆的值。

        Args:
            axis (str): Lx"、"Ly"、"Rx"、"Ry
        Returns:
            int : -·00 ~ 100
        """
        pass

    # __fun_type__: read
    def get_all():
        """获取所有按键及要感值.

        获取遥控器所有值.顺序为

        Args:
            无
        Returns:
            list : 
        """
        return get_joystick.get_all_data()
