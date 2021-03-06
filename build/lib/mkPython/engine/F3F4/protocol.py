# -*- coding: utf-8 -*-
from struct import pack, unpack

from utils.common import int_to_byte_2
from utils.mylog import console

from engine.F3F4.package import print_frame


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

def create_frame(data):
    protocol_frame = bytearray()
    protocol_frame.append(F3F4_PROTOCOL_HEAD)

    datalen = len(data) 

    data_len_byte = datalen.to_bytes(2, "little")

    head_check = (data_len_byte[0] + data_len_byte[1] + F3F4_PROTOCOL_HEAD) & 0xFF

    # add head check
    protocol_frame.append(head_check)
    protocol_frame += data_len_byte

    data_sum = 0  
    for i in range(len(data)):
        protocol_frame.append(data[i])
        data_sum += data[i]

    data_sum = data_sum & 0xFF
    protocol_frame.append(data_sum)   
    protocol_frame.append(COMMON_PROTOCOL_END)  
    
    return protocol_frame

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
        self.link = None
        self.frame_process_list = []
        self.__fsm_init()

    def print_frame(self, frame):
        __print_frame(frame)

    def register_frame_process(self, process, conditions = None):
        process.protocol = self
        self.frame_process_list.append(process)

    def parse_data_stream(self, data, d_info = None):
        self.__fsm(data)
        if self.frame_list:
            console.debug("%s"%self.frame_list)
            for item in self.frame_list:
                for process in self.frame_process_list:
                    ret = process.process(item, d_info)

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
    
    def send_protocol(self, package):
        console.debug("send_protocol %s"%package)
        if self.link:
            # print(create_frame(package))
            self.link.write(create_frame(package))