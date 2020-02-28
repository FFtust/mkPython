import time

class angle_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_angle(self, index = 1):
        return self.adapter.process.get_value("fa6115a5dde862e9622395cd289658b5", ( index ))
    def get_angle_speed(self, index = 1):
        return self.adapter.process.get_value("22c0f0812ff1a06572cc6124e126c57b", ( index ))
    def is_rotating_clockwise(self, index = 1):
        return self.adapter.process.get_value("bfb45510e0379b21eb0e354534984762", ( index ))
    def is_rotating_anticlockwise(self, index = 1):
        return self.adapter.process.get_value("0ecdb626db6f484680dfea29b3805d4c", ( index ))
    def reset_angle(self, index = 1):
        self.adapter.process.request("4b0dcf2bc13b4ff8af8a6d1ca4b0286c", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("cc16340ef1df6568622defad08faa434", ( mode,timestamp,index ))

class button_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def is_pressed(self, index = 1):
        return self.adapter.process.get_value("2fd17cf957a44197afccf71917fa5c7c", ( index ))
    def get_count(self, index = 1):
        return self.adapter.process.get_value("f139809beba109011b5fca14be947968", ( index ))
    def reset_count(self, index = 1):
        self.adapter.process.request("633df041e2e92f92c8226904d5cec429", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("a8baad0c0156c7a7f7bbcedf7c1c0916", ( mode,timestamp,index ))

class dc_motor_driver_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def set_power(self, power, index = 1):
        self.adapter.process.request("c6bd1dc08af87463370053b32fc28c71", ( power, index ))
    def set_power_with_time(self, power, t = 0, index = 1):
        self.adapter.process.request("5c07047ed13e66ea98aa5599e8ad1c80", ( power, t , index ))
    def change_power(self, power, index = 1):
        self.adapter.process.request("0ae77fc8c127a80eb669e35d763d7ac6", ( power, index ))
    def get_power(self, index = 1):
        return self.adapter.process.get_value("e134a86edfb48967cfce795669e2342c", ( index ))
    def get_load(self, index = 1):
        return self.adapter.process.get_value("fbf47367af62e84906a263c6e58e889b", ( index ))
    def stop_all(self, ):
        self.adapter.process.request("a40af40c915ee1c14abd858f95adddc9", ( ))
    def stop(self, index = 1):
        self.adapter.process.request("7995cdf7be28641545ac65d94dd897ef", ( index ))

class dual_rgb_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def set_report_mode(self, mode, timestamp, index = 1):
        self.adapter.process.request("a09070f318f73646f61b6413ad790b92", ( mode, timestamp, index ))
    def study(self, index = 1):
        self.adapter.process.request("32685a8da7b47a37c315edebcfd6eb4b", ( index ))
    def get_all_data(self, index = 1):
        return self.adapter.process.get_value("f48c9cc3bf6dddf4225db6e63a541b41", ( index ))
    def get_intensity(self, ch, index = 1):
        return self.adapter.process.get_value("d267823b39c30d057373fc12ca9009a7", ( ch, index ))
    def is_state(self, state, index = 1):
        return self.adapter.process.get_value("766acdca01afb1a1acf49894402401f2", ( state, index ))
    def get_offset_track_value(self, index = 1):
        return self.adapter.process.get_value("d1574581cce963e8ccd6a495d4f3d19b", ( index ))
    def is_color(self, ch, color, index = 1):
        return self.adapter.process.get_value("5aeccc87bcbfd6b5d23e7b11d97e8fae", ( ch, color, index ))
    def get_color(self, ch, index = 1):
        return self.adapter.process.get_value("a657494ae560ceaae55777aee54b7b59", ( ch, index ))
    def set_led_color(self, color, index = 1):
        self.adapter.process.request("09156092eb270cc9aff4527034e7d2e2", ( color, index ))
    def is_on_track(self, ch, index = 1):
        return self.adapter.process.get_value("41f12d5befaeef1c7bc29cdb9bfeb79e", ( ch, index ))
    def is_on_background(self, ch, index = 1):
        return self.adapter.process.get_value("27c0687eb6e6591b1254fed4b7051bf4", ( ch, index ))
    def set_motor_diff_speed_kp(self, value):
        self.adapter.process.request("6e7b577a26abb26e4b9ef10b0b37e216", ( value))
    def get_motor_diff_speed(self, index = 1):
        return self.adapter.process.get_value("6257d2242aaa58fba1d5b8c243d95333", ( index ))
    def get_red(self, ch, index = 1):
        return self.adapter.process.get_value("8c3813d327072b730c3cf311b67bf4b2", ( ch, index ))
    def get_green(self, ch, index = 1):
        return self.adapter.process.get_value("8ca398ed06ea75a57d02bd5b4fea4aa8", ( ch, index ))
    def get_blue(self, ch, index = 1):
        return self.adapter.process.get_value("39c9e7bee280ed50c88d74f9d3eaf563", ( ch, index ))
    def get_reflected_light(self, ch, index = 1):
        return self.adapter.process.get_value("75de78d8cd0892bedf0e183e6e32c716", ( ch, index ))
    def set_light_color(self, color, index = 1):
        self.adapter.process.request("46947b28e626ed4ad32aff06acea3ef7", ( color, index ))

class flame_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def is_active(self, index = 1):
        return self.adapter.process.get_value("43f0d77491c8419473a17732f57b8d71", ( index ))
    def get_value(self, index = 1):
        return self.adapter.process.get_value("0eb7bee77af43f4ed73e5dbea28767ab", ( index ))
    def set_report_mode(self, mode, timestamp, index = 1):
        self.adapter.process.request("6ecfce4520bc7a8c6f6f433a5d0cf427", ( mode, timestamp, index ))

class gas_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def is_active(self, level = "middle", index = 1):
        return self.adapter.process.get_value("ad72d23e5be460e6b40afb877b23125b", ( level , index ))
    def get_value(self, index = 1):
        return self.adapter.process.get_value("3677f5f5d7053d60cedd2d18eeba27d1", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("a3a5038fe5b0e6c234d586fc5675d77c", ( mode,timestamp,index ))

class humiture_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_relative_humidity(self, index = 1):
        self.adapter.process.request("388a03ffa4616b7194a7598babcb0772", ( index ))
    def get_temperature(self, opt = "celsius", index = 1):
        return self.adapter.process.get_value("4ba5c22dae40abef34c3f11ac10ec1be", ( opt , index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("9c667a7764c6a902796c2240a5d6a93b", ( mode,timestamp,index ))

class ir_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def receive(self, index = 1):
        return self.adapter.process.get_value("2d2f607927e4941d2089bfb1f0a64878", ( index ))
    def send(self, message, index = 1):
        self.adapter.process.request("56bfe0634270178fa572e73cba9cb7d9", ( message, index ))
    def send_learned_result(self, record_id = 1, index = 1):
        self.adapter.process.request("f83ef2b1a184445431a49dc13a7635fe", ( record_id , index ))
    def learn(self, record_id = 1, index = 1):
        self.adapter.process.request("386674bf9936c10f02224dd690431a8f", ( record_id , index ))
    def receive_remote_code(self, index = 1):
        return self.adapter.process.get_value("98ec9618de3d0429a597ec07bc4a0ca2", ( index ))
    def is_receive(self, cmd, index = 1):
        return self.adapter.process.get_value("a4c72727d4a331af373beccc20dc0934", ( cmd, index ))
    def __learn_online(self, record_id = 1, index = 1):
        return self.adapter.process.get_value("3a9892016387dc508e5a654df03f5540", ( record_id , index ))

class joystick_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_value(self, opt, index = 1):
        return self.adapter.process.get_value("f880519c62df3d3fa279c0f24b45d368", ( opt, index ))
    def is_active(self, opt, index = 1):
        return self.adapter.process.get_value("8a71d2ae6a8883fe0a0a2bbb54c71512", ( opt, index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("79b76b2928292a34b71cde8b8a51c46d", ( mode,timestamp,index ))
    def is_up(self, index = 1):
        return self.adapter.process.get_value("7aa92b5b40be18c1ad955c5f688ac052", ( index ))
    def is_down(self, index = 1):
        return self.adapter.process.get_value("6687c433de820a307fbdcc2169219d37", ( index ))
    def is_left(self, index = 1):
        return self.adapter.process.get_value("27101e22d845672b35d0c4974f119d3d", ( index ))
    def is_right(self, index = 1):
        return self.adapter.process.get_value("dea51efcfbcb1a3a06077926283174ca", ( index ))

class led_panel_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def _sting_to_bytes(self, string):
        self.adapter.process.request("274f777377ded92f31ab925ac2cd41a5", ( string))
    def _get_image(self, image_string):
        self.adapter.process.request("bef818ca85ee84cc8ddf023de14cfbf8", ( image_string))
    def show_image(self, image, pos_x = 0, pos_y = 0, time_s = None, index = 1):
        self.adapter.process.request("dd51cd4610ad1e02ce80ca45f9278538", ( image, pos_x , pos_y , time_s , index ))
    def show(self, message, pos_x = None, pos_y = None, wait = True, index = 1):
        self.adapter.process.request("2ccded1579dfa0cb23cacd27d6f3779c", ( message, pos_x , pos_y , wait , index ))
    def set_pixel(self, pos_x, pos_y, status, index = 1):
        self.adapter.process.request("582cab714b74d2cf657212fd450833a2", ( pos_x, pos_y, status, index ))
    def get_pixel(self, pos_x, pos_y, index = 1):
        return self.adapter.process.get_value("506acf1090be70c364693f64ea9ff719", ( pos_x, pos_y, index ))
    def toggle_pixel(self, pos_x, pos_y, index = 1):
        self.adapter.process.request("4acc66c1392d865190bf2b2fcc4ce938", ( pos_x, pos_y, index ))
    def clear(self, index = 1):
        self.adapter.process.request("e696af328fe516ae8563de118b93f89c", ( index ))

class led_strip_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def set_single(self, led_index, red_value, green_value, blue_value, index = 1):
        self.adapter.process.request("7ef1cd1c1d239d696afe9ddc99d9130c", ( led_index, red_value, green_value, blue_value, index ))
    def set_all(self, red_value, green_value, blue_value, index = 1):
        self.adapter.process.request("fb38b4bf53a78ce451a0e0a8d2bf3d2f", ( red_value, green_value, blue_value, index ))
    def off_all(self, index = 1):
        self.adapter.process.request("44b862d1275191d659cab0c7e413e4ff", ( index ))
    def set_red(self, led_index, value, index = 1):
        self.adapter.process.request("446da0a63c6db4bac09730bdf828ec80", ( led_index, value, index ))
    def set_green(self, led_index, value, index = 1):
        self.adapter.process.request("446d485046a4ed7be1126be819d25c3b", ( led_index, value, index ))
    def set_blue(self, led_index, value, index = 1):
        self.adapter.process.request("12fdc2987f2a16f2f40fdc774949f428", ( led_index, value, index ))
    def change_red(self, led_index, value, index = 1):
        self.adapter.process.request("552270856806abec0fc0f289cd28f557", ( led_index, value, index ))
    def change_green(self, led_index, value, index = 1):
        self.adapter.process.request("58c20935dc21e3f677141b6011d6c1e3", ( led_index, value, index ))
    def change_blue(self, led_index, value, index = 1):
        self.adapter.process.request("eff33a5fdfad4efaf05b9ca279945109", ( led_index, value, index ))
    def set_mode(self, mode, index =1):
        self.adapter.process.request("0999ee70bd6a0f8695065b6aead26e7c", ( mode, index ))
    def set_block(self, led_num, data, index = 1):
        self.adapter.process.request("5958086d43a0ade67642b439e5b330f6", ( led_num, data, index ))
    def set_effect(self, mode, speed, data, index = 1):
        self.adapter.process.request("12b443385cc7ca0b66afbb2d02799ff8", ( mode, speed, data, index ))
    def show(self, color, index = 1):
        self.adapter.process.request("4fe98bd611dcb535983383d1139837f6", ( color, index ))

class light_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_value(self, index = 1):
        return self.adapter.process.get_value("e840dce5f0220bdeffc25eb5106fe425", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("11850e8b701dbe619c31c25774e753d8", ( mode,timestamp,index ))

class magnetic_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def is_active(self, index = 1):
        return self.adapter.process.get_value("20cdf2ad1a2782fd2ff81e07d07cf2b8", ( index ))
    def get_count(self, index = 1):
        return self.adapter.process.get_value("f8b1b702ede21ddd6bcb06f5d53bc5d8", ( index ))
    def reset_count(self, index = 1):
        self.adapter.process.request("1afc7dde8d8a34068afd127e1c174417", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("1125b5d2aeaef660970fac528d70154b", ( mode,timestamp,index ))

class motion_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_acceleration(self, axis, index = 1):
        return self.adapter.process.get_value("1e9f13eda65bf6cfd972a4fc8ee6902c", ( axis, index ))
    def get_gyroscope(self, axis, index = 1):
        return self.adapter.process.get_value("0e0393173f05c5990e87735726e07093", ( axis, index ))
    def get_rotation(self, axis, index = 1):
        return self.adapter.process.get_value("a1371021085447e9ac68719c7e1d0368", ( axis, index ))
    def reset_rotation(self, axis = "all", index = 1):
        self.adapter.process.request("3b4e15e88d4eb6496c4ebecd18ac1df1", ( axis , index ))
    def is_shaken(self, level = "usual", index = 1):
        return self.adapter.process.get_value("5ca2f500862fe3de4c7d5ec58b440074", ( level , index ))
    def get_shake_strength(self, index = 1):
        return self.adapter.process.get_value("686a71845426f75175dcb1b42ef8bbc5", ( index ))
    def get_pitch(self, index = 1):
        return self.adapter.process.get_value("78522603788d0a501bad3cbe5bbc6c5b", ( index ))
    def get_roll(self, index = 1):
        return self.adapter.process.get_value("80203be974492342417b1d5b6976a926", ( index ))
    def is_tilted_left(self, index = 1):
        return self.adapter.process.get_value("0e3b7cfa9b02be77f74efc2667c60a69", ( index ))
    def is_tilted_right(self, index = 1):
        return self.adapter.process.get_value("4e5365e9d09c9c0ee88138f6234b531c", ( index ))
    def is_tilted_forward(self, index = 1):
        return self.adapter.process.get_value("e5fe54100833d011a1b93145580680a3", ( index ))
    def is_tilted_backward(self, index = 1):
        return self.adapter.process.get_value("91386c506fd6f58de8fdf9eaa8435d5b", ( index ))
    def is_face_up(self, index = 1):
        return self.adapter.process.get_value("db952cb3c6f1112559eb77ff50a2adff", ( index ))
    def is_face_down(self, index = 1):
        return self.adapter.process.get_value("a34fd5b1fcb988f70895da89a1590ec8", ( index ))
    def is_upright(self, index = 1):
        return self.adapter.process.get_value("a14c9243b305878ca573a3c94e3ff05d", ( index ))

class mult_touch_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def is_active(self, ch, index = 1):
        return self.adapter.process.get_value("97c6f4d9159ec6a41e12ce7f593d0251", ( ch, index ))
    def get_value(self, position, index = 1):
        return self.adapter.process.get_value("f516e9d8d4f64e0348f457b72c695986", ( position, index ))
    def reset_threshold(self, index = 1):
        self.adapter.process.request("feda9c35333d7ea601ec464207d0dacb", ( index ))
    def set_sensitivity(self, sen, index = 1):
        self.adapter.process.request("cea3a59e1ffb884b474287fe93430715", ( sen, index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("6de763e1347e2948000f62f557ef5048", ( mode,timestamp,index ))
    def get_all_status(self, index = 1):
        return self.adapter.process.get_value("a5c3b2fe8451bfe92aecb5aefbfbdd71", ( index ))

class pir_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def is_activated(self, index = 1):
        return self.adapter.process.get_value("2d125393232dc55083173f212387b9b2", ( index ))
    def get_count(self, index = 1):
        return self.adapter.process.get_value("9260e8864d8ee432f87eb7be609882fc", ( index ))
    def reset_count(self, index = 1):
        self.adapter.process.request("a91cd0985827caf7c34eeb3429653ce2", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("9a6f38ccbbb6cfa8b9a484c54693424f", ( mode,timestamp,index ))

class ranging_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_distance(self, index = 1):
        return self.adapter.process.get_value("e36ab4d0ec3adda7e8a81106872d661d", ( index ))
    def set_report_mode(self, mode, timestamp, index = 1):
        self.adapter.process.request("e6a10caffa1777f94ceb5e2fb8f8fd3f", ( mode, timestamp, index ))

class rgb_led_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def show(self, r, g, b, index = 1):
        self.adapter.process.request("eaf9626f958b2c31c7dbdb3a77b1ad95", ( r, g, b, index ))
    def set_red(self, val, index = 1):
        self.adapter.process.request("f8e1002a810a3c6e472d015f89419486", ( val, index ))
    def set_green(self, val, index = 1):
        self.adapter.process.request("0e7e5702abaee62b86f4966f18c1c6b3", ( val, index ))
    def set_blue(self, val, index = 1):
        self.adapter.process.request("bbd4215c9c4cc3095579e5a1989d4e88", ( val, index ))
    def change_red(self, val, index = 1):
        self.adapter.process.request("6fe46d9917b881c786d3f17455d45118", ( val, index ))
    def change_green(self, val, index = 1):
        self.adapter.process.request("828b68f260f2641b96708b59efc5cdfd", ( val, index ))
    def change_blue(self, val, index = 1):
        self.adapter.process.request("8ebe1fd251da8c5f0be32e97193d34f6", ( val, index ))
    def __get_info(self, index = 1):
        self.adapter.process.request("02a060e27a43e9e08039af2fee095c51", ( index ))
    def get_red(self, index = 1):
        return self.adapter.process.get_value("94254ff881cfc7a62b918cafd4e47bab", ( index ))
    def get_green(self, index = 1):
        return self.adapter.process.get_value("02e3043f87f962e20be924d497a4860e", ( index ))
    def get_blue(self, index = 1):
        return self.adapter.process.get_value("7b3c35dfb5f63f50ae0d914143531d51", ( index ))
    def off(self, index = 1):
        self.adapter.process.request("aee14b5378e0876995b539b868aa6062", ( index ))
    def __set_r_g_b(self, col_id, value, index):
        self.adapter.process.request("026e6064b248dce505a6b592e21143ea", ( col_id, value, index))
    def __change_r_g_b(self, col_id, value, index):
        self.adapter.process.request("cd6a1127e3a0e3cca092efc30a563583", ( col_id, value, index))
    def __get_r_g_b(self, index):
        self.adapter.process.request("97a313759b80aacf2d0fb9a2f0cdbb74", ( index))

class servo_driver_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def set_angle(self, angle, index = 1):
        self.adapter.process.request("f73f808de12909c4e7597652fa26ac11", ( angle, index ))
    def change_angle(self, angle, index = 1):
        self.adapter.process.request("ee648656652589a39e5d806968082801", ( angle, index ))
    def get_angle(self, index = 1):
        return self.adapter.process.get_value("0b1f53b2c60dec1ac594fcde1e74dc12", ( index ))
    def get_load(self, index = 1):
        return self.adapter.process.get_value("2f9b91b06a77fe2210d70fd9498fb092", ( index ))
    def reset(self, index = 1):
        self.adapter.process.request("17ec837118b7d6b1ee6196b90a7b2d13", ( index ))
    def release(self, index = 1):
        self.adapter.process.request("5567bf1cca84e20eab3050d8b6b54a62", ( index ))
    def set_report_mode(self, mode, timestamp, index = 1):
        self.adapter.process.request("2821b1c032e90a13866e1bfee7aebd3d", ( mode, timestamp, index ))

class slider_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_value(self, index = 1):
        return self.adapter.process.get_value("84100c049a10433e4097dafcd5ac8067", ( index ))
    def set_report_mode(self, mode, timestamp, index = 1):
        self.adapter.process.request("17b630306a6871f2190947b970b4d3d8", ( mode, timestamp, index ))

class smartservo_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def set_zero(self, index = 1):
        self.adapter.process.request("0e6556840e7b55be4db496a4ca60e1b2", ( index ))
    def move_to(self, position, speed, index = 1):
        self.adapter.process.request("1c43097a399b67aaac256d26b245967e", ( position, speed, index ))
    def move(self, position, speed, index = 1):
        self.adapter.process.request("715895b2bb1baf5e1ed924f510ac2bd4", ( position, speed, index ))
    def set_power(self, pwm, index = 1):
        self.adapter.process.request("190518d0bcef90ce68ad18d4e3156874", ( pwm, index ))
    def set_speed_upload_mode(self, mode, index = 1):
        self.adapter.process.request("81be450e539823dbb0263183879f3072", ( mode, index ))
    def set_position_upload_mode(self, mode, index = 1):
        self.adapter.process.request("ea6f20276f8e42223c6603bbffc496b9", ( mode, index ))
    def back_to_zero(self, speed, index = 1):
        self.adapter.process.request("d68008d1da04b9ddca5f2892d5d0285d", ( speed, index ))
    def move_to_in_time(self, position, time, index = 1):
        self.adapter.process.request("53aa45b307418e4741eaccc6fc605388", ( position, time, index ))
    def move_to_with_torque(self, position, speed, strength, index = 1):
        self.adapter.process.request("c9e6a5abbd0295d37628aea19d2f3436", ( position, speed, strength, index ))
    def move_with_torque(self, position, speed, strength, index = 1):
        self.adapter.process.request("689f106dd5e80951bca27658b5a1e0c2", ( position, speed, strength, index ))
    def lock(self, index = 1):
        self.adapter.process.request("cda57c21d5973bb5562cd5945514e55e", ( index ))
    def unlock(self, index = 1):
        self.adapter.process.request("b23a2291e2df8c36961384c3d3f0b79a", ( index ))
    def turn(self, angle, speed, index = 1):  # angle: drgree   speed:unit :degree per second
        self.adapter.process.request("ce541cabd222e6b2a44b3a1c3808544e", ( angle, speed, index ))
    def turn_to(self, angle, speed, index = 1 ): # angle: drgree   speed:unit :degree per second
        self.adapter.process.request("4efa168fa66642101b110c6ab3d8273d", ( angle, speed, index ))
    def stop(self, index = "all"):
        self.adapter.process.request("0421cd13c84277eeadb8a00fa7a9e78f", ( index ))
    def run(self, power, index = 1):
        self.adapter.process.request("e3eefe3e129e8d6aa29e27f64168108a", ( power, index ))
    def get_angle(self, index = 1):
        return self.adapter.process.get_value("3d7b98d077b754a26a218e910ee577ad", ( index ))
    def get_speed(self, index = 1):
        return self.adapter.process.get_value("8166e5b634834ef58efebba827998993", ( index ))
    # def get_cycles(self, index = 1):
        self.adapter.process.request("f370895323272439968cd887315a0276", ( index ))
    def lock_angle(self, index = "all"):
        self.adapter.process.request("ccce453c5b5a79fa0343f94ef6a2c9f3", ( index ))
    def release_angle(self, index = "all"):
        self.adapter.process.request("fd7ba507281632ddd3eba296d9757250", ( index ))
    def reset(self, index = "all"):
        self.adapter.process.request("2269d3aafaf23e3fbcdd30e342581bac", ( index ))

class smart_camera_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_fills_all_data(self, fills_id, index = 1):# 获取某个色块所有信息
        self.adapter.process.request("3367109ab7b0f15ffd9dfb1c729854f5", ( fills_id, index ))
    def set_fills_report_mode(self, mode, timestamp, index = 1):# 设置某个色块所有信息的上报模式
        self.adapter.process.request("8732e086fbf252891bba409597b33d90", ( mode, timestamp, index ))
    def get_fills_sigle_data(self, fills_id, type_id, index = 1):# 获取某个色块的单独的信息
        self.adapter.process.request("8f983d865affd83260a743dea35c7c1c", ( fills_id, type_id, index ))
    def get_line_all_data(self, index = 1):#获取线的所有信息
        self.adapter.process.request("935e8ca4d9fdcf69220b2816c8cff444", ( index ))
    def set_line_report_mode(self, mode, timestamp, index = 1):#设置线所有信息的上报模式
        self.adapter.process.request("3315a5f0d6f8a3a258dc0befcdbd3bad", ( mode, timestamp, index ))
    def get_line_sigle_data(self, type_id, index = 1):#获取线的单独的信息
        self.adapter.process.request("0c58adf85fddbd092026469d4f44e4ac", ( type_id, index ))
    def get_crossings_all_data(self, index = 1):#获交叉口的所有信息
        self.adapter.process.request("52a4c7e67e9698081d306fdb3a0610d2", ( index ))
    def set_crossings_report_mode(self, mode, timestamp, index = 1):#设置交叉口的所有信息的上报模式
        self.adapter.process.request("78a38a54e4bd11c3ae6e42cbe4acac1a", ( mode, timestamp, index ))
    def get_crossings_sigle_data(self, type_id, index = 1):#获取交叉口的单独的信息
        self.adapter.process.request("55873706abdd957443ffe192e8b5b490", ( type_id, index ))
    def get_crossings_line_angle_sigle_data(self, index = 1):#获取交叉口线角度的单独的信息
        self.adapter.process.request("1eeee001c453885101dbbd3965fb11ad", ( index ))
    def get_barcode_all_data(self, barcode_id, index = 1):#获取某个条形码的所有信息
        self.adapter.process.request("caf9968d713be22e14bad3cfcb5832db", ( barcode_id, index ))
    def set_barcode_report_mode(self, mode, timestamp, index = 1):#设置某个条形码的所有信息的上报模式
        self.adapter.process.request("50dada444c9d1ed786dd543a31e358cb", ( mode, timestamp, index ))
    def get_barcode_sigle_data(self, barcode_id, type_id, index = 1):#获取条形码X的单独的信息
        self.adapter.process.request("723344895a3d3a3f65b4aea9e82fc08d", ( barcode_id, type_id, index ))
    def get_button_data(self, index = 1):#获取按键的信息
        self.adapter.process.request("3978028caa718b93cd487883891af73b", ( index ))
    def set_button_report_mode(self, mode, timestamp, index = 1):#设置按键信息的上报模式
        self.adapter.process.request("2b3478f99d18a2811da847151bba0790", ( mode, timestamp, index ))
    def get_learn_data(self, index = 1):#获取学习的信息
        self.adapter.process.request("a9a171fb906ee12e46bc1eb7841aad82", ( index ))
    def set_camera_sensitometry(self, level, index = 1):#设置摄像头曝光度
        self.adapter.process.request("e3635c5e04ebf67501bd3f793a3e18a6", ( level, index ))
    def set_led_rgb(self, r, g, b, index = 1):#设置RGB灯
        self.adapter.process.request("8e899b753523e93325ba2d707bf370e2", ( r, g, b, index ))
    def set_fill_light_status(self, sta, index = 1):#设置补光灯状态
        self.adapter.process.request("0217c6a98f176383df28315260008c9c", ( sta, index ))
    def set_line_follow_vector_mode(self, mode, index = 1):#设置巡线vector模式（不开放）
        self.adapter.process.request("9b662cd71e72a67f132667d099f796c8", ( mode, index ))
    def set_line_follow_mode(self, mode, index = 1):#设置巡线模式
        self.adapter.process.request("39a85d6d3343421289f89a9ced4276e9", ( mode, index ))
    def get_turning_angle(self, index = 1):#获取按键的信息
        self.adapter.process.request("3bbb3ee672b18aacf95cae855e7f8887", ( index ))
    def get_fills_count(self, index = 1):#获取按键的信息
        self.adapter.process.request("f80158511e28b5270b17977f4ba8ee48", ( index ))
    def get_barcode_count(self, index = 1):#获取按键的信息
        self.adapter.process.request("4e49667052dc6a161cbbda638012ccd5", ( index ))
    def set_next_turning_angle(self, angle, index = 1):#设置下一次转向角度
        self.adapter.process.request("6b8a95d458f3cfa7f13261088848d9e5", ( angle, index ))
    def set_default_turning_angle(self, angle, index = 1):#设置默认的转向角度（不开放）
        self.adapter.process.request("3559380b8a54bd819723b9821cc6aa8e", ( angle, index ))
    def set_fills_learn_mode(self, fills_id, t, index = 1):#设置学习色块模式
        self.adapter.process.request("e5903f256f7a392027df1f6ca936ed0e", ( fills_id, t, index ))
    def stop_learn(self, index = 1):#设置结束学习（不开放）
        self.adapter.process.request("f7a5c592880a3c55cf296e380c9aeaf2", ( index ))
    def abandon_learn(self, index = 1):#设置放弃学习（不开放）
        self.adapter.process.request("90277f2ff68dae0df70613ce8dcd5a04", ( index ))
    def set_pixy_mode(self, mode, index = 1):#设置pixy模块模式
        self.adapter.process.request("8d8bde8f99790de5eba8d1d6ccd6e78c", ( mode, index ))
    def set_mode(self, mode = "color", index = 1):
        self.adapter.process.request("5bc5474366273eeaaf80a5c6ace24fd4", ( mode , index ))
    def learn(self, sign = 1, t = "until_button", index = 1):
        self.adapter.process.request("1ba1fda2974c203185a2c3d52e53c622", ( sign , t , index ))
    def detect_sign(self, sign, index = 1):
        self.adapter.process.request("180087564da61b8dbbe55ff3d2be89a0", ( sign, index ))
    def get_sign_x(self, sign, index = 1):
        self.adapter.process.request("8451b11dfa8cec4975c3812eee65a138", ( sign, index ))
    def get_sign_y(self, sign, index = 1):
        self.adapter.process.request("fd99ad95779c6986819511e2e01fa4e0", ( sign, index ))
    def get_sign_wide(self, sign, index = 1):
        self.adapter.process.request("62da024ba4f4c8c5f7d8f3e844c8ce96", ( sign, index ))
    def get_sign_hight(self, sign, index = 1):
        self.adapter.process.request("84af528ce88492c37d2a7f75db227d16", ( sign, index ))
    def detect_sign_location(self, sign, location, index = 1):
        self.adapter.process.request("1b16b346782f254847197c1f5226a1fb", ( sign, location, index ))
    def get_sign_location(self, sign, index = 1):
        self.adapter.process.request("66dc7ac17c7da2d58f6a196a6d334cfd", ( sign, index ))
    def __caculate_sign_location(self, x, y):
        self.adapter.process.request("2601437f4a239e6347553b080c071d8a", ( x, y))
    def open_light(self, index = 1):
        self.adapter.process.request("e7f1b75c5e5616949d2ff18bd5f257f3", ( index ))
    def close_light(self, index = 1):
        self.adapter.process.request("eac6389f9bf3d950e570185bc7d110a7", ( index ))
    def reset(self, index = 1):
        self.adapter.process.request("f9f0051e34932d84c76d8fc9621b8fc2", ( index ))
    def detect_label(self, label, index = 1):
        self.adapter.process.request("9914cb8ba8633ea463279fb7dab10e2a", ( label, index ))
    def get_label_x(self, sign, index = 1):
        self.adapter.process.request("afa982ab5989a64bc7732f29d8243ec8", ( sign, index ))
    def get_label_y(self, sign, index = 1):
        self.adapter.process.request("eea85d086952cf16200d4f0538e8f97e", ( sign, index ))
    def get_vector_end_x(self, index = 1):#line -> vector
        self.adapter.process.request("e5a09b2aedd8487b746a1fe5a48642b2", ( index ))
    def get_vector_end_y(self, index = 1):
        self.adapter.process.request("198e0dcb91e491f1b2b1de0b830db33d", ( index ))
    def get_vector_start_x(self, index = 1):
        self.adapter.process.request("61ade1867d3c6b9199ff2cb8e6facacb", ( index ))
    def get_vector_start_y(self, index = 1):
        self.adapter.process.request("2f8c50a520f98c46cc21abab3fceda2e", ( index ))
    def detect_cross(self, index = 1):
        self.adapter.process.request("aa1642b3221c3a22dc117780b97cf85c", ( index ))
    def get_cross_x(self, index = 1):
        self.adapter.process.request("94383e3805e399f011f22419efbb2051", ( index ))
    def get_cross_y(self, index = 1):
        self.adapter.process.request("fa34f4c53f895917521142dfc5323322", ( index ))
    def get_cross_road(self, index = 1):#获取交叉口数目？
        self.adapter.process.request("06dc505c6c7d695ea09e3834a8a7b517", ( index ))
    def get_cross_angle(self, sn = 1, index = 1):
        self.adapter.process.request("07a884b9288bee09bfc398e6732c86e1", ( sn , index ))
    def set_line(self, mode = "black", index = 1):
        self.adapter.process.request("92de4a6e8919fcc83530fa38b7735879", ( mode , index ))
    def set_vector_angle(self, angle, index = 1):
        self.adapter.process.request("55df5f962e3dc82b82e1839840494bcb", ( angle, index ))
    def get_vector_angle(self, index = 1):
        self.adapter.process.request("887439ff0dac3ceb63d2df96da055ff2", ( index ))
    def set_kp(self, kp, index = 1):
        self.adapter.process.request("fc6f8e7eddf0ffc3f2b029ca33ba971f", ( kp, index ))
    def get_fills_diff_speed(self, sign, tar_x, tar_y, index = 1):
        self.adapter.process.request("ded320335c6cfd5fa99b4e6e3c319eb8", ( sign, tar_x, tar_y, index ))
    def get_sign_diff_speed_x(self, sign, tar_x, index = 1):
        self.adapter.process.request("0479e803a3981fd07deb21eaefaaffed", ( sign, tar_x, index ))
    def get_sign_diff_speed_y(self, sign, tar_y, index = 1):
        self.adapter.process.request("fee60ef9e5a489c9536b491cd4a1a8bf", ( sign, tar_y, index ))
    def get_sign_diff_speed(self, sign, axis = "x", axis_val = 0, index = 1):
        self.adapter.process.request("d828e3545258f802bba5950bcfc01244", ( sign, axis , axis_val , index ))
    def get_barcode_diff_speed(self, label, tar_x, tar_y, index = 1):
        self.adapter.process.request("f8caeb8e18638542e74427d30b9bc505", ( label, tar_x, tar_y, index ))
    def get_label_diff_speed_x(self, label, tar_x, index = 1):
        self.adapter.process.request("e599affe7aed3b080bf6544fb348d0fe", ( label, tar_x, index ))
    def get_label_diff_speed_y(self, label, tar_y, index = 1):
        self.adapter.process.request("bf45d235d25e8efc07a228ec8fa57e2b", ( label, tar_y, index ))
    def get_label_diff_speed(self, label, axis = "x", axis_val = 0, index = 1):
        self.adapter.process.request("f45134d501430561da93642951a25d0c", ( label, axis , axis_val , index ))
    def get_follow_vector_diff_speed(self, index = 1):
        self.adapter.process.request("a7c43b2509c840bad68ce545d4f3bca6", ( index ))
    def is_lock_fills(self, sign, tar_x, tar_y, index = 1):
        self.adapter.process.request("a9d5599379fae0afde0b44b772202ce1", ( sign, tar_x, tar_y, index ))
    def is_lock_sign_x(self, sign, tar_x, index = 1):
        self.adapter.process.request("01dc574a5bc4361a21e7fd50fff9cdf1", ( sign, tar_x, index ))
    def is_lock_sign_y(self, sign, tar_y, index = 1):
        self.adapter.process.request("bfddae9be65c603ef4cd62ddf23ddb83", ( sign, tar_y, index ))
    def is_lock_sign(self, sign, axis = "x", axis_val = 0, index = 1):
        self.adapter.process.request("0bcd245c5da0a8f71d92afd113867669", ( sign, axis , axis_val , index ))
    def is_lock_barcode(self, label, tar_x, tar_y, index = 1):
        self.adapter.process.request("692e689d00aec7084214fe80a8cb51ca", ( label, tar_x, tar_y, index ))
    def is_lock_label_x(self, label, tar_x, index = 1):
        self.adapter.process.request("b0b2dd312ef8d233feee57937ebc2253", ( label, tar_x, index ))
    def is_lock_label_y(self, label, tar_y, index = 1):
        self.adapter.process.request("e4c9b22fe6035f90f4db3887634c609a", ( label, tar_y, index ))
    def is_lock_label(self, label, axis = "x", axis_val = 0, index = 1):
        self.adapter.process.request("d36eca82b0840f17c8c0533d0e2800e3", ( label, axis , axis_val , index ))

class soil_moisture_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_humidity(self, index = 1):
        return self.adapter.process.get_value("c7ea6205798cf839467f0c2a8abaecfe", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("4993a7977584a20212ce673b1e4b3836", ( mode,timestamp,index ))

class sound_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_loudness(self, index = 1):
        return self.adapter.process.get_value("1772353fa7fab93451520883e97c0ba8", ( index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("bc1de1b57727d6542717f2de06135d67", ( mode,timestamp,index ))

class speaker_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def stop_sounds(self, index = 1):
        self.adapter.process.request("c228622c0c3a3dc528c5d8d423dc093c", ( index ))
    def set_volume(self, val, index = 1):
        self.adapter.process.request("3a29b2d93b5c4a8a27e420d8f4dc3ae3", ( val, index ))
    def change_volume(self, val, index = 1):
        self.adapter.process.request("e1641b94484af06e5d37e8c7a42637ca", ( val, index ))
    def get_volume(self, index = 1):
        self.adapter.process.request("a2fe8cd3589f27c34545a881b05e671f", ( index ))
    def play_note(self, note, beat = None, index = 1):
        self.adapter.process.request("ed008a45d95ad5fcc3fe6c9a76ebf43c", ( note, beat , index ))
    def play_tone(self, freq, t = None, index = 1):
        self.adapter.process.request("f206cdb1bf4daf5c6c0d7b79962b5309", ( freq, t , index ))
    def play_melody(self, music, index = 1):
        self.adapter.process.request("18b177140042223782b977823bafc5ee", ( music, index ))
    def play_melody_until_done(self, music, index = 1):
        self.adapter.process.request("4b8ba90c930adaca1c25b0683c3fad14", ( music, index ))
    def is_playing(self, index = 1):
        self.adapter.process.request("d65f8d12172dfbb9cdd077f4ebd11f3c", ( index ))

class temp_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def _cal_fahrenheit_from_celsius(self, value):
        self.adapter.process.request("8e4377d0529d07de7178a79f54dbab31", ( value))
    def get_temperature(self, opt = "celsius", index = 1):
        return self.adapter.process.get_value("f71acb6fd6c8fa29cfa3cd461c184b32", ( opt , index ))
    def set_report_mode(self, mode,timestamp,index = 1):
        self.adapter.process.request("f13962126f162b77eb9a860fb1dd5b3a", ( mode,timestamp,index ))

class ultrasonic_sensor_c():
    def __init__(self, adapter):
        self.adapter = adapter
    def get_distance(self, index = 1):
        return self.adapter.process.get_value("5e7547a03e2bddad91eca45a5c61b61f", ( index ))
    def set_report_mode(self, mode, timestamp, index = 1):
        self.adapter.process.request("44224870a79c8992fb87bb126a7d3918", ( mode, timestamp, index ))


