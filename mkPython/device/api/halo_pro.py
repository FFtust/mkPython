#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

""" 
优先实现
joystic_c
button_c
speaker_c
microphone_c
motion_sensor_c
temp_sensor_c
light_sensor_c
led_c
tts_c

未描述功能但已经实现的功能：
mesh
上传模式广播
IOT

"""



class temp_sensor_c():
    def __init__(self):
        pass  

    # __fun_type__: read
    def get_temperature(self, t_type = "c"):
        """获取温度值.

        获取温度值，摄氏度或者华氏度。

        Args:
            t_type (str)：温度类型，“c” 摄氏度， “f” 华氏度 
        Returns:
            (int) :  s实际温度值；
        """
        pass    

class joystic_c():
    def __init__(self):
        pass  

    # __fun_type__: read
    def is_pressed(self, t_type = "center"):
        """五项开关按下状态.

        获取五项开关各方向按下状态按下

        Args:
            t_type (str)：五向开关按键方向。"up"/"down"/"left"/"right"/"center" 
        Returns:
            bool: 
        """
        pass    

    # __fun_type__: read
    def get_count(self, t_type = "center"):
        """五项开关被按下次数.

        获取五项开关各方向被按下的次数。

        Args:
            t_type (str)：五向开关按键方向。"up"/"down"/"left"/"right"/"center" 
        Returns:
            bool: 
        """
        pass    

    # __fun_type__: read
    def reset_count(self, t_type = "center"):
        """重置五项开关被按下状态.

        重置五项开关各方向被按下的次数。

        Args:
            t_type (str)：五向开关按键方向。"all"/up"/"down"/"left"/"right"/"center" 
        Returns:
            bool: 
        """
        pass    

class led_c():
    ''' led matrix '''
    def __init__(self):
        pass
    # __fun_type__: write
    def show_all(self, r, g, b, percentage):
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
            index (int): 1 ~ 5; led 编号
            r (int): 0 ~ 255; 红色分量
            g (int): 0 ~ 255; 绿色分量
            b (int): 0 ~ 255; 蓝色分量

        Returns:
            None        
        """
        pass
    # __fun_type__: write
    def move(self, offset):
        """ LED 矩阵整体偏移.

        整个LED矩阵像右移动（显示屏正面朝上，摇杆在左放置）offset个位置，offset为负值时，反向.

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
            led_id (int): 1 ~ 5; led 编号

        Returns:
            None
        
        """
        pass 
    # __fun_type__: write
    def off_all(self):
        """ 熄灭所有LED灯.

        设置5颗灯全部为为熄灭状态.

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

        设置所有或者部分灯珠的RGB值，共15字节.
        从1~5颗灯依次计算

        Args:
            data (list，tuple): 15字节数据
            offset (int): 无限制; 旋转偏移
        Returns:
            None
        
        """
        pass 

class button_c():
    def __init__(self):
        pass

    # __fun_type__: read
    def is_pressed(self, index = 0):
        """按键是否被按下.

        检测按键的状态是否被按下. 只有一个按键时，默认不填

        Args:
            index (int): 0~ ; 按键编号
        Returns:
            bool        
        """

        pass

    # __fun_type__: read
    def get_count(self, index = 0):
        """按键是否被按下.

        检测按键的状态是否被按下. 只有一个按键时，默认不填

        Args:
            index (int): 0~ ; 按键编号
        Returns:
            bool        
        """

        pass

    # __fun_type__: read
    def reset_count(self, index = 0):
        """按键是否被按下.

        检测按键的状态是否被按下. 只有一个按键时，默认不填

        Args:
            index (int): 0~ ; 按键编号
        Returns:
            bool        
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

    # __fun_type__: write
    def start_recognise(self, file_name = ""):
        """开始录音，并保存到 file_name 文件中.

        获取麦克风数据，并保存。

        Args:
            file_name (str): 保存的文件名
        Returns:
            无    
        """
        pass


    # __fun_type__: write
    def stop_recognise(self):
        """停止录音.

        停止录音。

        Args:
            无
        Returns:
            无    
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

    # __fun_type__: write
    def reset_rotation(self, axis = "all"):
        """初始化旋转的角度.

        初始化三轴旋转的角度为0, 起到相对位置的校准作用。。

        Args:
            axis (str): 'x'/'y'/'z'/"all"
        Returns:
            无
        """
        pass

    # __fun_type__: read
    def is_shaken(self):
        """获取摇晃触发状态.

        当光环板pro处于摇晃状态时，触发

        Args:
            无
        Returns:
            无
        """
        pass

    # __fun_type__: read
    def get_shake_strength(self):
        """获取摇晃强度.

        当光环板pro摇晃越快，该值越大

        Args:
            无
        Returns:
            (int): 0 ~ 100
        """
        pass


    # __fun_type__: read
    def is_tilted_left(self):
        """是否处于左倾状态.

        以光环板pro正面水平放置为标准。向左方倾斜15°以上，将被定义为左倾状态

        Args:
            无
        Returns:
            bool:
        """
        pass
    # __fun_type__: read
    def is_tilted_right(self):
        """是否处于右倾状态.

        以光环板pro正面水平放置为标准。向右方倾斜15°以上，将被定义为右倾状态

        Args:
            无
        Returns:
            bool:
        """
        pass
    # __fun_type__: read
    def is_arrow_up(self):
        """是否处于箭头向上状态.

        以光环板pro正面水平放置为标准。箭头向上倾斜15度以上将被定义为箭头向上状态。

        Args:
            无
        Returns:
            bool:
        """
        pass
    # __fun_type__: read
    def is_arrow_down(self):
        """是否处于箭头向下状态.

        以光环板pro正面水平放置为标准。箭头向下倾斜15度以上将被定义为箭头向下状态。

        Args:
            无
        Returns:
            bool:
        """
        pass
    # __fun_type__: read
    def is_screen_up(self):
        """光环板pro是否正面向上.

        以光环板pro正面水平放置为标准。上下左右倾斜角度在75度以内就定义为屏幕向上状态

        Args:
            无
        Returns:
            bool:
        """
        pass
    # __fun_type__: read
    def is_screen_down(self):
        """光环板pro是否反面向上.

        以光环板pro反面向上水平放置为标准。上下左右倾斜角度在75度以内就定义为屏幕向上状态

        Args:
            无
        Returns:
            bool:
        """
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
        """获取俯仰角.

        返回俯仰角角度
        Args:
            无
        Returns:
            (int): -180 ~ 180; 单位：度
        """
        pass
    # __fun_type__: read
    def get_roll(self):
        """获取翻滚角.

        返回翻滚角角角度
        Args:
            无
        Returns:
            (int): -90 ~ 90; 单位：度
        """
        pass
    # __fun_type__: read
    def get_yaw(self):
        """获取航向角.

        返回航向角角度（需要电子罗盘）
        Args:
            无
        Returns:
            (int): -90 ~ 90; 单位：度
        """
        pass 

class light_sensor_c():
    def __init__(self):
        pass

    # __fun_type__: read
    def get_value(self):
        """获取光线值.

        获取光线传感器的。

        Args:
            无
        Returns:
            int : 0 ~ 100    
        """
        pass      



class speaker_c(object):
    def __init__(self):
        pass

    # __fun_type__: read
    def get_volume(self):
        """获取音量大小.

        返回当前音乐播放的音量大小，包括蜂鸣器和音乐文件播放。
        Args:
            无
        Returns:
            (int): 0 ~ 100;
        """
        pass

    # __fun_type__: write
    def set_volume(self, value):
        """设置音量大小.

        返回当前音乐播放的音量大小，包括蜂鸣器和音乐文件播放。
        Args:
            value (int): 0 ~ 100; 音量设置值 
        Returns:
            无
        """
        pass

    # __fun_type__: write
    def change_volume(self, value):
        """改变音量大小.

        改变当前音乐播放的音量大小，包括蜂鸣器和音乐文件播放。
        Args:
            value (int): -100 ~ 100; 音量改变值 
        Returns:
            无
        """
        pass

    # __fun_type__: read
    def get_tempo(self):
        """获取音调播放速度大小.

        返回当前音调播放的速度大小， 包括蜂鸣器和乐器播放功能。 
        Args:
            无
        Returns:
            (int): 0 ~ 100;
        """
        pass

    # __fun_type__: write
    def set_tempo(self, value):
        """设置音调的播放速度大小.

        返回当前音调的播放速度，包括蜂鸣器和乐器播放功能。 
        Args:
            value (int): 0 ~ 100; 播放速度设置值 
        Returns:
            无
        """
        pass

    # __fun_type__: write
    def change_tempo(self, value):
        """改变音调的播放速度.

        改变当前音调的播放速度，包括蜂鸣器和乐器播放功能。
        Args:
            value (int): -100 ~ 100; 播放速度改变值 
        Returns:
            无
        """
        pass


    # __fun_type__: write
    def stop_sounds(self):
        """停止音乐播放.

        停止扬声器当前播放的内容。
        Args:
            无
        Returns:
            无
        """
        pass

    # __fun_type__: write
    def play_melody_until_done(self, file_name):
        """播放内置音效直到播放结束.

        播放音效名为file_name的内置音效，等待音乐播放结束，该函数返回。
        Args:
            file_name (str): 内置音效名称。 
        Returns:
            无
        """
        pass

    # __fun_type__: write
    def play_melody(self, file_name):
        """播放内置音效.

        播放音效名为file_name的内置音效，开始播放后，函数立刻返回。
        Args:
            file_name (str): 内置音效名称。 
        Returns:
            无
        """
         pass

     # __fun_type__: write
    def play_tone(self, frequency, time_s = None):
        """播放蜂鸣器特定频率音调.

        播放频率为frequency的方波音效
        Args:
            frequency (int):  20 ~ 5000； 蜂鸣器播放频率 
            time_s (float): 0 ~ ; 持续时间， 不填则一直响； 单位：秒 
        Returns:
            无
        """
        pass

    # __fun_type__: write
    def play_note(self, note, beat = None):
        """播放蜂鸣器特定音调.

        播放音调名称为 note 的音效，
        Args:
            无
        Returns:
            无
        """
        pass


def tts_c():
    def __init__(self):
        pass

    # __fun_type__: write    
    def set_voice(self, voice = ""):
        """设置TTS发音效果.

        设置TTS播放效果为男声、女生等。
        Args:
            voice (str):  "s_male/s_female/e_male/e_female"； 标准男声/标准女声/情感男声/情感女生 
        Returns:
            无
        """
        pass

    # __fun_type__: write    
    def set_speed(self, speed = 5):
        """设置TTS发音速度.

        设置TTS播放速度，值越大，速度越快， 默认为5
        Args:
            speed (int):  0 ~ 15； 播放速度  
        Returns:
            无
        """
        pass

    # __fun_type__: write
    def say(self, meessage):
        """TTS播放文字.

        播放message的内容，自动识别语言。播放效果和 set_voice 和set_speed相关
        Args:
            meessage (str):  要播放的文字 
        Returns:
            无
        """  
        pass

def display_c():
     def __init__(self):
        pass

    # __fun_type__: write
    def set_paint_color(self, color):
        pass

    # __fun_type__: write
    def clear(self):
        pass
##########################################################
    # __fun_type__: write
    def print(self, message):
        pass

    # __fun_type__: write
    def print_line(self, mesage):
        pass

##########################################################
    # __fun_type__: write
    def draw_point(self, pos_x, pos_y):
        pass

    # __fun_type__: write
    def draw_line(self, s_x, s_y, e_x, e_y):
        pass

    # __fun_type__: write
    def draw_circle(self, pos_x, pos_y, r):
        pass

    # __fun_type__: write
    def draw_rectangular(self, pos_x, pos_y, length, width):
        pass

    # __fun_type__: write
    def draw_triangle(self, x1, y1, x2, y2, x3, y3):
        pass

############################################################
    # __fun_type__: write
    def draw_progress(self, percentage):
        pass

    # __fun_type__: write
    def draw_line_chart(self, value):
        pass

    # __fun_type__: write
    def draw_bar_chart(self, value):
        pass

    # __fun_type__: write
    def set_chart_title(self, title):
        pass
############################################################
    # __fun_type__: write
    def show_qr_code(self, link):
        pass
        
    # __fun_type__: write
    def set_qr_title(self, title):
        pass


DEFAULT_AP_IP    = "192.168.4.1"
DEFAULT_STA_IP   = "192.168.4.2"
DEFAULT_NETMARK  = "255.255.255.0"
DEFAULT_GATEWAY  = "192.168.1.1"
DEFAULT_DNS      = "172.16.50.20"
DEFAULT_AUTHMODE = AUTH_WPA2_PSK
DEFAULT_PORT     = 5050
class network_c(object):
    def __init__(self):
        pass

    # __fun_type__: write
    def config_ap(self, ssid, password, authmode  = DEFAULT_AUTHMODE):    
        pass

    # __fun_type__: write
    def config_sta(self, ssid, password):    
        pass

    # __fun_type__: read
    def is_connected(self):
        pass

    # __fun_type__: write
    def set_ip(self, ip, if_mode = None):
        pass

    # __fun_type__: write
    def set_subnet_mark(self, mark, if_mode = None):
        pass
    # __fun_type__: write
    def set_gateway(self, gw, if_mode = None):
        pass

    # __fun_type__: write
    def create_client(self):
        pass

    # __fun_type__: write
    def client_connect_to(self, ip_to, port = DEFAULT_PORT):
        pass

    # __fun_type__: write
    def create_server(self, port = DEFAULT_PORT):
        pass

    # __fun_type__: write
    def server_wait_connection(self, port = DEFAULT_PORT):
        pass

    # __fun_type__: read
    def server_get_connections(self, port = DEFAULT_PORT):
        pass

    # __fun_type__: read
    def server_get_latest_connection(self, port = DEFAULT_PORT):
        pass

    # __fun_type__: write
    def write(self, data, mode, ip_to, port = DEFAULT_PORT):
        pass

    # __fun_type__: write
    def write_line(self, data, mode, ip_to, port = DEFAULT_PORT):
        pass

    # __fun_type__: read
    def read(self, mode, ip_from, port = DEFAULT_PORT):
        pass

    # __fun_type__: read
    def read_line(self, mode, ip_from, port = DEFAULT_PORT):
        pass
