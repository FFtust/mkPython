import time

class angle_sensor_c():
    def __init__(self):
        pass
    # __fun_type__: read
    def get_angle(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_angle_speed(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_rotating_clockwise(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_rotating_anticlockwise(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def reset_angle(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_report_mode(self, mode,timestamp,index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
