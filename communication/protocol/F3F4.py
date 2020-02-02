# -*- coding: utf-8 -*-
from struct import pack, unpack

from utils.common import int_to_byte_2
from utils.mylog import console

'''
F3F4 frame structure
----*----*----*----*----*----*----*----*----*----*
head|h_c |len1|len2|cmd |da_1| ...|da_n|sum |end |   
----*----*----*----*----*----*----*----*----*----*
 F3 | ** | ** | ** | ** | ** | ** | ** | ** | F4 |
----*----*----*----*----*----*----*----*----*----*
description:
h_c : h_c(head_check) = (head + len1 + len2) & 0xf7
len1: low bits of the data region length 
len2: high bits of the data region length
cmd : command id
da_*: data region
sum : the sum of data region, sum = (da_1 + *** + da_n) & 0xf7 
'''

F3F4_PROTOCOL_HEAD = 0xF3
COMMON_PROTOCOL_END = 0xF4

class F3F4_frame():
    # about frame limits
    FRAME_MAX_LEN = 1024
    FRAME_MAX_NUM = 32

    # protocol catch FSM state
    FSM_S_HEAD = 0
    FSM_S_HEAD_CHECK = 1
    FSM_S_LEN_1 = 2
    FSM_S_LEN_2 = 3
    FSM_S_DATA = 4
    FSM_S_DATA_CHECK = 5
    FSM_S_END = 6

    def __init__(self):
        self.frame_process_cb_list = []
        self.__fsm_init()


    def create_frame(self, data):
        protocol_frame = bytearray()
        protocol_frame.append(F3F4_PROTOCOL_HEAD)
    
        datalen = 1 + len(data) 

        data_len_byte = datalen.to_bytes(2, "little")

        head_check = (data_len_byte[0] + data_len_byte[1] + F3F4_PROTOCOL_HEAD) & 0xFF

        # add head check
        protocol_frame.append(head_check)
        protocol_frame += data_len_byte

        data_sum = 0  
        for i in range(len(data)):
            data_sum += data[i]

        data_sum = data_sum & 0xFF
        protocol_frame.append(data_sum)   
        protocol_frame.append(COMMON_PROTOCOL_END)  
        
        return protocol_frame

    def print_frame(self, frame):
        __print_frame(frame)

    def register_frame_cb(self, cb, conditions = None):
        self.frame_process_cb_list.append(cb)

    def parse_data_stream(self, data, d_info = None):
        self.__fsm(data)
        if self.frame_list:
            print(self.frame_list)
            for item in self.frame_list:
                for cb in self.frame_process_cb_list:
                    ret = cb(item, d_info)

                    # process result
                    if ret:
                        pass
                self.frame_list.remove(item)

    # FSM processing
    def __fsm_init(self):    
        '''
        frame FSM manager
        '''
        self.fsm_state = self.FSM_S_HEAD
        self.recv_buffer = bytearray()
        self.recv_len = 0
        self.head_checksum = 0
        self.data_region_len = 0

        self.frame_list = []

    # Input a stream data, split stream to frame and save in frame_list
    def __fsm(self, stream):
        # this variable indicate the number of datas should be read next time
        ret_num = 1
        for c in stream:
            receive_frame = None

            if len(self.recv_buffer) > self.FRAME_MAX_LEN:
                self.fsm_state = self.S_HEAD

            if (self.FSM_S_HEAD == self.fsm_state):
                if (F3F4_PROTOCOL_HEAD == c):
                    self.recv_buffer = bytearray()
                    self.recv_buffer.append(c)
                    self.fsm_state = self.FSM_S_HEAD_CHECK

            elif (self.FSM_S_HEAD_CHECK == self.fsm_state):
                self.recv_buffer.append(c)
                self.head_checksum = c
                self.fsm_state = self.FSM_S_LEN_1

            elif (self.FSM_S_LEN_1 == self.fsm_state):
                self.recv_buffer.append(c)
                self.data_region_len = c
                self.fsm_state = self.FSM_S_LEN_2

            elif (self.FSM_S_LEN_2 == self.fsm_state):
                self.recv_buffer.append(c)
                self.data_region_len += c * 0xFF
                head_checksum = (self.recv_buffer[0] + self.recv_buffer[2] + self.recv_buffer[3]) & 0xFF
                if (head_checksum == self.head_checksum):
                    self.fsm_state = self.FSM_S_DATA
                    self.recv_len = 0
                    # head check successed, read the reserved datas
                    # 2 = checksum(1) + 0xF4(1)
                    ret_num = self.data_region_len + 2

                else:
                    self.fsm_state = self.FSM_S_HEAD

            elif (self.FSM_S_DATA == self.fsm_state):
                self.recv_buffer.append(c)
                self.recv_len += 1
                if (self.data_region_len == self.recv_len):
                    self.fsm_state = self.FSM_S_DATA_CHECK

            elif (self.FSM_S_DATA_CHECK == self.fsm_state):
                self.recv_buffer.append(c)
                data_checksum = 0
                for i in self.recv_buffer[4 : -1]:
                    data_checksum += i
                data_checksum = data_checksum & 0xFF
                if (data_checksum == self.recv_buffer[-1]):
                    self.fsm_state = self.FSM_S_END
                else:
                    self.fsm_state = self.FSM_S_HEAD

            elif (self.FSM_S_END == self.fsm_state):
                self.recv_buffer.append(c)
                if (COMMON_PROTOCOL_END == c):
                    receive_frame = self.recv_buffer[:]
                self.fsm_state = self.FSM_S_HEAD

            if receive_frame:
                console.debug("F3F4 received frame %s" %receive_frame)
                # frame_list do not contain the protocol structure datas
                self.frame_list.append(receive_frame[4 : -2])

        if len(self.frame_list) > self.FRAME_MAX_NUM:
            console.warning("F3F4 frame list overflow, clear")
            self.frame_list.clear()

        return ret_num

'''
private functions and variables
'''
ONLINE_CMD_ID = 0x28
PROTOCOL_SUBSCRIBE_ID = 0x29
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

# script to prtocol frame
def __create_frame(servive_id, exec_str, serial_num = 0):
    protocol_frame = bytearray()
    protocol_frame.append(F3F4_PROTOCOL_HEAD)
    
    if cinfig.service_id_enable:
        service_byte_len = 1
    else:
        service_byte_len = 0


    if script_package_type == config.SCRIPT_PACKAGE_TYPE_BIGSTRING:
        # protocol_id + service_id + serial num + strlen(2)
        datalen = 1 + service_byte_len + SERIAL_NUM_LEN + 2 + len(exec_str)

    elif script_package_type == config.SCRIPT_PACKAGE_TYPE_STRING:
        # protocol_id + service_id + serial num + strlen
        datalen = 1 + service_byte_len + SERIAL_NUM_LEN + 1 + len(exec_str)       
    elif script_package_type == config.SCRIPT_PACKAGE_TYPE_STRING0:
        # protocol_id + service_id + serial num + '\0'
        datalen = 1 + service_byte_len + SERIAL_NUM_LEN + len(exec_str) + 1  

    data_len_byte = datalen.to_bytes(2, "little")

    head_check = (data_len_byte[0] + data_len_byte[1] + F3F4_PROTOCOL_HEAD) & 0xFF

    # add head check
    protocol_frame.append(head_check)
    protocol_frame += data_len_byte

    data_sum = 0  
    # add protocol id
    protocol_frame.append(ONLINE_CMD_ID)
    data_sum += ONLINE_CMD_ID
    
    if SERVICE_ID_ENABLE:
        # add servive id
        protocol_frame.append(servive_id)
        data_sum += servive_id
    
    # add serial num, 2 bytes
    if SERIAL_NUM_LEN == 2:
        serial_num_bytes = serial_num.to_bytes(2, "little")
        protocol_frame += serial_num_bytes
        data_sum += serial_num_bytes[0]
        data_sum += serial_num_bytes[1]
    elif SERIAL_NUM_LEN == 1:
        protocol_frame.append(serial_num)
        data_sum += serial_num

    # add script bytes
    if SCRIPT_PACKAGE_TYPE == SCRIPT_PACKAGE_TYPE_BIGSTRING:
        strbytes = __bigstring_package(exec_str)  
    elif SCRIPT_PACKAGE_TYPE == SCRIPT_PACKAGE_TYPE_STRING:
        strbytes = __string_package(exec_str) 
    elif SCRIPT_PACKAGE_TYPE == SCRIPT_PACKAGE_TYPE_STRING0:
        strbytes = __string0_package(exec_str)
        
    protocol_frame += strbytes
    for i in range(len(strbytes)):
        data_sum += strbytes[i]

    data_sum = data_sum & 0xFF
    protocol_frame.append(data_sum)   
    protocol_frame.append(COMMON_PROTOCOL_END)  
    
    # print("whole frame", protocol_frame)
    
    return protocol_frame


