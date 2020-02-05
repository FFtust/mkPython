#!/usr/bin/python3.7 
# -*- coding: utf-8 -*- 

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
            index (int): 1 ~ 12; led 编号
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
    def is_pressed(self, index = 0):
        """按键是否被按下.

        检测按键的状态是否被按下. 只有一个按键时，默认不填

        Args:
            index (int): 0~ ; 按键编号
        Returns:
            bool        
        """

        pass
