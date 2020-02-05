import time
from engine.interface import get_value, request


class led_c():
    def __init__(self):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ())
    def show_all(self, r, g, b, percentage):
        request("1cbdb2953d92c3e10c8e2deeda188cee", ( r, g, b, percentage))
    def show_single(self, index, r, g, b):
        request("a581882c591598190744c5a2966554cd", ( index, r, g, b))
    def move(self, offset):
        request("3734a903022249b3010be1897042568e", ( offset))
    def off_single(self, led_id):
        request("44c010a12ca2d7f2c4dbef562e4aafe2", ( led_id))
    def off_all(self):
        request("317dc2aa04b0f93ef2d4cc071ad0a4de", ())
    def clear(self):
        request("01bc6f8efa4202821e95f4fdf6298b30", ())
    def show_ring(self, color, offset = 0):
        request("33c7c3da13b8092ea0aba22a8c5b3820", ( color, offset ))
    def ring_graph(self, pct):
        request("12b28ad7db42f18ac72cf391943d710b", ( pct))
    def show_animation(self, name, wait = True):
        request("14e116547c19444be327cb603ba4c4cc", ( name, wait ))
    def show_full_color(self, data, offset = 0):
        request("978e3bbc7af8d29a108cb3b121d18c97", ( data, offset ))

class button_c():
    def __init__(self):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ())
    def is_pressed(self, index = 0):
        return get_value("53826c458e60223a09b69fa64eb8d251", ( index ))

class touchpad0_c(object):
    def __init__(self, touchpad_id):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ( touchpad_id))
    def is_touched(self):
        return get_value("fd9e4a1a080800e08a7b02793cbdddf7", ())
    def set_touch_threshold(self, value):
        request("cb84d9e3b7d31d27a82a88afecb7dfee", ( value))
    def set_touch_sensitivity(self, level):
        request("ed11cbba0cd10bc29cf519fa34f99262", ( level))
    def get_value(self):
        return get_value("d4a2961923ef128e277f41088ab3dca8", ())

class touchpad1_c(object):
    def __init__(self, touchpad_id):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ( touchpad_id))
    def is_touched(self):
        return get_value("fd9e4a1a080800e08a7b02793cbdddf7", ())
    def set_touch_threshold(self, value):
        request("cb84d9e3b7d31d27a82a88afecb7dfee", ( value))
    def set_touch_sensitivity(self, level):
        request("ed11cbba0cd10bc29cf519fa34f99262", ( level))
    def get_value(self):
        return get_value("d4a2961923ef128e277f41088ab3dca8", ())

class touchpad2_c(object):
    def __init__(self, touchpad_id):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ( touchpad_id))
    def is_touched(self):
        return get_value("fd9e4a1a080800e08a7b02793cbdddf7", ())
    def set_touch_threshold(self, value):
        request("cb84d9e3b7d31d27a82a88afecb7dfee", ( value))
    def set_touch_sensitivity(self, level):
        request("ed11cbba0cd10bc29cf519fa34f99262", ( level))
    def get_value(self):
        return get_value("d4a2961923ef128e277f41088ab3dca8", ())

class touchpad3_c(object):
    def __init__(self, touchpad_id):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ( touchpad_id))
    def is_touched(self):
        return get_value("fd9e4a1a080800e08a7b02793cbdddf7", ())
    def set_touch_threshold(self, value):
        request("cb84d9e3b7d31d27a82a88afecb7dfee", ( value))
    def set_touch_sensitivity(self, level):
        request("ed11cbba0cd10bc29cf519fa34f99262", ( level))
    def get_value(self):
        return get_value("d4a2961923ef128e277f41088ab3dca8", ())

class microphone_c():
    def __init__(self):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ())
    def get_loudness(self):
        return get_value("95882c6974eb398220d140105cd07c39", ())

class motion_sensor_c(object):
    def __init__(self):
        request("2eacefd9a69c9d858e68ad3e94691bf9", ())
    def get_acceleration(self, axis):
        return get_value("5fee334e9e6f426c4fcc1acd439963dd", ( axis))
    def get_gyroscope(self, axis):
        return get_value("d1a1eeea22735312c050a7bf813df20e", ( axis))
    def get_rotation(self, axis):
        return get_value("1baeb0fe49174b1978fc19d77b19c5f4", ( axis))
    def reset_rotation(self, axis = "all"):
        return get_value("fdc5e3eda9428657ff8561ba901025fe", ( axis ))
    def is_shaked(self):
        return get_value("d529fc7d3f66ef2d149bd90be0dd9a87", ())
    def is_shaken(self):
        return get_value("f7d17d9a9cc93decaeb48e49af9be00b", ())
    def get_shake_strength(self):
        return get_value("53ba0a365d752f3afc396f67921deee7", ())
    def is_tilted_left(self):
        return get_value("9f7ead3f7aedc5d210e510fe187348a5", ())
    def is_tilted_right(self):
        return get_value("c8761d7f440677be5990c4d23ec71530", ())
    def is_arrow_up(self):
        return get_value("41addabccef6428382c84c8a8aefc33c", ())
    def is_arrow_down(self):
        return get_value("02631576a6d6dcd1787130b6a6f54b7b", ())
    def is_led_ring_up(self):
        return get_value("d1294f5cbf0b3da7313f5f565297eca5", ())
    def is_led_ring_down(self):
        return get_value("9f05f7bd21700717e2b46ef9e32ef557", ())
    def is_rotate_clockwise(self):
        return get_value("4d1682caec0a16bda05ef54f5cba6a61", ())
    def is_rotate_anticlockwise(self):
        return get_value("8d809efb166fff4327b10d8f9f912951", ())
    def is_free_fall(self):
        return get_value("6a39c608bd650c12961019b153afc7a5", ())
    def get_pitch(self):
        return get_value("7fb3a7285965b72c52f8a00ae84c1f7e", ())
    def get_roll(self):
        return get_value("3805c44f8a18e831d758fa452eb6a70a", ())
    def get_yaw(self):
        return get_value("2814b3bab04704fd0046e5eb05b11498", ())
