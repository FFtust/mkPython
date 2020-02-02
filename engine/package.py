# -*- coding: utf-8 -*-  
from struct import pack, unpack
import config

from utils.common import int_to_byte_2
from utils.mylog  import console

ONLINE_CMD_ID = 0x28
PROTOCOL_SUBSCRIBE_ID = 0x29


# script to online package
def create_package(servive_id, exec_str, serial_num = 0):
    package_bytes = bytearray()
    
    if cinfig.service_id_enable:
        service_byte_len = 1
    else:
        service_byte_len = 0

    # add protocol id
    package_bytes.append(ONLINE_CMD_ID)
    
    if SERVICE_ID_ENABLE:
        # add servive id
        package_bytes.append(servive_id)
    
    # add serial num, 2 bytes
    if SERIAL_NUM_LEN == 2:
        serial_num_bytes = serial_num.to_bytes(2, "little")
        package_bytes += serial_num_bytes
    elif SERIAL_NUM_LEN == 1:
        package_bytes.append(serial_num)

    # add script bytes
    if SCRIPT_PACKAGE_TYPE == SCRIPT_PACKAGE_TYPE_BIGSTRING:
        strbytes = __bigstring_package(exec_str)  
    elif SCRIPT_PACKAGE_TYPE == SCRIPT_PACKAGE_TYPE_STRING:
        strbytes = __string_package(exec_str) 
    elif SCRIPT_PACKAGE_TYPE == SCRIPT_PACKAGE_TYPE_STRING0:
        strbytes = __string0_package(exec_str)
        
    package_bytes += strbytes
    
    conslole.debug("whole package %s" %package_bytes)
    
    return package_bytes

def print_frame(frame):
    out_str = ""
    for i in range(len(frame)):
        temp = ('%2x' %frame[i])
        temp = temp.replace(" ", "0")
        out_str += temp
        out_str += " "
    print(out_str)

    out_str = ""
    for i in range(len(frame)):
        temp = ('%2x' %frame[i])
        temp = temp.replace(" ", "0")
        temp = "0x" + temp.replace(" ", "0") + ','
        out_str += temp
        out_str += " "

    print(out_str)
 


def __string0_package(string):
    ret_frame = bytearray()
    strbytes = bytes(string, "utf8")
    ret_frame += strbytes
    # add string end code
    ret_frame.append(0x00)    
    
    return ret_frame

def __string_package(string):
    ret_frame = bytearray()
    l = len(string) & 0xff
    # add string len, one byte
    ret_frame.append(l) 
    strbytes = bytes(string, "utf8")
    if len(strbytes) > 255:
        ret_frame += strbytes[0 : 256]
    else:
        ret_frame += strbytes
    
    return ret_frame
 
def __bigstring_package(string):
    ret_frame = bytearray()
    l = len(string)
    l_bytes = int_to_byte_2(l)
    # add string len, two bytes
    ret_frame += l_bytes
    strbytes = bytes(string, "utf8")
    ret_frame += strbytes
    
    return ret_frame