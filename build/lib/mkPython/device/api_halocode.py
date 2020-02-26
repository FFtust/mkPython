import time



class led_c():

    def __init__(self, adapter):

        self.adapter = adapter

    def show_all(self, r, g, b, percentage = 100):
        self.adapter.process.request("16d39837918e0da88b3a83036286ec49", ( r, g, b, percentage ))

    def show_single(self, index, r, g, b):
        self.adapter.process.request("4717c56f3741f1b9d0e82f630031a2fc", ( index, r, g, b))

    def move(self, offset = 1):
        self.adapter.process.request("3164e897ffb74c0994c83a84f4938989", ( offset ))

    def off_single(self, led_id):
        self.adapter.process.request("d057d4e05265152f591947da67e56cdf", ( led_id))

    def off_all(self):
        self.adapter.process.request("2cb1b550dde3e171e4ff97f096c699e0", ())

    def clear(self):
        self.adapter.process.request("15904b85962ca174176d6289144ff3b4", ())

    def show_ring(self, color, offset = 0):
        self.adapter.process.request("54e1cbba961cb133b1bcf1eb88488589", ( color, offset ))

    def ring_graph(self, pct):
        self.adapter.process.request("af902a2ae397b1510964db394611d39d", ( pct))

    def show_animation(self, name, wait = True):
        self.adapter.process.request("052e9358ddd5876394e485e7bc842c7f", ( name, wait ))

    def show_full_color(self, data, offset = 0):
        self.adapter.process.request("1d51112c29269f59f75785191734f7f3", ( data, offset ))



class button_c():

    def __init__(self, adapter):

        self.adapter = adapter

    def is_pressed(self):
        return self.adapter.process.get_value("071f15bdd29f54daa4d0d6e244b31fe7", ())



class touchpad0_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def is_touched(self):
        return self.adapter.process.get_value("f28c95e27c689be70a83e1f9776cc8e2", ())

    def set_touch_threshold(self, value):
        self.adapter.process.request("0aee33b41b57a1a3a326fabe5062538c", ( value))

    def set_touch_sensitivity(self, level):
        self.adapter.process.request("03a628307601332a55f13fd4424f15eb", ( level))

    def get_value(self):
        return self.adapter.process.get_value("5f0cadda9f806e01f88da8b87559cb6e", ())



class touchpad1_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def is_touched(self):
        return self.adapter.process.get_value("d1d4308dd5d22c17d3966c47ccd60f70", ())

    def set_touch_threshold(self, value):
        self.adapter.process.request("b8af32fa7771f6cfdebe0af870248a58", ( value))

    def set_touch_sensitivity(self, level):
        self.adapter.process.request("9a4fa1a80cac2513dc07754668aa3de1", ( level))

    def get_value(self):
        return self.adapter.process.get_value("c9f686cc9879592922d3f0516c62c0ca", ())



class touchpad2_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def is_touched(self):
        return self.adapter.process.get_value("186334acb28cdef742ee9b481762f6d6", ())

    def set_touch_threshold(self, value):
        self.adapter.process.request("dd2358abccfdd6df3fea1ad60eb7034f", ( value))

    def set_touch_sensitivity(self, level):
        self.adapter.process.request("294cb80724362dd06337f1c796738802", ( level))

    def get_value(self):
        return self.adapter.process.get_value("e92dfe510847bbb1c6952251a0772419", ())



class touchpad3_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def is_touched(self):
        return self.adapter.process.get_value("4a059a33204d77954ecc2d9dcc3973a2", ())

    def set_touch_threshold(self, value):
        self.adapter.process.request("30711506f4ff8ba45f41139629c59516", ( value))

    def set_touch_sensitivity(self, level):
        self.adapter.process.request("6e9673465d792ac0071a6b259fc730cc", ( level))

    def get_value(self):
        return self.adapter.process.get_value("22b1f497925330eeb3a7c7eeae24736e", ())



class microphone_c():

    def __init__(self, adapter):

        self.adapter = adapter

    def get_loudness(self):
        return self.adapter.process.get_value("f0821febe5198537519aab9a5a47197e", ())



class motion_sensor_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def get_acceleration(self, axis):
        return self.adapter.process.get_value("fd5eb585e9b2da0346e75c3aa066d575", ( axis))

    def get_gyroscope(self, axis):
        return self.adapter.process.get_value("676088755be7dc9b51e3c60d4444d09e", ( axis))

    def get_rotation(self, axis):
        return self.adapter.process.get_value("066e7834857a4070facfb0baf6b344da", ( axis))

    def reset_rotation(self, axis = "all"):
        return self.adapter.process.get_value("8c5f098af82a67337f2aa2965872878a", ( axis ))

    def is_shaked(self):
        return self.adapter.process.get_value("af2bbb0169521bc353a0829d9a58adc6", ())

    def is_shaken(self):
        return self.adapter.process.get_value("0b0ba2fb03cd4a73f6bd831e174d9a2b", ())

    def get_shake_strength(self):
        return self.adapter.process.get_value("be0aec15129dc99d3b5efec0a040c963", ())

    def is_tilted_left(self):
        return self.adapter.process.get_value("cbeb1fa02d5a645797624655bed3ac68", ())

    def is_tilted_right(self):
        return self.adapter.process.get_value("901e878b9b14644df9032ccefba6f226", ())

    def is_arrow_up(self):
        return self.adapter.process.get_value("9fd0728c4f03885a0492856a1c6395f5", ())

    def is_arrow_down(self):
        return self.adapter.process.get_value("86e52f136a91118254740ba848341fc4", ())

    def is_led_ring_up(self):
        return self.adapter.process.get_value("9ce98198f29487eb18a518fa42eea594", ())

    def is_led_ring_down(self):
        return self.adapter.process.get_value("0f6ddf923e2e30672629c0287f4fbfe9", ())

    def is_rotate_clockwise(self):
        return self.adapter.process.get_value("f3aa9846dacb496e054c142917cf79cf", ())

    def is_rotate_anticlockwise(self):
        return self.adapter.process.get_value("78209dc05f90233b38ced40067f73ff9", ())

    def is_free_fall(self):
        return self.adapter.process.get_value("1985ad3fbec9e16c23186c23ad804288", ())

    def get_pitch(self):
        return self.adapter.process.get_value("bf545bd2aead7ec5841b1ae355433fa1", ())

    def get_roll(self):
        return self.adapter.process.get_value("9c1816917b4f5c2488fcc98898cf9800", ())

    def get_yaw(self):
        return self.adapter.process.get_value("02ec9ecd2e720e53f308d71ad809ec04", ())



class speaker_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def change_volume(self, value):
        self.adapter.process.request("4831e56f6ffc3a35d49886f515622672", ( value))

    def set_volume(self, value):
        self.adapter.process.request("f38cbb8d8da8bf5ff93d045faaf78478", ( value))

    def get_volume(self):
        return self.adapter.process.get_value("27f1196853afd41fd7a20c0b38f739b5", ())

    def stop_sounds(self):
        self.adapter.process.request("7e79c2ebbcbbfc1d1cc2661ccdc1a993", ())

    def play_melody_until_done(self, file_name):
        self.adapter.process.request("beac26c872bb855eb07aafaddd37a496", ( file_name))

    def play_melody(self, file_name):
        self.adapter.process.request("67327e689d2fb0644300a14f991f2676", ( file_name))

    def play_tone(self, frequency, time_s = None):
        self.adapter.process.request("7e0558574c28779fcd007636cecc0be4", ( frequency, time_s ))

    def play_note(self, note, beat = None):
        self.adapter.process.request("bd47d1106fd9fc62d1afb7380da748dd", ( note, beat ))

    def rest(self, beat):
        self.adapter.process.request("3d418b161ccb6a5858678f3ed7b2b4d2", ( beat))



class pin0_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def read_digital(self):
        return self.adapter.process.get_value("03500ba4f639e7e827034a45296159ba", ())

    def write_digital(self, value):
        self.adapter.process.request("7569b5cc303a9bbaba0e6a06757c676d", ( value))

    def servo_write(self, value):
        self.adapter.process.request("6b2038d5adb67ea72adbde3986c0d47a", ( value))

    def read_analog(self):
        return self.adapter.process.get_value("94baad9388b68b81d89ad54a23ad02b8", ())

    def write_analog(self, value):
        self.adapter.process.request("a7b4e6938b470b0d1a5510bc311e8297", ( value))

    def is_touched(self):
        return self.adapter.process.get_value("a8d5d32f31b9cf001df6721550cae625", ())

    def set_touchpad_threshold(self, value):
        self.adapter.process.request("3df31b68fe679f4188b7fda7ab3e7551", ( value))

    def set_touchpad_sensitivity(self, level):
        self.adapter.process.request("f97f5fcd43569c8e6abef498dfa19c75", ( level))

    def get_touchpad_value(self):
        return self.adapter.process.get_value("58f743e79801661c6e2f99d23ad6bd1b", ())

    def set_pwm_frequency(self, frequency):
        self.adapter.process.request("ba0d00eb3065dfb9df6b9f5ba717f159", ( frequency))

    def set_pwm_duty(self, duty):
        self.adapter.process.request("227e88bbd5d58053a20709348b15a0a1", ( duty))

    def play_note(self, note, beat = None):
        self.adapter.process.request("77fac382ffc895a98fb4533296f60a26", ( note, beat ))

    def play_tone(self, frequency, time_s = None):
        self.adapter.process.request("48f19540b30cd3fcad2bfe768b878f93", ( frequency, time_s ))



class pin1_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def read_digital(self):
        return self.adapter.process.get_value("dcbf6cdd1ba2f5c49ff329ddf3e4546e", ())

    def write_digital(self, value):
        self.adapter.process.request("090e3a30d60a4422743c8f30b48ea178", ( value))

    def servo_write(self, value):
        self.adapter.process.request("636704ef720c5296cc063803ab6c59e5", ( value))

    def read_analog(self):
        return self.adapter.process.get_value("faa404b1eca9c1975e2c21068dc42e39", ())

    def write_analog(self, value):
        self.adapter.process.request("f7218f6aeb76795d5e307b88a4b73af8", ( value))

    def is_touched(self):
        return self.adapter.process.get_value("57aaf0cad26a8af38f4c147737aa3911", ())

    def set_touchpad_threshold(self, value):
        self.adapter.process.request("1da6bf8d65ebcb7c5eee7df177e9e7f5", ( value))

    def set_touchpad_sensitivity(self, level):
        self.adapter.process.request("b8df55c84bb5fc9d034154f8c5f1e359", ( level))

    def get_touchpad_value(self):
        return self.adapter.process.get_value("1f4be97c6799440eb51fc32e29333100", ())

    def set_pwm_frequency(self, frequency):
        self.adapter.process.request("5be5480f846cc10365bcfbaa4e26cc27", ( frequency))

    def set_pwm_duty(self, duty):
        self.adapter.process.request("5a2b93139183e960c6a216ad90a2f7e5", ( duty))

    def play_note(self, note, beat = None):
        self.adapter.process.request("c0423c59b53106953c78241ff5665b82", ( note, beat ))

    def play_tone(self, frequency, time_s = None):
        self.adapter.process.request("06b1f7e83132023b11fcf08f915a33d6", ( frequency, time_s ))



class pin2_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def read_digital(self):
        return self.adapter.process.get_value("c1464cf2a5de65cd1a165f4ba9c68327", ())

    def write_digital(self, value):
        self.adapter.process.request("ae11ac44924739f0be73c03701f5613e", ( value))

    def servo_write(self, value):
        self.adapter.process.request("8c9bac5b255acde719f044f3b049c66c", ( value))

    def read_analog(self):
        return self.adapter.process.get_value("ce2f3b5269773c1a29919309ddb5e624", ())

    def write_analog(self, value):
        self.adapter.process.request("6c6e772d5344fd86ee0d2b16f357e7ba", ( value))

    def is_touched(self):
        return self.adapter.process.get_value("b5fdc846aa59ac94217c9cd04e083eaa", ())

    def set_touchpad_threshold(self, value):
        self.adapter.process.request("387e44f9819ecde6b4c8e5135fe289ca", ( value))

    def set_touchpad_sensitivity(self, level):
        self.adapter.process.request("574ec4561c26abd2e10ca027ceb12bd8", ( level))

    def get_touchpad_value(self):
        return self.adapter.process.get_value("a611346b22ea41fe2f4e72b640c643b0", ())

    def set_pwm_frequency(self, frequency):
        self.adapter.process.request("3bbc08f28f720c45e70df1b7eb1f9072", ( frequency))

    def set_pwm_duty(self, duty):
        self.adapter.process.request("5468285aba2c2e320b4e1f75ae79a197", ( duty))

    def play_note(self, note, beat = None):
        self.adapter.process.request("1b71725b5b69c00df54baa732ebfaef0", ( note, beat ))

    def play_tone(self, frequency, time_s = None):
        self.adapter.process.request("295a25f7e28d3777dcaf903c6bf5ee94", ( frequency, time_s ))



class pin3_c(object):

    def __init__(self, adapter):

        self.adapter = adapter

    def read_digital(self):
        return self.adapter.process.get_value("4a3dc4bd34df3e469d824d21255dff53", ())

    def write_digital(self, value):
        self.adapter.process.request("9e890a0534779b27a1ab116d25a1b5e2", ( value))

    def servo_write(self, value):
        self.adapter.process.request("6ea9256f1a41a40b394159430052b002", ( value))

    def read_analog(self):
        return self.adapter.process.get_value("ab4b8062acc72052b643bff57a444a40", ())

    def write_analog(self, value):
        self.adapter.process.request("dfc6dd68e621711252c1ddd2495f5bc2", ( value))

    def is_touched(self):
        return self.adapter.process.get_value("81ac296525012099cd7fee4c0c9d276f", ())

    def set_touchpad_threshold(self, value):
        self.adapter.process.request("5fabcefec096ec0cb634bad577e304e6", ( value))

    def set_touchpad_sensitivity(self, level):
        self.adapter.process.request("8184d8638efa1165d5a39d18dde9c807", ( level))

    def get_touchpad_value(self):
        return self.adapter.process.get_value("728a162e4dc07ddf0747eb845f3593a6", ())

    def set_pwm_frequency(self, frequency):
        self.adapter.process.request("16b777d37bdc6efcd5280123eb1155b7", ( frequency))

    def set_pwm_duty(self, duty):
        self.adapter.process.request("45b412013eb8f244dfc2d54840e30c12", ( duty))

    def play_note(self, note, beat = None):
        self.adapter.process.request("b519527590454ff2e38c1311485cf448", ( note, beat ))

    def play_tone(self, frequency, time_s = None):
        self.adapter.process.request("136a9b8d758a0db2fe92ff6230678c3e", ( frequency, time_s ))



class mesh_c():

    def __init__(self, adapter):

        self.adapter = adapter

    def start_group(self, group_name):
        self.adapter.process.request("497314bd4c2c7f492e472e4bd5902049", ( group_name))

    def join_group(self, group_name):
        self.adapter.process.request("f7e2fed3e20a0294ada53d82df0a7f20", ( group_name))

    def get_info(self, message):
        return self.adapter.process.get_value("bbaae12da4085e0c1a466ab11d1f7d58", ( message))

    def broadcast(self, message, value = ""):
        self.adapter.process.request("3d4df0d2cbc0f71a40c2f4322c659ac7", ( message, value ))



class wifi_c():

    def __init__(self, adapter):

        self.adapter = adapter

    def is_connected(self):
        return self.adapter.process.get_value("7233c2b0368d9b25d7e7ffcb004737bb", ())

    def connect(self):
        self.adapter.process.request("bd1de88cc76a8dbff3a0adea09a34234", ())

    def disconnect(self):
        self.adapter.process.request("0f1a0e5f2a038f04e246171639dccaef", ())

    def get_mac(self):
        return self.adapter.process.get_value("4610be2ca54f1f013a62c0cc7757ca50", ())

    def start(self, ssid, password):
        self.adapter.process.request("2f132726f0ff47efd96a4a024af361aa", ( ssid, password))

