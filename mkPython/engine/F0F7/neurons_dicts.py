# create by neurons_dict_create.py
#release_note: add command for smart servo  
# Mon Mar 09 09:28:05 2020
general_command_request_dict = {'assign_id': {'type': 16, 'subtype': None, 1: 'BYTE', 'para_num': 1}, 'reset_block': {'type': 17, 'subtype': None, 'para_num': 0}, 'query_version': {'type': 18, 'subtype': None, 'para_num': 0}, 'set_baud_rate': {'type': 19, 'subtype': None, 1: 'BYTE', 'para_num': 1}, 'test_traffic': {'type': 20, 'subtype': None, 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 4: 'BYTE', 5: 'BYTE', 'para_num': 5}, 'universal_response': {'type': 21, 'subtype': None, 1: 'BYTE', 'para_num': 1}, 'set_command_response': {'type': 97, 'subtype': 1, 1: 'BYTE', 'para_num': 1}, 'set_block_rgb_led': {'type': 97, 'subtype': 2, 1: 'byte', 2: 'byte', 3: 'byte', 'para_num': 3}, 'handshake': {'type': 97, 'subtype': 3, 'para_num': 0}}
general_command_response_dict = {4096: {'name': 'assign_id', 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 4608: {'name': 'query_version', 1: 'BYTE', 2: 'BYTE', 3: 'SHORT', 'para_num': 3}, 5120: {'name': 'test_traffic', 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 4: 'BYTE', 5: 'BYTE', 'para_num': 5}, 5376: {'name': 'universal_response', 1: 'BYTE', 'para_num': 1}}
common_neurons_command_request_dict = {25372: {'name': 'm_mq2_sensor', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25611: {'name': 'm_button', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'get_pressed_count': {'command_id': 2, 'para_num': 0}, 'reset_count': {'command_id': 3, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25612: {'name': 'm_joystick', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25368: {'name': 'm_temp_sensor', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25369: {'name': 'm_humiture_sensor', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25613: {'name': 'm_slider', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25362: {'name': 'm_ranging_sensor', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25371: {'name': 'm_flame', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25367: {'name': 'm_pir', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'get_count': {'command_id': 2, 'para_num': 0}, 'reset_count': {'command_id': 3, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25614: {'name': 'm_angle_sensor', 'function': {'get_angle': {'command_id': 1, 'para_num': 0}, 'get_dir': {'command_id': 2, 'para_num': 0}, 'get_angle_speed': {'command_id': 4, 'para_num': 0}, 'reset': {'command_id': 3, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 26116: {'name': 'm_speaker', 'function': {'get_volume': {'command_id': 5, 'para_num': 0}, 'get_status': {'command_id': 7, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'play_melody': {'command_id': 1, 1: 'STR1', 'para_num': 1}, 'play_frequency': {'command_id': 2, 1: 'SHORT', 'para_num': 1}, 'set_volume': {'command_id': 3, 1: 'byte', 'para_num': 1}, 'change_volume': {'command_id': 4, 1: 'byte', 'para_num': 1}, 'stop': {'command_id': 6, 'para_num': 0}}}, 25097: {'name': 'm_dc_motor', 'function': {'get_power': {'command_id': 2, 'para_num': 0}, 'get_load': {'command_id': 4, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_power': {'command_id': 1, 1: 'byte', 'para_num': 1}, 'change_power': {'command_id': 3, 1: 'byte', 'para_num': 1}}}, 25098: {'name': 'm_servo', 'function': {'get_angle': {'command_id': 2, 'para_num': 0}, 'get_load': {'command_id': 4, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_angle': {'command_id': 1, 1: 'SHORT', 'para_num': 1}, 'change_angle': {'command_id': 3, 1: 'short', 'para_num': 1}, 'goto_zero': {'command_id': 5, 'para_num': 0}, 'release': {'command_id': 6, 'para_num': 0}}}, 25863: {'name': 'm_rgb', 'function': {'show': {'command_id': 1, 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 'set_red': {'command_id': 2, 1: 'SHORT', 'para_num': 1}, 'set_green': {'command_id': 3, 1: 'SHORT', 'para_num': 1}, 'set_blue': {'command_id': 4, 1: 'SHORT', 'para_num': 1}, 'get_info': {'command_id': 5, 'para_num': 0}}}, 25865: {'name': 'm_led_panel', 'function': {'show_pixel': {'command_id': 1, 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 'para_num': 3}, 'show_image': {'command_id': 2, 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 4: 'SHORT', 5: 'SHORT', 6: 'SHORT', 7: 'SHORT', 8: 'SHORT', 9: 'SHORT', 10: 'SHORT', 11: 'SHORT', 12: 'SHORT', 13: 'SHORT', 14: 'SHORT', 15: 'SHORT', 16: 'SHORT', 'para_num': 16}, 'clear': {'command_id': 3, 'para_num': 0}, 'get_pixel': {'command_id': 4, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'toggle_pixel': {'command_id': 5, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'toggle_pixel2': {'command_id': 5, 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 'para_num': 3}, 'show_str_with_pos': {'command_id': 6, 1: 'short', 2: 'short', 3: 'STR2', 'para_num': 3}, 'show_str': {'command_id': 7, 1: 'STR2', 'para_num': 1}, 'get_status': {'command_id': 8, 'para_num': 0}, 'show_str_until_done': {'command_id': 10, 1: 'STR2', 'para_num': 1}}}, 25366: {'name': 'm_ultrasonic_sensor', 'function': {'get_centimeter': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25864: {'name': 'm_rgb_led_ring', 'function': {'set_rgb': {'command_id': 1, 1: 'BYTE', 2: 'SHORT', 3: 'SHORT', 4: 'SHORT', 'para_num': 4}, 'off_all': {'command_id': 4, 'para_num': 0}, 'set_red': {'command_id': 5, 1: 'BYTE', 2: 'SHORT', 'para_num': 2}, 'set_green': {'command_id': 6, 1: 'BYTE', 2: 'SHORT', 'para_num': 2}, 'set_blue': {'command_id': 7, 1: 'BYTE', 2: 'SHORT', 'para_num': 2}, 'change_red': {'command_id': 8, 1: 'BYTE', 2: 'short', 'para_num': 2}, 'change_green': {'command_id': 9, 1: 'BYTE', 2: 'short', 'para_num': 2}, 'change_blue': {'command_id': 10, 1: 'BYTE', 2: 'short', 'para_num': 2}, 'set_mode': {'command_id': 11, 1: 'BYTE', 'para_num': 1}, 'set_block': {'command_id': 12, 1: 'STR1', 'para_num': 1}}}, 25361: {'name': 'm_dual_rgb_sensor', 'function': {'study': {'command_id': 1, 'para_num': 0}, 'calibration': {'command_id': 2, 'para_num': 0}, 'get_intensity': {'command_id': 3, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_state': {'command_id': 4, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_offset': {'command_id': 5, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_color': {'command_id': 6, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_all_data': {'command_id': 7, 'para_num': 0}, 'get_color_rgb': {'command_id': 8, 'para_num': 0}, 'get_evm_data': {'command_id': 9, 'para_num': 0}, 'get_reflect_data': {'command_id': 10, 'para_num': 0}, 'set_light_color': {'command_id': 16, 1: 'BYTE', 'para_num': 1}, 'set_rgb_color': {'command_id': 17, 1: 'BYTE', 'para_num': 1}, 'set_intensity_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_state_report_mode': {'command_id': 126, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_offset_report_mode': {'command_id': 125, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_color_report_mode': {'command_id': 124, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_all_data_report_mode': {'command_id': 123, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25364: {'name': 'm_light_sensor', 'function': {'get_intensity': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25365: {'name': 'm_soil_moisture', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25363: {'name': 'm_sound_sensor', 'function': {'get_loudness': {'command_id': 1, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 25610: {'name': 'm_mult_touch', 'function': {'get_status': {'command_id': 1, 'para_num': 0}, 'get_value': {'command_id': 2, 1: 'BYTE', 'para_num': 1}, 'reset': {'command_id': 3, 'para_num': 0}, 'set_sensitivity': {'command_id': 4, 1: 'BYTE', 'para_num': 1}}}, 25374: {'name': 'm_magneto_dependent_sensor', 'function': {'get_value': {'command_id': 1, 'para_num': 0}, 'get_count': {'command_id': 2, 'para_num': 0}, 'reset_count': {'command_id': 3, 'para_num': 0}, 'set_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 26626: {'name': 'm_ir_sensor', 'function': {'send_str': {'command_id': 2, 1: 'STR1', 'para_num': 1}, 'record': {'command_id': 3, 1: 'long', 2: 'BYTE', 'para_num': 2}, 'send_record': {'command_id': 4, 1: 'BYTE', 'para_num': 1}, 'read_cmd': {'command_id': 7, 'para_num': 0}, 'read_str': {'command_id': 8, 'para_num': 0}}}, 25370: {'name': 'm_motion_sensor', 'function': {'inquire_data': {'command_id': 1, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'regiter_data': {'command_id': 1, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'unregiter_data': {'command_id': 1, 1: 'BYTE', 'para_num': 1}, 'reset_z': {'command_id': 4, 'para_num': 0}, 'reset_x': {'command_id': 5, 'para_num': 0}, 'reset_y': {'command_id': 6, 'para_num': 0}, 'get_shake_strength': {'command_id': 1, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'get_acc_x': {'command_id': 2, 'para_num': 0}, 'get_acc_y': {'command_id': 3, 'para_num': 0}, 'get_acc_z': {'command_id': 4, 'para_num': 0}, 'get_gyr_x': {'command_id': 5, 'para_num': 0}, 'get_gyr_y': {'command_id': 6, 'para_num': 0}, 'get_gyr_z': {'command_id': 7, 'para_num': 0}, 'get_pitch': {'command_id': 8, 'para_num': 0}, 'get_roll': {'command_id': 9, 'para_num': 0}, 'get_rotate_z': {'command_id': 10, 'para_num': 0}, 'get_rotate_x': {'command_id': 11, 'para_num': 0}, 'get_rotate_y': {'command_id': 12, 'para_num': 0}}}, 26627: {'name': 'm_halobot', 'function': {'ir_send': {'command_id': 1, 1: 'STR1', 'para_num': 1}, 'ir_receive': {'command_id': 11, 1: 'STR1', 'para_num': 1}, 'ir_send_remote_code': {'command_id': 10, 1: 'SHORT', 2: 'byte', 'para_num': 2}, 'ir_receive_remote_code': {'command_id': 2, 'para_num': 0}, 'servo_get_angle': {'command_id': 3, 1: 'BYTE', 'para_num': 1}, 'servo_get_current': {'command_id': 4, 1: 'BYTE', 'para_num': 1}, 'servo_set_angle': {'command_id': 5, 1: 'BYTE', 2: 'SHORT', 'para_num': 2}, 'servo_change_angle': {'command_id': 8, 1: 'BYTE', 2: 'short', 'para_num': 2}, 'servo_release': {'command_id': 9, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'dc_motor_set_power': {'command_id': 6, 1: 'BYTE', 2: 'byte', 'para_num': 2}, 'button_get_value': {'command_id': 7, 'para_num': 0}, 'button_set_report_mode': {'command_id': 31, 1: 'BYTE', 2: 'long', 'para_num': 2}}}, 26375: {'name': 'm_mbot', 'function': {'run': {'command_id': 1, 1: 'float', 2: 'float', 'para_num': 2}}}, 24576: {'name': 'm_smartservo', 'function': {'lock_unlock': {'command_id': 22, 1: 'BYTE', 'para_num': 1}, 'get_position': {'command_id': 54, 1: 'BYTE', 'para_num': 1}, 'get_speed': {'command_id': 35, 1: 'BYTE', 'para_num': 1}, 'set_zero': {'command_id': 48, 'para_num': 0}, 'move_to': {'command_id': 51, 1: 'long', 2: 'SHORT', 'para_num': 2}, 'move': {'command_id': 52, 1: 'long', 2: 'SHORT', 'para_num': 2}, 'move_to_in_time': {'command_id': 42, 1: 'float', 2: 'SHORT', 'para_num': 2}, 'set_pwm': {'command_id': 53, 1: 'short', 'para_num': 1}, 'back_to_zero': {'command_id': 55, 1: 'BYTE', 2: 'SHORT', 'para_num': 2}, 'move_to_with_torque': {'command_id': 56, 1: 'long', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 'move_with_torque': {'command_id': 57, 1: 'long', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 'speed_loop': {'command_id': 58, 1: 'byte', 'para_num': 1}, 'if_arrived': {'command_id': 64, 'para_num': 0}, 'error_report': {'command_id': 65, 'para_num': 0}, 'error_state_clear': {'command_id': 66, 'para_num': 0}, 'back_to_zero_dir': {'command_id': 67, 1: 'BYTE', 2: 'SHORT', 'para_num': 2}}}, 25375: {'name': 'm_smart_camera', 'function': {'get_fills_all_data': {'command_id': 1, 1: 'BYTE', 'para_num': 1}, 'set_fills_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_fills_sigle_data': {'command_id': 2, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'get_line_all_data': {'command_id': 3, 'para_num': 0}, 'set_line_report_mode': {'command_id': 126, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_line_sigle_data': {'command_id': 4, 1: 'BYTE', 'para_num': 1}, 'get_crossings_all_data': {'command_id': 5, 'para_num': 0}, 'set_crossings_report_mode': {'command_id': 125, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_crossings_sigle_data': {'command_id': 6, 1: 'BYTE', 'para_num': 1}, 'get_crossings_line_angle_sigle_data': {'command_id': 7, 'para_num': 0}, 'get_barcode_all_data': {'command_id': 8, 1: 'BYTE', 'para_num': 1}, 'set_barcode_report_mode': {'command_id': 124, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_barcode_sigle_data': {'command_id': 9, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'get_button_data': {'command_id': 10, 'para_num': 0}, 'set_button_report_mode': {'command_id': 123, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'get_learn_data': {'command_id': 11, 'para_num': 0}, 'set_camera_sensitometry': {'command_id': 32, 1: 'SHORT', 'para_num': 1}, 'set_led_rgb': {'command_id': 33, 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 'set_fill_light_status': {'command_id': 34, 1: 'BYTE', 'para_num': 1}, 'set_line_follow_vector_mode': {'command_id': 35, 1: 'BYTE', 'para_num': 1}, 'set_line_follow_mode': {'command_id': 36, 1: 'BYTE', 'para_num': 1}, 'get_turning_angle': {'command_id': 12, 'para_num': 0}, 'get_fills_count': {'command_id': 13, 'para_num': 0}, 'get_barcode_count': {'command_id': 14, 'para_num': 0}, 'set_next_turning_angle': {'command_id': 37, 1: 'short', 'para_num': 1}, 'set_default_turning_angle': {'command_id': 38, 1: 'short', 'para_num': 1}, 'set_fills_learn_mode': {'command_id': 43, 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 'stop_learn': {'command_id': 40, 'para_num': 0}, 'abandon_learn': {'command_id': 41, 'para_num': 0}, 'set_pixy_mode': {'command_id': 42, 1: 'BYTE', 'para_num': 1}}}, 25615: {'name': 'm_fingertip_piano', 'function': {'set_rgb': {'command_id': 1, 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 'get_button_state': {'command_id': 2, 'para_num': 0}, 'get_touchpad_state': {'command_id': 3, 'para_num': 0}, 'get_joystick_state': {'command_id': 4, 'para_num': 0}, 'get_joystick_value': {'command_id': 5, 'para_num': 0}, 'get_gesture': {'command_id': 6, 'para_num': 0}, 'get_distance': {'command_id': 7, 'para_num': 0}, 'get_touchpad_value': {'command_id': 8, 'para_num': 0}, 'get_button_count': {'command_id': 9, 'para_num': 0}, 'ir_sensor_calibration': {'command_id': 16, 'para_num': 0}, 'reset_button_count': {'command_id': 17, 1: 'BYTE', 'para_num': 1}, 'set_button_report_mode': {'command_id': 127, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_touchpad_report_mode': {'command_id': 126, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_joystick_state_report_mode': {'command_id': 125, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_joystick_value_report_mode': {'command_id': 124, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_gesture_report_mode': {'command_id': 123, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_distance_report_mode': {'command_id': 122, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_touchpad_value_report_mode': {'command_id': 121, 1: 'BYTE', 2: 'long', 'para_num': 2}, 'set_button_count_report_mode': {'command_id': 120, 1: 'BYTE', 2: 'long', 'para_num': 2}}}}
common_neurons_command_response_dict = {25361: {'name': 'm_dual_rgb_sensor', 'function': {3: {'command_name': 'get_intensity', 1: 'SHORT', 2: 'SHORT', 'para_num': 2}, 4: {'command_name': 'get_state', 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 5: {'command_name': 'get_offset', 1: 'short', 'para_num': 1}, 6: {'command_name': 'get_color', 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 7: {'command_name': 'get_all_data', 1: 'SHORT', 2: 'SHORT', 3: 'BYTE', 4: 'BYTE', 5: 'short', 6: 'BYTE', 7: 'BYTE', 'para_num': 7}, 8: {'command_name': 'get_color_rgb', 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 4: 'SHORT', 5: 'SHORT', 6: 'SHORT', 'para_num': 6}, 9: {'command_name': 'get_evm_data', 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 10: {'command_name': 'get_reflect_data', 1: 'SHORT', 2: 'SHORT', 'para_num': 2}}}, 25372: {'name': 'm_mq2_sensor', 'function': {1: {'command_name': 'get_value', 1: 'BYTE', 'para_num': 1}}}, 25611: {'name': 'm_button', 'function': {1: {'command_name': 'get_value', 1: 'BYTE', 'para_num': 1}, 2: {'command_name': 'get_pressed_count', 1: 'long', 'para_num': 1}}}, 25612: {'name': 'm_joystick', 'function': {1: {'command_name': 'get_value', 1: 'byte', 2: 'byte', 'para_num': 2}}}, 25368: {'name': 'm_temp_sensor', 'function': {1: {'command_name': 'get_value', 1: 'float', 'para_num': 1}}}, 25369: {'name': 'm_humiture_sensor0x63', 'function': {1: {'command_name': 'get_value', 1: 'byte', 2: 'BYTE', 'para_num': 2}}}, 25613: {'name': 'm_slider', 'function': {1: {'command_name': 'get_value', 1: 'BYTE', 'para_num': 1}}}, 25362: {'name': 'm_ranging_sensor', 'function': {1: {'command_name': 'get_value', 1: 'float', 'para_num': 1}}}, 25371: {'name': 'm_flame', 'function': {1: {'command_name': 'get_value', 1: 'BYTE', 'para_num': 1}}}, 25367: {'name': 'm_pir', 'function': {1: {'command_name': 'get_value', 1: 'BYTE', 'para_num': 1}, 2: {'command_name': 'get_count', 1: 'long', 'para_num': 1}}}, 25614: {'name': 'm_angle_sensor', 'function': {1: {'command_name': 'get_angle', 1: 'long', 'para_num': 1}, 2: {'command_name': 'get_dir', 1: 'BYTE', 'para_num': 1}, 4: {'command_name': 'get_angle_speed', 1: 'long', 'para_num': 1}}}, 26116: {'name': 'm_speaker', 'function': {5: {'command_name': 'get_volume', 1: 'byte', 'para_num': 1}, 7: {'command_name': 'get_status', 1: 'BYTE', 'para_num': 1}}}, 25097: {'name': 'm_dc_motor', 'function': {2: {'command_name': 'get_power', 1: 'byte', 'para_num': 1}, 4: {'command_name': 'get_load', 1: 'SHORT', 'para_num': 1}}}, 25098: {'name': 'm_servo', 'function': {2: {'command_name': 'get_angle', 1: 'SHORT', 'para_num': 1}, 4: {'command_name': 'get_load', 1: 'SHORT', 'para_num': 1}}}, 25863: {'name': 'm_rgb', 'function': {5: {'command_name': 'get_info', 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}}}, 25865: {'name': 'm_led_panel', 'function': {4: {'command_name': 'get_pixel', 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 'para_num': 3}, 8: {'command_name': 'get_status', 1: 'BYTE', 'para_num': 1}}}, 25366: {'name': 'm_ultrasonic_sensor', 'function': {1: {'command_name': 'get_centimeter', 1: 'float', 'para_num': 1}}}, 25364: {'name': 'm_light_sensor', 'function': {1: {'command_name': 'get_intensity', 1: 'BYTE', 'para_num': 1}}}, 25365: {'name': 'm_soil_moisture', 'function': {1: {'command_name': 'get_intensity', 1: 'BYTE', 'para_num': 1}}}, 25363: {'name': 'm_sound_sensor', 'function': {1: {'command_name': 'get_intensity', 1: 'BYTE', 'para_num': 1}}}, 25610: {'name': 'm_mult_touch', 'function': {1: {'command_name': 'get_status', 1: 'byte', 'para_num': 1}, 2: {'command_name': 'get_value', 1: 'short', 'para_num': 1}}}, 25374: {'name': 'm_magneto_dependent_sensor', 'function': {1: {'command_name': 'get_value', 1: 'BYTE', 'para_num': 1}, 2: {'command_name': 'get_count', 1: 'long', 'para_num': 1}}}, 26626: {'name': 'm_ir_sensor', 'function': {1: {'command_name': 'read_cmd', 1: 'SHORT', 2: 'SHORT', 'para_num': 2}, 2: {'command_name': 'read_str', 1: 'STR3', 'para_num': 1}}}, 25370: {'name': 'm_motion_sensor', 'function': {1: {'command_name': 'get_shake_strength', 1: 'BYTE', 'para_num': 1}, 2: {'command_name': 'get_acc_x', 1: 'float', 'para_num': 1}, 3: {'command_name': 'get_acc_y', 1: 'float', 'para_num': 1}, 4: {'command_name': 'get_acc_z', 1: 'float', 'para_num': 1}, 5: {'command_name': 'get_gyr_x', 1: 'float', 'para_num': 1}, 6: {'command_name': 'get_gyr_y', 1: 'float', 'para_num': 1}, 7: {'command_name': 'get_gyr_z', 1: 'float', 'para_num': 1}, 8: {'command_name': 'get_pitch', 1: 'short', 'para_num': 1}, 9: {'command_name': 'get_roll', 1: 'short', 'para_num': 1}, 10: {'command_name': 'get_rotate_z', 1: 'short', 'para_num': 1}, 11: {'command_name': 'get_rotate_x', 1: 'short', 'para_num': 1}, 12: {'command_name': 'get_rotate_y', 1: 'short', 'para_num': 1}}}, 26627: {'name': 'm_halobot', 'function': {11: {'command_name': 'ir_receive', 1: 'STR1', 'para_num': 1}, 2: {'command_name': 'ir_receive_remote_code', 1: 'SHORT', 2: 'byte', 'para_num': 2}, 3: {'command_name': 'servo_get_angle', 1: 'BYTE', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 4: {'command_name': 'servo_get_current', 1: 'BYTE', 2: 'SHORT', 3: 'SHORT', 'para_num': 3}, 7: {'command_name': 'button_get_value', 1: 'BYTE', 'para_num': 1}}}, 24576: {'name': 'm_smartservo', 'function': {35: {'command_name': 'get_speed', 1: 'float', 'para_num': 1}, 54: {'command_name': 'get_position', 1: 'long', 'para_num': 1}, 64: {'command_name': 'if_arrived', 1: 'BYTE', 'para_num': 1}, 65: {'command_name': 'error_report', 1: 'BYTE', 'para_num': 1}}}, 25375: {'name': 'm_smart_camera', 'function': {1: {'command_name': 'get_fills_all_data', 1: 'BYTE', 2: 'SHORT', 3: 'SHORT', 4: 'SHORT', 5: 'SHORT', 'para_num': 5}, 2: {'command_name': 'get_fills_sigle_data', 1: 'BYTE', 2: 'BYTE', 3: 'SHORT', 'para_num': 3}, 3: {'command_name': 'get_line_all_data', 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 4: 'BYTE', 'para_num': 4}, 4: {'command_name': 'get_line_sigle_data', 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 5: {'command_name': 'get_crossings_all_data', 1: 'short', 2: 'short', 3: 'short', 4: 'short', 5: 'short', 6: 'short', 7: 'short', 8: 'short', 9: 'short', 'para_num': 9}, 6: {'command_name': 'get_crossings_sigle_data', 1: 'BYTE', 2: 'short', 'para_num': 2}, 7: {'command_name': 'get_crossings_line_angle_sigle_data', 1: 'short', 2: 'short', 3: 'short', 4: 'short', 5: 'short', 6: 'short', 'para_num': 6}, 8: {'command_name': 'get_barcode_all_data', 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 'para_num': 3}, 9: {'command_name': 'get_barcode_sigle_data', 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 'para_num': 3}, 10: {'command_name': 'get_button_data', 1: 'BYTE', 'para_num': 1}, 11: {'command_name': 'get_learn_data', 1: 'BYTE', 'para_num': 1}, 12: {'command_name': 'get_turning_angle', 1: 'short', 'para_num': 1}, 13: {'command_name': 'get_fills_count', 1: 'BYTE', 'para_num': 1}, 14: {'command_name': 'get_barcode_count', 1: 'BYTE', 'para_num': 1}}}, 25615: {'name': 'm_fingertip_piano', 'function': {2: {'command_name': 'get_button_state', 1: 'BYTE', 2: 'BYTE', 'para_num': 2}, 3: {'command_name': 'get_touchpad_state', 1: 'BYTE', 2: 'BYTE', 3: 'BYTE', 4: 'BYTE', 'para_num': 4}, 4: {'command_name': 'get_joystick_state', 1: 'byte', 2: 'byte', 'para_num': 2}, 5: {'command_name': 'get_joystick_value', 1: 'byte', 2: 'byte', 'para_num': 2}, 6: {'command_name': 'get_gesture', 1: 'BYTE', 'para_num': 1}, 7: {'command_name': 'get_distance', 1: 'BYTE', 'para_num': 1}, 8: {'command_name': 'get_touchpad_value', 1: 'SHORT', 2: 'SHORT', 3: 'SHORT', 4: 'SHORT', 'para_num': 4}, 9: {'command_name': 'get_button_count', 1: 'long', 2: 'long', 'para_num': 2}}}}
common_neurons_command_default_result_dict = {'m_dual_rgb_sensor': {'get_intensity': [0, 0], 'get_state': [0, 0], 'get_offset': [0], 'get_color': [0, 0], 'get_all_data': [0, 0, 0, 0, 0, 0, 0], 'get_color_rgb': [0, 0, 0, 0, 0, 0], 'get_evm_data': [0, 0], 'get_reflect_data': [0, 0]}, 'm_mq2_sensor': {'get_value': [0]}, 'm_button': {'get_value': [0], 'get_pressed_count': [0]}, 'm_joystick': {'get_value': [0, 0]}, 'm_temp_sensor': {'get_value': [0]}, 'm_humiture_sensor0x63': {'get_value': [0, 0]}, 'm_slider': {'get_value': [0]}, 'm_ranging_sensor': {'get_value': [0]}, 'm_flame': {'get_value': [0]}, 'm_pir': {'get_value': [0], 'get_count': [0]}, 'm_angle_sensor': {'get_angle': [0], 'get_dir': [0], 'get_angle_speed': [0]}, 'm_speaker': {'get_volume': [0], 'get_status': [0]}, 'm_dc_motor': {'get_power': [0], 'get_load': [0]}, 'm_servo': {'get_angle': [0], 'get_load': [0]}, 'm_rgb': {'get_info': [0, 0, 0]}, 'm_led_panel': {'get_pixel': [0, 0, 0], 'get_status': [0]}, 'm_ultrasonic_sensor': {'get_centimeter': [0]}, 'm_light_sensor': {'get_intensity': [0]}, 'm_soil_moisture': {'get_intensity': [0]}, 'm_sound_sensor': {'get_intensity': [0]}, 'm_mult_touch': {'get_status': [0], 'get_value': [0]}, 'm_magneto_dependent_sensor': {'get_value': [0], 'get_count': [0]}, 'm_ir_sensor': {'read_cmd': [0, 0], 'read_str': [0]}, 'm_motion_sensor': {'get_shake_strength': [0], 'get_acc_x': [0], 'get_acc_y': [0], 'get_acc_z': [0], 'get_gyr_x': [0], 'get_gyr_y': [0], 'get_gyr_z': [0], 'get_pitch': [0], 'get_roll': [0], 'get_rotate_z': [0], 'get_rotate_x': [0], 'get_rotate_y': [0]}, 'm_halobot': {'ir_receive': [0], 'ir_receive_remote_code': [0, 0], 'servo_get_angle': [0, 0, 0], 'servo_get_current': [0, 0, 0], 'button_get_value': [0]}, 'm_smartservo': {'get_speed': [0], 'get_position': [0], 'if_arrived': [0], 'error_report': [0]}, 'm_smart_camera': {'get_fills_all_data': [0, 0, 0, 0, 0], 'get_fills_sigle_data': [0, 0, 0], 'get_line_all_data': [0, 0, 0, 0], 'get_line_sigle_data': [0, 0], 'get_crossings_all_data': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'get_crossings_sigle_data': [0, 0], 'get_crossings_line_angle_sigle_data': [0, 0, 0, 0, 0, 0], 'get_barcode_all_data': [0, 0, 0], 'get_barcode_sigle_data': [0, 0, 0], 'get_button_data': [0], 'get_learn_data': [0], 'get_turning_angle': [0], 'get_fills_count': [0], 'get_barcode_count': [0]}, 'm_fingertip_piano': {'get_button_state': [0, 0], 'get_touchpad_state': [0, 0, 0, 0], 'get_joystick_state': [0, 0], 'get_joystick_value': [0, 0], 'get_gesture': [0], 'get_distance': [0], 'get_touchpad_value': [0, 0, 0, 0], 'get_button_count': [0, 0]}}
