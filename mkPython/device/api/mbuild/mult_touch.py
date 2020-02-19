import time

class mult_touch_c():
    def __init__(self):
        pass
        
    # __fun_type__: read
    def is_active(self, ch, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    # __fun_type__: read
    def get_value(self, position, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def reset_threshold(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
    def set_sensitivity(self, sen, index = 1):
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
    # __fun_type__: read
    def get_all_status(self, index = 1):
        """简介. 

        详细描述。

        Args:
            index (int)： 模块ID。同类的第几个模块
        Returns:
            (int) :  返回值；
        """
