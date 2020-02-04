
#coding=UTF-8

class led_c():
    ''' led matrix '''
    def __init__(self):
        pass

    def show_all(self, r, g, b, percentage):
        """control all the leds.

        set all leds with r/g/b components.

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
        """control single led.

        set led which id is 'index' with r/g/b components.

        Args:
            index (int): 1 ~ 12; led index
            r (int): 0 ~ 255; color component abou red 
            g (int): 0 ~ 255; color component abou green
            b (int): 0 ~ 255; color component abou blue

        Returns:
            None
        Raises:
        
        """
        pass

    def move(self, offset):
        """function description.

        led matrix move with offset.

        Args:
            offset (int): no limit; offset of led index 

        Returns:
            None
        Raises:
        
        """
        pass

class button_c():
    def __init__(self):
        pass

    def is_pressed(self, index = 0):
        """function description.

        is button status actived.

        Args:
            index (int): 0~ ; button index 
        Returns:
            bool
        Raises:
        
        """

        pass
