import time
from engine.interface import get_value, request


class led_c():
    def __init__(self):
        request("f4f2cdc3a4ed04256d2e0b12cec89fc7", ())
    def show_all(self, r, g, b, percentage = 100):
        request("16d39837918e0da88b3a83036286ec49", ( r, g, b, percentage ))
    def show_single(self, index, r, g, b):
        request("4717c56f3741f1b9d0e82f630031a2fc", ( index, r, g, b))
    def move(self, offset = 1):
        request("3164e897ffb74c0994c83a84f4938989", ( offset ))
    def off_single(self, led_id):
        request("d057d4e05265152f591947da67e56cdf", ( led_id))
    def off_all(self):
        request("2cb1b550dde3e171e4ff97f096c699e0", ())
    def clear(self):
        request("15904b85962ca174176d6289144ff3b4", ())
    def show_ring(self, color, offset = 0):
        request("54e1cbba961cb133b1bcf1eb88488589", ( color, offset ))
    def ring_graph(self, pct):
        request("af902a2ae397b1510964db394611d39d", ( pct))
    def show_animation(self, name, wait = True):
        request("052e9358ddd5876394e485e7bc842c7f", ( name, wait ))
    def show_full_color(self, data, offset = 0):
        request("1d51112c29269f59f75785191734f7f3", ( data, offset ))

class button_c():
    def __init__(self):
        request("7052d3b4202ecfa2e398a35fe6bfa83b", ())
    def is_pressed(self, index = 0):
        return get_value("071f15bdd29f54daa4d0d6e244b31fe7", ( index ))

class touchpad0_c(object):
    def __init__(self):
        request("d0ec7b5048388016d21d52a2a399abef", ())
    def is_touched(self):
        return get_value("f28c95e27c689be70a83e1f9776cc8e2", ())
    def set_touch_threshold(self, value):
        request("0aee33b41b57a1a3a326fabe5062538c", ( value))
    def set_touch_sensitivity(self, level):
        request("03a628307601332a55f13fd4424f15eb", ( level))
    def get_value(self):
        return get_value("5f0cadda9f806e01f88da8b87559cb6e", ())

class touchpad1_c(object):
    def __init__(self):
        request("41d0023c5e2607e5e1d04911d4d69d75", ())
    def is_touched(self):
        return get_value("d1d4308dd5d22c17d3966c47ccd60f70", ())
    def set_touch_threshold(self, value):
        request("b8af32fa7771f6cfdebe0af870248a58", ( value))
    def set_touch_sensitivity(self, level):
        request("9a4fa1a80cac2513dc07754668aa3de1", ( level))
    def get_value(self):
        return get_value("c9f686cc9879592922d3f0516c62c0ca", ())

class touchpad2_c(object):
    def __init__(self):
        request("c45179bf8c1b41cff1b8212150a7cb66", ())
    def is_touched(self):
        return get_value("186334acb28cdef742ee9b481762f6d6", ())
    def set_touch_threshold(self, value):
        request("dd2358abccfdd6df3fea1ad60eb7034f", ( value))
    def set_touch_sensitivity(self, level):
        request("294cb80724362dd06337f1c796738802", ( level))
    def get_value(self):
        return get_value("e92dfe510847bbb1c6952251a0772419", ())

class touchpad3_c(object):
    def __init__(self):
        request("8d4e58f23f2af227ef4c7d62d724a143", ())
    def is_touched(self):
        return get_value("4a059a33204d77954ecc2d9dcc3973a2", ())
    def set_touch_threshold(self, value):
        request("30711506f4ff8ba45f41139629c59516", ( value))
    def set_touch_sensitivity(self, level):
        request("6e9673465d792ac0071a6b259fc730cc", ( level))
    def get_value(self):
        return get_value("22b1f497925330eeb3a7c7eeae24736e", ())

class microphone_c():
    def __init__(self):
        request("a51e56d37eddade49d47a08c097c4a6e", ())
    def get_loudness(self):
        return get_value("f0821febe5198537519aab9a5a47197e", ())

class motion_sensor_c(object):
    def __init__(self):
        request("60c2853371bb36fc1737d4ddaf681d29", ())
    def get_acceleration(self, axis):
        return get_value("fd5eb585e9b2da0346e75c3aa066d575", ( axis))
    def get_gyroscope(self, axis):
        return get_value("676088755be7dc9b51e3c60d4444d09e", ( axis))
    def get_rotation(self, axis):
        return get_value("066e7834857a4070facfb0baf6b344da", ( axis))
    def reset_rotation(self, axis = "all"):
        return get_value("8c5f098af82a67337f2aa2965872878a", ( axis ))
    def is_shaked(self):
        return get_value("af2bbb0169521bc353a0829d9a58adc6", ())
    def is_shaken(self):
        return get_value("0b0ba2fb03cd4a73f6bd831e174d9a2b", ())
    def get_shake_strength(self):
        return get_value("be0aec15129dc99d3b5efec0a040c963", ())
    def is_tilted_left(self):
        return get_value("cbeb1fa02d5a645797624655bed3ac68", ())
    def is_tilted_right(self):
        return get_value("901e878b9b14644df9032ccefba6f226", ())
    def is_arrow_up(self):
        return get_value("9fd0728c4f03885a0492856a1c6395f5", ())
    def is_arrow_down(self):
        return get_value("86e52f136a91118254740ba848341fc4", ())
    def is_led_ring_up(self):
        return get_value("9ce98198f29487eb18a518fa42eea594", ())
    def is_led_ring_down(self):
        return get_value("0f6ddf923e2e30672629c0287f4fbfe9", ())
    def is_rotate_clockwise(self):
        return get_value("f3aa9846dacb496e054c142917cf79cf", ())
    def is_rotate_anticlockwise(self):
        return get_value("78209dc05f90233b38ced40067f73ff9", ())
    def is_free_fall(self):
        return get_value("1985ad3fbec9e16c23186c23ad804288", ())
    def get_pitch(self):
        return get_value("bf545bd2aead7ec5841b1ae355433fa1", ())
    def get_roll(self):
        return get_value("9c1816917b4f5c2488fcc98898cf9800", ())
    def get_yaw(self):
        return get_value("02ec9ecd2e720e53f308d71ad809ec04", ())
