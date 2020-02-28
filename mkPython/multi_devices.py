import time 
import os
from adapter.halo import adapter_halo

from device.api_halocode import *

import device.api_mbuild 
from adapter.halo_mbuild import bind_to_device

from adapter.mbuild import adapter_mbuild


class api_template():
    def __init__(self):
        pass

def create_new(device_name, port, boardrate = 115200):
    ''' create new device
    "halo"/ "mbuild"
    '''
    if device_name == "halo":
        adapter = adapter_halo(port)
        adapter.start()

        halo = api_template()
        halo.led = led_c(adapter)
        halo.button = button_c(adapter) 
        halo.touchpad0 = touchpad0_c(adapter) 
        halo.touchpad1 = touchpad1_c(adapter) 
        halo.touchpad2 = touchpad2_c(adapter) 
        halo.touchpad3 = touchpad3_c(adapter) 
        halo.microphone = microphone_c(adapter)
        halo.motion_sensor = motion_sensor_c(adapter)
        halo.pin0 = pin0_c(adapter) 
        halo.pin1 = pin1_c(adapter) 
        halo.pin2 = pin2_c(adapter) 
        halo.pin3 = pin3_c(adapter) 
        halo.speaker = speaker_c(adapter)
        halo.mesh = mesh_c(adapter)
        halo.wifi = wifi_c(adapter)
        halo.gamepad = gamepad_c(adapter)

        bind_to_device(adapter)
        mbuild = api_template()
        halo.mbuild = mbuild
        # rename api, compatiable with micropython API
        halo.mbuild.dual_rgb_sensor = device.api_mbuild.dual_rgb_sensor_c(adapter)
        halo.mbuild.servo_driver = device.api_mbuild.servo_driver_c(adapter)
        halo.mbuild.speaker = device.api_mbuild.speaker_c(adapter)
        halo.mbuild.dc_motor_driver = device.api_mbuild.dc_motor_driver_c(adapter)
        halo.mbuild.pir_sensor = device.api_mbuild.pir_sensor_c(adapter)
        halo.mbuild.ultrasonic_sensor = device.api_mbuild.ultrasonic_sensor_c(adapter)
        halo.mbuild.led_strip = device.api_mbuild.led_strip_c(adapter)
        halo.mbuild.ranging_sensor = device.api_mbuild.ranging_sensor_c(adapter)
        halo.mbuild.humiture_sensor = device.api_mbuild.humiture_sensor_c(adapter)
        halo.mbuild.slider = device.api_mbuild.slider_c(adapter)
        halo.mbuild.led_panel = device.api_mbuild.led_panel_c(adapter)
        halo.mbuild.button = device.api_mbuild.button_c(adapter)
        halo.mbuild.angle_sensor = device.api_mbuild.angle_sensor_c(adapter)
        halo.mbuild.flame_sensor = device.api_mbuild.flame_sensor_c(adapter)
        halo.mbuild.mq2_gas_sensor = device.api_mbuild.gas_sensor_c(adapter)
        halo.mbuild.ir_transceiver = device.api_mbuild.ir_sensor_c(adapter)
        halo.mbuild.joystick = device.api_mbuild.joystick_c(adapter)
        halo.mbuild.light_sensor = device.api_mbuild.light_sensor_c(adapter)
        halo.mbuild.motion_sensor = device.api_mbuild.motion_sensor_c(adapter)
        halo.mbuild.multi_touch = device.api_mbuild.mult_touch_c(adapter)
        halo.mbuild.soil_moisture = device.api_mbuild.soil_moisture_sensor_c(adapter)
        halo.mbuild.sound_sensor = device.api_mbuild.sound_sensor_c(adapter)
        halo.mbuild.temp_sensor = device.api_mbuild.temp_sensor_c(adapter)
        halo.mbuild.rgb_led = device.api_mbuild.rgb_led_c(adapter)
        halo.mbuild.magnetic_sensor = device.api_mbuild.magnetic_sensor_c(adapter)
        halo.mbuild.smartservo = device.api_mbuild.smartservo_c(adapter)
        halo.mbuild.smart_servo = mbuild.smartservo
        halo.mbuild.smart_camera = device.api_mbuild.smart_camera_c(adapter)
        # compatible
        halo.mbuild.dual_rgb_color_sensor = mbuild.dual_rgb_sensor
        halo.mbuild.led_driver = mbuild.led_strip
        halo.mbuild.motor_driver = mbuild.dc_motor_driver

        return halo
    elif device_name == "mbuild":
        # for build 
        import device.mbuild_modules.servo_driver as servo_driver
        import device.mbuild_modules.speaker as speaker
        import device.mbuild_modules.dc_motor_driver as dc_motor_driver
        import device.mbuild_modules.pir_sensor as pir_sensor
        import device.mbuild_modules.ultrasonic_sensor as ultrasonic_sensor
        import device.mbuild_modules.led_strip as led_strip
        import device.mbuild_modules.ranging_sensor as ranging_sensor
        import device.mbuild_modules.humiture_sensor as humiture_sensor
        import device.mbuild_modules.slider as slider
        import device.mbuild_modules.dual_rgb_sensor as dual_rgb_sensor
        import device.mbuild_modules.led_panel as led_panel
        import device.mbuild_modules.button as button
        import device.mbuild_modules.angle_sensor as angle_sensor
        import device.mbuild_modules.flame_sensor as flame_sensor
        import device.mbuild_modules.gas_sensor as mq2_gas_sensor
        import device.mbuild_modules.ir_sensor as ir_transceiver
        import device.mbuild_modules.joystick as joystick
        import device.mbuild_modules.light_sensor as light_sensor
        import device.mbuild_modules.motion_sensor as motion_sensor
        import device.mbuild_modules.mult_touch as multi_touch
        import device.mbuild_modules.soil_moisture_sensor as soil_moisture
        import device.mbuild_modules.sound_sensor as sound_sensor
        import device.mbuild_modules.temp_sensor as temp_sensor
        # add for 006
        import device.mbuild_modules.rgb_led as rgb_led
        import device.mbuild_modules.magnetic_sensor as magnetic_sensor
        import device.mbuild_modules.smartservo as smartservo
        import device.mbuild_modules.smart_camera as smart_camera
        import device.mbuild_modules.mbot as mbot
        # colorful_handle
        import device.mbuild_modules.colorful_handle as colorful_handle

        mbuild = api_template()
        mbuild.servo_driver = servo_driver
        mbuild.speaker = speaker
        mbuild.dc_motor_driver = dc_motor_driver
        mbuild.pir_sensor = pir_sensor
        mbuild.ultrasonic_sensor = ultrasonic_sensor
        mbuild.led_strip = led_strip
        mbuild.ranging_sensor = ranging_sensor
        mbuild.humiture_sensor = humiture_sensor
        mbuild.slider = slider
        mbuild.dual_rgb_sensor = dual_rgb_sensor
        mbuild.led_panel = led_panel
        mbuild.button = button
        mbuild.angle_sensor = angle_sensor
        mbuild.flame_sensor = flame_sensor
        mbuild.mq2_gas_sensor = mq2_gas_sensor
        mbuild.ir_transceiver = ir_transceiver
        mbuild.joystick = joystick
        mbuild.light_sensor = light_sensor
        mbuild.motion_sensor = motion_sensor
        mbuild.multi_touch = multi_touch
        mbuild.soil_moisture = soil_moisture
        mbuild.sound_sensor = sound_sensor
        mbuild.temp_sensor = temp_sensor
        # add for 006
        mbuild.rgb_led = rgb_led
        mbuild.magnetic_sensor = magnetic_sensor
        # two names about samrt servo
        mbuild.smartservo = smartservo
        mbuild.smart_servo = smartservo
        mbuild.smart_camera = smart_camera

        # colorful_handle
        mbuild.colorful_handle = colorful_handle

        return mbuild