import engine.F3F4.process
import engine.F3F4.protocol
import link.commu_uart

from engine.F3F4.package import create_package, print_frame
from engine.F3F4.protocol import create_frame

from device.table_mbuild import *

def bind_to_device(adapter):
    add_table_to_device(adapter, table_dual_rgb_sensor_tag)
    add_table_to_device(adapter, table_angle_sensor_tag)
    add_table_to_device(adapter, table_button_tag)
    add_table_to_device(adapter, table_dc_motor_driver_tag)
    add_table_to_device(adapter, table_flame_sensor_tag)
    add_table_to_device(adapter, table_gas_sensor_tag)
    add_table_to_device(adapter, table_humiture_sensor_tag)
    add_table_to_device(adapter, table_ir_transceiver_tag)
    add_table_to_device(adapter, table_joystick_tag)
    add_table_to_device(adapter, table_led_panel_tag)
    add_table_to_device(adapter, table_led_strip_tag)
    add_table_to_device(adapter, table_light_sensor_tag)
    add_table_to_device(adapter, table_magnetic_sensor_tag)
    add_table_to_device(adapter, table_motion_sensor_tag)
    add_table_to_device(adapter, table_multi_touch_tag)
    add_table_to_device(adapter, table_pir_sensor_tag)
    add_table_to_device(adapter, table_ranging_sensor_tag)
    add_table_to_device(adapter, table_rgb_led_tag)
    add_table_to_device(adapter, table_servo_driver_tag)
    add_table_to_device(adapter, table_slider_tag)
    add_table_to_device(adapter, table_smartservo_tag)
    add_table_to_device(adapter, table_smart_camera_tag)
    add_table_to_device(adapter, table_soil_moisture_sensor_tag)
    add_table_to_device(adapter, table_sound_sensor_tag)
    add_table_to_device(adapter, table_speaker_tag)
    add_table_to_device(adapter, table_temp_sensor_tag)
    add_table_to_device(adapter, table_ultrasonic_sensor_tag)

    adapter.link_obj.write(create_frame(create_package("mbuild.dual_rgb_sensor.__REPORT_TIME = 50", 0x00, 0x04)))

def add_table_to_device(adapter, table_tag):
    table_key = {}
    key_index = len(adapter.process.data_tag)
    for item in table_tag:
        table_tag[item]['key'] = key_index 
        table_key.update({str(key_index): {"tag":item, "obj":table_tag[item]["obj"]}})
        table_key[str(key_index)]['obj'].key = str(key_index)

        key_index += 1


    adapter.process.data_tag.update(table_tag)
    adapter.process.data_key.update(table_key)
