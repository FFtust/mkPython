
#coding=UTF-8

class led_c():
    ''' led matrix '''
    def __init__(self):
        pass

    def show_all(self, r, g, b, percentage):
        """function description.

        set all led.

        Args:
            r (int): 0 ~ 255; color component abou red 
            g (int): 0 ~ 255; color component abou green
            b (int): 0 ~ 255; color component abou blue
            percentage (int): 0 ~ 100; brightness percentage
        Returns:
            None

        """
        pass

    def show_single(self, index, r, g, b):
        """function description.

        set single led.

        Args:
            r (int): 0 ~ 255; color component abou red 
            g (int): 0 ~ 255; color component abou green
            b (int): 0 ~ 255; color component abou blue

        Returns:
            None

        """
        pass

    def move(self, offset):
        """function description.

        led matrix move with offset.

        Args:
            offset (int): no limit; offset of led index 

        Returns:
            None

        """
        pass

class button_c():
    def __init__(self):
        pass

    def is_pressed(self, index = 0):
        """function description.

        is button status actived.

        Returns:
            bool

        """

        pass
