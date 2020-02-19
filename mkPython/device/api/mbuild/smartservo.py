import time

class smartservo_c():
    def __init__(self):
        pass
        
    def set_zero(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def move_to(self, position, speed, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def move(self, position, speed, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_power(self, pwm, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_speed_upload_mode(self, mode, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_position_upload_mode(self, mode, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def back_to_zero(self, speed, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def move_to_in_time(self, position, time, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def move_to_with_torque(self, position, speed, strength, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def move_with_torque(self, position, speed, strength, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def lock(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def unlock(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def turn(self, angle, speed, index = 1):  # angle: drgree   speed:unit :degree per second
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def turn_to(self, angle, speed, index = 1 ): # angle: drgree   speed:unit :degree per second
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def stop(self, index = "all"):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def run(self, power, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
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
    def get_speed(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # def get_cycles(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def lock_angle(self, index = "all"):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def release_angle(self, index = "all"):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def reset(self, index = "all"):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
