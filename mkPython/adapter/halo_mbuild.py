import engine.F3F4.process
import engine.F3F4.protocol
import link.commu_uart

from device.table_mbuild import *

def bind_to_device(adapter):
    # add_table_to_device(adapter, table_dc_motor_driver_tag)
    add_table_to_device(adapter, table_dual_rgb_sensor_tag)

def add_table_to_device(adapter, table_tag):
    table_key = {}
    key_index = len(adapter.process.data_tag)
    for item in table_tag:
        table_tag[item]['key'] = key_index 
        table_key.update({key_index: {"tag":item, "obj":table_tag[item]["obj"]}})
        key_index += 1


    adapter.process.data_tag.update(table_tag)
    adapter.process.data_key.update(table_key)
    # print(adapter.data_base.data_tag)
    # print(adapter.data_base.data_key)