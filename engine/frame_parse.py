class serial_num_c():
    def __init__(self):
        self.current_num = 0

    @property
    def value():
        value = self.current_num
        self.current_num += 1
        self.current_num &= 0xFFFF

        return value

serial_num = serial_num_c()
