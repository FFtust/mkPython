import time

class motion_sensor_c():
    def __init__(self):
        pass
        
    # __fun_type__: read
    def get_acceleration(self, axis, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_gyroscope(self, axis, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_rotation(self, axis, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def reset_rotation(self, axis = "all", index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_shaken(self, level = "usual", index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_shake_strength(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_pitch(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_roll(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_tilted_left(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_tilted_right(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_tilted_forward(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_tilted_backward(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_face_up(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_face_down(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def is_upright(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
