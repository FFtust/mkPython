import time

class smart_camera_c():
    def __init__(self):
        pass
        
    def get_fills_all_data(self, fills_id, index = 1):# 获取某个色块所有信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_fills_report_mode(self, mode, timestamp, index = 1):# 设置某个色块所有信息的上报模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_fills_sigle_data(self, fills_id, type_id, index = 1):# 获取某个色块的单独的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_line_all_data(self, index = 1):#获取线的所有信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_line_report_mode(self, mode, timestamp, index = 1):#设置线所有信息的上报模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_line_sigle_data(self, type_id, index = 1):#获取线的单独的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_crossings_all_data(self, index = 1):#获交叉口的所有信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_crossings_report_mode(self, mode, timestamp, index = 1):#设置交叉口的所有信息的上报模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_crossings_sigle_data(self, type_id, index = 1):#获取交叉口的单独的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_crossings_line_angle_sigle_data(self, index = 1):#获取交叉口线角度的单独的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_barcode_all_data(self, barcode_id, index = 1):#获取某个条形码的所有信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_barcode_report_mode(self, mode, timestamp, index = 1):#设置某个条形码的所有信息的上报模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_barcode_sigle_data(self, barcode_id, type_id, index = 1):#获取条形码X的单独的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_button_data(self, index = 1):#获取按键的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_button_report_mode(self, mode, timestamp, index = 1):#设置按键信息的上报模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_learn_data(self, index = 1):#获取学习的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_camera_sensitometry(self, level, index = 1):#设置摄像头曝光度
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_led_rgb(self, r, g, b, index = 1):#设置RGB灯
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_fill_light_status(self, sta, index = 1):#设置补光灯状态
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_line_follow_vector_mode(self, mode, index = 1):#设置巡线vector模式（不开放）
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_line_follow_mode(self, mode, index = 1):#设置巡线模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_turning_angle(self, index = 1):#获取按键的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_fills_count(self, index = 1):#获取按键的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_barcode_count(self, index = 1):#获取按键的信息
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_next_turning_angle(self, angle, index = 1):#设置下一次转向角度
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_default_turning_angle(self, angle, index = 1):#设置默认的转向角度（不开放）
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_fills_learn_mode(self, fills_id, t, index = 1):#设置学习色块模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def stop_learn(self, index = 1):#设置结束学习（不开放）
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def abandon_learn(self, index = 1):#设置放弃学习（不开放）
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_pixy_mode(self, mode, index = 1):#设置pixy模块模式
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_mode(self, mode = "color", index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def learn(self, sign = 1, t = "until_button", index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def detect_sign(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_x(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_y(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_wide(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_hight(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def detect_sign_location(self, sign, location, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_location(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def __caculate_sign_location(self, x, y):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def open_light(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def close_light(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def reset(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def detect_label(self, label, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_label_x(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_label_y(self, sign, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_vector_end_x(self, index = 1):#line -> vector
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_vector_end_y(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_vector_start_x(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_vector_start_y(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def detect_cross(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_cross_x(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_cross_y(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_cross_road(self, index = 1):#获取交叉口数目？
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_cross_angle(self, sn = 1, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_line(self, mode = "black", index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_vector_angle(self, angle, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_vector_angle(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_kp(self, kp, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_fills_diff_speed(self, sign, tar_x, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_diff_speed_x(self, sign, tar_x, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_diff_speed_y(self, sign, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_sign_diff_speed(self, sign, axis = "x", axis_val = 0, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_barcode_diff_speed(self, label, tar_x, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_label_diff_speed_x(self, label, tar_x, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_label_diff_speed_y(self, label, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_label_diff_speed(self, label, axis = "x", axis_val = 0, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def get_follow_vector_diff_speed(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_fills(self, sign, tar_x, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_sign_x(self, sign, tar_x, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_sign_y(self, sign, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_sign(self, sign, axis = "x", axis_val = 0, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_barcode(self, label, tar_x, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_label_x(self, label, tar_x, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_label_y(self, label, tar_y, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def is_lock_label(self, label, axis = "x", axis_val = 0, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
